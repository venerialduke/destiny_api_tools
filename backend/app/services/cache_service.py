"""
Advanced caching service with multiple backends and intelligent invalidation.
Supports in-memory, Redis, and hybrid caching strategies.
"""

import json
import time
import pickle
import hashlib
import logging
import threading
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, List, Union, Callable
from dataclasses import dataclass, field
from collections import defaultdict

from ..config import config


logger = logging.getLogger(__name__)


@dataclass
class CacheEntry:
    """Represents a cached item with metadata."""
    value: Any
    created_at: float
    expires_at: float
    access_count: int = 0
    last_accessed: float = field(default_factory=time.time)
    tags: List[str] = field(default_factory=list)
    size_bytes: int = 0
    
    def is_expired(self) -> bool:
        """Check if the cache entry has expired."""
        return time.time() > self.expires_at
    
    def is_stale(self, stale_threshold: float = 0.8) -> bool:
        """Check if the cache entry is approaching expiration."""
        total_ttl = self.expires_at - self.created_at
        elapsed = time.time() - self.created_at
        return elapsed >= (total_ttl * stale_threshold)
    
    def touch(self):
        """Update access statistics."""
        self.access_count += 1
        self.last_accessed = time.time()


class CacheBackend(ABC):
    """Abstract base class for cache backends."""
    
    @abstractmethod
    def get(self, key: str) -> Optional[CacheEntry]:
        """Get item from cache."""
        pass
    
    @abstractmethod
    def set(self, key: str, entry: CacheEntry) -> bool:
        """Set item in cache."""
        pass
    
    @abstractmethod
    def delete(self, key: str) -> bool:
        """Delete item from cache."""
        pass
    
    @abstractmethod
    def clear(self) -> bool:
        """Clear all items from cache."""
        pass
    
    @abstractmethod
    def get_stats(self) -> Dict[str, Any]:
        """Get cache statistics."""
        pass


class InMemoryCache(CacheBackend):
    """In-memory cache backend with LRU eviction."""
    
    def __init__(self, max_size: int = 1000, max_memory_mb: int = 100):
        self.max_size = max_size
        self.max_memory_bytes = max_memory_mb * 1024 * 1024
        self.cache: Dict[str, CacheEntry] = {}
        self.lock = threading.RLock()
        
        # Statistics
        self.hits = 0
        self.misses = 0
        self.evictions = 0
        self.current_memory = 0
    
    def get(self, key: str) -> Optional[CacheEntry]:
        """Get item from memory cache."""
        with self.lock:
            entry = self.cache.get(key)
            if entry:
                if entry.is_expired():
                    self.delete(key)
                    self.misses += 1
                    return None
                else:
                    entry.touch()
                    self.hits += 1
                    return entry
            else:
                self.misses += 1
                return None
    
    def set(self, key: str, entry: CacheEntry) -> bool:
        """Set item in memory cache."""
        with self.lock:
            # Remove existing entry if present
            if key in self.cache:
                old_entry = self.cache[key]
                self.current_memory -= old_entry.size_bytes
            
            # Calculate entry size
            entry.size_bytes = self._calculate_size(entry.value)
            
            # Check if we need to evict entries
            self._evict_if_needed(entry.size_bytes)
            
            # Store the entry
            self.cache[key] = entry
            self.current_memory += entry.size_bytes
            
            return True
    
    def delete(self, key: str) -> bool:
        """Delete item from memory cache."""
        with self.lock:
            if key in self.cache:
                entry = self.cache.pop(key)
                self.current_memory -= entry.size_bytes
                return True
            return False
    
    def clear(self) -> bool:
        """Clear all items from memory cache."""
        with self.lock:
            self.cache.clear()
            self.current_memory = 0
            return True
    
    def _calculate_size(self, obj: Any) -> int:
        """Estimate object size in bytes."""
        try:
            return len(pickle.dumps(obj))
        except:
            # Fallback estimate
            return len(str(obj).encode('utf-8'))
    
    def _evict_if_needed(self, new_entry_size: int):
        """Evict entries if cache limits are exceeded."""
        # Check size limit
        while len(self.cache) >= self.max_size:
            self._evict_lru()
        
        # Check memory limit
        while (self.current_memory + new_entry_size) > self.max_memory_bytes:
            if not self._evict_lru():
                break  # No more entries to evict
    
    def _evict_lru(self) -> bool:
        """Evict least recently used entry."""
        if not self.cache:
            return False
        
        # Find LRU entry
        lru_key = min(self.cache.keys(), 
                     key=lambda k: self.cache[k].last_accessed)
        
        self.delete(lru_key)
        self.evictions += 1
        return True
    
    def get_stats(self) -> Dict[str, Any]:
        """Get memory cache statistics."""
        with self.lock:
            total_requests = self.hits + self.misses
            hit_rate = (self.hits / total_requests * 100) if total_requests > 0 else 0
            
            return {
                'backend': 'memory',
                'size': len(self.cache),
                'max_size': self.max_size,
                'memory_usage_mb': self.current_memory / 1024 / 1024,
                'max_memory_mb': self.max_memory_bytes / 1024 / 1024,
                'hits': self.hits,
                'misses': self.misses,
                'hit_rate_percent': round(hit_rate, 2),
                'evictions': self.evictions
            }


class RedisCache(CacheBackend):
    """Redis cache backend for distributed caching."""
    
    def __init__(self, redis_url: str = None):
        self.redis_url = redis_url or config.cache.redis_url
        self._redis = None
        self._connected = False
        
        # Statistics
        self.hits = 0
        self.misses = 0
        
        self._connect()
    
    def _connect(self):
        """Connect to Redis."""
        try:
            import redis
            self._redis = redis.from_url(self.redis_url)
            # Test connection
            self._redis.ping()
            self._connected = True
            logger.info("Connected to Redis cache")
        except ImportError:
            logger.warning("Redis not available - install redis package for distributed caching")
            self._connected = False
        except Exception as e:
            logger.warning(f"Failed to connect to Redis: {e}")
            self._connected = False
    
    def get(self, key: str) -> Optional[CacheEntry]:
        """Get item from Redis cache."""
        if not self._connected:
            return None
        
        try:
            data = self._redis.get(f"cache:{key}")
            if data:
                entry = pickle.loads(data)
                if entry.is_expired():
                    self.delete(key)
                    self.misses += 1
                    return None
                else:
                    entry.touch()
                    self.hits += 1
                    return entry
            else:
                self.misses += 1
                return None
        except Exception as e:
            logger.error(f"Redis get error: {e}")
            self.misses += 1
            return None
    
    def set(self, key: str, entry: CacheEntry) -> bool:
        """Set item in Redis cache."""
        if not self._connected:
            return False
        
        try:
            ttl = int(entry.expires_at - time.time())
            if ttl > 0:
                data = pickle.dumps(entry)
                self._redis.setex(f"cache:{key}", ttl, data)
                return True
            return False
        except Exception as e:
            logger.error(f"Redis set error: {e}")
            return False
    
    def delete(self, key: str) -> bool:
        """Delete item from Redis cache."""
        if not self._connected:
            return False
        
        try:
            result = self._redis.delete(f"cache:{key}")
            return result > 0
        except Exception as e:
            logger.error(f"Redis delete error: {e}")
            return False
    
    def clear(self) -> bool:
        """Clear all cache items from Redis."""
        if not self._connected:
            return False
        
        try:
            keys = self._redis.keys("cache:*")
            if keys:
                self._redis.delete(*keys)
            return True
        except Exception as e:
            logger.error(f"Redis clear error: {e}")
            return False
    
    def get_stats(self) -> Dict[str, Any]:
        """Get Redis cache statistics."""
        total_requests = self.hits + self.misses
        hit_rate = (self.hits / total_requests * 100) if total_requests > 0 else 0
        
        stats = {
            'backend': 'redis',
            'connected': self._connected,
            'hits': self.hits,
            'misses': self.misses,
            'hit_rate_percent': round(hit_rate, 2)
        }
        
        if self._connected:
            try:
                info = self._redis.info()
                stats.update({
                    'redis_version': info.get('redis_version'),
                    'used_memory_mb': info.get('used_memory', 0) / 1024 / 1024,
                    'total_keys': info.get('db0', {}).get('keys', 0) if 'db0' in info else 0
                })
            except Exception as e:
                logger.error(f"Redis stats error: {e}")
        
        return stats


class HybridCache(CacheBackend):
    """Hybrid cache using both memory and Redis backends."""
    
    def __init__(self, memory_cache: InMemoryCache = None, redis_cache: RedisCache = None):
        self.memory_cache = memory_cache or InMemoryCache()
        self.redis_cache = redis_cache or RedisCache()
        
    def get(self, key: str) -> Optional[CacheEntry]:
        """Get item from hybrid cache (memory first, then Redis)."""
        # Try memory cache first
        entry = self.memory_cache.get(key)
        if entry:
            return entry
        
        # Try Redis cache
        entry = self.redis_cache.get(key)
        if entry:
            # Store in memory cache for faster future access
            self.memory_cache.set(key, entry)
            return entry
        
        return None
    
    def set(self, key: str, entry: CacheEntry) -> bool:
        """Set item in both memory and Redis caches."""
        memory_result = self.memory_cache.set(key, entry)
        redis_result = self.redis_cache.set(key, entry)
        return memory_result or redis_result
    
    def delete(self, key: str) -> bool:
        """Delete item from both caches."""
        memory_result = self.memory_cache.delete(key)
        redis_result = self.redis_cache.delete(key)
        return memory_result or redis_result
    
    def clear(self) -> bool:
        """Clear both caches."""
        memory_result = self.memory_cache.clear()
        redis_result = self.redis_cache.clear()
        return memory_result and redis_result
    
    def get_stats(self) -> Dict[str, Any]:
        """Get combined cache statistics."""
        memory_stats = self.memory_cache.get_stats()
        redis_stats = self.redis_cache.get_stats()
        
        return {
            'backend': 'hybrid',
            'memory': memory_stats,
            'redis': redis_stats
        }


class AdvancedCacheService:
    """Advanced caching service with intelligent features."""
    
    def __init__(self, backend: CacheBackend = None):
        self.backend = backend or self._create_default_backend()
        self.prefix = "destiny_api:"
        
        # Tag tracking for cache invalidation
        self.tag_map: Dict[str, List[str]] = defaultdict(list)
        self.lock = threading.RLock()
        
        # Background refresh tracking
        self.refresh_functions: Dict[str, Callable] = {}
    
    def _create_default_backend(self) -> CacheBackend:
        """Create default cache backend based on configuration."""
        if config.cache.redis_url and config.cache.redis_url != 'redis://localhost:6379':
            # Use hybrid cache if Redis is configured
            return HybridCache()
        else:
            # Use memory cache only
            return InMemoryCache(
                max_size=config.cache.max_size,
                max_memory_mb=100
            )
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get value from cache."""
        full_key = self.prefix + key
        entry = self.backend.get(full_key)
        
        if entry:
            # Check for background refresh
            if entry.is_stale() and key in self.refresh_functions:
                self._schedule_background_refresh(key)
            
            return entry.value
        
        return default
    
    def set(self, key: str, value: Any, ttl: int = None, tags: List[str] = None) -> bool:
        """Set value in cache with optional TTL and tags."""
        if ttl is None:
            ttl = config.cache.default_ttl
        
        tags = tags or []
        full_key = self.prefix + key
        
        entry = CacheEntry(
            value=value,
            created_at=time.time(),
            expires_at=time.time() + ttl,
            tags=tags
        )
        
        result = self.backend.set(full_key, entry)
        
        if result and tags:
            with self.lock:
                for tag in tags:
                    self.tag_map[tag].append(full_key)
        
        return result
    
    def delete(self, key: str) -> bool:
        """Delete value from cache."""
        full_key = self.prefix + key
        return self.backend.delete(full_key)
    
    def invalidate_by_tag(self, tag: str) -> int:
        """Invalidate all cache entries with the specified tag."""
        with self.lock:
            keys = self.tag_map.get(tag, [])
            count = 0
            
            for key in keys:
                if self.backend.delete(key):
                    count += 1
            
            # Clean up tag map
            if tag in self.tag_map:
                del self.tag_map[tag]
            
            logger.info(f"Invalidated {count} cache entries with tag: {tag}")
            return count
    
    def mget(self, keys: List[str]) -> Dict[str, Any]:
        """Get multiple values from cache."""
        result = {}
        for key in keys:
            value = self.get(key)
            if value is not None:
                result[key] = value
        return result
    
    def mset(self, mapping: Dict[str, Any], ttl: int = None, tags: List[str] = None) -> int:
        """Set multiple values in cache."""
        count = 0
        for key, value in mapping.items():
            if self.set(key, value, ttl, tags):
                count += 1
        return count
    
    def cached(self, key: str = None, ttl: int = None, tags: List[str] = None):
        """Decorator for caching function results."""
        def decorator(func):
            def wrapper(*args, **kwargs):
                # Generate cache key
                cache_key = key or self._generate_cache_key(func.__name__, args, kwargs)
                
                # Try to get from cache
                result = self.get(cache_key)
                if result is not None:
                    return result
                
                # Execute function and cache result
                result = func(*args, **kwargs)
                self.set(cache_key, result, ttl, tags)
                
                # Store refresh function for background updates
                self.refresh_functions[cache_key] = lambda: func(*args, **kwargs)
                
                return result
            return wrapper
        return decorator
    
    def _generate_cache_key(self, func_name: str, args: tuple, kwargs: dict) -> str:
        """Generate a cache key from function name and arguments."""
        key_data = {
            'function': func_name,
            'args': args,
            'kwargs': sorted(kwargs.items())
        }
        
        key_str = json.dumps(key_data, sort_keys=True, default=str)
        return hashlib.md5(key_str.encode()).hexdigest()
    
    def _schedule_background_refresh(self, key: str):
        """Schedule background refresh of stale cache entry."""
        if key in self.refresh_functions:
            def refresh_task():
                try:
                    refresh_func = self.refresh_functions[key]
                    new_value = refresh_func()
                    self.set(key, new_value)
                    logger.debug(f"Background refreshed cache key: {key}")
                except Exception as e:
                    logger.error(f"Background refresh failed for {key}: {e}")
            
            # Execute in background thread
            import threading
            thread = threading.Thread(target=refresh_task, daemon=True)
            thread.start()
    
    def get_stats(self) -> Dict[str, Any]:
        """Get comprehensive cache statistics."""
        backend_stats = self.backend.get_stats()
        
        with self.lock:
            tag_count = len(self.tag_map)
            tagged_keys = sum(len(keys) for keys in self.tag_map.values())
        
        return {
            **backend_stats,
            'prefix': self.prefix,
            'tags_count': tag_count,
            'tagged_keys': tagged_keys,
            'refresh_functions': len(self.refresh_functions)
        }
    
    def clear(self) -> bool:
        """Clear all cache data."""
        with self.lock:
            self.tag_map.clear()
            self.refresh_functions.clear()
        
        return self.backend.clear()


# Global cache service instance
cache_service = AdvancedCacheService()


def get_cache() -> AdvancedCacheService:
    """Get the global cache service instance."""
    return cache_service


# Convenience functions
def cache_get(key: str, default: Any = None) -> Any:
    """Get value from cache."""
    return cache_service.get(key, default)


def cache_set(key: str, value: Any, ttl: int = None, tags: List[str] = None) -> bool:
    """Set value in cache."""
    return cache_service.set(key, value, ttl, tags)


def cache_delete(key: str) -> bool:
    """Delete value from cache."""
    return cache_service.delete(key)


def cache_invalidate_tag(tag: str) -> int:
    """Invalidate all cache entries with tag."""
    return cache_service.invalidate_by_tag(tag)


def cached(key: str = None, ttl: int = None, tags: List[str] = None):
    """Decorator for caching function results."""
    return cache_service.cached(key, ttl, tags)