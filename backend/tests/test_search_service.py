"""
Test suite for advanced search functionality.
"""

import pytest
from unittest.mock import Mock, patch
from app.services.search_service import (
    AdvancedSearchService, SearchQuery, SearchFilter, SearchSort, 
    SearchType, SortOrder, SearchIndex
)


class TestSearchIndex:
    """Test search index functionality."""
    
    def setup_method(self):
        """Setup test environment."""
        self.index = SearchIndex()
    
    def test_add_document(self):
        """Test adding a document to the index."""
        doc_id = "test_doc_1"
        document = {
            "displayProperties": {
                "name": "Test Item",
                "description": "A test item for searching"
            },
            "type": "weapon"
        }
        
        self.index.add_document(doc_id, document, "items")
        
        assert doc_id in self.index.documents
        assert self.index.documents[doc_id]['data'] == document
        assert self.index.documents[doc_id]['source'] == "items"
    
    def test_remove_document(self):
        """Test removing a document from the index."""
        doc_id = "test_doc_1"
        document = {"name": "Test Item"}
        
        self.index.add_document(doc_id, document)
        assert doc_id in self.index.documents
        
        self.index.remove_document(doc_id)
        assert doc_id not in self.index.documents
    
    def test_text_search(self):
        """Test basic text search."""
        # Add test documents
        self.index.add_document("item1", {
            "displayProperties": {"name": "Exotic Weapon", "description": "Powerful gun"}
        })
        self.index.add_document("item2", {
            "displayProperties": {"name": "Legendary Armor", "description": "Strong protection"}
        })
        
        # Search for "weapon"
        query = SearchQuery(text="weapon")
        results = self.index.search(query)
        
        # Should find the weapon item
        assert len(results) > 0
        assert any(doc_id == "item1" for doc_id, score in results)
    
    def test_exact_search(self):
        """Test exact phrase search."""
        self.index.add_document("item1", {
            "displayProperties": {"name": "Ace of Spades"}
        })
        self.index.add_document("item2", {
            "displayProperties": {"name": "Ace Hardware"}
        })
        
        query = SearchQuery(text="Ace of Spades", search_type=SearchType.EXACT)
        results = self.index.search(query)
        
        # Should find exact match
        assert len(results) > 0
        doc_ids = [doc_id for doc_id, score in results]
        assert "item1" in doc_ids
    
    def test_filter_search(self):
        """Test search with filters."""
        self.index.add_document("item1", {
            "displayProperties": {"name": "Weapon 1"},
            "type": "weapon",
            "tier": "exotic"
        })
        self.index.add_document("item2", {
            "displayProperties": {"name": "Armor 1"},
            "type": "armor",
            "tier": "legendary"
        })
        
        # Search with type filter
        filter_obj = SearchFilter(field="type", operator="eq", value="weapon")
        query = SearchQuery(filters=[filter_obj])
        results = self.index.search(query)
        
        # Should only find weapon
        assert len(results) == 1
        assert results[0][0] == "item1"
    
    def test_search_scoring(self):
        """Test search result scoring."""
        self.index.add_document("item1", {
            "displayProperties": {
                "name": "Test Item",
                "description": "This is a test item"
            }
        })
        self.index.add_document("item2", {
            "displayProperties": {
                "name": "Another Item",
                "description": "Test test test test"  # More matches
            }
        })
        
        query = SearchQuery(text="test")
        results = self.index.search(query)
        
        # Results should be scored and sorted
        assert len(results) == 2
        # Item with more matches should score higher
        assert results[0][1] >= results[1][1]
    
    def test_get_stats(self):
        """Test getting index statistics."""
        self.index.add_document("item1", {"name": "Test"})
        self.index.add_document("item2", {"name": "Another"})
        
        stats = self.index.get_stats()
        
        assert stats['total_documents'] == 2
        assert stats['total_terms'] > 0
        assert 'last_update' in stats


class TestAdvancedSearchService:
    """Test advanced search service functionality."""
    
    def setup_method(self):
        """Setup test environment."""
        self.search_service = AdvancedSearchService()
    
    def test_service_initialization(self):
        """Test search service initializes correctly."""
        assert self.search_service is not None
        assert 'items' in self.search_service.indexes
        assert 'activities' in self.search_service.indexes
        assert 'classes' in self.search_service.indexes
    
    def test_index_manifest_data(self):
        """Test indexing manifest data."""
        manifest_data = {
            'DestinyInventoryItemDefinition': {
                '12345': {
                    'displayProperties': {
                        'name': 'Test Weapon',
                        'description': 'A powerful weapon'
                    },
                    'itemTypeDisplayName': 'Auto Rifle',
                    'inventory': {
                        'tierTypeName': 'Exotic'
                    }
                }
            }
        }
        
        self.search_service.index_manifest_data(manifest_data)
        
        # Check that item was indexed
        items_index = self.search_service.indexes['items']
        assert '12345' in items_index.documents
        
        # Test search
        query = SearchQuery(text="weapon")
        results = self.search_service.search(query, ['items'])
        
        assert results.total_hits > 0
        assert any(result.id == '12345' for result in results.results)
    
    @patch('app.services.search_service.get_cache')
    def test_search_caching(self, mock_get_cache):
        """Test search result caching."""
        mock_cache = Mock()
        mock_cache.get.return_value = None  # No cached result
        mock_cache.set.return_value = None
        mock_get_cache.return_value = mock_cache
        
        # Add test data
        self.search_service.indexes['items'].add_document('item1', {
            'displayProperties': {'name': 'Test Item'}
        }, 'items')
        
        query = SearchQuery(text="test")
        results = self.search_service.search(query)
        
        # Should have called cache.set to store results
        mock_cache.set.assert_called()
    
    def test_search_suggestions(self):
        """Test search suggestions."""
        # Add some search history
        self.search_service._record_search("test query")
        self.search_service._record_search("another test")
        self.search_service._record_search("different search")
        
        suggestions = self.search_service.suggest("test", limit=5)
        
        # Should return suggestions starting with "test"
        assert len(suggestions) <= 5
        for suggestion in suggestions:
            assert suggestion.lower().startswith("test")
    
    def test_get_facets(self):
        """Test facet generation."""
        # Add test data with facetable fields
        self.search_service.indexes['items'].add_document('item1', {
            'displayProperties': {'name': 'Weapon 1'},
            'tier_name': 'Exotic'
        }, 'items')
        self.search_service.indexes['items'].add_document('item2', {
            'displayProperties': {'name': 'Weapon 2'},
            'tier_name': 'Legendary'
        }, 'items')
        self.search_service.indexes['items'].add_document('item3', {
            'displayProperties': {'name': 'Weapon 3'},
            'tier_name': 'Exotic'
        }, 'items')
        
        facets = self.search_service.get_facets('tier_name')
        
        assert 'Exotic' in facets
        assert 'Legendary' in facets
        assert facets['Exotic'] == 2  # Two exotic items
        assert facets['Legendary'] == 1  # One legendary item
    
    def test_search_with_sorting(self):
        """Test search with custom sorting."""
        # Add test data
        self.search_service.indexes['items'].add_document('item1', {
            'displayProperties': {'name': 'Alpha Item'}
        }, 'items')
        self.search_service.indexes['items'].add_document('item2', {
            'displayProperties': {'name': 'Beta Item'}
        }, 'items')
        
        # Search with name sorting
        sort_spec = SearchSort(field='displayProperties.name', order=SortOrder.ASC)
        query = SearchQuery(text="item", sorts=[sort_spec])
        results = self.search_service.search(query)
        
        # Should be sorted alphabetically
        assert len(results.results) >= 2
        # First result should be "Alpha Item"
        assert 'Alpha' in results.results[0].data['displayProperties']['name']
    
    def test_search_with_pagination(self):
        """Test search with pagination."""
        # Add multiple test items
        for i in range(10):
            self.search_service.indexes['items'].add_document(f'item{i}', {
                'displayProperties': {'name': f'Test Item {i}'}
            }, 'items')
        
        # Search with limit and offset
        query = SearchQuery(text="test", limit=3, offset=2)
        results = self.search_service.search(query)
        
        assert len(results.results) <= 3
        assert results.total_hits >= 10
    
    def test_search_field_filtering(self):
        """Test search with include/exclude fields."""
        self.search_service.indexes['items'].add_document('item1', {
            'displayProperties': {'name': 'Test Item', 'description': 'Test description'},
            'sensitive_data': 'should be excluded',
            'stats': {'damage': 100}
        }, 'items')
        
        # Search with field exclusion
        query = SearchQuery(
            text="test",
            exclude_fields=['sensitive_data', 'stats']
        )
        results = self.search_service.search(query)
        
        assert len(results.results) > 0
        # Excluded fields should not be in results
        result_data = results.results[0].data
        assert 'sensitive_data' not in result_data
        assert 'stats' not in result_data
        assert 'displayProperties' in result_data
    
    def test_clear_cache(self):
        """Test cache clearing."""
        with patch('app.services.search_service.get_cache') as mock_get_cache:
            mock_cache = Mock()
            mock_get_cache.return_value = mock_cache
            
            self.search_service.clear_cache()
            
            # Should call delete_by_pattern for search-related cache keys
            mock_cache.delete_by_pattern.assert_called()
    
    def test_get_stats(self):
        """Test getting search service statistics."""
        # Add some test data
        self.search_service.indexes['items'].add_document('item1', {'name': 'Test'}, 'items')
        
        stats = self.search_service.get_stats()
        
        assert 'total_documents' in stats
        assert 'content_types' in stats
        assert 'indexes' in stats
        assert stats['total_documents'] >= 1
        assert stats['content_types'] == len(self.search_service.indexes)


class TestSearchAPI:
    """Test search API endpoints."""
    
    @pytest.fixture
    def client(self):
        """Create test client."""
        from app import create_app
        app = create_app(testing=True)
        with app.test_client() as client:
            yield client
    
    def test_advanced_search_endpoint(self, client):
        """Test advanced search POST endpoint."""
        search_data = {
            "text": "test",
            "search_type": "text",
            "limit": 10,
            "highlight": True
        }
        
        response = client.post('/api/core/search/search', 
                              json=search_data,
                              content_type='application/json')
        
        assert response.status_code == 200
        data = response.get_json()
        assert 'success' in data
        if data['success']:
            assert 'data' in data
            assert 'results' in data['data']
            assert 'total_hits' in data['data']
    
    def test_search_suggestions_endpoint(self, client):
        """Test search suggestions endpoint."""
        response = client.get('/api/core/search/suggest?q=test&limit=5')
        
        assert response.status_code == 200
        data = response.get_json()
        assert 'success' in data
        if data['success']:
            assert 'data' in data
            assert 'suggestions' in data['data']
    
    def test_quick_search_endpoint(self, client):
        """Test quick search endpoint."""
        response = client.get('/api/core/search/quick-search?q=test&limit=5')
        
        assert response.status_code == 200
        data = response.get_json()
        assert 'success' in data
        if data['success']:
            assert 'data' in data
            assert 'results' in data['data']
    
    def test_facets_endpoint(self, client):
        """Test facets endpoint."""
        response = client.get('/api/core/search/facets/tier_name?limit=10')
        
        assert response.status_code == 200
        data = response.get_json()
        assert 'success' in data
        if data['success']:
            assert 'data' in data
            assert 'field' in data['data']
            assert 'values' in data['data']
    
    def test_search_stats_endpoint(self, client):
        """Test search statistics endpoint."""
        response = client.get('/api/core/search/stats')
        
        assert response.status_code == 200
        data = response.get_json()
        assert 'success' in data
        if data['success']:
            assert 'data' in data
            assert 'total_documents' in data['data']
    
    def test_index_status_endpoint(self, client):
        """Test search index status endpoint."""
        response = client.get('/api/core/search/index/status')
        
        assert response.status_code == 200
        data = response.get_json()
        assert 'success' in data
        if data['success']:
            assert 'data' in data
            assert 'indexed' in data['data']
            assert 'status' in data['data']
    
    def test_search_validation(self, client):
        """Test search request validation."""
        # Invalid search type
        search_data = {
            "text": "test",
            "search_type": "invalid_type"
        }
        
        response = client.post('/api/core/search/search', 
                              json=search_data,
                              content_type='application/json')
        
        assert response.status_code == 400
        data = response.get_json()
        assert 'success' in data
        assert not data['success']
    
    def test_search_with_filters(self, client):
        """Test search with filters."""
        search_data = {
            "text": "test",
            "filters": [
                {
                    "field": "tier_name",
                    "operator": "eq",
                    "value": "Exotic"
                }
            ]
        }
        
        response = client.post('/api/core/search/search', 
                              json=search_data,
                              content_type='application/json')
        
        assert response.status_code == 200
        data = response.get_json()
        assert 'success' in data
    
    def test_search_with_sorting(self, client):
        """Test search with sorting."""
        search_data = {
            "text": "test",
            "sorts": [
                {
                    "field": "displayProperties.name",
                    "order": "asc"
                }
            ]
        }
        
        response = client.post('/api/core/search/search', 
                              json=search_data,
                              content_type='application/json')
        
        assert response.status_code == 200
        data = response.get_json()
        assert 'success' in data


if __name__ == '__main__':
    pytest.main([__file__])