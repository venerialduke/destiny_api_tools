"""
Advanced search service for Destiny 2 content with filtering, sorting, and optimization.
Provides comprehensive search capabilities across all manifest data with performance optimization.
"""

import re
import time
import logging
import threading
from typing import Dict, List, Any, Optional, Union, Tuple
from dataclasses import dataclass, field
from collections import defaultdict
from enum import Enum

from ..config import config
from .cache_service import get_cache
from .performance_monitor import get_performance_monitor
from .data_pipeline import get_data_pipeline

logger = logging.getLogger(__name__)


class SearchType(Enum):
    """Types of search operations."""
    TEXT = "text"
    FUZZY = "fuzzy"
    EXACT = "exact"
    REGEX = "regex"
    SEMANTIC = "semantic"


class SortOrder(Enum):
    """Sort order options."""
    ASC = "asc"
    DESC = "desc"


@dataclass
class SearchFilter:
    """Represents a search filter."""
    field: str
    operator: str  # eq, ne, gt, gte, lt, lte, in, not_in, contains, starts_with, ends_with
    value: Any
    case_sensitive: bool = False


@dataclass
class SearchSort:
    """Represents search sorting criteria."""
    field: str
    order: SortOrder = SortOrder.ASC
    priority: int = 1  # Lower numbers = higher priority


@dataclass
class SearchQuery:
    """Complete search query specification."""
    text: str = ""
    search_type: SearchType = SearchType.TEXT
    filters: List[SearchFilter] = field(default_factory=list)
    sorts: List[SearchSort] = field(default_factory=list)
    limit: int = 50
    offset: int = 0
    include_fields: Optional[List[str]] = None
    exclude_fields: Optional[List[str]] = None
    highlight: bool = True
    facets: Optional[List[str]] = None
    boost_fields: Optional[Dict[str, float]] = None


@dataclass
class SearchResult:
    """Individual search result item."""
    id: str
    source: str  # items, activities, classes, etc.
    data: Dict[str, Any]
    score: float = 0.0
    highlights: Optional[Dict[str, List[str]]] = None
    explanation: Optional[str] = None


@dataclass
class SearchResponse:
    """Complete search response."""
    results: List[SearchResult]
    total_hits: int
    query_time: float
    facets: Optional[Dict[str, Dict[str, int]]] = None
    suggestions: Optional[List[str]] = None
    debug_info: Optional[Dict[str, Any]] = None


class SearchIndex:
    """In-memory search index for fast text searching."""
    
    def __init__(self):
        self.documents: Dict[str, Dict[str, Any]] = {}
        self.inverted_index: Dict[str, Dict[str, float]] = defaultdict(lambda: defaultdict(float))
        self.field_indexes: Dict[str, Dict[str, List[str]]] = defaultdict(lambda: defaultdict(list))
        self.lock = threading.RLock()
        self.last_update = 0
        
        # Search configuration
        self.stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were'
        }
        self.min_word_length = 2
        self.boost_exact_match = 2.0
        self.boost_starts_with = 1.5
    
    def add_document(self, doc_id: str, document: Dict[str, Any], source: str = "unknown"):
        """Add a document to the search index."""
        with self.lock:
            # Store the full document
            self.documents[doc_id] = {
                'data': document,
                'source': source,
                'indexed_at': time.time()
            }
            
            # Extract searchable text and build inverted index
            searchable_text = self._extract_searchable_text(document)
            terms = self._tokenize(searchable_text)
            
            # Calculate term frequencies
            term_counts = defaultdict(int)
            for term in terms:
                term_counts[term] += 1
            
            # Add to inverted index with TF-IDF-like scoring
            for term, count in term_counts.items():
                tf = count / len(terms) if terms else 0
                self.inverted_index[term][doc_id] = tf
            
            # Build field-specific indexes
            self._index_fields(doc_id, document)
            
            self.last_update = time.time()
    
    def remove_document(self, doc_id: str):
        """Remove a document from the search index."""
        with self.lock:
            if doc_id in self.documents:
                # Remove from inverted index
                for term_docs in self.inverted_index.values():
                    term_docs.pop(doc_id, None)
                
                # Remove from field indexes
                for field_index in self.field_indexes.values():
                    for value_docs in field_index.values():
                        if doc_id in value_docs:
                            value_docs.remove(doc_id)
                
                # Remove document
                del self.documents[doc_id]
                self.last_update = time.time()
    
    def search(self, query: SearchQuery) -> List[Tuple[str, float]]:
        """Search the index and return document IDs with scores."""
        with self.lock:
            if not query.text and not query.filters:
                return []
            
            # Text search
            text_results = self._search_text(query.text, query.search_type) if query.text else {}
            
            # Apply filters
            filtered_results = self._apply_filters(text_results, query.filters)
            
            # Apply field boosts
            if query.boost_fields:
                filtered_results = self._apply_boosts(filtered_results, query.boost_fields)
            
            # Sort results by score
            sorted_results = sorted(filtered_results.items(), key=lambda x: x[1], reverse=True)
            
            return sorted_results
    
    def _extract_searchable_text(self, document: Dict[str, Any]) -> str:
        """Extract searchable text from a document."""
        text_parts = []
        
        def extract_text(obj, depth=0):
            if depth > 3:  # Prevent infinite recursion
                return
            
            if isinstance(obj, dict):
                for key, value in obj.items():
                    if key in ['name', 'displayName', 'description', 'flavorText', 'searchableText']:
                        if isinstance(value, str):
                            text_parts.append(value)
                    elif isinstance(value, (dict, list)):
                        extract_text(value, depth + 1)
            elif isinstance(obj, list):
                for item in obj:
                    extract_text(item, depth + 1)
            elif isinstance(obj, str):
                text_parts.append(obj)
        
        extract_text(document)
        return ' '.join(text_parts)
    
    def _tokenize(self, text: str) -> List[str]:
        """Tokenize text into searchable terms."""
        if not text:
            return []
        
        # Convert to lowercase and split on non-alphanumeric characters
        words = re.findall(r'\b\w+\b', text.lower())
        
        # Filter out stop words and short words
        terms = [
            word for word in words 
            if len(word) >= self.min_word_length and word not in self.stop_words
        ]
        
        return terms
    
    def _index_fields(self, doc_id: str, document: Dict[str, Any]):
        """Build field-specific indexes for filtering."""
        def index_field(obj, prefix=""):
            if isinstance(obj, dict):
                for key, value in obj.items():
                    field_name = f"{prefix}.{key}" if prefix else key
                    if isinstance(value, (str, int, float, bool)):
                        self.field_indexes[field_name][str(value)].append(doc_id)
                    elif isinstance(value, list):
                        for item in value:
                            if isinstance(item, (str, int, float, bool)):
                                self.field_indexes[field_name][str(item)].append(doc_id)
                            elif isinstance(item, dict):
                                index_field(item, field_name)
                    elif isinstance(value, dict):
                        index_field(value, field_name)
        
        index_field(document)
    
    def _search_text(self, text: str, search_type: SearchType) -> Dict[str, float]:
        """Perform text search based on search type."""
        if search_type == SearchType.EXACT:
            return self._search_exact(text)
        elif search_type == SearchType.FUZZY:
            return self._search_fuzzy(text)
        elif search_type == SearchType.REGEX:
            return self._search_regex(text)
        else:  # Default to text search
            return self._search_text_default(text)
    
    def _search_text_default(self, text: str) -> Dict[str, float]:
        """Default text search with relevance scoring."""
        query_terms = self._tokenize(text)
        if not query_terms:
            return {}
        
        doc_scores = defaultdict(float)
        
        for term in query_terms:
            # Exact term matches
            if term in self.inverted_index:
                for doc_id, tf in self.inverted_index[term].items():
                    idf = len(self.documents) / len(self.inverted_index[term])
                    score = tf * idf
                    doc_scores[doc_id] += score
            
            # Partial matches (starts with)
            for indexed_term in self.inverted_index:
                if indexed_term.startswith(term):
                    for doc_id, tf in self.inverted_index[indexed_term].items():
                        idf = len(self.documents) / len(self.inverted_index[indexed_term])
                        score = tf * idf * self.boost_starts_with
                        doc_scores[doc_id] += score
        
        return dict(doc_scores)
    
    def _search_exact(self, text: str) -> Dict[str, float]:
        """Exact phrase search."""
        text_lower = text.lower()
        doc_scores = {}
        
        for doc_id, doc_info in self.documents.items():
            searchable_text = self._extract_searchable_text(doc_info['data']).lower()
            if text_lower in searchable_text:
                # Boost exact matches
                doc_scores[doc_id] = self.boost_exact_match
        
        return doc_scores
    
    def _search_fuzzy(self, text: str) -> Dict[str, float]:
        """Fuzzy search with edit distance tolerance."""
        query_terms = self._tokenize(text)
        doc_scores = defaultdict(float)
        
        for term in query_terms:
            # Find similar terms using simple character overlap
            for indexed_term in self.inverted_index:
                similarity = self._calculate_similarity(term, indexed_term)
                if similarity > 0.7:  # 70% similarity threshold
                    for doc_id, tf in self.inverted_index[indexed_term].items():
                        score = tf * similarity
                        doc_scores[doc_id] += score
        
        return dict(doc_scores)
    
    def _search_regex(self, pattern: str) -> Dict[str, float]:
        """Regular expression search."""
        try:
            regex = re.compile(pattern, re.IGNORECASE)
            doc_scores = {}
            
            for doc_id, doc_info in self.documents.items():
                searchable_text = self._extract_searchable_text(doc_info['data'])
                if regex.search(searchable_text):
                    doc_scores[doc_id] = 1.0
            
            return doc_scores
        except re.error:
            logger.warning(f"Invalid regex pattern: {pattern}")
            return {}
    
    def _calculate_similarity(self, term1: str, term2: str) -> float:
        """Calculate similarity between two terms using character overlap."""
        if not term1 or not term2:
            return 0.0
        
        set1 = set(term1)
        set2 = set(term2)
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        
        return intersection / union if union > 0 else 0.0
    
    def _apply_filters(self, text_results: Dict[str, float], filters: List[SearchFilter]) -> Dict[str, float]:
        """Apply filters to search results."""
        if not filters:
            return text_results
        
        filtered_results = {}
        
        for doc_id, score in text_results.items():
            if self._document_matches_filters(doc_id, filters):
                filtered_results[doc_id] = score
        
        return filtered_results
    
    def _document_matches_filters(self, doc_id: str, filters: List[SearchFilter]) -> bool:
        """Check if a document matches all filters."""
        if doc_id not in self.documents:
            return False
        
        document = self.documents[doc_id]['data']
        
        for filter_obj in filters:
            if not self._apply_single_filter(document, filter_obj):
                return False
        
        return True
    
    def _apply_single_filter(self, document: Dict[str, Any], filter_obj: SearchFilter) -> bool:
        """Apply a single filter to a document."""
        value = self._get_nested_value(document, filter_obj.field)
        if value is None:
            return False
        
        filter_value = filter_obj.value
        
        # Handle case sensitivity
        if isinstance(value, str) and isinstance(filter_value, str) and not filter_obj.case_sensitive:
            value = value.lower()
            filter_value = filter_value.lower()
        
        # Apply operator
        if filter_obj.operator == 'eq':
            return value == filter_value
        elif filter_obj.operator == 'ne':
            return value != filter_value
        elif filter_obj.operator == 'gt':
            return value > filter_value
        elif filter_obj.operator == 'gte':
            return value >= filter_value
        elif filter_obj.operator == 'lt':
            return value < filter_value
        elif filter_obj.operator == 'lte':
            return value <= filter_value
        elif filter_obj.operator == 'in':
            return value in filter_value
        elif filter_obj.operator == 'not_in':
            return value not in filter_value
        elif filter_obj.operator == 'contains':
            return str(filter_value) in str(value)
        elif filter_obj.operator == 'starts_with':
            return str(value).startswith(str(filter_value))
        elif filter_obj.operator == 'ends_with':
            return str(value).endswith(str(filter_value))
        
        return False
    
    def _get_nested_value(self, obj: Dict[str, Any], path: str) -> Any:
        """Get a nested value from a dictionary using dot notation."""
        keys = path.split('.')
        current = obj
        
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return None
        
        return current
    
    def _apply_boosts(self, results: Dict[str, float], boost_fields: Dict[str, float]) -> Dict[str, float]:
        """Apply field-based score boosts."""
        boosted_results = {}
        
        for doc_id, score in results.items():
            boosted_score = score
            document = self.documents[doc_id]['data']
            
            for field, boost in boost_fields.items():
                value = self._get_nested_value(document, field)
                if value:
                    boosted_score *= boost
            
            boosted_results[doc_id] = boosted_score
        
        return boosted_results
    
    def get_stats(self) -> Dict[str, Any]:
        """Get index statistics."""
        with self.lock:
            return {
                'total_documents': len(self.documents),
                'total_terms': len(self.inverted_index),
                'total_fields': len(self.field_indexes),
                'last_update': self.last_update,
                'memory_usage': {
                    'documents': len(str(self.documents)),
                    'inverted_index': len(str(self.inverted_index)),
                    'field_indexes': len(str(self.field_indexes))
                }
            }


class AdvancedSearchService:
    """Advanced search service with comprehensive filtering and optimization."""
    
    def __init__(self):
        self.cache = get_cache()
        self.performance_monitor = get_performance_monitor()
        self.data_pipeline = get_data_pipeline()
        
        # Search indexes for different content types
        self.indexes = {
            'items': SearchIndex(),
            'activities': SearchIndex(),
            'classes': SearchIndex(),
            'vendors': SearchIndex(),
            'lore': SearchIndex()
        }
        
        # Search configuration
        self.default_limit = 50
        self.max_limit = 500
        self.cache_ttl = 300  # 5 minutes
        self.suggestion_cache_ttl = 3600  # 1 hour
        
        # Popular search terms for suggestions
        self.popular_terms = set()
        self.search_history = []
        self.max_history_size = 1000
        
        self.lock = threading.RLock()
    
    def index_manifest_data(self, manifest_data: Dict[str, Any]):
        """Index manifest data for searching."""
        start_time = time.time()
        
        try:
            # Index different types of content
            if 'DestinyInventoryItemDefinition' in manifest_data:
                self._index_items(manifest_data['DestinyInventoryItemDefinition'])
            
            if 'DestinyActivityDefinition' in manifest_data:
                self._index_activities(manifest_data['DestinyActivityDefinition'])
            
            if 'DestinyClassDefinition' in manifest_data:
                self._index_classes(manifest_data['DestinyClassDefinition'])
            
            indexing_time = time.time() - start_time
            logger.info(f"Manifest data indexed in {indexing_time:.2f}s")
            
            # Cache indexing completion
            self.cache.set(
                'search_index_status',
                {
                    'indexed_at': time.time(),
                    'indexing_time': indexing_time,
                    'total_documents': sum(len(index.documents) for index in self.indexes.values())
                },
                ttl=self.cache_ttl
            )
            
        except Exception as e:
            logger.error(f"Error indexing manifest data: {e}")
            raise
    
    def search(self, query: SearchQuery, content_types: Optional[List[str]] = None) -> SearchResponse:
        """Perform advanced search across content types."""
        start_time = time.time()
        
        # Generate cache key
        cache_key = self._generate_cache_key(query, content_types)
        
        # Check cache first
        cached_result = self.cache.get(cache_key)
        if cached_result:
            logger.debug(f"Search cache hit for key: {cache_key}")
            return SearchResponse(**cached_result)
        
        try:
            # Validate and normalize query
            normalized_query = self._normalize_query(query)
            
            # Determine content types to search
            if not content_types:
                content_types = list(self.indexes.keys())
            
            # Perform search across all specified content types
            all_results = []
            total_hits = 0
            
            for content_type in content_types:
                if content_type in self.indexes:
                    index_results = self.indexes[content_type].search(normalized_query)
                    
                    # Convert to SearchResult objects
                    for doc_id, score in index_results:
                        document = self.indexes[content_type].documents[doc_id]
                        search_result = SearchResult(
                            id=doc_id,
                            source=content_type,
                            data=document['data'],
                            score=score,
                            highlights=self._generate_highlights(document['data'], normalized_query) if normalized_query.highlight else None
                        )
                        all_results.append(search_result)
                        total_hits += 1
            
            # Apply global sorting
            if normalized_query.sorts:
                all_results = self._apply_sorting(all_results, normalized_query.sorts)
            else:
                # Default sort by score
                all_results.sort(key=lambda x: x.score, reverse=True)
            
            # Apply pagination
            paginated_results = all_results[normalized_query.offset:normalized_query.offset + normalized_query.limit]
            
            # Generate facets if requested
            facets = self._generate_facets(all_results, normalized_query.facets) if normalized_query.facets else None
            
            # Generate suggestions
            suggestions = self._generate_suggestions(normalized_query.text) if normalized_query.text else None
            
            query_time = time.time() - start_time
            
            # Create response
            response = SearchResponse(
                results=paginated_results,
                total_hits=total_hits,
                query_time=query_time,
                facets=facets,
                suggestions=suggestions
            )
            
            # Cache the result
            self.cache.set(cache_key, response.__dict__, ttl=self.cache_ttl)
            
            # Record search history for suggestions
            self._record_search(normalized_query.text)
            
            # Record performance metrics
            self.performance_monitor.recordMetric('Search_Query', query_time * 1000, {
                'content_types': content_types,
                'total_hits': total_hits,
                'has_filters': len(normalized_query.filters) > 0,
                'cached': False
            })
            
            logger.debug(f"Search completed in {query_time:.3f}s, {total_hits} hits")
            
            return response
            
        except Exception as e:
            logger.error(f"Search error: {e}")
            self.performance_monitor.recordError(e, {'context': 'AdvancedSearch'})
            raise
    
    def suggest(self, partial_text: str, limit: int = 10) -> List[str]:
        """Generate search suggestions based on partial input."""
        cache_key = f"suggestions:{partial_text}:{limit}"
        cached_suggestions = self.cache.get(cache_key)
        
        if cached_suggestions:
            return cached_suggestions
        
        suggestions = []
        partial_lower = partial_text.lower()
        
        # Find matching terms from popular searches
        for term in self.popular_terms:
            if term.lower().startswith(partial_lower):
                suggestions.append(term)
                if len(suggestions) >= limit:
                    break
        
        # Add suggestions from search history
        for search_term in reversed(self.search_history):
            if search_term.lower().startswith(partial_lower) and search_term not in suggestions:
                suggestions.append(search_term)
                if len(suggestions) >= limit:
                    break
        
        # Cache suggestions
        self.cache.set(cache_key, suggestions, ttl=self.suggestion_cache_ttl)
        
        return suggestions
    
    def get_facets(self, field: str, query: Optional[SearchQuery] = None, limit: int = 20) -> Dict[str, int]:
        """Get facet values for a specific field."""
        facet_counts = defaultdict(int)
        
        # If query provided, filter documents first
        if query:
            # Get matching documents
            for content_type in self.indexes:
                results = self.indexes[content_type].search(query)
                for doc_id, _ in results:
                    document = self.indexes[content_type].documents[doc_id]['data']
                    value = self._get_nested_value(document, field)
                    if value:
                        facet_counts[str(value)] += 1
        else:
            # Get all values for the field
            for content_type in self.indexes:
                for doc_id, doc_info in self.indexes[content_type].documents.items():
                    value = self._get_nested_value(doc_info['data'], field)
                    if value:
                        facet_counts[str(value)] += 1
        
        # Sort by count and limit
        sorted_facets = dict(sorted(facet_counts.items(), key=lambda x: x[1], reverse=True)[:limit])
        
        return sorted_facets
    
    def _index_items(self, items: Dict[str, Any]):
        """Index inventory items."""
        index = self.indexes['items']
        
        for item_hash, item_data in items.items():
            try:
                # Enhance item data with searchable fields
                enhanced_item = {
                    **item_data,
                    'hash': item_hash,
                    'searchable_text': self._create_item_searchable_text(item_data),
                    'tier_name': item_data.get('inventory', {}).get('tierTypeName', ''),
                    'type_name': item_data.get('itemTypeDisplayName', ''),
                    'category_hashes': item_data.get('itemCategoryHashes', []),
                    'damage_type': item_data.get('damageTypeHashes', [])
                }
                
                index.add_document(item_hash, enhanced_item, 'items')
                
            except Exception as e:
                logger.error(f"Error indexing item {item_hash}: {e}")
    
    def _index_activities(self, activities: Dict[str, Any]):
        """Index activities."""
        index = self.indexes['activities']
        
        for activity_hash, activity_data in activities.items():
            try:
                enhanced_activity = {
                    **activity_data,
                    'hash': activity_hash,
                    'searchable_text': self._create_activity_searchable_text(activity_data)
                }
                
                index.add_document(activity_hash, enhanced_activity, 'activities')
                
            except Exception as e:
                logger.error(f"Error indexing activity {activity_hash}: {e}")
    
    def _index_classes(self, classes: Dict[str, Any]):
        """Index classes."""
        index = self.indexes['classes']
        
        for class_hash, class_data in classes.items():
            try:
                enhanced_class = {
                    **class_data,
                    'hash': class_hash,
                    'searchable_text': self._create_class_searchable_text(class_data)
                }
                
                index.add_document(class_hash, enhanced_class, 'classes')
                
            except Exception as e:
                logger.error(f"Error indexing class {class_hash}: {e}")
    
    def _create_item_searchable_text(self, item_data: Dict[str, Any]) -> str:
        """Create searchable text for an item."""
        text_parts = []
        
        # Basic item info
        display_props = item_data.get('displayProperties', {})
        text_parts.append(display_props.get('name', ''))
        text_parts.append(display_props.get('description', ''))
        
        # Item type and tier
        text_parts.append(item_data.get('itemTypeDisplayName', ''))
        text_parts.append(item_data.get('inventory', {}).get('tierTypeName', ''))
        
        # Flavor text
        flavor_text = item_data.get('flavorText', '')
        if flavor_text:
            text_parts.append(flavor_text)
        
        return ' '.join(text_parts)
    
    def _create_activity_searchable_text(self, activity_data: Dict[str, Any]) -> str:
        """Create searchable text for an activity."""
        text_parts = []
        
        display_props = activity_data.get('displayProperties', {})
        text_parts.append(display_props.get('name', ''))
        text_parts.append(display_props.get('description', ''))
        
        return ' '.join(text_parts)
    
    def _create_class_searchable_text(self, class_data: Dict[str, Any]) -> str:
        """Create searchable text for a class."""
        text_parts = []
        
        display_props = class_data.get('displayProperties', {})
        text_parts.append(display_props.get('name', ''))
        text_parts.append(display_props.get('description', ''))
        
        return ' '.join(text_parts)
    
    def _normalize_query(self, query: SearchQuery) -> SearchQuery:
        """Normalize and validate search query."""
        # Limit the limit :)
        if query.limit > self.max_limit:
            query.limit = self.max_limit
        
        # Ensure minimum limit
        if query.limit <= 0:
            query.limit = self.default_limit
        
        # Ensure valid offset
        if query.offset < 0:
            query.offset = 0
        
        return query
    
    def _generate_cache_key(self, query: SearchQuery, content_types: Optional[List[str]]) -> str:
        """Generate cache key for search query."""
        key_parts = [
            f"text:{query.text}",
            f"type:{query.search_type.value}",
            f"filters:{len(query.filters)}",
            f"sorts:{len(query.sorts)}",
            f"limit:{query.limit}",
            f"offset:{query.offset}",
            f"types:{','.join(sorted(content_types or []))}"
        ]
        
        return f"search:{'|'.join(key_parts)}"
    
    def _apply_sorting(self, results: List[SearchResult], sorts: List[SearchSort]) -> List[SearchResult]:
        """Apply custom sorting to search results."""
        def sort_key(result):
            keys = []
            for sort_spec in sorted(sorts, key=lambda s: s.priority):
                value = self._get_nested_value(result.data, sort_spec.field)
                if value is None:
                    value = "" if isinstance(value, str) else 0
                
                # Reverse for descending order
                if sort_spec.order == SortOrder.DESC:
                    if isinstance(value, (int, float)):
                        value = -value
                    elif isinstance(value, str):
                        value = value[::-1]  # Reverse string for lexicographic sort
                
                keys.append(value)
            
            return tuple(keys)
        
        return sorted(results, key=sort_key)
    
    def _generate_highlights(self, document: Dict[str, Any], query: SearchQuery) -> Dict[str, List[str]]:
        """Generate search result highlights."""
        if not query.text:
            return {}
        
        highlights = {}
        query_terms = set(word.lower() for word in query.text.split())
        
        # Highlight in name and description fields
        for field in ['displayProperties.name', 'displayProperties.description', 'flavorText']:
            value = self._get_nested_value(document, field)
            if value and isinstance(value, str):
                highlighted = self._highlight_text(value, query_terms)
                if highlighted != value:
                    highlights[field] = [highlighted]
        
        return highlights
    
    def _highlight_text(self, text: str, query_terms: set) -> str:
        """Add highlighting markers to text."""
        if not query_terms:
            return text
        
        highlighted = text
        for term in query_terms:
            pattern = re.compile(re.escape(term), re.IGNORECASE)
            highlighted = pattern.sub(f"<mark>\\g<0></mark>", highlighted)
        
        return highlighted
    
    def _generate_facets(self, results: List[SearchResult], facet_fields: List[str]) -> Dict[str, Dict[str, int]]:
        """Generate facet counts from search results."""
        facets = {}
        
        for field in facet_fields:
            facet_counts = defaultdict(int)
            
            for result in results:
                value = self._get_nested_value(result.data, field)
                if value:
                    facet_counts[str(value)] += 1
            
            # Sort by count and convert to regular dict
            sorted_facets = dict(sorted(facet_counts.items(), key=lambda x: x[1], reverse=True))
            facets[field] = sorted_facets
        
        return facets
    
    def _generate_suggestions(self, query_text: str) -> List[str]:
        """Generate search suggestions based on query."""
        if len(query_text) < 2:
            return []
        
        return self.suggest(query_text, limit=5)
    
    def _get_nested_value(self, obj: Dict[str, Any], path: str) -> Any:
        """Get nested value from dictionary using dot notation."""
        keys = path.split('.')
        current = obj
        
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return None
        
        return current
    
    def _record_search(self, query_text: str):
        """Record search for suggestions and analytics."""
        if not query_text or len(query_text) < 2:
            return
        
        with self.lock:
            # Add to popular terms
            self.popular_terms.add(query_text)
            
            # Add to search history
            self.search_history.append(query_text)
            
            # Limit history size
            if len(self.search_history) > self.max_history_size:
                self.search_history.pop(0)
    
    def clear_cache(self):
        """Clear search cache."""
        cache_patterns = ['search:', 'suggestions:', 'facets:']
        for pattern in cache_patterns:
            self.cache.delete_by_pattern(pattern)
    
    def get_stats(self) -> Dict[str, Any]:
        """Get search service statistics."""
        index_stats = {}
        total_docs = 0
        
        for content_type, index in self.indexes.items():
            stats = index.get_stats()
            index_stats[content_type] = stats
            total_docs += stats['total_documents']
        
        return {
            'total_documents': total_docs,
            'content_types': len(self.indexes),
            'popular_terms_count': len(self.popular_terms),
            'search_history_size': len(self.search_history),
            'indexes': index_stats
        }


# Global search service instance
search_service = AdvancedSearchService()


def get_search_service() -> AdvancedSearchService:
    """Get the global search service instance."""
    return search_service


def search_content(query: SearchQuery, content_types: Optional[List[str]] = None) -> SearchResponse:
    """Perform content search."""
    return search_service.search(query, content_types)


def suggest_searches(partial_text: str, limit: int = 10) -> List[str]:
    """Get search suggestions."""
    return search_service.suggest(partial_text, limit)


def get_facet_values(field: str, query: Optional[SearchQuery] = None, limit: int = 20) -> Dict[str, int]:
    """Get facet values for a field."""
    return search_service.get_facets(field, query, limit)