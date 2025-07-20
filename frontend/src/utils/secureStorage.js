/**
 * Secure storage utility for handling sensitive data like authentication tokens.
 * Provides encrypted storage with automatic expiration and security features.
 */

import appConfig from '../config/appConfig';

class SecureStorage {
  constructor() {
    this.storagePrefix = 'destiny_api_';
    this.encryptionEnabled = appConfig.isProduction();
    this.defaultTTL = appConfig.cache.userDataTTL;
  }

  /**
   * Simple encryption for sensitive data (in production, use proper encryption)
   */
  _encrypt(data) {
    if (!this.encryptionEnabled) {
      return data;
    }

    // Simple XOR encryption for demo - use proper encryption in production
    const key = this._getEncryptionKey();
    const encrypted = data.split('').map((char, i) => 
      String.fromCharCode(char.charCodeAt(0) ^ key.charCodeAt(i % key.length))
    ).join('');
    
    return btoa(encrypted); // Base64 encode
  }

  /**
   * Simple decryption for sensitive data
   */
  _decrypt(encryptedData) {
    if (!this.encryptionEnabled) {
      return encryptedData;
    }

    try {
      const key = this._getEncryptionKey();
      const decoded = atob(encryptedData);
      
      const decrypted = decoded.split('').map((char, i) => 
        String.fromCharCode(char.charCodeAt(0) ^ key.charCodeAt(i % key.length))
      ).join('');
      
      return decrypted;
    } catch (error) {
      console.error('Decryption failed:', error);
      return null;
    }
  }

  /**
   * Get encryption key (in production, derive from more secure source)
   */
  _getEncryptionKey() {
    return 'destiny-api-tools-key-' + window.location.hostname;
  }

  /**
   * Create storage item with metadata
   */
  _createStorageItem(value, ttl = this.defaultTTL) {
    return {
      value: this._encrypt(JSON.stringify(value)),
      timestamp: Date.now(),
      ttl: ttl,
      version: '1.0'
    };
  }

  /**
   * Parse storage item and validate
   */
  _parseStorageItem(item) {
    try {
      const parsed = JSON.parse(item);
      
      // Check if item has expired
      if (parsed.ttl > 0 && Date.now() > parsed.timestamp + parsed.ttl) {
        return null;
      }

      // Decrypt and parse value
      const decryptedValue = this._decrypt(parsed.value);
      if (decryptedValue === null) {
        return null;
      }

      return JSON.parse(decryptedValue);
    } catch (error) {
      console.error('Error parsing storage item:', error);
      return null;
    }
  }

  /**
   * Store sensitive data securely
   */
  setItem(key, value, options = {}) {
    try {
      const { ttl = this.defaultTTL, persistent = false } = options;
      const fullKey = this.storagePrefix + key;
      const storageItem = this._createStorageItem(value, ttl);
      
      const storage = persistent ? localStorage : sessionStorage;
      storage.setItem(fullKey, JSON.stringify(storageItem));
      
      return true;
    } catch (error) {
      console.error('Error storing item:', error);
      return false;
    }
  }

  /**
   * Retrieve and decrypt sensitive data
   */
  getItem(key) {
    try {
      const fullKey = this.storagePrefix + key;
      
      // Try sessionStorage first, then localStorage
      let item = sessionStorage.getItem(fullKey);
      if (!item) {
        item = localStorage.getItem(fullKey);
      }
      
      if (!item) {
        return null;
      }

      const value = this._parseStorageItem(item);
      
      // Remove expired item
      if (value === null) {
        this.removeItem(key);
        return null;
      }

      return value;
    } catch (error) {
      console.error('Error retrieving item:', error);
      return null;
    }
  }

  /**
   * Remove item from storage
   */
  removeItem(key) {
    try {
      const fullKey = this.storagePrefix + key;
      sessionStorage.removeItem(fullKey);
      localStorage.removeItem(fullKey);
      return true;
    } catch (error) {
      console.error('Error removing item:', error);
      return false;
    }
  }

  /**
   * Check if item exists and is not expired
   */
  hasItem(key) {
    return this.getItem(key) !== null;
  }

  /**
   * Clear all app-related storage items
   */
  clear() {
    try {
      const keysToRemove = [];
      
      // Find all keys with our prefix
      for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        if (key && key.startsWith(this.storagePrefix)) {
          keysToRemove.push(key);
        }
      }
      
      for (let i = 0; i < sessionStorage.length; i++) {
        const key = sessionStorage.key(i);
        if (key && key.startsWith(this.storagePrefix)) {
          keysToRemove.push(key);
        }
      }
      
      // Remove all found keys
      keysToRemove.forEach(key => {
        localStorage.removeItem(key);
        sessionStorage.removeItem(key);
      });
      
      return true;
    } catch (error) {
      console.error('Error clearing storage:', error);
      return false;
    }
  }

  /**
   * Clean up expired items
   */
  cleanup() {
    try {
      const now = Date.now();
      const keysToRemove = [];
      
      // Check localStorage
      for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        if (key && key.startsWith(this.storagePrefix)) {
          try {
            const item = JSON.parse(localStorage.getItem(key));
            if (item.ttl > 0 && now > item.timestamp + item.ttl) {
              keysToRemove.push({ storage: localStorage, key });
            }
          } catch (error) {
            // Remove corrupted items
            keysToRemove.push({ storage: localStorage, key });
          }
        }
      }
      
      // Check sessionStorage
      for (let i = 0; i < sessionStorage.length; i++) {
        const key = sessionStorage.key(i);
        if (key && key.startsWith(this.storagePrefix)) {
          try {
            const item = JSON.parse(sessionStorage.getItem(key));
            if (item.ttl > 0 && now > item.timestamp + item.ttl) {
              keysToRemove.push({ storage: sessionStorage, key });
            }
          } catch (error) {
            // Remove corrupted items
            keysToRemove.push({ storage: sessionStorage, key });
          }
        }
      }
      
      // Remove expired items
      keysToRemove.forEach(({ storage, key }) => {
        storage.removeItem(key);
      });
      
      return keysToRemove.length;
    } catch (error) {
      console.error('Error during cleanup:', error);
      return 0;
    }
  }
}

/**
 * Token-specific storage utilities
 */
class TokenStorage extends SecureStorage {
  constructor() {
    super();
    this.tokenKeys = {
      accessToken: 'auth_access_token',
      refreshToken: 'auth_refresh_token',
      userData: 'auth_user_data',
      tokenExpiry: 'auth_token_expiry'
    };
  }

  /**
   * Store authentication tokens securely
   */
  setTokens(tokens) {
    const { accessToken, refreshToken, expiresIn, userData } = tokens;
    const expiryTime = Date.now() + (expiresIn * 1000);

    const success = [
      this.setItem(this.tokenKeys.accessToken, accessToken, { 
        ttl: expiresIn * 1000, 
        persistent: false // Access tokens should not persist across sessions
      }),
      this.setItem(this.tokenKeys.refreshToken, refreshToken, { 
        ttl: 30 * 24 * 60 * 60 * 1000, // 30 days
        persistent: true // Refresh tokens can persist
      }),
      this.setItem(this.tokenKeys.tokenExpiry, expiryTime, { 
        ttl: expiresIn * 1000, 
        persistent: false 
      })
    ];

    if (userData) {
      success.push(this.setItem(this.tokenKeys.userData, userData, { 
        ttl: this.defaultTTL, 
        persistent: true 
      }));
    }

    return success.every(Boolean);
  }

  /**
   * Get access token if valid
   */
  getAccessToken() {
    const token = this.getItem(this.tokenKeys.accessToken);
    const expiry = this.getItem(this.tokenKeys.tokenExpiry);
    
    if (!token || !expiry) {
      return null;
    }

    // Check if token is expired (with 5 minute buffer)
    const bufferTime = 5 * 60 * 1000; // 5 minutes
    if (Date.now() >= expiry - bufferTime) {
      this.clearTokens();
      return null;
    }

    return token;
  }

  /**
   * Get refresh token
   */
  getRefreshToken() {
    return this.getItem(this.tokenKeys.refreshToken);
  }

  /**
   * Get user data
   */
  getUserData() {
    return this.getItem(this.tokenKeys.userData);
  }

  /**
   * Check if user is authenticated
   */
  isAuthenticated() {
    return this.getAccessToken() !== null;
  }

  /**
   * Check if access token is close to expiry
   */
  isTokenExpiringSoon(bufferMinutes = 10) {
    const expiry = this.getItem(this.tokenKeys.tokenExpiry);
    if (!expiry) return false;

    const bufferTime = bufferMinutes * 60 * 1000;
    return Date.now() >= expiry - bufferTime;
  }

  /**
   * Clear all authentication data
   */
  clearTokens() {
    Object.values(this.tokenKeys).forEach(key => {
      this.removeItem(key);
    });
  }

  /**
   * Update access token (during refresh)
   */
  updateAccessToken(accessToken, expiresIn) {
    const expiryTime = Date.now() + (expiresIn * 1000);
    
    return [
      this.setItem(this.tokenKeys.accessToken, accessToken, { 
        ttl: expiresIn * 1000, 
        persistent: false 
      }),
      this.setItem(this.tokenKeys.tokenExpiry, expiryTime, { 
        ttl: expiresIn * 1000, 
        persistent: false 
      })
    ].every(Boolean);
  }
}

// Create singleton instances
const secureStorage = new SecureStorage();
const tokenStorage = new TokenStorage();

// Auto-cleanup on app start
if (appConfig.isDevelopment()) {
  const cleaned = secureStorage.cleanup();
  if (cleaned > 0) {
    console.log(`🧹 Cleaned up ${cleaned} expired storage items`);
  }
}

// Periodic cleanup
setInterval(() => {
  secureStorage.cleanup();
}, 10 * 60 * 1000); // Every 10 minutes

export { secureStorage, tokenStorage };
export default secureStorage;