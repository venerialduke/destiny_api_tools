/**
 * Base service exports for consistent service architecture
 */

export { default as BaseService, APIError, NetworkError } from './BaseService';

// Common service utilities
export const ServiceUtils = {
  /**
   * Create a standard cache key for API requests
   */
  createCacheKey: (endpoint, params = {}) => {
    const sortedParams = Object.keys(params)
      .sort()
      .map(key => `${key}=${params[key]}`)
      .join('&');
    
    return `${endpoint}${sortedParams ? `?${sortedParams}` : ''}`;
  },

  /**
   * Format error for user display
   */
  formatError: (error) => {
    if (error instanceof APIError) {
      return {
        title: 'API Error',
        message: error.message,
        code: error.code,
        canRetry: error.response?.status >= 500 || error.response?.status === 429
      };
    } else if (error instanceof NetworkError) {
      return {
        title: 'Connection Error',
        message: 'Unable to connect to the server. Please check your internet connection.',
        code: 'NETWORK_ERROR',
        canRetry: true
      };
    } else {
      return {
        title: 'Unexpected Error',
        message: error.message || 'An unexpected error occurred',
        code: 'UNKNOWN_ERROR',
        canRetry: false
      };
    }
  },

  /**
   * Validate required parameters
   */
  validateParams: (params, required = []) => {
    const missing = required.filter(param => 
      params[param] === undefined || params[param] === null || params[param] === ''
    );
    
    if (missing.length > 0) {
      throw new Error(`Missing required parameters: ${missing.join(', ')}`);
    }
  },

  /**
   * Debounce function for search/input handling
   */
  debounce: (func, wait) => {
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
};