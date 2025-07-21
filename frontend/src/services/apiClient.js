import BaseService from './base/BaseService';
import { authService } from './authService';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

class ApiClient extends BaseService {
  constructor() {
    // Create a simple API client with token management
    const apiClient = {
      get: (url, config = {}) => this._makeRequest('GET', url, null, config),
      post: (url, data, config = {}) => this._makeRequest('POST', url, data, config),
      put: (url, data, config = {}) => this._makeRequest('PUT', url, data, config),
      delete: (url, config = {}) => this._makeRequest('DELETE', url, null, config)
    };
    
    super(apiClient);
    this.baseURL = API_BASE_URL;
  }

  /**
   * Internal method to make authenticated requests with token management
   */
  async _makeRequest(method, url, data = null, config = {}) {
    const fullUrl = url.startsWith('http') ? url : `${this.baseURL}${url}`;
    
    // Get auth headers
    const token = localStorage.getItem('accessToken');
    const headers = {
      'Content-Type': 'application/json',
      ...config.headers
    };
    
    if (token) {
      headers.Authorization = `Bearer ${token}`;
    }

    const requestConfig = {
      method,
      headers,
      ...config
    };

    if (data && (method === 'POST' || method === 'PUT')) {
      requestConfig.body = JSON.stringify(data);
    }

    try {
      const response = await fetch(fullUrl, requestConfig);
      
      // Handle 401 with token refresh
      if (response.status === 401 && token) {
        const refreshToken = localStorage.getItem('refreshToken');
        if (refreshToken && !config._isRetry) {
          try {
            const tokens = await authService.refreshToken(refreshToken);
            
            // Update stored tokens
            localStorage.setItem('accessToken', tokens.accessToken);
            localStorage.setItem('refreshToken', tokens.refreshToken);
            
            // Retry the original request with new token
            const retryHeaders = {
              ...headers,
              Authorization: `Bearer ${tokens.accessToken}`
            };
            
            const retryResponse = await fetch(fullUrl, {
              ...requestConfig,
              headers: retryHeaders,
              _isRetry: true
            });
            
            if (!retryResponse.ok) {
              throw new Error(`Request failed: ${retryResponse.status}`);
            }
            
            return retryResponse.json();
          } catch (refreshError) {
            // Refresh failed, redirect to login
            localStorage.removeItem('accessToken');
            localStorage.removeItem('refreshToken');
            localStorage.removeItem('userData');
            window.location.href = '/login';
            throw new Error('Authentication failed');
          }
        } else {
          throw new Error('Authentication required');
        }
      }
      
      if (!response.ok) {
        throw new Error(`Request failed: ${response.status}`);
      }
      
      return response.json();
    } catch (error) {
      throw error;
    }
  }

  // Auth endpoints
  async login() {
    const cacheKey = this.createCacheKey('auth/login');
    
    return this.withErrorHandling(
      async () => this._makeRequest('GET', '/auth/login'),
      { cacheKey, cacheTTL: 60000, retry: 1 }
    );
  }

  async exchangeCode(code) {
    return this.withErrorHandling(
      async () => this._makeRequest('POST', '/auth/callback', { code }),
      { retry: 2, deduplicateRequests: false }
    );
  }

  async refreshTokens(refreshToken) {
    return this.withErrorHandling(
      async () => this._makeRequest('POST', '/auth/refresh', { refresh_token: refreshToken }),
      { retry: 2, deduplicateRequests: false }
    );
  }

  // User endpoints
  async getUserProfile() {
    const cacheKey = this.createCacheKey('core/user/profile');
    
    return this.withErrorHandling(
      async () => this._makeRequest('GET', '/core/user/profile'),
      { cacheKey, cacheTTL: 300000, retry: 2 } // 5 minute cache
    );
  }

  async getUserMemberships() {
    const cacheKey = this.createCacheKey('core/user/memberships');
    
    return this.withErrorHandling(
      async () => this._makeRequest('GET', '/core/user/memberships'),
      { cacheKey, cacheTTL: 600000, retry: 2 } // 10 minute cache
    );
  }

  async getCharacters(membershipType, membershipId) {
    const cacheKey = this.createCacheKey('characters', { membershipType, membershipId });
    
    return this.withErrorHandling(
      async () => this._makeRequest('GET', `/core/user/characters/${membershipType}/${membershipId}`),
      { cacheKey, cacheTTL: 300000, retry: 2 } // 5 minute cache
    );
  }

  async getCharacterDetails(membershipType, membershipId, characterId) {
    const cacheKey = this.createCacheKey('character-details', { membershipType, membershipId, characterId });
    
    return this.withErrorHandling(
      async () => this._makeRequest('GET', `/core/user/character/${membershipType}/${membershipId}/${characterId}`),
      { cacheKey, cacheTTL: 300000, retry: 2 } // 5 minute cache
    );
  }

  async getCharacterEquipment(membershipType, membershipId, characterId) {
    const cacheKey = this.createCacheKey('character-equipment', { membershipType, membershipId, characterId });
    
    return this.withErrorHandling(
      async () => this._makeRequest('GET', `/core/user/character/${membershipType}/${membershipId}/${characterId}/equipment`),
      { cacheKey, cacheTTL: 60000, retry: 2 } // 1 minute cache for equipment
    );
  }

  async searchPlayer(bungieName, membershipType) {
    const cacheKey = this.createCacheKey('search-player', { bungieName, membershipType });
    
    return this.withErrorHandling(
      async () => this._makeRequest('POST', `/core/user/search/${membershipType}`, { bungie_name: bungieName }),
      { cacheKey, cacheTTL: 300000, retry: 1 } // 5 minute cache for searches
    );
  }

  // Core endpoints
  async getHealthCheck() {
    return this.withErrorHandling(
      async () => this._makeRequest('GET', '/core/health'),
      { retry: 1, cacheTTL: 30000 } // 30 second cache for health checks
    );
  }

  async getManifest() {
    const cacheKey = this.createCacheKey('core/manifest');
    
    return this.withErrorHandling(
      async () => this._makeRequest('GET', '/core/manifest'),
      { cacheKey, cacheTTL: 3600000, retry: 2 } // 1 hour cache for manifest
    );
  }

  async getSettings() {
    const cacheKey = this.createCacheKey('core/settings');
    
    return this.withErrorHandling(
      async () => this._makeRequest('GET', '/core/settings'),
      { cacheKey, cacheTTL: 600000, retry: 2 } // 10 minute cache for settings
    );
  }

  // Generic request methods with BaseService error handling
  async get(url, config = {}) {
    const cacheKey = config.cacheKey || this.createCacheKey(url);
    
    return this.withErrorHandling(
      async () => this._makeRequest('GET', url, null, config),
      { cacheKey, cacheTTL: config.cacheTTL || 300000, retry: config.retry || 2 }
    );
  }

  async post(url, data = {}, config = {}) {
    return this.withErrorHandling(
      async () => this._makeRequest('POST', url, data, config),
      { retry: config.retry || 2, deduplicateRequests: false }
    );
  }

  async put(url, data = {}, config = {}) {
    return this.withErrorHandling(
      async () => this._makeRequest('PUT', url, data, config),
      { retry: config.retry || 2, deduplicateRequests: false }
    );
  }

  async delete(url, config = {}) {
    return this.withErrorHandling(
      async () => this._makeRequest('DELETE', url, null, config),
      { retry: config.retry || 1, deduplicateRequests: false }
    );
  }
}

export const apiClient = new ApiClient();