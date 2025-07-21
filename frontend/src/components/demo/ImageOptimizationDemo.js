import React, { useState, useEffect } from 'react';
import demoApiService from '../../services/demo/demoApiService';

const ImageOptimizationDemo = () => {
  const [imageStats, setImageStats] = useState(null);
  const [requestStats, setRequestStats] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [testResults, setTestResults] = useState(null);

  useEffect(() => {
    loadStats();
    // Refresh stats every 5 seconds
    const interval = setInterval(loadStats, 5000);
    return () => clearInterval(interval);
  }, []);

  const loadStats = async () => {
    try {
      const [imgStats, reqStats] = await Promise.all([
        demoApiService.getImagePerformanceMetrics(),
        Promise.resolve(demoApiService.getRequestMetrics())
      ]);
      
      setImageStats(imgStats.cache_statistics);
      setRequestStats(reqStats);
    } catch (error) {
      console.error('Failed to load stats:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const runPerformanceTest = async () => {
    setIsLoading(true);
    try {
      // Test with a known icon
      const testIcon = '/common/destiny2_content/icons/804b3ab35037730a4f93cc33a9282081.jpg';
      const results = await demoApiService.testImagePerformance(testIcon, ['webp', 'jpg']);
      setTestResults(results);
    } catch (error) {
      console.error('Performance test failed:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const clearCache = async () => {
    try {
      demoApiService.clearCache();
      await loadStats();
    } catch (error) {
      console.error('Failed to clear cache:', error);
    }
  };

  const formatBytes = (bytes) => {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  };

  if (isLoading && !imageStats) {
    return (
      <div className="bg-gray-800 rounded-lg p-6">
        <div className="animate-pulse">
          <div className="h-4 bg-gray-700 rounded w-1/4 mb-4"></div>
          <div className="space-y-3">
            <div className="h-3 bg-gray-700 rounded"></div>
            <div className="h-3 bg-gray-700 rounded w-5/6"></div>
            <div className="h-3 bg-gray-700 rounded w-4/6"></div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="bg-gray-800 rounded-lg p-6 space-y-6">
      <div className="flex items-center justify-between">
        <h3 className="text-lg font-semibold text-white">Performance Dashboard</h3>
        <div className="flex space-x-2">
          <button
            onClick={runPerformanceTest}
            className="px-3 py-1 bg-blue-600 hover:bg-blue-700 rounded text-sm transition-colors"
            disabled={isLoading}
          >
            {isLoading ? 'Testing...' : 'Run Test'}
          </button>
          <button
            onClick={clearCache}
            className="px-3 py-1 bg-red-600 hover:bg-red-700 rounded text-sm transition-colors"
          >
            Clear Cache
          </button>
        </div>
      </div>

      {/* Image Cache Statistics */}
      {imageStats && (
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
          <div className="bg-gray-700 rounded-lg p-4 text-center">
            <div className="text-2xl font-bold text-blue-400">
              {imageStats.cache_size_mb?.toFixed(1) || 0} MB
            </div>
            <div className="text-sm text-gray-400">Cache Size</div>
          </div>
          
          <div className="bg-gray-700 rounded-lg p-4 text-center">
            <div className="text-2xl font-bold text-green-400">
              {imageStats.hit_rate_percent?.toFixed(1) || 0}%
            </div>
            <div className="text-sm text-gray-400">Hit Rate</div>
          </div>
          
          <div className="bg-gray-700 rounded-lg p-4 text-center">
            <div className="text-2xl font-bold text-purple-400">
              {imageStats.total_requests || 0}
            </div>
            <div className="text-sm text-gray-400">Total Requests</div>
          </div>
          
          <div className="bg-gray-700 rounded-lg p-4 text-center">
            <div className="text-2xl font-bold text-orange-400">
              {imageStats.downloads || 0}
            </div>
            <div className="text-sm text-gray-400">Downloads</div>
          </div>
        </div>
      )}

      {/* API Request Statistics */}
      {requestStats && (
        <div className="bg-gray-700 rounded-lg p-4">
          <h4 className="font-medium text-white mb-3">API Performance</h4>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm">
            <div>
              <span className="text-gray-400">API Requests:</span>
              <span className="ml-2 text-white font-medium">{requestStats.totalRequests}</span>
            </div>
            <div>
              <span className="text-gray-400">Cache Hits:</span>
              <span className="ml-2 text-green-400 font-medium">{requestStats.cacheHitRate}%</span>
            </div>
            <div>
              <span className="text-gray-400">Avg Response:</span>
              <span className="ml-2 text-blue-400 font-medium">{requestStats.averageTime}ms</span>
            </div>
            <div>
              <span className="text-gray-400">Fastest:</span>
              <span className="ml-2 text-purple-400 font-medium">{requestStats.fastestRequest}ms</span>
            </div>
          </div>
        </div>
      )}

      {/* Performance Test Results */}
      {testResults && (
        <div className="bg-gray-700 rounded-lg p-4">
          <h4 className="font-medium text-white mb-3">Latest Performance Test</h4>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {Object.entries(testResults).map(([format, data]) => (
              <div key={format} className="bg-gray-800 rounded p-3">
                <div className="flex justify-between items-center mb-2">
                  <span className="font-medium text-white capitalize">{format}</span>
                  {data.cacheStatus && (
                    <span className={`px-2 py-1 rounded text-xs ${
                      data.cacheStatus === 'HIT' ? 'bg-green-600' : 'bg-orange-600'
                    }`}>
                      {data.cacheStatus}
                    </span>
                  )}
                </div>
                <div className="space-y-1 text-sm">
                  <div className="flex justify-between">
                    <span className="text-gray-400">Time:</span>
                    <span className="text-white">{data.duration}ms</span>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-gray-400">Size:</span>
                    <span className="text-white">{data.sizeFormatted}</span>
                  </div>
                </div>
              </div>
            ))}
          </div>

          {/* Comparison Summary */}
          {testResults.webp && testResults.jpg && (
            <div className="mt-4 p-3 bg-green-900/20 border border-green-700 rounded">
              <div className="text-sm space-y-1">
                <div className="flex justify-between">
                  <span className="text-green-400">Size Savings:</span>
                  <span className="text-white font-medium">
                    {Math.round((1 - testResults.webp.size / testResults.jpg.size) * 100)}%
                  </span>
                </div>
                <div className="flex justify-between">
                  <span className="text-green-400">Speed Improvement:</span>
                  <span className="text-white font-medium">
                    {Math.round(testResults.jpg.duration / testResults.webp.duration)}x faster
                  </span>
                </div>
              </div>
            </div>
          )}
        </div>
      )}

      {/* Optimization Benefits */}
      <div className="bg-gradient-to-r from-green-900/20 to-blue-900/20 border border-green-700/50 rounded-lg p-4">
        <h4 className="font-medium text-white mb-3">Optimization Benefits</h4>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm">
          <div className="text-center">
            <div className="text-2xl text-green-400 mb-1">📈</div>
            <div className="text-white font-medium">50-80% Smaller</div>
            <div className="text-gray-400">File Size Reduction</div>
          </div>
          <div className="text-center">
            <div className="text-2xl text-blue-400 mb-1">⚡</div>
            <div className="text-white font-medium">10x Faster</div>
            <div className="text-gray-400">Cache Performance</div>
          </div>
          <div className="text-center">
            <div className="text-2xl text-purple-400 mb-1">🎯</div>
            <div className="text-white font-medium">Smart Sizing</div>
            <div className="text-gray-400">Responsive Images</div>
          </div>
        </div>
      </div>

      {/* Status Indicator */}
      <div className="flex items-center justify-center space-x-2 text-sm">
        <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
        <span className="text-green-400">Image optimization system active</span>
      </div>
    </div>
  );
};

export default ImageOptimizationDemo;