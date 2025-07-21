import React, { useState, useRef, useEffect } from 'react';

const OptimizedImage = ({ 
  icon, 
  alt, 
  size = 'medium', 
  className = '', 
  priority = false,
  onLoadComplete = null,
  showPerformanceInfo = false
}) => {
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(false);
  const [loadTime, setLoadTime] = useState(null);
  const [imageInfo, setImageInfo] = useState(null);
  const startTimeRef = useRef(null);

  // Get the appropriate image URL based on icon structure
  const getImageUrl = () => {
    if (!icon) return null;
    
    // If icon is a string (legacy format), use backend proxy for HTTPS compatibility
    if (typeof icon === 'string') {
      if (icon.startsWith('http')) {
        return icon;
      } else {
        // Use backend proxy instead of direct Bungie URL for HTTPS compatibility
        const cleanPath = icon.startsWith('/') ? icon.substring(1) : icon;
        return `${process.env.REACT_APP_API_URL}/images/proxy/${cleanPath}?format=webp&size=${size}`;
      }
    }
    
    // If icon is an object with optimized URLs, use the optimized version
    if (typeof icon === 'object' && icon.optimized && icon.optimized[size]) {
      const optimizedUrl = icon.optimized[size];
      // If it's a relative URL, make it absolute
      if (optimizedUrl.startsWith('/api/')) {
        return `${process.env.REACT_APP_API_URL.replace('/api', '')}${optimizedUrl}`;
      }
      return optimizedUrl;
    }
    
    // Fallback to proxy URL if available
    if (typeof icon === 'object' && icon.proxy) {
      return `${icon.proxy}?format=webp&size=${size}`;
    }
    
    // Fallback to original URL
    if (typeof icon === 'object' && icon.original) {
      return icon.original;
    }
    
    return null;
  };

  const getFallbackUrl = () => {
    if (!icon) return null;
    
    // If we have an object with original URL, use that as fallback
    if (typeof icon === 'object' && icon.original) {
      return icon.original;
    }
    
    // If we have an object with proxy URL, use that
    if (typeof icon === 'object' && icon.proxy) {
      return icon.proxy;
    }
    
    // If it's a string and not a full URL, make it one
    if (typeof icon === 'string' && !icon.startsWith('http')) {
      return `https://bungie.net${icon}`;
    }
    
    // If it's a string, return it directly
    if (typeof icon === 'string') {
      return icon;
    }
    
    // If we can't determine the URL, return null
    return null;
  };

  const imageUrl = getImageUrl();
  const fallbackUrl = getFallbackUrl();
  
  // Debug logging (only in development)
  if (process.env.NODE_ENV === 'development') {
    console.log('OptimizedImage Debug:', {
      icon,
      size,
      imageUrl,
      fallbackUrl,
      iconType: typeof icon
    });
  }

  useEffect(() => {
    if (!imageUrl) {
      setError(true);
      setIsLoading(false);
      return;
    }

    startTimeRef.current = performance.now();
    setIsLoading(true);
    setError(false);
  }, [imageUrl]);

  const handleLoad = (event) => {
    const endTime = performance.now();
    const duration = startTimeRef.current ? Math.round(endTime - startTimeRef.current) : 0;
    
    setIsLoading(false);
    setError(false);
    setLoadTime(duration);
    
    // Get image info
    const img = event.target;
    setImageInfo({
      naturalWidth: img.naturalWidth,
      naturalHeight: img.naturalHeight,
      displayWidth: img.width,
      displayHeight: img.height
    });
    
    if (onLoadComplete) {
      onLoadComplete(duration);
    }
  };

  const handleError = () => {
    setIsLoading(false);
    setError(true);
    
    if (onLoadComplete) {
      onLoadComplete(-1);
    }
  };

  if (!imageUrl) {
    return (
      <div className={`bg-gray-700 flex items-center justify-center ${className}`}>
        <span className="text-gray-400 text-xs">No Image</span>
      </div>
    );
  }

  // Don't render if the URL is still an object (malformed)
  if (typeof imageUrl === 'object') {
    console.error('Image URL is an object instead of string:', imageUrl);
    return (
      <div className={`bg-gray-700 flex items-center justify-center ${className}`}>
        <span className="text-gray-400 text-xs">Invalid URL</span>
      </div>
    );
  }

  return (
    <div className={`relative ${className}`}>
      {/* Main Image */}
      <img
        src={imageUrl}
        alt={alt}
        className={`w-full h-full object-cover transition-opacity duration-200 ${
          isLoading ? 'opacity-0' : 'opacity-100'
        }`}
        onLoad={handleLoad}
        onError={handleError}
        loading={priority ? 'eager' : 'lazy'}
      />

      {/* Fallback Image */}
      {error && fallbackUrl && fallbackUrl !== imageUrl && (
        <img
          src={fallbackUrl}
          alt={alt}
          className="absolute inset-0 w-full h-full object-cover"
          onLoad={() => {
            console.log('Fallback image loaded:', fallbackUrl);
            setError(false);
            setIsLoading(false);
          }}
          onError={() => {
            console.log('Fallback image also failed:', fallbackUrl);
          }}
        />
      )}

      {/* Loading Spinner */}
      {isLoading && (
        <div className="absolute inset-0 flex items-center justify-center bg-gray-700">
          <div className="animate-spin rounded-full h-1/2 w-1/2 border-b-2 border-blue-500"></div>
        </div>
      )}

      {/* Error Placeholder */}
      {error && (!fallbackUrl || fallbackUrl === imageUrl) && (
        <div className="absolute inset-0 flex items-center justify-center bg-gray-700">
          <div className="text-center">
            <div className="text-2xl mb-1">❌</div>
            <div className="text-xs text-gray-400">Load Failed</div>
          </div>
        </div>
      )}

      {/* Performance Info Overlay */}
      {showPerformanceInfo && loadTime !== null && !isLoading && !error && (
        <div className="absolute top-1 right-1 bg-black/70 text-white text-xs px-2 py-1 rounded">
          {loadTime}ms
        </div>
      )}

      {/* WebP Indicator */}
      {!isLoading && !error && imageUrl.includes('format=webp') && (
        <div className="absolute bottom-1 left-1 bg-green-600/80 text-white text-xs px-1 rounded">
          WebP
        </div>
      )}

      {/* Size Indicator */}
      {!isLoading && !error && imageInfo && showPerformanceInfo && (
        <div className="absolute bottom-1 right-1 bg-blue-600/80 text-white text-xs px-1 rounded">
          {imageInfo.naturalWidth}x{imageInfo.naturalHeight}
        </div>
      )}
    </div>
  );
};

export default OptimizedImage;