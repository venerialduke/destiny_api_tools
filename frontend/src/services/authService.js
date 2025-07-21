import BaseService from './base/BaseService';
import { tokenStorage } from '../utils/secureStorage';
import appConfig from '../config/appConfig';

const API_BASE_URL = appConfig.api.baseURL;

class AuthService extends BaseService {
  constructor() {
    // Create a simple API client for auth requests
    const apiClient = {
      get: (url, config = {}) => fetch(url, { 
        method: 'GET', 
        headers: { 'Content-Type': 'application/json' },
        ...config 
      }).then(res => res.json()),
      post: (url, data, config = {}) => fetch(url, { 
        method: 'POST', 
        headers: { 'Content-Type': 'application/json', ...config.headers },
        body: JSON.stringify(data),
        ...config 
      }).then(res => res.json())
    };
    
    super(apiClient);
    this.baseURL = `${API_BASE_URL}/auth`;
  }

  async getAuthUrl() {
    console.log('🔐 FRONTEND AUTH: getAuthUrl() called');
    console.log(`🔐 FRONTEND AUTH: Request URL: ${this.baseURL}/login`);
    console.log(`🔐 FRONTEND AUTH: API Base URL: ${API_BASE_URL}`);
    
    const cacheKey = this.createCacheKey('auth-url');
    
    return this.withErrorHandling(
      async () => {
        console.log('🔐 FRONTEND AUTH: Making fetch request...');
        
        const response = await fetch(`${this.baseURL}/login`);
        
        console.log(`🔐 FRONTEND AUTH: Response status: ${response.status}`);
        console.log(`🔐 FRONTEND AUTH: Response ok: ${response.ok}`);
        console.log(`🔐 FRONTEND AUTH: Response headers:`, Object.fromEntries(response.headers.entries()));
        
        if (!response.ok) {
          const errorText = await response.text();
          console.error(`❌ FRONTEND AUTH ERROR: ${response.status} - ${errorText}`);
          throw new Error(`Auth URL request failed: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('🔐 FRONTEND AUTH: Response data:', data);
        
        // Store state for CSRF protection using secure storage
        if (data.state) {
          console.log('🔐 FRONTEND AUTH: Storing OAuth state');
          tokenStorage.setItem('oauth_state', data.state, { 
            ttl: 10 * 60 * 1000, // 10 minutes
            persistent: false 
          });
        }
        
        console.log(`🔐 FRONTEND AUTH: Returning auth URL: ${data.auth_url}`);
        return data.auth_url;
      },
      {
        cacheKey,
        cacheTTL: 60000, // 1 minute cache for auth URLs
        retry: 1
      }
    );
  }

  async exchangeCodeForTokens(code) {
    return this.withErrorHandling(
      async () => {
        const response = await fetch(`${this.baseURL}/callback`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ code })
        });
        
        if (!response.ok) {
          throw new Error(`Token exchange failed: ${response.status}`);
        }
        
        const data = await response.json();
        
        const tokens = {
          accessToken: data.access_token,
          refreshToken: data.refresh_token,
          expiresIn: data.expires_in,
          userData: data.user_data
        };
        
        // Store tokens securely
        tokenStorage.setTokens(tokens);
        
        return tokens;
      },
      {
        retry: 2,
        deduplicateRequests: false // Don't cache token exchanges
      }
    );
  }

  async refreshToken(refreshToken) {
    return this.withErrorHandling(
      async () => {
        const response = await fetch(`${this.baseURL}/refresh`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ refresh_token: refreshToken })
        });
        
        if (!response.ok) {
          throw new Error(`Token refresh failed: ${response.status}`);
        }
        
        const data = await response.json();
        
        const tokens = {
          accessToken: data.access_token,
          refreshToken: data.refresh_token,
          expiresIn: data.expires_in
        };
        
        // Update stored tokens
        tokenStorage.updateAccessToken(tokens.accessToken, tokens.expiresIn);
        
        return tokens;
      },
      {
        retry: 2,
        deduplicateRequests: false // Don't cache token refreshes
      }
    );
  }

  async logout() {
    return this.withErrorHandling(
      async () => {
        const response = await fetch(`${this.baseURL}/logout`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' }
        });
        
        if (!response.ok) {
          throw new Error(`Logout failed: ${response.status}`);
        }
        
        return response.json();
      },
      {
        retry: 1,
        deduplicateRequests: false
      }
    ).catch(error => {
      // Logout can fail but we should still clear local storage
      console.error('Logout request failed:', error);
      return null; // Return null on failure to allow cleanup
    }).finally(() => {
      // Always clear tokens on logout
      tokenStorage.clearTokens();
    });
  }

  /**
   * Get current access token
   */
  getAccessToken() {
    return tokenStorage.getAccessToken();
  }

  /**
   * Get current refresh token
   */
  getRefreshToken() {
    return tokenStorage.getRefreshToken();
  }

  /**
   * Get current user data
   */
  getUserData() {
    return tokenStorage.getUserData();
  }

  /**
   * Check if user is authenticated
   */
  isAuthenticated() {
    return tokenStorage.isAuthenticated();
  }

  /**
   * Check if token needs refresh
   */
  shouldRefreshToken() {
    return tokenStorage.isTokenExpiringSoon();
  }

  /**
   * Clear all authentication data
   */
  clearAuthData() {
    tokenStorage.clearTokens();
  }

  getAuthHeaders(token) {
    return {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    };
  }
}

export const authService = new AuthService();