import React, { useState } from 'react';
import ItemSearch from '../../components/demo/ItemSearch';
import ItemGrid from '../../components/demo/ItemGrid';
import ItemDetail from '../../components/demo/ItemDetail';
import ImageOptimizationDemo from '../../components/demo/ImageOptimizationDemo';
import ErrorBoundary from '../../components/shared/ErrorBoundary';
import '../../styles/demo.css';

const ImageDemoPage = () => {
  const [selectedItem, setSelectedItem] = useState(null);
  const [searchResults, setSearchResults] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [showPerformanceDemo, setShowPerformanceDemo] = useState(false);

  const handleItemSelect = (item) => {
    setSelectedItem(item);
  };

  const handleBackToSearch = () => {
    setSelectedItem(null);
  };

  const handleSearchResults = (results, loading) => {
    setSearchResults(results);
    setIsLoading(loading);
  };

  return (
    <ErrorBoundary>
      <div className="min-h-screen bg-gray-900 text-white">
        {/* Header */}
        <div className="bg-gray-800 border-b border-gray-700">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
            <div className="flex items-center justify-between">
              <div>
                <h1 className="text-3xl font-bold text-white">
                  Image Optimization Demo
                </h1>
                <p className="mt-2 text-gray-400">
                  Discover Destiny items with lightning-fast image loading
                </p>
              </div>
              <button
                onClick={() => setShowPerformanceDemo(!showPerformanceDemo)}
                className="bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded-lg text-sm font-medium transition-colors"
              >
                {showPerformanceDemo ? 'Hide' : 'Show'} Performance Stats
              </button>
            </div>
          </div>
        </div>

        {/* Performance Demo Widget */}
        {showPerformanceDemo && (
          <div className="bg-gray-800 border-b border-gray-700">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
              <ImageOptimizationDemo />
            </div>
          </div>
        )}

        {/* Main Content */}
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          {selectedItem ? (
            // Detail View
            <ItemDetail 
              item={selectedItem} 
              onBack={handleBackToSearch}
            />
          ) : (
            // Search & Grid View
            <div className="space-y-8">
              {/* Search Interface */}
              <ItemSearch onResults={handleSearchResults} />
              
              {/* Results Grid */}
              <ItemGrid 
                items={searchResults}
                isLoading={isLoading}
                onItemSelect={handleItemSelect}
              />
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="bg-gray-800 border-t border-gray-700 mt-16">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
            <div className="text-center text-gray-400">
              <p>
                This demo showcases WebP optimization, intelligent caching, and responsive image sizing.
              </p>
              <p className="mt-2 text-sm">
                Images load up to 10x faster and use 50% less bandwidth compared to traditional methods.
              </p>
            </div>
          </div>
        </div>
      </div>
    </ErrorBoundary>
  );
};

export default ImageDemoPage;