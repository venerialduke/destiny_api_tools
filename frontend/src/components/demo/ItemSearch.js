import React, { useState, useEffect, useCallback } from 'react';
import demoApiService from '../../services/demo/demoApiService';

const ItemSearch = ({ onResults }) => {
  const [query, setQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('all');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const categories = [
    { value: 'all', label: 'All Items', icon: '🔍' },
    { value: 'weapon', label: 'Weapons', icon: '⚔️' },
    { value: 'armor', label: 'Armor', icon: '🛡️' },
    { value: 'consumable', label: 'Consumables', icon: '💊' },
    { value: 'mod', label: 'Mods', icon: '🔧' }
  ];

  // Debounced search function
  const debouncedSearch = useCallback(
    debounce(async (searchQuery, category) => {
      if (!searchQuery.trim() && category === 'all') {
        onResults([], false);
        return;
      }

      setIsLoading(true);
      setError(null);

      try {
        const filters = category !== 'all' ? { [category]: 'true' } : {};
        const results = await demoApiService.searchItems(searchQuery, { filters });
        onResults(results.items || [], false);
      } catch (err) {
        setError(err.message);
        onResults([], false);
      } finally {
        setIsLoading(false);
      }
    }, 300),
    [onResults]
  );

  // Effect to trigger search when query or category changes
  useEffect(() => {
    debouncedSearch(query, selectedCategory);
  }, [query, selectedCategory, debouncedSearch]);

  const handleQueryChange = (e) => {
    setQuery(e.target.value);
  };

  const handleCategoryChange = (category) => {
    setSelectedCategory(category);
  };

  const handleQuickSearch = (quickQuery) => {
    setQuery(quickQuery);
  };

  const quickSearchTerms = [
    'Gjallarhorn', 'Ace of Spades', 'Thorn', 'Last Word', 'Fatebringer',
    'Vex Mythoclast', 'Hawkmoon', 'Outbreak', 'Whisper'
  ];

  return (
    <div className="space-y-6">
      {/* Search Input */}
      <div className="relative">
        <div className="relative">
          <input
            type="text"
            value={query}
            onChange={handleQueryChange}
            placeholder="Search for weapons, armor, or any Destiny item..."
            className="w-full px-4 py-3 bg-gray-800 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          />
          <div className="absolute right-3 top-3">
            {isLoading ? (
              <div className="animate-spin rounded-full h-6 w-6 border-b-2 border-blue-500"></div>
            ) : (
              <svg className="h-6 w-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
            )}
          </div>
        </div>
        
        {error && (
          <div className="absolute top-full left-0 right-0 mt-2 p-3 bg-red-900 border border-red-700 rounded-lg text-red-200 text-sm">
            <div className="flex items-center">
              <svg className="h-4 w-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              Error: {error}
            </div>
          </div>
        )}
      </div>

      {/* Category Filters */}
      <div className="flex flex-wrap gap-2">
        {categories.map((category) => (
          <button
            key={category.value}
            onClick={() => handleCategoryChange(category.value)}
            className={`px-4 py-2 rounded-lg font-medium transition-colors flex items-center space-x-2 ${
              selectedCategory === category.value
                ? 'bg-blue-600 text-white'
                : 'bg-gray-800 text-gray-300 hover:bg-gray-700'
            }`}
          >
            <span>{category.icon}</span>
            <span>{category.label}</span>
          </button>
        ))}
      </div>

      {/* Quick Search Suggestions */}
      <div className="space-y-3">
        <h3 className="text-sm font-medium text-gray-400">Quick Search:</h3>
        <div className="flex flex-wrap gap-2">
          {quickSearchTerms.map((term) => (
            <button
              key={term}
              onClick={() => handleQuickSearch(term)}
              className="px-3 py-1 text-sm bg-gray-800 text-gray-300 rounded-full hover:bg-gray-700 transition-colors"
            >
              {term}
            </button>
          ))}
        </div>
      </div>

      {/* Search Stats */}
      {(query || selectedCategory !== 'all') && (
        <div className="text-sm text-gray-400 flex items-center space-x-4">
          <span>
            {isLoading ? 'Searching...' : `Search for "${query || selectedCategory}"`}
          </span>
          <div className="flex items-center space-x-2">
            <span className="w-2 h-2 bg-green-500 rounded-full"></span>
            <span>Optimized images enabled</span>
          </div>
        </div>
      )}
    </div>
  );
};

// Debounce utility function
function debounce(func, wait) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}

export default ItemSearch;