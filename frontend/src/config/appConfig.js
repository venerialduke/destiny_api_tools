/**
 * Centralized configuration management for the frontend application.
 * Provides consistent configuration patterns and environment variable handling.
 */

class AppConfig {
  constructor() {
    this._validateEnvironment();
    this._setupAPISettings();
    this._setupUISettings();
    this._setupCacheSettings();
    this._setupPerformanceSettings();
  }

  _validateEnvironment() {
    /**
     * Validate required environment variables are available
     */
    const requiredVars = ['REACT_APP_API_URL'];
    const missingVars = requiredVars.filter(varName => !process.env[varName]);
    
    if (missingVars.length > 0) {
      console.warn(`Missing environment variables: ${missingVars.join(', ')}`);
    }
  }

  _setupAPISettings() {
    /**
     * Configure API-related settings
     */
    console.log('🔧 CONFIG: Setting up API settings');
    console.log('🔧 CONFIG: REACT_APP_API_URL from env:', process.env.REACT_APP_API_URL);
    
    this.api = {
      baseURL: process.env.REACT_APP_API_URL || 'http://localhost:5000/api',
      timeout: parseInt(process.env.REACT_APP_API_TIMEOUT) || 30000,
      retryAttempts: parseInt(process.env.REACT_APP_RETRY_ATTEMPTS) || 3,
      retryDelay: parseInt(process.env.REACT_APP_RETRY_DELAY) || 1000,
      maxConcurrentRequests: parseInt(process.env.REACT_APP_MAX_CONCURRENT_REQUESTS) || 5
    };
    
    console.log('🔧 CONFIG: Final API baseURL:', this.api.baseURL);
  }

  _setupUISettings() {
    /**
     * Configure UI-related settings
     */
    this.ui = {
      theme: process.env.REACT_APP_DEFAULT_THEME || 'dark',
      itemsPerPage: parseInt(process.env.REACT_APP_ITEMS_PER_PAGE) || 20,
      debounceDelay: parseInt(process.env.REACT_APP_DEBOUNCE_DELAY) || 300,
      animationDuration: parseInt(process.env.REACT_APP_ANIMATION_DURATION) || 200,
      imageLoadTimeout: parseInt(process.env.REACT_APP_IMAGE_LOAD_TIMEOUT) || 10000
    };
  }

  _setupCacheSettings() {
    /**
     * Configure caching behavior
     */
    this.cache = {
      defaultTTL: parseInt(process.env.REACT_APP_CACHE_DEFAULT_TTL) || 300000, // 5 minutes
      maxSize: parseInt(process.env.REACT_APP_CACHE_MAX_SIZE) || 100,
      manifestTTL: parseInt(process.env.REACT_APP_MANIFEST_CACHE_TTL) || 3600000, // 1 hour
      userDataTTL: parseInt(process.env.REACT_APP_USER_DATA_CACHE_TTL) || 1800000, // 30 minutes
      searchResultsTTL: parseInt(process.env.REACT_APP_SEARCH_CACHE_TTL) || 600000, // 10 minutes
      enabled: process.env.REACT_APP_CACHE_ENABLED !== 'false'
    };
  }

  _setupPerformanceSettings() {
    /**
     * Configure performance monitoring and optimization
     */
    this.performance = {
      enableMetrics: process.env.REACT_APP_ENABLE_METRICS !== 'false',
      metricsReportInterval: parseInt(process.env.REACT_APP_METRICS_INTERVAL) || 60000, // 1 minute
      imageOptimization: process.env.REACT_APP_IMAGE_OPTIMIZATION !== 'false',
      lazyLoadImages: process.env.REACT_APP_LAZY_LOAD_IMAGES !== 'false',
      requestDeduplication: process.env.REACT_APP_REQUEST_DEDUPLICATION !== 'false'
    };
  }

  /**
   * Get environment-specific settings
   */
  getEnvironment() {
    return process.env.NODE_ENV || 'development';
  }

  /**
   * Check if running in development mode
   */
  isDevelopment() {
    return this.getEnvironment() === 'development';
  }

  /**
   * Check if running in production mode
   */
  isProduction() {
    return this.getEnvironment() === 'production';
  }

  /**
   * Get API endpoints configuration
   */
  getAPIEndpoints() {
    return {
      auth: {
        login: '/auth/login',
        callback: '/auth/callback',
        refresh: '/auth/refresh',
        logout: '/auth/logout'
      },
      user: {
        profile: '/core/user/profile',
        memberships: '/core/user/memberships',
        characters: (membershipType, membershipId) => 
          `/core/user/characters/${membershipType}/${membershipId}`,
        characterDetails: (membershipType, membershipId, characterId) => 
          `/core/user/character/${membershipType}/${membershipId}/${characterId}`,
        equipment: (membershipType, membershipId, characterId) => 
          `/core/user/character/${membershipType}/${membershipId}/${characterId}/equipment`,
        search: (membershipType) => `/core/user/search/${membershipType}`
      },
      core: {
        health: '/core/health',
        manifest: '/core/manifest',
        settings: '/core/settings'
      },
      demo: {
        searchItems: '/manifest/items/search',
        itemDetails: (itemHash) => `/manifest/items/${itemHash}`,
        imageMetrics: '/images/cache/stats',
        imageProxy: (iconPath, format, size) => 
          `/images/proxy${iconPath}?format=${format}&size=${size}`
      }
    };
  }

  /**
   * Get cache configuration for specific data types
   */
  getCacheConfig(dataType) {
    const configs = {
      'manifest': { ttl: this.cache.manifestTTL },
      'user-data': { ttl: this.cache.userDataTTL },
      'search-results': { ttl: this.cache.searchResultsTTL },
      'auth-tokens': { ttl: 0 }, // Never cache auth tokens in memory
      'character-data': { ttl: this.cache.userDataTTL },
      'item-details': { ttl: this.cache.manifestTTL },
      'default': { ttl: this.cache.defaultTTL }
    };

    return configs[dataType] || configs['default'];
  }

  /**
   * Get performance settings for specific operations
   */
  getPerformanceSettings(operation) {
    const baseSettings = {
      timeout: this.api.timeout,
      retryAttempts: this.api.retryAttempts,
      retryDelay: this.api.retryDelay
    };

    const operationSettings = {
      'auth': {
        ...baseSettings,
        retryAttempts: 2, // Fewer retries for auth
        timeout: 10000 // Shorter timeout for auth
      },
      'user-data': {
        ...baseSettings,
        retryAttempts: 3,
        timeout: 15000
      },
      'manifest': {
        ...baseSettings,
        retryAttempts: 2,
        timeout: 30000 // Longer timeout for large manifest data
      },
      'search': {
        ...baseSettings,
        retryAttempts: 2,
        timeout: 10000
      },
      'images': {
        ...baseSettings,
        retryAttempts: 1,
        timeout: this.ui.imageLoadTimeout
      }
    };

    return operationSettings[operation] || baseSettings;
  }

  /**
   * Get configuration summary for debugging
   */
  getConfigSummary() {
    return {
      environment: this.getEnvironment(),
      api: {
        baseURL: this.api.baseURL,
        timeout: this.api.timeout,
        retryAttempts: this.api.retryAttempts
      },
      cache: {
        enabled: this.cache.enabled,
        defaultTTL: this.cache.defaultTTL,
        maxSize: this.cache.maxSize
      },
      performance: {
        enableMetrics: this.performance.enableMetrics,
        imageOptimization: this.performance.imageOptimization,
        requestDeduplication: this.performance.requestDeduplication
      }
    };
  }

  /**
   * Log configuration for debugging (development only)
   */
  logConfig() {
    if (this.isDevelopment()) {
      console.group('🔧 App Configuration');
      console.table(this.getConfigSummary());
      console.groupEnd();
    }
  }
}

// Create and export singleton instance
const appConfig = new AppConfig();

// Log configuration in development
if (appConfig.isDevelopment()) {
  appConfig.logConfig();
}

export default appConfig;

// Named exports for specific configurations
export const apiConfig = appConfig.api;
export const uiConfig = appConfig.ui;
export const cacheConfig = appConfig.cache;
export const performanceConfig = appConfig.performance;