/**
 * Base service class for consistent API interaction patterns,
 * error handling, and performance monitoring across the frontend.
 */

import appConfig from '../../config/appConfig';
import performanceMonitor from '../../utils/performanceMonitor';

class APIError extends Error {
  constructor(message, code, details, response) {
    super(message);
    this.name = 'APIError';
    this.code = code;
    this.details = details;
    this.response = response;
  }
}

class NetworkError extends Error {
  constructor(message, originalError) {
    super(message);
    this.name = 'NetworkError';
    this.originalError = originalError;
  }
}

class BaseService {
  constructor(apiClient) {
    this.apiClient = apiClient;
    this.cache = new Map();
    this.pendingRequests = new Map();
    
    // Performance tracking
    this.requestCount = 0;
    this.totalRequestTime = 0;
    this.errorCount = 0;
  }

  /**
   * Execute an operation with consistent error handling and retry logic.
   * @param {Function} operation - The async operation to execute
   * @param {Object} options - Options for retry and caching
   * @returns {Promise<any>} - The operation result
   */
  async withErrorHandling(operation, options = {}) {
    const {
      retry = appConfig.api.retryAttempts,
      retryDelay = appConfig.api.retryDelay,
      cacheKey = null,
      cacheTTL = appConfig.cache.defaultTTL,
      timeout = appConfig.api.timeout,
      deduplicateRequests = appConfig.performance.requestDeduplication
    } = options;

    // Check cache first
    if (cacheKey && this.isCacheValid(cacheKey)) {
      return this.getFromCache(cacheKey);
    }

    // Check for duplicate requests
    if (deduplicateRequests && cacheKey && this.pendingRequests.has(cacheKey)) {
      return this.pendingRequests.get(cacheKey);
    }

    const startTime = performance.now();
    let lastError;

    const executeOperation = async () => {
      try {
        const result = await Promise.race([
          operation(),
          this.createTimeoutPromise(timeout)
        ]);

        // Cache successful result
        if (cacheKey && result) {
          this.setCache(cacheKey, result, cacheTTL);
        }

        // Update performance metrics
        const duration = performance.now() - startTime;
        this.updatePerformanceMetrics(duration, true);
        
        // Record in performance monitor
        if (appConfig.performance.enableMetrics) {
          performanceMonitor.recordRequest(
            'BaseService Request', 
            'UNKNOWN', 
            duration, 
            true, 
            cacheKey && this.isCacheValid(cacheKey)
          );
        }

        return result;
      } catch (error) {
        this.errorCount++;
        throw this.transformError(error);
      } finally {
        // Clean up pending request
        if (cacheKey) {
          this.pendingRequests.delete(cacheKey);
        }
      }
    };

    // Store pending request for deduplication
    if (deduplicateRequests && cacheKey) {
      const promise = executeOperation();
      this.pendingRequests.set(cacheKey, promise);
      return promise;
    }

    // Execute with retry logic
    for (let attempt = 0; attempt <= retry; attempt++) {
      try {
        return await executeOperation();
      } catch (error) {
        lastError = error;
        
        if (attempt < retry && this.shouldRetry(error)) {
          await this.delay(retryDelay * Math.pow(2, attempt)); // Exponential backoff
          continue;
        }
        
        break;
      }
    }

    // All attempts failed
    const duration = performance.now() - startTime;
    this.updatePerformanceMetrics(duration, false);
    
    // Record error in performance monitor
    if (appConfig.performance.enableMetrics) {
      performanceMonitor.recordRequest(
        'BaseService Request', 
        'UNKNOWN', 
        duration, 
        false, 
        false
      );
      performanceMonitor.recordError(lastError, { context: 'BaseService' });
    }
    
    throw lastError;
  }

  /**
   * Determine if an error should trigger a retry.
   * @param {Error} error - The error to check
   * @returns {boolean} - Whether to retry
   */
  shouldRetry(error) {
    if (error instanceof NetworkError) {
      return true;
    }
    
    if (error instanceof APIError) {
      // Retry on server errors and rate limiting
      const retryableStatuses = [429, 500, 502, 503, 504];
      return retryableStatuses.includes(error.response?.status);
    }
    
    return false;
  }

  /**
   * Transform various error types into consistent APIError format.
   * @param {Error} error - The original error
   * @returns {APIError|NetworkError} - Transformed error
   */
  transformError(error) {
    if (error instanceof APIError || error instanceof NetworkError) {
      return error;
    }

    // Handle fetch/axios errors
    if (error.response) {
      // Server responded with error status
      const responseData = error.response.data || {};
      
      return new APIError(
        responseData.error?.message || responseData.message || `HTTP ${error.response.status}`,
        responseData.error?.code || 'HTTP_ERROR',
        responseData.error?.details || responseData,
        error.response
      );
    } else if (error.request) {
      // Network error
      return new NetworkError(
        'Network error - please check your connection',
        error
      );
    } else {
      // Other error
      return new APIError(
        error.message || 'An unexpected error occurred',
        'UNKNOWN_ERROR',
        { originalError: error.toString() }
      );
    }
  }

  /**
   * Create a timeout promise that rejects after specified milliseconds.
   * @param {number} ms - Timeout in milliseconds
   * @returns {Promise} - Promise that rejects on timeout
   */
  createTimeoutPromise(ms) {
    return new Promise((_, reject) => {
      setTimeout(() => {
        reject(new NetworkError(`Request timed out after ${ms}ms`));
      }, ms);
    });
  }

  /**
   * Delay execution for specified milliseconds.
   * @param {number} ms - Delay in milliseconds
   * @returns {Promise} - Promise that resolves after delay
   */
  delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

  /**
   * Check if cached data is still valid.
   * @param {string} key - Cache key
   * @returns {boolean} - Whether cache is valid
   */
  isCacheValid(key) {
    const cached = this.cache.get(key);
    if (!cached) return false;
    
    return Date.now() < cached.expiry;
  }

  /**
   * Get data from cache.
   * @param {string} key - Cache key
   * @returns {any} - Cached data
   */
  getFromCache(key) {
    const cached = this.cache.get(key);
    return cached ? cached.data : null;
  }

  /**
   * Set data in cache with TTL.
   * @param {string} key - Cache key
   * @param {any} data - Data to cache
   * @param {number} ttl - Time to live in milliseconds
   */
  setCache(key, data, ttl) {
    this.cache.set(key, {
      data,
      expiry: Date.now() + ttl,
      createdAt: Date.now()
    });

    // Cleanup old cache entries (simple LRU)
    if (this.cache.size > appConfig.cache.maxSize) {
      const entries = Array.from(this.cache.entries());
      const entriesToRemove = Math.floor(appConfig.cache.maxSize * 0.2); // Remove 20%
      const oldestEntries = entries
        .sort((a, b) => a[1].createdAt - b[1].createdAt)
        .slice(0, entriesToRemove);
      
      oldestEntries.forEach(([key]) => this.cache.delete(key));
    }
  }

  /**
   * Clear all cached data.
   */
  clearCache() {
    this.cache.clear();
    this.pendingRequests.clear();
  }

  /**
   * Clear specific cache entry.
   * @param {string} key - Cache key to clear
   */
  clearCacheEntry(key) {
    this.cache.delete(key);
    this.pendingRequests.delete(key);
  }

  /**
   * Update performance tracking metrics.
   * @param {number} duration - Request duration in milliseconds
   * @param {boolean} success - Whether request was successful
   */
  updatePerformanceMetrics(duration, success) {
    this.requestCount++;
    this.totalRequestTime += duration;
    
    if (!success) {
      this.errorCount++;
    }
  }

  /**
   * Get performance statistics for this service.
   * @returns {Object} - Performance stats
   */
  getPerformanceStats() {
    return {
      requestCount: this.requestCount,
      errorCount: this.errorCount,
      successRate: this.requestCount > 0 ? 
        ((this.requestCount - this.errorCount) / this.requestCount * 100).toFixed(1) : 0,
      averageRequestTime: this.requestCount > 0 ? 
        (this.totalRequestTime / this.requestCount).toFixed(1) : 0,
      totalRequestTime: this.totalRequestTime.toFixed(1),
      cacheSize: this.cache.size,
      pendingRequests: this.pendingRequests.size
    };
  }

  /**
   * Reset performance tracking statistics.
   */
  resetPerformanceStats() {
    this.requestCount = 0;
    this.totalRequestTime = 0;
    this.errorCount = 0;
  }

  /**
   * Create a cache key from parameters.
   * @param {string} endpoint - API endpoint
   * @param {Object} params - Request parameters
   * @returns {string} - Cache key
   */
  createCacheKey(endpoint, params = {}) {
    const sortedParams = Object.keys(params)
      .sort()
      .map(key => `${key}=${params[key]}`)
      .join('&');
    
    return `${endpoint}${sortedParams ? `?${sortedParams}` : ''}`;
  }

  /**
   * Batch multiple requests with error handling.
   * @param {Array<Function>} requests - Array of request functions
   * @param {Object} options - Batch options
   * @returns {Promise<Array>} - Array of results
   */
  async batchRequests(requests, options = {}) {
    const { concurrency = 5, continueOnError = true } = options;
    
    const results = [];
    
    for (let i = 0; i < requests.length; i += concurrency) {
      const batch = requests.slice(i, i + concurrency);
      
      const batchPromises = batch.map(async (request, index) => {
        try {
          return await this.withErrorHandling(request, options);
        } catch (error) {
          if (continueOnError) {
            console.warn(`Batch request ${i + index} failed:`, error);
            return { error, index: i + index };
          }
          throw error;
        }
      });
      
      const batchResults = await Promise.all(batchPromises);
      results.push(...batchResults);
    }
    
    return results;
  }
}

// Export error classes for use in other services
export { APIError, NetworkError };
export default BaseService;