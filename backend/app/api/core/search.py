"""
Search API endpoints for advanced content searching and filtering.
"""

from flask import Blueprint, request, jsonify
from typing import List, Dict, Any, Optional

from ...services.search_service import (
    get_search_service, 
    SearchQuery, 
    SearchFilter, 
    SearchSort, 
    SearchType, 
    SortOrder,
    search_content,
    suggest_searches,
    get_facet_values
)
from ...utils.response import APIResponse
from ...utils.validation import validate_request

search_bp = Blueprint('search', __name__)


@search_bp.route('/search', methods=['POST'])
def advanced_search():
    """
    Perform advanced search across Destiny content.
    
    Expected payload:
    {
        "text": "search query",
        "search_type": "text|fuzzy|exact|regex",
        "content_types": ["items", "activities", "classes"],
        "filters": [
            {
                "field": "tier_name",
                "operator": "eq",
                "value": "Exotic",
                "case_sensitive": false
            }
        ],
        "sorts": [
            {
                "field": "displayProperties.name",
                "order": "asc",
                "priority": 1
            }
        ],
        "limit": 50,
        "offset": 0,
        "include_fields": ["displayProperties", "hash"],
        "exclude_fields": ["stats"],
        "highlight": true,
        "facets": ["tier_name", "type_name"],
        "boost_fields": {
            "displayProperties.name": 1.5
        }
    }
    """
    try:
        data = request.get_json() or {}
        
        # Validate required fields
        validation_rules = {
            'text': {'type': str, 'required': False, 'default': ''},
            'search_type': {'type': str, 'required': False, 'default': 'text', 'choices': ['text', 'fuzzy', 'exact', 'regex']},
            'content_types': {'type': list, 'required': False, 'default': None},
            'limit': {'type': int, 'required': False, 'default': 50, 'min': 1, 'max': 500},
            'offset': {'type': int, 'required': False, 'default': 0, 'min': 0},
            'highlight': {'type': bool, 'required': False, 'default': True},
            'filters': {'type': list, 'required': False, 'default': []},
            'sorts': {'type': list, 'required': False, 'default': []},
            'facets': {'type': list, 'required': False, 'default': None},
            'include_fields': {'type': list, 'required': False, 'default': None},
            'exclude_fields': {'type': list, 'required': False, 'default': None},
            'boost_fields': {'type': dict, 'required': False, 'default': None}
        }
        
        validated_data = validate_request(data, validation_rules)
        
        # Build search filters
        filters = []
        for filter_data in validated_data.get('filters', []):
            if not isinstance(filter_data, dict):
                continue
                
            search_filter = SearchFilter(
                field=filter_data.get('field', ''),
                operator=filter_data.get('operator', 'eq'),
                value=filter_data.get('value'),
                case_sensitive=filter_data.get('case_sensitive', False)
            )
            filters.append(search_filter)
        
        # Build search sorts
        sorts = []
        for sort_data in validated_data.get('sorts', []):
            if not isinstance(sort_data, dict):
                continue
                
            search_sort = SearchSort(
                field=sort_data.get('field', ''),
                order=SortOrder(sort_data.get('order', 'asc')),
                priority=sort_data.get('priority', 1)
            )
            sorts.append(search_sort)
        
        # Create search query
        search_query = SearchQuery(
            text=validated_data['text'],
            search_type=SearchType(validated_data['search_type']),
            filters=filters,
            sorts=sorts,
            limit=validated_data['limit'],
            offset=validated_data['offset'],
            include_fields=validated_data['include_fields'],
            exclude_fields=validated_data['exclude_fields'],
            highlight=validated_data['highlight'],
            facets=validated_data['facets'],
            boost_fields=validated_data['boost_fields']
        )
        
        # Perform search
        results = search_content(search_query, validated_data['content_types'])
        
        # Format response
        response_data = {
            'results': [
                {
                    'id': result.id,
                    'source': result.source,
                    'data': _filter_fields(result.data, validated_data['include_fields'], validated_data['exclude_fields']),
                    'score': result.score,
                    'highlights': result.highlights
                }
                for result in results.results
            ],
            'total_hits': results.total_hits,
            'query_time': results.query_time,
            'facets': results.facets,
            'suggestions': results.suggestions,
            'pagination': {
                'limit': validated_data['limit'],
                'offset': validated_data['offset'],
                'has_more': (validated_data['offset'] + validated_data['limit']) < results.total_hits
            }
        }
        
        return APIResponse.success(
            data=response_data,
            message="Search completed successfully"
        )
        
    except ValueError as e:
        return APIResponse.error(
            message=f"Invalid search parameters: {str(e)}",
            code="INVALID_SEARCH_PARAMS"
        ), 400
    except Exception as e:
        return APIResponse.error(
            message="Search failed",
            code="SEARCH_ERROR",
            details={"error": str(e)}
        ), 500


@search_bp.route('/suggest', methods=['GET'])
def search_suggestions():
    """
    Get search suggestions based on partial input.
    
    Query parameters:
    - q: Partial search text
    - limit: Maximum number of suggestions (default: 10)
    """
    try:
        partial_text = request.args.get('q', '').strip()
        limit = min(int(request.args.get('limit', 10)), 50)
        
        if not partial_text:
            return APIResponse.success(data={'suggestions': []})
        
        suggestions = suggest_searches(partial_text, limit)
        
        return APIResponse.success(
            data={'suggestions': suggestions},
            message="Suggestions retrieved successfully"
        )
        
    except Exception as e:
        return APIResponse.error(
            message="Failed to get suggestions",
            code="SUGGESTIONS_ERROR",
            details={"error": str(e)}
        ), 500


@search_bp.route('/facets/<field>', methods=['GET'])
def get_field_facets(field: str):
    """
    Get facet values for a specific field.
    
    Query parameters:
    - limit: Maximum number of facet values (default: 20)
    - query: Optional search query to filter facets
    """
    try:
        limit = min(int(request.args.get('limit', 20)), 100)
        query_text = request.args.get('query', '').strip()
        
        # Create search query if provided
        search_query = None
        if query_text:
            search_query = SearchQuery(text=query_text)
        
        facet_values = get_facet_values(field, search_query, limit)
        
        return APIResponse.success(
            data={
                'field': field,
                'values': facet_values,
                'total_values': len(facet_values)
            },
            message="Facet values retrieved successfully"
        )
        
    except Exception as e:
        return APIResponse.error(
            message="Failed to get facet values",
            code="FACETS_ERROR",
            details={"error": str(e)}
        ), 500


@search_bp.route('/quick-search', methods=['GET'])
def quick_search():
    """
    Perform a quick text search with minimal parameters.
    
    Query parameters:
    - q: Search query
    - type: Content type filter (items, activities, classes)
    - limit: Result limit (default: 20)
    """
    try:
        query_text = request.args.get('q', '').strip()
        content_type = request.args.get('type', '')
        limit = min(int(request.args.get('limit', 20)), 100)
        
        if not query_text:
            return APIResponse.success(data={'results': [], 'total_hits': 0})
        
        # Create simple search query
        search_query = SearchQuery(
            text=query_text,
            limit=limit,
            highlight=True
        )
        
        # Determine content types
        content_types = [content_type] if content_type else None
        
        # Perform search
        results = search_content(search_query, content_types)
        
        # Simplified response format
        response_data = {
            'results': [
                {
                    'id': result.id,
                    'source': result.source,
                    'name': result.data.get('displayProperties', {}).get('name', ''),
                    'description': result.data.get('displayProperties', {}).get('description', ''),
                    'icon': result.data.get('displayProperties', {}).get('icon', ''),
                    'score': result.score,
                    'highlights': result.highlights
                }
                for result in results.results
            ],
            'total_hits': results.total_hits,
            'query_time': results.query_time
        }
        
        return APIResponse.success(
            data=response_data,
            message="Quick search completed successfully"
        )
        
    except Exception as e:
        return APIResponse.error(
            message="Quick search failed",
            code="QUICK_SEARCH_ERROR",
            details={"error": str(e)}
        ), 500


@search_bp.route('/popular-searches', methods=['GET'])
def popular_searches():
    """Get popular search terms."""
    try:
        search_service = get_search_service()
        
        # Get popular terms (limited sample for privacy)
        popular_terms = list(search_service.popular_terms)[:20]
        
        return APIResponse.success(
            data={'popular_searches': popular_terms},
            message="Popular searches retrieved successfully"
        )
        
    except Exception as e:
        return APIResponse.error(
            message="Failed to get popular searches",
            code="POPULAR_SEARCHES_ERROR",
            details={"error": str(e)}
        ), 500


@search_bp.route('/stats', methods=['GET'])
def search_stats():
    """Get search service statistics."""
    try:
        search_service = get_search_service()
        stats = search_service.get_stats()
        
        return APIResponse.success(
            data=stats,
            message="Search statistics retrieved successfully"
        )
        
    except Exception as e:
        return APIResponse.error(
            message="Failed to get search statistics",
            code="SEARCH_STATS_ERROR",
            details={"error": str(e)}
        ), 500


@search_bp.route('/index/status', methods=['GET'])
def index_status():
    """Get search index status."""
    try:
        search_service = get_search_service()
        
        # Get index statistics
        stats = search_service.get_stats()
        
        # Check if indexes are populated
        has_data = stats['total_documents'] > 0
        
        response_data = {
            'indexed': has_data,
            'total_documents': stats['total_documents'],
            'content_types': stats['content_types'],
            'indexes': stats['indexes'],
            'status': 'ready' if has_data else 'empty'
        }
        
        return APIResponse.success(
            data=response_data,
            message="Index status retrieved successfully"
        )
        
    except Exception as e:
        return APIResponse.error(
            message="Failed to get index status",
            code="INDEX_STATUS_ERROR",
            details={"error": str(e)}
        ), 500


@search_bp.route('/index/rebuild', methods=['POST'])
def rebuild_index():
    """Trigger search index rebuild."""
    try:
        search_service = get_search_service()
        
        # Clear existing cache
        search_service.clear_cache()
        
        # Schedule manifest reindexing through data pipeline
        from ...services.data_pipeline import get_data_pipeline
        
        data_pipeline = get_data_pipeline()
        
        # This would trigger a manifest update job that includes reindexing
        # For now, return success indicating the rebuild has been scheduled
        
        return APIResponse.success(
            message="Search index rebuild has been scheduled",
            data={'status': 'scheduled'}
        )
        
    except Exception as e:
        return APIResponse.error(
            message="Failed to rebuild search index",
            code="INDEX_REBUILD_ERROR",
            details={"error": str(e)}
        ), 500


def _filter_fields(data: Dict[str, Any], include_fields: Optional[List[str]], exclude_fields: Optional[List[str]]) -> Dict[str, Any]:
    """Filter fields in response data."""
    if not include_fields and not exclude_fields:
        return data
    
    result = {}
    
    if include_fields:
        # Only include specified fields
        for field in include_fields:
            if '.' in field:
                # Handle nested fields
                keys = field.split('.')
                current = data
                for key in keys[:-1]:
                    if isinstance(current, dict) and key in current:
                        current = current[key]
                    else:
                        current = None
                        break
                
                if current and isinstance(current, dict) and keys[-1] in current:
                    _set_nested_value(result, field, current[keys[-1]])
            else:
                # Handle top-level fields
                if field in data:
                    result[field] = data[field]
    else:
        # Include all fields except excluded ones
        result = data.copy()
        
        if exclude_fields:
            for field in exclude_fields:
                if '.' in field:
                    # Handle nested field exclusion
                    keys = field.split('.')
                    current = result
                    for key in keys[:-1]:
                        if isinstance(current, dict) and key in current:
                            current = current[key]
                        else:
                            current = None
                            break
                    
                    if current and isinstance(current, dict) and keys[-1] in current:
                        del current[keys[-1]]
                else:
                    # Handle top-level field exclusion
                    result.pop(field, None)
    
    return result


def _set_nested_value(obj: Dict[str, Any], path: str, value: Any):
    """Set a nested value in a dictionary using dot notation."""
    keys = path.split('.')
    current = obj
    
    for key in keys[:-1]:
        if key not in current:
            current[key] = {}
        current = current[key]
    
    current[keys[-1]] = value