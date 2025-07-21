/**
 * Advanced Search Component
 * Provides comprehensive search functionality with filtering, sorting, and real-time suggestions.
 */

import React, { useState, useEffect, useCallback, useMemo } from 'react';
import { Search, Filter, SortAsc, SortDesc, X, ChevronDown, Loader } from 'lucide-react';
import { debounce } from 'lodash';
import apiClient from '../../services/apiClient';
import performanceMonitor from '../../utils/performanceMonitor';

const AdvancedSearch = ({ 
  onResults, 
  contentTypes = ['items', 'activities', 'classes'],
  showFilters = true,
  showSorting = true,
  placeholder = "Search for weapons, armor, activities...",
  className = ""
}) => {
  // Search state
  const [query, setQuery] = useState('');
  const [searchType, setSearchType] = useState('text');
  const [selectedContentTypes, setSelectedContentTypes] = useState(contentTypes);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  
  // Filter state
  const [filters, setFilters] = useState([]);
  const [showFilterPanel, setShowFilterPanel] = useState(false);
  const [availableFields, setAvailableFields] = useState({});
  
  // Sort state
  const [sorts, setSorts] = useState([]);
  const [showSortPanel, setShowSortPanel] = useState(false);
  
  // Suggestion state
  const [suggestions, setSuggestions] = useState([]);
  const [showSuggestions, setShowSuggestions] = useState(false);
  const [selectedSuggestion, setSelectedSuggestion] = useState(-1);
  
  // Facet state
  const [facets, setFacets] = useState({});
  const [showFacets, setShowFacets] = useState(false);
  
  // Search configuration
  const searchTypes = [
    { value: 'text', label: 'Text Search', description: 'Standard text matching' },
    { value: 'fuzzy', label: 'Fuzzy Search', description: 'Tolerates typos and variations' },
    { value: 'exact', label: 'Exact Match', description: 'Exact phrase matching' },
    { value: 'regex', label: 'Regular Expression', description: 'Pattern matching' }
  ];
  
  const contentTypeOptions = [
    { value: 'items', label: 'Items', icon: '🎯', color: 'blue' },
    { value: 'activities', label: 'Activities', icon: '🎮', color: 'green' },
    { value: 'classes', label: 'Classes', icon: '⚡', color: 'purple' },
    { value: 'vendors', label: 'Vendors', icon: '🏪', color: 'orange' },
    { value: 'lore', label: 'Lore', icon: '📚', color: 'yellow' }
  ];
  
  const filterOperators = [
    { value: 'eq', label: 'Equals' },
    { value: 'ne', label: 'Not Equals' },
    { value: 'contains', label: 'Contains' },
    { value: 'starts_with', label: 'Starts With' },
    { value: 'ends_with', label: 'Ends With' },
    { value: 'gt', label: 'Greater Than' },
    { value: 'gte', label: 'Greater Than or Equal' },
    { value: 'lt', label: 'Less Than' },
    { value: 'lte', label: 'Less Than or Equal' },
    { value: 'in', label: 'In List' },
    { value: 'not_in', label: 'Not In List' }
  ];
  
  // Debounced search function
  const debouncedSearch = useCallback(
    debounce(async (searchQuery, searchConfig) => {
      if (!searchQuery.trim() && filters.length === 0) {
        onResults([]);
        setSuggestions([]);
        setFacets({});
        return;
      }
      
      setIsLoading(true);
      setError(null);
      
      const startTime = performance.now();
      
      try {
        const searchPayload = {
          text: searchQuery,
          search_type: searchConfig.type,
          content_types: searchConfig.contentTypes,
          filters: filters,
          sorts: sorts,
          limit: 50,
          offset: 0,
          highlight: true,
          facets: ['tier_name', 'type_name', 'category_hashes']
        };
        
        const response = await apiClient.post('/api/core/search/search', searchPayload);
        
        if (response.data.success) {
          const { results, total_hits, facets: responseFacets, suggestions: responseSuggestions } = response.data.data;
          
          onResults(results, {
            totalHits: total_hits,
            queryTime: response.data.data.query_time,
            pagination: response.data.data.pagination
          });
          
          setFacets(responseFacets || {});
          
          if (responseSuggestions && responseSuggestions.length > 0) {
            setSuggestions(responseSuggestions);
          }
          
          // Record performance
          const duration = performance.now() - startTime;
          performanceMonitor.recordRequest(
            `/api/core/search/search`,
            'POST',
            duration,
            true,
            false
          );
          
        } else {
          throw new Error(response.data.message || 'Search failed');
        }
        
      } catch (err) {
        const duration = performance.now() - startTime;
        setError(err.response?.data?.message || err.message || 'Search failed');
        onResults([]);
        
        performanceMonitor.recordRequest(
          `/api/core/search/search`,
          'POST',
          duration,
          false,
          false
        );
        performanceMonitor.recordError(err, { context: 'AdvancedSearch' });
        
      } finally {
        setIsLoading(false);
      }
    }, 300),
    [filters, sorts, onResults]
  );
  
  // Debounced suggestions function
  const debouncedSuggestions = useCallback(
    debounce(async (partialQuery) => {
      if (partialQuery.length < 2) {
        setSuggestions([]);
        return;
      }
      
      try {
        const response = await apiClient.get('/api/core/search/suggest', {
          params: { q: partialQuery, limit: 8 }
        });
        
        if (response.data.success) {
          setSuggestions(response.data.data.suggestions || []);
        }
      } catch (err) {
        console.warn('Failed to get suggestions:', err);
        setSuggestions([]);
      }
    }, 200),
    []
  );
  
  // Effect to trigger search when parameters change
  useEffect(() => {
    const searchConfig = {
      type: searchType,
      contentTypes: selectedContentTypes
    };
    
    debouncedSearch(query, searchConfig);
  }, [query, searchType, selectedContentTypes, filters, sorts, debouncedSearch]);
  
  // Effect to get suggestions when query changes
  useEffect(() => {
    if (query.trim() && showSuggestions) {
      debouncedSuggestions(query);
    } else {
      setSuggestions([]);
    }
  }, [query, showSuggestions, debouncedSuggestions]);
  
  // Load available filter fields
  useEffect(() => {
    const loadFilterFields = async () => {
      try {
        const response = await apiClient.get('/api/core/search/stats');
        if (response.data.success) {
          // Extract available fields from index statistics
          const fields = {
            items: ['displayProperties.name', 'tier_name', 'type_name', 'category_hashes'],
            activities: ['displayProperties.name', 'activityTypeHash', 'destinationHash'],
            classes: ['displayProperties.name', 'classType']
          };
          setAvailableFields(fields);
        }
      } catch (err) {
        console.warn('Failed to load filter fields:', err);
      }
    };
    
    loadFilterFields();
  }, []);
  
  // Handle query input
  const handleQueryChange = (e) => {
    const newQuery = e.target.value;
    setQuery(newQuery);
    setShowSuggestions(true);
    setSelectedSuggestion(-1);
  };
  
  // Handle search type change
  const handleSearchTypeChange = (type) => {
    setSearchType(type);
  };
  
  // Handle content type toggle
  const handleContentTypeToggle = (type) => {
    setSelectedContentTypes(prev => 
      prev.includes(type) 
        ? prev.filter(t => t !== type)
        : [...prev, type]
    );
  };
  
  // Handle adding filter
  const addFilter = () => {
    const newFilter = {
      id: Date.now(),
      field: '',
      operator: 'eq',
      value: '',
      case_sensitive: false
    };
    setFilters(prev => [...prev, newFilter]);
  };
  
  // Handle updating filter
  const updateFilter = (id, updates) => {
    setFilters(prev => prev.map(filter => 
      filter.id === id ? { ...filter, ...updates } : filter
    ));
  };
  
  // Handle removing filter
  const removeFilter = (id) => {
    setFilters(prev => prev.filter(filter => filter.id !== id));
  };
  
  // Handle adding sort
  const addSort = () => {
    const newSort = {
      id: Date.now(),
      field: '',
      order: 'asc',
      priority: sorts.length + 1
    };
    setSorts(prev => [...prev, newSort]);
  };
  
  // Handle updating sort
  const updateSort = (id, updates) => {
    setSorts(prev => prev.map(sort => 
      sort.id === id ? { ...sort, ...updates } : sort
    ));
  };
  
  // Handle removing sort
  const removeSort = (id) => {
    setSorts(prev => prev.filter(sort => sort.id !== id));
  };
  
  // Handle suggestion selection
  const handleSuggestionSelect = (suggestion) => {
    setQuery(suggestion);
    setShowSuggestions(false);
    setSelectedSuggestion(-1);
  };
  
  // Handle keyboard navigation
  const handleKeyDown = (e) => {
    if (!showSuggestions || suggestions.length === 0) return;
    
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      setSelectedSuggestion(prev => 
        prev < suggestions.length - 1 ? prev + 1 : prev
      );
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      setSelectedSuggestion(prev => prev > 0 ? prev - 1 : -1);
    } else if (e.key === 'Enter' && selectedSuggestion >= 0) {
      e.preventDefault();
      handleSuggestionSelect(suggestions[selectedSuggestion]);
    } else if (e.key === 'Escape') {
      setShowSuggestions(false);
      setSelectedSuggestion(-1);
    }
  };
  
  // Memoized filter fields based on selected content types
  const currentFilterFields = useMemo(() => {
    const fields = new Set();
    selectedContentTypes.forEach(type => {
      if (availableFields[type]) {
        availableFields[type].forEach(field => fields.add(field));
      }
    });
    return Array.from(fields);
  }, [selectedContentTypes, availableFields]);
  
  return (
    <div className={`space-y-4 ${className}`}>
      {/* Main Search Input */}
      <div className="relative">
        <div className="relative">
          <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
            <Search className="h-5 w-5 text-gray-400" />
          </div>
          <input
            type="text"
            value={query}
            onChange={handleQueryChange}
            onKeyDown={handleKeyDown}
            onFocus={() => setShowSuggestions(true)}
            onBlur={() => setTimeout(() => setShowSuggestions(false), 200)}
            placeholder={placeholder}
            className="block w-full pl-10 pr-12 py-3 bg-gray-800 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          />
          <div className="absolute inset-y-0 right-0 pr-3 flex items-center">
            {isLoading ? (
              <Loader className="h-5 w-5 text-blue-400 animate-spin" />
            ) : (
              <div className="flex items-center space-x-2">
                {showFilters && (
                  <button
                    onClick={() => setShowFilterPanel(!showFilterPanel)}
                    className={`p-1 rounded ${showFilterPanel ? 'text-blue-400' : 'text-gray-400 hover:text-gray-300'}`}
                    title="Filters"
                  >
                    <Filter className="h-4 w-4" />
                  </button>
                )}
                {showSorting && (
                  <button
                    onClick={() => setShowSortPanel(!showSortPanel)}
                    className={`p-1 rounded ${showSortPanel ? 'text-blue-400' : 'text-gray-400 hover:text-gray-300'}`}
                    title="Sorting"
                  >
                    <SortAsc className="h-4 w-4" />
                  </button>
                )}
              </div>
            )}
          </div>
        </div>
        
        {/* Error Display */}
        {error && (
          <div className="absolute top-full left-0 right-0 mt-2 p-3 bg-red-900 border border-red-700 rounded-lg text-red-200 text-sm">
            <div className="flex items-center">
              <X className="h-4 w-4 mr-2" />
              {error}
            </div>
          </div>
        )}
        
        {/* Suggestions Dropdown */}
        {showSuggestions && suggestions.length > 0 && (
          <div className="absolute top-full left-0 right-0 mt-1 bg-gray-800 border border-gray-600 rounded-lg shadow-lg z-50">
            {suggestions.map((suggestion, index) => (
              <button
                key={index}
                onClick={() => handleSuggestionSelect(suggestion)}
                className={`w-full px-4 py-2 text-left hover:bg-gray-700 first:rounded-t-lg last:rounded-b-lg ${
                  index === selectedSuggestion ? 'bg-gray-700' : ''
                }`}
              >
                <div className="flex items-center">
                  <Search className="h-3 w-3 mr-2 text-gray-400" />
                  <span className="text-white">{suggestion}</span>
                </div>
              </button>
            ))}
          </div>
        )}
      </div>
      
      {/* Search Type Selection */}
      <div className="flex flex-wrap gap-2">
        {searchTypes.map((type) => (
          <button
            key={type.value}
            onClick={() => handleSearchTypeChange(type.value)}
            className={`px-3 py-1 rounded-full text-sm font-medium transition-colors ${
              searchType === type.value
                ? 'bg-blue-600 text-white'
                : 'bg-gray-800 text-gray-300 hover:bg-gray-700'
            }`}
            title={type.description}
          >
            {type.label}
          </button>
        ))}
      </div>
      
      {/* Content Type Selection */}
      <div className="space-y-2">
        <label className="text-sm font-medium text-gray-400">Search In:</label>
        <div className="flex flex-wrap gap-2">
          {contentTypeOptions.map((type) => (
            <button
              key={type.value}
              onClick={() => handleContentTypeToggle(type.value)}
              className={`px-3 py-2 rounded-lg font-medium transition-colors flex items-center space-x-2 ${
                selectedContentTypes.includes(type.value)
                  ? `bg-${type.color}-600 text-white`
                  : 'bg-gray-800 text-gray-300 hover:bg-gray-700'
              }`}
            >
              <span>{type.icon}</span>
              <span>{type.label}</span>
            </button>
          ))}
        </div>
      </div>
      
      {/* Filter Panel */}
      {showFilterPanel && showFilters && (
        <div className="bg-gray-800 border border-gray-600 rounded-lg p-4 space-y-4">
          <div className="flex items-center justify-between">
            <h3 className="text-sm font-medium text-white">Filters</h3>
            <button
              onClick={addFilter}
              className="px-3 py-1 bg-blue-600 text-white rounded text-sm hover:bg-blue-700"
            >
              Add Filter
            </button>
          </div>
          
          {filters.map((filter) => (
            <FilterRow
              key={filter.id}
              filter={filter}
              fields={currentFilterFields}
              operators={filterOperators}
              onUpdate={(updates) => updateFilter(filter.id, updates)}
              onRemove={() => removeFilter(filter.id)}
            />
          ))}
          
          {filters.length === 0 && (
            <p className="text-gray-400 text-sm">No filters added. Click "Add Filter" to get started.</p>
          )}
        </div>
      )}
      
      {/* Sort Panel */}
      {showSortPanel && showSorting && (
        <div className="bg-gray-800 border border-gray-600 rounded-lg p-4 space-y-4">
          <div className="flex items-center justify-between">
            <h3 className="text-sm font-medium text-white">Sorting</h3>
            <button
              onClick={addSort}
              className="px-3 py-1 bg-blue-600 text-white rounded text-sm hover:bg-blue-700"
            >
              Add Sort
            </button>
          </div>
          
          {sorts.map((sort) => (
            <SortRow
              key={sort.id}
              sort={sort}
              fields={currentFilterFields}
              onUpdate={(updates) => updateSort(sort.id, updates)}
              onRemove={() => removeSort(sort.id)}
            />
          ))}
          
          {sorts.length === 0 && (
            <p className="text-gray-400 text-sm">No sorting applied. Results sorted by relevance.</p>
          )}
        </div>
      )}
      
      {/* Facets Panel */}
      {Object.keys(facets).length > 0 && (
        <div className="bg-gray-800 border border-gray-600 rounded-lg p-4">
          <button
            onClick={() => setShowFacets(!showFacets)}
            className="flex items-center justify-between w-full text-left"
          >
            <h3 className="text-sm font-medium text-white">Refine Results</h3>
            <ChevronDown className={`h-4 w-4 text-gray-400 transition-transform ${showFacets ? 'rotate-180' : ''}`} />
          </button>
          
          {showFacets && (
            <div className="mt-4 space-y-4">
              {Object.entries(facets).map(([field, values]) => (
                <FacetGroup
                  key={field}
                  field={field}
                  values={values}
                  onSelect={(value) => {
                    // Add facet value as filter
                    const newFilter = {
                      id: Date.now(),
                      field: field,
                      operator: 'eq',
                      value: value,
                      case_sensitive: false
                    };
                    setFilters(prev => [...prev, newFilter]);
                  }}
                />
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  );
};

// Filter Row Component
const FilterRow = ({ filter, fields, operators, onUpdate, onRemove }) => {
  return (
    <div className="flex items-center space-x-2">
      <select
        value={filter.field}
        onChange={(e) => onUpdate({ field: e.target.value })}
        className="bg-gray-700 border border-gray-600 rounded px-2 py-1 text-white text-sm"
      >
        <option value="">Select Field</option>
        {fields.map(field => (
          <option key={field} value={field}>{field}</option>
        ))}
      </select>
      
      <select
        value={filter.operator}
        onChange={(e) => onUpdate({ operator: e.target.value })}
        className="bg-gray-700 border border-gray-600 rounded px-2 py-1 text-white text-sm"
      >
        {operators.map(op => (
          <option key={op.value} value={op.value}>{op.label}</option>
        ))}
      </select>
      
      <input
        type="text"
        value={filter.value}
        onChange={(e) => onUpdate({ value: e.target.value })}
        placeholder="Value"
        className="bg-gray-700 border border-gray-600 rounded px-2 py-1 text-white text-sm flex-1"
      />
      
      <button
        onClick={onRemove}
        className="p-1 text-red-400 hover:text-red-300"
        title="Remove Filter"
      >
        <X className="h-4 w-4" />
      </button>
    </div>
  );
};

// Sort Row Component  
const SortRow = ({ sort, fields, onUpdate, onRemove }) => {
  return (
    <div className="flex items-center space-x-2">
      <select
        value={sort.field}
        onChange={(e) => onUpdate({ field: e.target.value })}
        className="bg-gray-700 border border-gray-600 rounded px-2 py-1 text-white text-sm"
      >
        <option value="">Select Field</option>
        {fields.map(field => (
          <option key={field} value={field}>{field}</option>
        ))}
      </select>
      
      <select
        value={sort.order}
        onChange={(e) => onUpdate({ order: e.target.value })}
        className="bg-gray-700 border border-gray-600 rounded px-2 py-1 text-white text-sm"
      >
        <option value="asc">Ascending</option>
        <option value="desc">Descending</option>
      </select>
      
      <button
        onClick={onRemove}
        className="p-1 text-red-400 hover:text-red-300"
        title="Remove Sort"
      >
        <X className="h-4 w-4" />
      </button>
    </div>
  );
};

// Facet Group Component
const FacetGroup = ({ field, values, onSelect }) => {
  const [expanded, setExpanded] = useState(false);
  const displayLimit = 5;
  const valuesToShow = expanded ? Object.entries(values) : Object.entries(values).slice(0, displayLimit);
  
  return (
    <div>
      <h4 className="text-xs font-medium text-gray-300 mb-2 capitalize">
        {field.replace(/([A-Z])/g, ' $1').replace(/_/g, ' ')}
      </h4>
      <div className="space-y-1">
        {valuesToShow.map(([value, count]) => (
          <button
            key={value}
            onClick={() => onSelect(value)}
            className="flex items-center justify-between w-full text-left px-2 py-1 text-sm text-gray-300 hover:bg-gray-700 rounded"
          >
            <span className="truncate">{value}</span>
            <span className="text-xs text-gray-500 ml-2">({count})</span>
          </button>
        ))}
        
        {Object.keys(values).length > displayLimit && (
          <button
            onClick={() => setExpanded(!expanded)}
            className="text-xs text-blue-400 hover:text-blue-300"
          >
            {expanded ? 'Show Less' : `Show ${Object.keys(values).length - displayLimit} More`}
          </button>
        )}
      </div>
    </div>
  );
};

export default AdvancedSearch;