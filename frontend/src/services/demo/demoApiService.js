import BaseService from '../base/BaseService';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5001/api';

class DemoApiService extends BaseService {
  constructor() {
    // Create a simple API client
    const apiClient = {
      get: (url, config = {}) => fetch(url, { method: 'GET', ...config }).then(res => res.json()),
      post: (url, data, config = {}) => fetch(url, { 
        method: 'POST', 
        headers: { 'Content-Type': 'application/json', ...config.headers },
        body: JSON.stringify(data),
        ...config 
      }).then(res => res.json())
    };
    
    super(apiClient);
    this.baseUrl = API_BASE_URL;
  }

  async searchItems(query, options = {}) {
    const params = new URLSearchParams({
      q: query,
      limit: options.limit || 20,
      offset: options.offset || 0,
      ...options.filters
    });

    const cacheKey = this.createCacheKey('search', { query, ...options });
    
    return this.withErrorHandling(
      async () => {
        const response = await fetch(`${this.baseUrl}/manifest/items/search?${params}`);
        
        if (!response.ok) {
          throw new Error(`Search failed: ${response.status}`);
        }
        
        return response.json();
      },
      {
        cacheKey,
        cacheTTL: 300000, // 5 minutes
        retry: 2
      }
    );
  }

  async getItemDetails(itemHash) {
    const cacheKey = this.createCacheKey('item', { hash: itemHash });
    
    return this.withErrorHandling(
      async () => {
        const response = await fetch(`${this.baseUrl}/manifest/items/${itemHash}`);
        
        if (!response.ok) {
          throw new Error(`Item fetch failed: ${response.status}`);
        }
        
        return response.json();
      },
      {
        cacheKey,
        cacheTTL: 600000, // 10 minutes for item details
        retry: 2
      }
    );
  }

  async getImagePerformanceMetrics() {
    return this.withErrorHandling(
      async () => {
        const response = await fetch(`${this.baseUrl}/images/cache/stats`);
        
        if (!response.ok) {
          throw new Error(`Metrics fetch failed: ${response.status}`);
        }
        
        return response.json();
      },
      {
        cacheTTL: 10000, // 10 seconds for metrics
        retry: 1
      }
    ).catch(() => {
      // Return default metrics on error
      return {
        cache_statistics: {
          cache_size_mb: 0,
          hit_rate_percent: 0,
          total_requests: 0,
          cache_hits: 0,
          downloads: 0,
          errors: 0
        }
      };
    });
  }

  // Image loading performance testing
  async testImagePerformance(iconPath, formats = ['webp', 'jpg']) {
    const results = {};
    
    for (const format of formats) {
      const startTime = performance.now();
      
      try {
        const imageUrl = format === 'original' 
          ? `https://bungie.net${iconPath}`
          : `${this.baseUrl}/images/proxy${iconPath}?format=${format}&size=medium`;
        
        const response = await fetch(imageUrl);
        
        if (!response.ok) {
          throw new Error(`Image fetch failed: ${response.status}`);
        }
        
        const blob = await response.blob();
        const duration = performance.now() - startTime;
        
        results[format] = {
          duration: Math.round(duration),
          size: blob.size,
          sizeFormatted: this.formatBytes(blob.size),
          url: imageUrl,
          cacheStatus: response.headers.get('X-Cache-Status') || 'UNKNOWN'
        };
      } catch (error) {
        results[format] = {
          error: error.message,
          duration: -1,
          size: 0
        };
      }
    }
    
    return results;
  }

  // Override base class method to include additional metrics
  getRequestMetrics() {
    const baseStats = this.getPerformanceStats();
    
    return {
      totalRequests: baseStats.requestCount,
      cacheHits: baseStats.requestCount - baseStats.errorCount, // Approximate
      cacheHitRate: baseStats.successRate,
      averageTime: baseStats.averageRequestTime,
      fastestRequest: '0', // Not tracked in base class
      slowestRequest: '0'  // Not tracked in base class
    };
  }

  formatBytes(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  }

  // Override base class clearCache to also reset performance stats
  clearCache() {
    super.clearCache();
    this.resetPerformanceStats();
  }
}

// Create and export a singleton instance
const demoApiService = new DemoApiService();
export default demoApiService;