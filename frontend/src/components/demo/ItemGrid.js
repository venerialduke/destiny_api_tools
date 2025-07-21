import React from 'react';
import ItemCard from './ItemCard';

const ItemGrid = ({ items, isLoading, onItemSelect }) => {
  if (isLoading) {
    return (
      <div className="space-y-4">
        <div className="text-center py-8">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500 mx-auto"></div>
          <p className="mt-4 text-gray-400">Searching for items...</p>
        </div>
      </div>
    );
  }

  if (!items || items.length === 0) {
    return (
      <div className="text-center py-12">
        <div className="text-6xl mb-4">🔍</div>
        <h3 className="text-xl font-medium text-gray-300 mb-2">No items found</h3>
        <p className="text-gray-400">
          Try searching for weapons like "Gjallarhorn" or "Ace of Spades"
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Results Header */}
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-xl font-semibold text-white">
            Search Results ({items.length} items)
          </h2>
          <p className="text-gray-400 text-sm mt-1">
            All images are optimized with WebP format and intelligent caching
          </p>
        </div>
        
        {/* Performance Indicator */}
        <div className="flex items-center space-x-2 text-sm">
          <div className="flex items-center space-x-1">
            <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
            <span className="text-green-400">Fast Loading</span>
          </div>
          <div className="flex items-center space-x-1">
            <div className="w-2 h-2 bg-blue-500 rounded-full"></div>
            <span className="text-blue-400">WebP Optimized</span>
          </div>
        </div>
      </div>

      {/* Items Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4">
        {items.map((item, index) => (
          <ItemCard
            key={item.hash || index}
            item={item}
            onClick={() => onItemSelect(item)}
            priority={index < 10} // Prioritize loading for first 10 items
          />
        ))}
      </div>

      {/* Load More Hint */}
      {items.length >= 20 && (
        <div className="text-center py-6">
          <p className="text-gray-400 text-sm">
            Showing first {items.length} results. Try more specific search terms for better results.
          </p>
        </div>
      )}
    </div>
  );
};

export default ItemGrid;