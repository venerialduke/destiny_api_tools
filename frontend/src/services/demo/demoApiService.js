const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5001/api';

class DemoApiService {
  constructor() {
    this.cache = new Map();
    this.requestMetrics = {
      totalRequests: 0,
      cacheHits: 0,
      totalTime: 0,
      fastestRequest: Infinity,
      slowestRequest: 0
    };
  }

  async searchItems(query, options = {}) {
    const startTime = performance.now();
    
    try {
      const params = new URLSearchParams({
        q: query,
        limit: options.limit || 20,
        offset: options.offset || 0,
        ...options.filters
      });

      const cacheKey = `search_${params.toString()}`;
      
      // Check cache first
      if (this.cache.has(cacheKey)) {
        this.requestMetrics.cacheHits++;
        this.requestMetrics.totalRequests++;
        return this.cache.get(cacheKey);
      }

      const response = await fetch(`${API_BASE_URL}/manifest/items/search?${params}`);
      
      if (!response.ok) {
        throw new Error(`Search failed: ${response.status}`);
      }

      const data = await response.json();
      
      // Cache the result
      this.cache.set(cacheKey, data);
      
      // Update metrics
      const duration = performance.now() - startTime;
      this.updateMetrics(duration);
      
      return data;
    } catch (error) {
      console.error('Search error:', error);
      throw error;
    }
  }

  async getItemDetails(itemHash) {
    const startTime = performance.now();
    
    try {
      const cacheKey = `item_${itemHash}`;
      
      // Check cache first
      if (this.cache.has(cacheKey)) {
        this.requestMetrics.cacheHits++;
        this.requestMetrics.totalRequests++;
        return this.cache.get(cacheKey);
      }

      const response = await fetch(`${API_BASE_URL}/manifest/items/${itemHash}`);
      
      if (!response.ok) {
        throw new Error(`Item fetch failed: ${response.status}`);
      }

      const data = await response.json();
      
      // Cache the result
      this.cache.set(cacheKey, data);
      
      // Update metrics
      const duration = performance.now() - startTime;
      this.updateMetrics(duration);
      
      return data;
    } catch (error) {
      console.error('Item details error:', error);
      throw error;
    }
  }

  async getImagePerformanceMetrics() {
    try {
      const response = await fetch(`${API_BASE_URL}/images/cache/stats`);
      
      if (!response.ok) {
        throw new Error(`Metrics fetch failed: ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      console.error('Metrics error:', error);
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
    }
  }

  // Image loading performance testing
  async testImagePerformance(iconPath, formats = ['webp', 'jpg']) {
    const results = {};
    
    for (const format of formats) {
      const startTime = performance.now();
      
      try {
        const imageUrl = format === 'original' 
          ? `https://bungie.net${iconPath}`
          : `${API_BASE_URL}/images/proxy${iconPath}?format=${format}&size=medium`;
        
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

  updateMetrics(duration) {
    this.requestMetrics.totalRequests++;
    this.requestMetrics.totalTime += duration;
    this.requestMetrics.fastestRequest = Math.min(this.requestMetrics.fastestRequest, duration);
    this.requestMetrics.slowestRequest = Math.max(this.requestMetrics.slowestRequest, duration);
  }

  getRequestMetrics() {
    const { totalRequests, cacheHits, totalTime, fastestRequest, slowestRequest } = this.requestMetrics;
    
    return {
      totalRequests,
      cacheHits,
      cacheHitRate: totalRequests > 0 ? (cacheHits / totalRequests * 100).toFixed(1) : 0,
      averageTime: totalRequests > 0 ? (totalTime / totalRequests).toFixed(1) : 0,
      fastestRequest: fastestRequest === Infinity ? 0 : fastestRequest.toFixed(1),
      slowestRequest: slowestRequest.toFixed(1)
    };
  }

  formatBytes(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  }

  clearCache() {
    this.cache.clear();
    this.requestMetrics = {
      totalRequests: 0,
      cacheHits: 0,
      totalTime: 0,
      fastestRequest: Infinity,
      slowestRequest: 0
    };
  }
}

// Create and export a singleton instance
const demoApiService = new DemoApiService();
export default demoApiService;