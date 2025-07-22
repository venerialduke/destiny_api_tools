/**
 * Service for handling Destiny 2 image assets with optimization and caching
 */

import { apiClient } from './apiClient';

class ImageService {
    constructor() {
        this.cache = new Map();
        this.pendingRequests = new Map();
    }

    /**
     * Get optimized image URL for a Destiny 2 icon path
     * @param {string} iconPath - The icon path from Destiny manifest
     * @param {Object} options - Image options
     * @param {string} options.format - Image format (webp, jpg, png, original)
     * @param {string} options.size - Image size (small, medium, large, or WxH)
     * @returns {string} Optimized image URL
     */
    getImageUrl(iconPath, options = {}) {
        if (!iconPath) {
            return this.getPlaceholderUrl();
        }

        // Clean icon path
        const cleanPath = iconPath.startsWith('/') ? iconPath : `/${iconPath}`;
        
        // Default options
        const format = options.format || 'webp';
        const size = options.size || 'medium';
        
        // Build query parameters
        const params = new URLSearchParams();
        if (format !== 'original') {
            params.append('format', format);
        }
        if (size && size !== 'original') {
            params.append('size', size);
        }
        
        // Build full URL - for images, use relative URLs to avoid mixed content issues
        const baseUrl = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';
        const queryString = params.toString();
        return `${baseUrl}/images/proxy${cleanPath}${queryString ? '?' + queryString : ''}`;
    }

    /**
     * Get multiple image URLs in a batch request
     * @param {string[]} iconPaths - Array of icon paths
     * @param {Object} options - Image options
     * @returns {Promise<Object>} Map of icon paths to URLs
     */
    async getBatchImageUrls(iconPaths, options = {}) {
        try {
            const requestKey = JSON.stringify({ iconPaths, options });
            
            // Check cache first
            if (this.cache.has(requestKey)) {
                return this.cache.get(requestKey);
            }

            // Check for pending request
            if (this.pendingRequests.has(requestKey)) {
                return await this.pendingRequests.get(requestKey);
            }

            // Make new request
            const request = apiClient.post('/images/batch-urls', {
                icon_paths: iconPaths.filter(path => path), // Remove empty paths
                format: options.format || 'webp',
                size: options.size || 'medium'
            });

            this.pendingRequests.set(requestKey, request);

            const response = await request;
            const result = response.images || {};
            
            // Cache the result
            this.cache.set(requestKey, result);
            this.pendingRequests.delete(requestKey);
            
            return result;
        } catch (error) {
            console.error('Error fetching batch image URLs:', error);
            const requestKey = JSON.stringify({ iconPaths, options });
            this.pendingRequests.delete(requestKey);
            
            // Return fallback URLs
            const fallback = {};
            iconPaths.forEach(path => {
                if (path) {
                    fallback[path] = this.getImageUrl(path, options);
                }
            });
            return fallback;
        }
    }

    /**
     * Get placeholder image URL for missing icons
     * @returns {string} Placeholder image URL
     */
    getPlaceholderUrl() {
        // Return a data URL for a simple placeholder
        return 'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjQiIGhlaWdodD0iNjQiIHZpZXdCb3g9IjAgMCA2NCA2NCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHJlY3Qgd2lkdGg9IjY0IiBoZWlnaHQ9IjY0IiBmaWxsPSIjMzMzIi8+CjxwYXRoIGQ9Ik0yMCAyMGgyNHYyNEgyMHoiIGZpbGw9IiM1NTUiLz4KPC9zdmc+';
    }

    /**
     * Preload an image to ensure it's cached
     * @param {string} iconPath - Icon path to preload
     * @param {Object} options - Image options
     * @returns {Promise<boolean>} True if loaded successfully
     */
    async preloadImage(iconPath, options = {}) {
        if (!iconPath) return false;

        try {
            const url = this.getImageUrl(iconPath, options);
            
            return new Promise((resolve) => {
                const img = new Image();
                img.onload = () => resolve(true);
                img.onerror = () => resolve(false);
                img.src = url;
            });
        } catch (error) {
            console.error('Error preloading image:', error);
            return false;
        }
    }

    /**
     * Preload multiple images
     * @param {string[]} iconPaths - Array of icon paths
     * @param {Object} options - Image options
     * @returns {Promise<number>} Number of successfully loaded images
     */
    async preloadImages(iconPaths, options = {}) {
        const promises = iconPaths.map(path => this.preloadImage(path, options));
        const results = await Promise.all(promises);
        return results.filter(success => success).length;
    }

    /**
     * Get appropriate image size based on use case
     * @param {string} useCase - The use case (thumbnail, card, detail, etc.)
     * @returns {string} Appropriate size parameter
     */
    getSizeForUseCase(useCase) {
        const sizeMap = {
            'thumbnail': 'small',      // 64x64
            'card': 'medium',          // 128x128
            'detail': 'large',         // 256x256
            'icon': 'small',           // 64x64
            'emblem': 'medium',        // 128x128
            'armor': 'medium',         // 128x128
            'weapon': 'medium',        // 128x128
            'perk': 'small',           // 64x64
            'badge': 'small'           // 64x64
        };
        
        return sizeMap[useCase] || 'medium';
    }

    /**
     * Get cache statistics (for debugging)
     * @returns {Object} Cache statistics
     */
    getCacheStats() {
        return {
            cacheSize: this.cache.size,
            pendingRequests: this.pendingRequests.size,
            cacheKeys: Array.from(this.cache.keys()).slice(0, 10) // First 10 for debugging
        };
    }

    /**
     * Clear the local cache
     */
    clearCache() {
        this.cache.clear();
        this.pendingRequests.clear();
    }
}

// Create and export singleton instance
export const imageService = new ImageService();