"""
Image caching and proxy service for Destiny manifest assets.
"""

import os
import hashlib
import requests
import time
from datetime import datetime, timedelta
from typing import Optional, Tuple
from urllib.parse import urlparse
from PIL import Image
import io


class ImageService:
    """Service for caching and serving Destiny image assets."""
    
    def __init__(self, cache_dir: str = "data/images", max_cache_size_gb: float = 2.0):
        """
        Initialize image service.
        
        Args:
            cache_dir: Directory to store cached images
            max_cache_size_gb: Maximum cache size in GB
        """
        self.cache_dir = cache_dir
        self.max_cache_size = max_cache_size_gb * 1024 * 1024 * 1024  # Convert to bytes
        
        # Ensure cache directory exists
        os.makedirs(cache_dir, exist_ok=True)
        
        # Bungie CDN base URL
        self.bungie_base_url = "https://www.bungie.net"
        
        # Cache statistics
        self.stats = {
            'hits': 0,
            'misses': 0,
            'downloads': 0,
            'errors': 0,
            'cache_size_bytes': 0
        }
        
        # Update cache size
        self._update_cache_size()
    
    def get_image_url(self, icon_path: str, format: str = 'webp', size: Optional[str] = None) -> str:
        """
        Get optimized image URL (proxy endpoint).
        
        Args:
            icon_path: Bungie icon path (e.g., "/common/destiny2_content/icons/...")
            format: Desired format ('webp', 'jpg', 'png')
            size: Optional size ('small', 'medium', 'large', or 'WxH')
            
        Returns:
            Local proxy URL
        """
        if not icon_path:
            return ""
        
        # Build proxy URL with parameters
        params = []
        if format != 'original':
            params.append(f'format={format}')
        if size:
            params.append(f'size={size}')
        
        query_string = '&'.join(params)
        proxy_url = f"/api/images/proxy/{icon_path.lstrip('/')}"
        
        if query_string:
            proxy_url += f"?{query_string}"
        
        return proxy_url
    
    def get_cached_image(self, icon_path: str, format: str = 'original', 
                        size: Optional[str] = None) -> Optional[Tuple[bytes, str, datetime]]:
        """
        Get image from cache.
        
        Returns:
            Tuple of (image_data, content_type, cached_time) or None if not cached
        """
        cache_key = self._get_cache_key(icon_path, format, size)
        cache_file = os.path.join(self.cache_dir, f"{cache_key}.cache")
        meta_file = os.path.join(self.cache_dir, f"{cache_key}.meta")
        
        if os.path.exists(cache_file) and os.path.exists(meta_file):
            try:
                # Read metadata
                with open(meta_file, 'r') as f:
                    lines = f.read().strip().split('\n')
                    content_type = lines[0]
                    cached_time = datetime.fromisoformat(lines[1])
                
                # Check if cache is still valid (7 days)
                if datetime.now() - cached_time < timedelta(days=7):
                    # Read image data
                    with open(cache_file, 'rb') as f:
                        image_data = f.read()
                    
                    self.stats['hits'] += 1
                    return image_data, content_type, cached_time
                else:
                    # Cache expired, clean up
                    os.remove(cache_file)
                    os.remove(meta_file)
            except Exception:
                # Corrupted cache, clean up
                if os.path.exists(cache_file):
                    os.remove(cache_file)
                if os.path.exists(meta_file):
                    os.remove(meta_file)
        
        self.stats['misses'] += 1
        return None
    
    def download_and_cache_image(self, icon_path: str, format: str = 'original', 
                                size: Optional[str] = None) -> Optional[Tuple[bytes, str]]:
        """
        Download image from Bungie and cache it.
        
        Returns:
            Tuple of (image_data, content_type) or None if download failed
        """
        if not icon_path:
            return None
        
        try:
            # Download from Bungie
            url = f"{self.bungie_base_url}{icon_path}"
            headers = {
                'User-Agent': 'Destiny-API-Tools/1.0',
                'Accept': 'image/webp,image/jpeg,image/png,image/*'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            image_data = response.content
            content_type = response.headers.get('content-type', 'image/jpeg')
            
            # Process image if format/size conversion requested
            if format != 'original' or size:
                image_data, content_type = self._process_image(image_data, format, size)
            
            # Cache the image
            self._cache_image(icon_path, format, size, image_data, content_type)
            
            self.stats['downloads'] += 1
            return image_data, content_type
            
        except Exception as e:
            self.stats['errors'] += 1
            print(f"Error downloading image {icon_path}: {e}")
            return None
    
    def _process_image(self, image_data: bytes, format: str, size: Optional[str]) -> Tuple[bytes, str]:
        """Process image for format conversion and resizing."""
        try:
            # Open image with PIL
            image = Image.open(io.BytesIO(image_data))
            
            # Resize if requested
            if size:
                if size == 'small':
                    target_size = (64, 64)
                elif size == 'medium':
                    target_size = (128, 128)
                elif size == 'large':
                    target_size = (256, 256)
                elif 'x' in size.lower():
                    # Custom size like "96x96"
                    width, height = size.lower().split('x')
                    target_size = (int(width), int(height))
                else:
                    target_size = image.size
                
                if target_size != image.size:
                    image = image.resize(target_size, Image.Resampling.LANCZOS)
            
            # Convert format if requested
            output_format = format.upper()
            if output_format == 'WEBP':
                content_type = 'image/webp'
                save_kwargs = {'quality': 85, 'method': 6}
            elif output_format == 'JPG' or output_format == 'JPEG':
                content_type = 'image/jpeg'
                save_kwargs = {'quality': 90, 'optimize': True}
                # Convert RGBA to RGB for JPEG
                if image.mode in ('RGBA', 'LA'):
                    background = Image.new('RGB', image.size, (255, 255, 255))
                    background.paste(image, mask=image.split()[-1] if image.mode == 'RGBA' else None)
                    image = background
            elif output_format == 'PNG':
                content_type = 'image/png'
                save_kwargs = {'optimize': True}
            else:
                # Keep original format
                return image_data, 'image/jpeg'  # Default content type
            
            # Save processed image
            output_buffer = io.BytesIO()
            image.save(output_buffer, format=output_format, **save_kwargs)
            processed_data = output_buffer.getvalue()
            
            return processed_data, content_type
            
        except Exception as e:
            print(f"Error processing image: {e}")
            return image_data, 'image/jpeg'  # Return original on error
    
    def _cache_image(self, icon_path: str, format: str, size: Optional[str], 
                    image_data: bytes, content_type: str):
        """Cache image data and metadata."""
        cache_key = self._get_cache_key(icon_path, format, size)
        cache_file = os.path.join(self.cache_dir, f"{cache_key}.cache")
        meta_file = os.path.join(self.cache_dir, f"{cache_key}.meta")
        
        try:
            # Write image data
            with open(cache_file, 'wb') as f:
                f.write(image_data)
            
            # Write metadata
            with open(meta_file, 'w') as f:
                f.write(f"{content_type}\n")
                f.write(f"{datetime.now().isoformat()}\n")
            
            # Update cache size
            self.stats['cache_size_bytes'] += len(image_data)
            
            # Clean cache if over limit
            self._cleanup_cache_if_needed()
            
        except Exception as e:
            print(f"Error caching image: {e}")
    
    def _get_cache_key(self, icon_path: str, format: str, size: Optional[str]) -> str:
        """Generate cache key for image."""
        key_data = f"{icon_path}:{format}:{size or 'original'}"
        return hashlib.md5(key_data.encode()).hexdigest()
    
    def _update_cache_size(self):
        """Update cache size statistics."""
        total_size = 0
        try:
            for filename in os.listdir(self.cache_dir):
                if filename.endswith('.cache'):
                    file_path = os.path.join(self.cache_dir, filename)
                    total_size += os.path.getsize(file_path)
        except Exception:
            pass
        
        self.stats['cache_size_bytes'] = total_size
    
    def _cleanup_cache_if_needed(self):
        """Clean up old cache files if over size limit."""
        if self.stats['cache_size_bytes'] <= self.max_cache_size:
            return
        
        try:
            # Get all cache files with their access times
            cache_files = []
            for filename in os.listdir(self.cache_dir):
                if filename.endswith('.cache'):
                    file_path = os.path.join(self.cache_dir, filename)
                    access_time = os.path.getatime(file_path)
                    file_size = os.path.getsize(file_path)
                    cache_files.append((access_time, file_path, file_size, filename))
            
            # Sort by access time (oldest first)
            cache_files.sort(key=lambda x: x[0])
            
            # Remove oldest files until under limit
            for access_time, cache_file, file_size, filename in cache_files:
                if self.stats['cache_size_bytes'] <= self.max_cache_size * 0.8:  # Leave 20% buffer
                    break
                
                try:
                    # Remove cache and meta files
                    base_name = filename[:-6]  # Remove .cache extension
                    meta_file = os.path.join(self.cache_dir, f"{base_name}.meta")
                    
                    os.remove(cache_file)
                    if os.path.exists(meta_file):
                        os.remove(meta_file)
                    
                    self.stats['cache_size_bytes'] -= file_size
                    
                except Exception:
                    continue
            
        except Exception as e:
            print(f"Error cleaning up cache: {e}")
    
    def get_cache_stats(self) -> dict:
        """Get cache statistics."""
        self._update_cache_size()
        
        hit_rate = 0
        if self.stats['hits'] + self.stats['misses'] > 0:
            hit_rate = self.stats['hits'] / (self.stats['hits'] + self.stats['misses']) * 100
        
        return {
            'cache_size_mb': self.stats['cache_size_bytes'] / (1024 * 1024),
            'max_cache_size_mb': self.max_cache_size / (1024 * 1024),
            'cache_usage_percent': (self.stats['cache_size_bytes'] / self.max_cache_size) * 100,
            'hit_rate_percent': hit_rate,
            'total_requests': self.stats['hits'] + self.stats['misses'],
            'cache_hits': self.stats['hits'],
            'cache_misses': self.stats['misses'],
            'downloads': self.stats['downloads'],
            'errors': self.stats['errors']
        }
    
    def clear_cache(self):
        """Clear all cached images."""
        try:
            for filename in os.listdir(self.cache_dir):
                if filename.endswith(('.cache', '.meta')):
                    os.remove(os.path.join(self.cache_dir, filename))
            
            # Reset stats
            self.stats['cache_size_bytes'] = 0
            
        except Exception as e:
            print(f"Error clearing cache: {e}")


# Global image service instance
_image_service = None

def get_image_service() -> ImageService:
    """Get the global image service instance."""
    global _image_service
    if _image_service is None:
        _image_service = ImageService()
    return _image_service