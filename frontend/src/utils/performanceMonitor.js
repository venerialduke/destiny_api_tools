/**
 * Frontend performance monitoring utilities for tracking client-side metrics.
 * Provides request timing, error tracking, and performance insights.
 */

import appConfig from '../config/appConfig';

class PerformanceMonitor {
  constructor() {
    this.metrics = new Map();
    this.requestHistory = [];
    this.errorHistory = [];
    this.maxHistorySize = 1000;
    
    // Performance observers
    this.observers = new Map();
    
    // Statistics
    this.stats = {
      totalRequests: 0,
      successfulRequests: 0,
      failedRequests: 0,
      totalResponseTime: 0,
      cacheHits: 0,
      networkErrors: 0
    };
    
    // Initialize monitoring if enabled
    if (appConfig.performance.enableMetrics) {
      this.initializeMonitoring();
    }
  }

  /**
   * Initialize performance monitoring
   */
  initializeMonitoring() {
    // Web Vitals monitoring
    this.initializeWebVitals();
    
    // Resource timing monitoring
    this.initializeResourceTiming();
    
    // Navigation timing monitoring
    this.initializeNavigationTiming();
    
    // User interactions monitoring
    this.initializeUserInteractions();
    
    console.log('🚀 Performance monitoring initialized');
  }

  /**
   * Initialize Web Vitals monitoring (LCP, FID, CLS)
   */
  initializeWebVitals() {
    if (typeof window !== 'undefined' && 'PerformanceObserver' in window) {
      // Largest Contentful Paint (LCP)
      try {
        const lcpObserver = new PerformanceObserver((list) => {
          for (const entry of list.getEntries()) {
            this.recordMetric('LCP', entry.startTime, {
              element: entry.element?.tagName,
              url: entry.url
            });
          }
        });
        lcpObserver.observe({ entryTypes: ['largest-contentful-paint'] });
        this.observers.set('lcp', lcpObserver);
      } catch (error) {
        console.warn('LCP observer not supported:', error);
      }

      // First Input Delay (FID)
      try {
        const fidObserver = new PerformanceObserver((list) => {
          for (const entry of list.getEntries()) {
            this.recordMetric('FID', entry.processingStart - entry.startTime, {
              inputType: entry.name
            });
          }
        });
        fidObserver.observe({ entryTypes: ['first-input'] });
        this.observers.set('fid', fidObserver);
      } catch (error) {
        console.warn('FID observer not supported:', error);
      }

      // Cumulative Layout Shift (CLS)
      try {
        let clsValue = 0;
        const clsObserver = new PerformanceObserver((list) => {
          for (const entry of list.getEntries()) {
            if (!entry.hadRecentInput) {
              clsValue += entry.value;
              this.recordMetric('CLS', clsValue);
            }
          }
        });
        clsObserver.observe({ entryTypes: ['layout-shift'] });
        this.observers.set('cls', clsObserver);
      } catch (error) {
        console.warn('CLS observer not supported:', error);
      }
    }
  }

  /**
   * Initialize resource timing monitoring
   */
  initializeResourceTiming() {
    if (typeof window !== 'undefined' && 'PerformanceObserver' in window) {
      try {
        const resourceObserver = new PerformanceObserver((list) => {
          for (const entry of list.getEntries()) {
            this.recordResourceTiming(entry);
          }
        });
        resourceObserver.observe({ entryTypes: ['resource'] });
        this.observers.set('resource', resourceObserver);
      } catch (error) {
        console.warn('Resource timing observer not supported:', error);
      }
    }
  }

  /**
   * Initialize navigation timing monitoring
   */
  initializeNavigationTiming() {
    if (typeof window !== 'undefined' && window.performance && window.performance.timing) {
      const timing = window.performance.timing;
      
      // Calculate key timing metrics
      const navigationStart = timing.navigationStart;
      const domContentLoaded = timing.domContentLoadedEventEnd - navigationStart;
      const loadComplete = timing.loadEventEnd - navigationStart;
      const domInteractive = timing.domInteractive - navigationStart;
      
      this.recordMetric('DOM_Content_Loaded', domContentLoaded);
      this.recordMetric('Load_Complete', loadComplete);
      this.recordMetric('DOM_Interactive', domInteractive);
      
      // DNS and connection timing
      if (timing.domainLookupEnd > 0) {
        this.recordMetric('DNS_Lookup', timing.domainLookupEnd - timing.domainLookupStart);
      }
      
      if (timing.connectEnd > 0) {
        this.recordMetric('Connection_Time', timing.connectEnd - timing.connectStart);
      }
    }
  }

  /**
   * Initialize user interaction monitoring
   */
  initializeUserInteractions() {
    if (typeof window !== 'undefined') {
      // Click tracking
      document.addEventListener('click', (event) => {
        this.recordUserInteraction('click', {
          element: event.target.tagName,
          className: event.target.className,
          id: event.target.id
        });
      });

      // Page visibility changes
      document.addEventListener('visibilitychange', () => {
        this.recordMetric('Page_Visibility_Change', Date.now(), {
          hidden: document.hidden
        });
      });
    }
  }

  /**
   * Record a performance metric
   */
  recordMetric(name, value, metadata = {}) {
    const metric = {
      name,
      value,
      timestamp: Date.now(),
      metadata
    };

    if (!this.metrics.has(name)) {
      this.metrics.set(name, []);
    }

    const metricHistory = this.metrics.get(name);
    metricHistory.push(metric);

    // Limit history size
    if (metricHistory.length > this.maxHistorySize) {
      metricHistory.shift();
    }

    // Log significant metrics in development
    if (appConfig.isDevelopment() && this.isSignificantMetric(name, value)) {
      console.log(`📊 ${name}: ${value}ms`, metadata);
    }
  }

  /**
   * Record resource timing information
   */
  recordResourceTiming(entry) {
    const resourceType = this.getResourceType(entry.name);
    const loadTime = entry.responseEnd - entry.startTime;
    
    this.recordMetric(`Resource_Load_${resourceType}`, loadTime, {
      url: entry.name,
      size: entry.transferSize,
      cached: entry.transferSize === 0
    });

    // Track slow resources
    if (loadTime > 1000) { // Slower than 1 second
      this.recordMetric('Slow_Resource', loadTime, {
        url: entry.name,
        type: resourceType
      });
    }
  }

  /**
   * Record user interaction
   */
  recordUserInteraction(type, metadata = {}) {
    this.recordMetric(`User_${type}`, Date.now(), metadata);
  }

  /**
   * Record API request performance
   */
  recordRequest(url, method, duration, success, fromCache = false) {
    this.stats.totalRequests++;
    this.stats.totalResponseTime += duration;

    if (success) {
      this.stats.successfulRequests++;
    } else {
      this.stats.failedRequests++;
    }

    if (fromCache) {
      this.stats.cacheHits++;
    }

    const request = {
      url,
      method,
      duration,
      success,
      fromCache,
      timestamp: Date.now()
    };

    this.requestHistory.push(request);

    // Limit history size
    if (this.requestHistory.length > this.maxHistorySize) {
      this.requestHistory.shift();
    }

    // Record as metric
    this.recordMetric('API_Request', duration, {
      method,
      success,
      fromCache,
      endpoint: this.extractEndpoint(url)
    });

    // Track slow requests
    if (duration > 2000) { // Slower than 2 seconds
      this.recordMetric('Slow_API_Request', duration, {
        url,
        method
      });
    }
  }

  /**
   * Record an error
   */
  recordError(error, context = {}) {
    const errorInfo = {
      message: error.message || error,
      stack: error.stack,
      context,
      timestamp: Date.now(),
      url: window.location.href,
      userAgent: navigator.userAgent
    };

    this.errorHistory.push(errorInfo);

    // Limit history size
    if (this.errorHistory.length > this.maxHistorySize) {
      this.errorHistory.shift();
    }

    this.recordMetric('Error', 1, errorInfo);

    // Log in development
    if (appConfig.isDevelopment()) {
      console.error('💥 Error recorded:', errorInfo);
    }
  }

  /**
   * Record network error
   */
  recordNetworkError(url, method, error) {
    this.stats.networkErrors++;
    this.recordError(error, {
      type: 'network',
      url,
      method
    });
  }

  /**
   * Get performance statistics
   */
  getStats() {
    const avgResponseTime = this.stats.totalRequests > 0 
      ? this.stats.totalResponseTime / this.stats.totalRequests 
      : 0;

    const successRate = this.stats.totalRequests > 0 
      ? (this.stats.successfulRequests / this.stats.totalRequests) * 100 
      : 0;

    const cacheHitRate = this.stats.totalRequests > 0 
      ? (this.stats.cacheHits / this.stats.totalRequests) * 100 
      : 0;

    return {
      ...this.stats,
      averageResponseTime: avgResponseTime,
      successRate: successRate,
      cacheHitRate: cacheHitRate,
      errorRate: ((this.stats.failedRequests / this.stats.totalRequests) * 100) || 0,
      metricsCount: Array.from(this.metrics.values()).reduce((sum, arr) => sum + arr.length, 0),
      requestHistorySize: this.requestHistory.length,
      errorHistorySize: this.errorHistory.length
    };
  }

  /**
   * Get metric summary
   */
  getMetricSummary(metricName, duration = 300000) { // Last 5 minutes
    if (!this.metrics.has(metricName)) {
      return null;
    }

    const cutoffTime = Date.now() - duration;
    const recentMetrics = this.metrics.get(metricName)
      .filter(metric => metric.timestamp >= cutoffTime);

    if (recentMetrics.length === 0) {
      return null;
    }

    const values = recentMetrics.map(m => m.value);
    values.sort((a, b) => a - b);

    return {
      count: values.length,
      min: Math.min(...values),
      max: Math.max(...values),
      avg: values.reduce((sum, val) => sum + val, 0) / values.length,
      median: values[Math.floor(values.length / 2)],
      p95: values[Math.floor(values.length * 0.95)],
      latest: recentMetrics[recentMetrics.length - 1]?.value
    };
  }

  /**
   * Get recent errors
   */
  getRecentErrors(count = 10) {
    return this.errorHistory.slice(-count);
  }

  /**
   * Get slow requests
   */
  getSlowRequests(threshold = 2000, count = 10) {
    return this.requestHistory
      .filter(req => req.duration > threshold)
      .slice(-count);
  }

  /**
   * Generate performance report
   */
  generateReport() {
    const stats = this.getStats();
    
    const report = {
      timestamp: Date.now(),
      overview: stats,
      webVitals: {
        lcp: this.getMetricSummary('LCP'),
        fid: this.getMetricSummary('FID'),
        cls: this.getMetricSummary('CLS')
      },
      apiPerformance: {
        averageResponseTime: stats.averageResponseTime,
        slowRequests: this.getSlowRequests().length,
        cacheEffectiveness: stats.cacheHitRate
      },
      errors: {
        totalErrors: this.errorHistory.length,
        recentErrors: this.getRecentErrors(5)
      },
      recommendations: this.generateRecommendations(stats)
    };

    return report;
  }

  /**
   * Generate performance recommendations
   */
  generateRecommendations(stats) {
    const recommendations = [];

    if (stats.averageResponseTime > 1000) {
      recommendations.push({
        type: 'performance',
        priority: 'high',
        message: 'API response times are slow. Consider optimizing requests or implementing caching.'
      });
    }

    if (stats.cacheHitRate < 30) {
      recommendations.push({
        type: 'caching',
        priority: 'medium',
        message: 'Cache hit rate is low. Review caching strategy and TTL settings.'
      });
    }

    if (stats.errorRate > 5) {
      recommendations.push({
        type: 'reliability',
        priority: 'high',
        message: 'Error rate is high. Review error handling and retry logic.'
      });
    }

    const lcpSummary = this.getMetricSummary('LCP');
    if (lcpSummary && lcpSummary.avg > 2500) {
      recommendations.push({
        type: 'web-vitals',
        priority: 'medium',
        message: 'Largest Contentful Paint is slow. Optimize images and critical resources.'
      });
    }

    const fidSummary = this.getMetricSummary('FID');
    if (fidSummary && fidSummary.avg > 100) {
      recommendations.push({
        type: 'web-vitals',
        priority: 'medium',
        message: 'First Input Delay is high. Optimize JavaScript execution.'
      });
    }

    return recommendations;
  }

  /**
   * Helper methods
   */
  isSignificantMetric(name, value) {
    const significantThresholds = {
      'LCP': 2500,
      'FID': 100,
      'API_Request': 1000,
      'Resource_Load_image': 500,
      'Resource_Load_script': 200
    };

    return value > (significantThresholds[name] || 1000);
  }

  getResourceType(url) {
    if (url.match(/\.(jpg|jpeg|png|gif|webp|svg)$/i)) return 'image';
    if (url.match(/\.(js)$/i)) return 'script';
    if (url.match(/\.(css)$/i)) return 'stylesheet';
    if (url.match(/\.(woff|woff2|ttf|eot)$/i)) return 'font';
    if (url.includes('/api/')) return 'api';
    return 'other';
  }

  extractEndpoint(url) {
    try {
      const urlObj = new URL(url);
      return urlObj.pathname.split('/').slice(0, 4).join('/'); // First 3 path segments
    } catch {
      return url;
    }
  }

  /**
   * Export data for analysis
   */
  exportData() {
    return {
      metrics: Object.fromEntries(this.metrics),
      requests: this.requestHistory,
      errors: this.errorHistory,
      stats: this.getStats(),
      timestamp: Date.now()
    };
  }

  /**
   * Clear all data
   */
  clearData() {
    this.metrics.clear();
    this.requestHistory.length = 0;
    this.errorHistory.length = 0;
    this.stats = {
      totalRequests: 0,
      successfulRequests: 0,
      failedRequests: 0,
      totalResponseTime: 0,
      cacheHits: 0,
      networkErrors: 0
    };
  }

  /**
   * Cleanup observers
   */
  destroy() {
    for (const observer of this.observers.values()) {
      observer.disconnect();
    }
    this.observers.clear();
  }
}

// Create singleton instance
const performanceMonitor = new PerformanceMonitor();

// Auto-export performance data in development
if (appConfig.isDevelopment()) {
  window.performanceMonitor = performanceMonitor;
  
  // Log performance report every 30 seconds in development
  setInterval(() => {
    const report = performanceMonitor.generateReport();
    console.group('📊 Performance Report');
    console.table(report.overview);
    if (report.recommendations.length > 0) {
      console.warn('Recommendations:', report.recommendations);
    }
    console.groupEnd();
  }, 30000);
}

export default performanceMonitor;