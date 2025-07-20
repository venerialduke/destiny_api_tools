"""
Connection pool manager for optimized HTTP connections to external APIs.
Provides efficient connection reuse and resource management.
"""

import time
import logging
import threading
from typing import Dict, Any, Optional, List
from urllib.parse import urlparse
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests.packages.urllib3.poolmanager import PoolManager

from ..config import config


logger = logging.getLogger(__name__)


class OptimizedHTTPAdapter(HTTPAdapter):
    """Enhanced HTTP adapter with optimized connection pooling."""
    
    def __init__(self, 
                 pool_connections: int = 10,
                 pool_maxsize: int = 50,
                 max_retries: int = 3,
                 pool_block: bool = False,
                 **kwargs):
        """
        Initialize optimized HTTP adapter.
        
        Args:
            pool_connections: Number of connection pools
            pool_maxsize: Maximum connections per pool
            max_retries: Number of retry attempts
            pool_block: Whether to block when pool is full
        """
        super().__init__(**kwargs)
        
        self.config = {
            'pool_connections': pool_connections,
            'pool_maxsize': pool_maxsize,
            'pool_block': pool_block
        }
        
        # Configure retry strategy
        retry_strategy = Retry(
            total=max_retries,
            backoff_factor=config.api.retry_backoff_factor,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "POST", "PUT", "DELETE"]
        )
        
        self.max_retries = retry_strategy
    
    def init_poolmanager(self, *args, **kwargs):
        """Initialize the urllib3 PoolManager with optimized settings."""
        kwargs.update(self.config)
        return super().init_poolmanager(*args, **kwargs)


class ConnectionPoolManager:
    """Manages connection pools for different services and endpoints."""
    
    def __init__(self):
        self._pools: Dict[str, requests.Session] = {}
        self._pool_stats: Dict[str, Dict[str, Any]] = {}
        self._lock = threading.RLock()
        self._created_at = time.time()
        
        # Default pool configurations
        self.pool_configs = {
            'bungie_api': {
                'pool_connections': 20,
                'pool_maxsize': 100,
                'timeout': config.api.timeout,
                'max_retries': config.api.retry_attempts
            },
            'oauth': {
                'pool_connections': 5,
                'pool_maxsize': 20,
                'timeout': 15,
                'max_retries': 2
            },
            'manifest': {
                'pool_connections': 2,
                'pool_maxsize': 10,
                'timeout': 60,
                'max_retries': 2
            },
            'default': {
                'pool_connections': 10,
                'pool_maxsize': 50,
                'timeout': 30,
                'max_retries': 3
            }
        }
    
    def get_session(self, pool_name: str = 'default') -> requests.Session:
        """
        Get or create a session for the specified pool.
        
        Args:
            pool_name: Name of the connection pool
            
        Returns:
            Configured requests session
        """
        with self._lock:
            if pool_name not in self._pools:
                self._pools[pool_name] = self._create_session(pool_name)
                self._pool_stats[pool_name] = {
                    'created_at': time.time(),
                    'request_count': 0,
                    'error_count': 0,
                    'total_time': 0.0,
                    'last_used': time.time()
                }
                logger.info(f"Created new connection pool: {pool_name}")
            
            # Update last used timestamp
            self._pool_stats[pool_name]['last_used'] = time.time()
            
            return self._pools[pool_name]
    
    def _create_session(self, pool_name: str) -> requests.Session:
        """Create a new session with optimized configuration."""
        config_data = self.pool_configs.get(pool_name, self.pool_configs['default'])
        
        session = requests.Session()
        
        # Create optimized adapter
        adapter = OptimizedHTTPAdapter(
            pool_connections=config_data['pool_connections'],
            pool_maxsize=config_data['pool_maxsize'],
            max_retries=config_data['max_retries']
        )
        
        # Mount adapter for both HTTP and HTTPS
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        
        # Set default timeout
        session.timeout = config_data['timeout']
        
        return session
    
    def record_request(self, pool_name: str, duration: float, success: bool = True):
        """Record request statistics for monitoring."""
        with self._lock:
            if pool_name in self._pool_stats:
                stats = self._pool_stats[pool_name]
                stats['request_count'] += 1
                stats['total_time'] += duration
                stats['last_used'] = time.time()
                
                if not success:
                    stats['error_count'] += 1
    
    def get_pool_stats(self, pool_name: str = None) -> Dict[str, Any]:
        """Get statistics for a specific pool or all pools."""
        with self._lock:
            if pool_name:
                if pool_name in self._pool_stats:
                    stats = self._pool_stats[pool_name].copy()
                    if stats['request_count'] > 0:
                        stats['average_time'] = stats['total_time'] / stats['request_count']
                        stats['error_rate'] = stats['error_count'] / stats['request_count']
                    else:
                        stats['average_time'] = 0
                        stats['error_rate'] = 0
                    return stats
                return {}
            else:
                # Return all pool stats
                all_stats = {}
                for name, stats in self._pool_stats.items():
                    pool_stats = stats.copy()
                    if pool_stats['request_count'] > 0:
                        pool_stats['average_time'] = pool_stats['total_time'] / pool_stats['request_count']
                        pool_stats['error_rate'] = pool_stats['error_count'] / pool_stats['request_count']
                    else:
                        pool_stats['average_time'] = 0
                        pool_stats['error_rate'] = 0
                    all_stats[name] = pool_stats
                return all_stats
    
    def cleanup_idle_pools(self, max_idle_time: int = 3600):
        """Clean up pools that haven't been used recently."""
        current_time = time.time()
        pools_to_remove = []
        
        with self._lock:
            for pool_name, stats in self._pool_stats.items():
                if current_time - stats['last_used'] > max_idle_time:
                    pools_to_remove.append(pool_name)
            
            for pool_name in pools_to_remove:
                if pool_name in self._pools:
                    self._pools[pool_name].close()
                    del self._pools[pool_name]
                    del self._pool_stats[pool_name]
                    logger.info(f"Cleaned up idle connection pool: {pool_name}")
        
        return len(pools_to_remove)
    
    def close_all_pools(self):
        """Close all connection pools."""
        with self._lock:
            for session in self._pools.values():
                session.close()
            self._pools.clear()
            self._pool_stats.clear()
            logger.info("Closed all connection pools")
    
    def get_summary(self) -> Dict[str, Any]:
        """Get summary information about all pools."""
        with self._lock:
            return {
                'total_pools': len(self._pools),
                'uptime_seconds': time.time() - self._created_at,
                'pool_names': list(self._pools.keys()),
                'total_requests': sum(stats['request_count'] for stats in self._pool_stats.values()),
                'total_errors': sum(stats['error_count'] for stats in self._pool_stats.values())
            }


class RequestBatcher:
    """Batches multiple requests for efficient processing."""
    
    def __init__(self, max_batch_size: int = 10, max_wait_time: float = 0.1):
        """
        Initialize request batcher.
        
        Args:
            max_batch_size: Maximum requests per batch
            max_wait_time: Maximum time to wait for batching (seconds)
        """
        self.max_batch_size = max_batch_size
        self.max_wait_time = max_wait_time
        self._pending_requests: List[Dict[str, Any]] = []
        self._lock = threading.Lock()
        self._batch_timer: Optional[threading.Timer] = None
    
    def add_request(self, request_info: Dict[str, Any]) -> Any:
        """
        Add a request to the batch queue.
        
        Args:
            request_info: Dictionary containing request details
            
        Returns:
            Response when batch is processed
        """
        with self._lock:
            self._pending_requests.append(request_info)
            
            # If batch is full, process immediately
            if len(self._pending_requests) >= self.max_batch_size:
                return self._process_batch()
            
            # Start timer if this is the first request in batch
            if len(self._pending_requests) == 1:
                self._batch_timer = threading.Timer(self.max_wait_time, self._process_batch)
                self._batch_timer.start()
    
    def _process_batch(self) -> List[Any]:
        """Process the current batch of requests."""
        with self._lock:
            if not self._pending_requests:
                return []
            
            # Cancel timer if running
            if self._batch_timer:
                self._batch_timer.cancel()
                self._batch_timer = None
            
            # Process all pending requests
            batch = self._pending_requests.copy()
            self._pending_requests.clear()
            
            logger.debug(f"Processing batch of {len(batch)} requests")
            
            # Execute requests concurrently
            results = []
            for request_info in batch:
                try:
                    # Execute the request
                    response = self._execute_request(request_info)
                    results.append(response)
                except Exception as e:
                    logger.error(f"Batch request failed: {e}")
                    results.append({'error': str(e)})
            
            return results
    
    def _execute_request(self, request_info: Dict[str, Any]) -> Any:
        """Execute a single request from the batch."""
        # This would be implemented based on the specific request type
        # For now, return a placeholder
        return {'status': 'success', 'data': request_info}


# Global connection pool manager instance
connection_pool_manager = ConnectionPoolManager()


def get_optimized_session(pool_name: str = 'default') -> requests.Session:
    """
    Get an optimized session for making HTTP requests.
    
    Args:
        pool_name: Name of the connection pool to use
        
    Returns:
        Configured requests session
    """
    return connection_pool_manager.get_session(pool_name)


def record_request_metrics(pool_name: str, duration: float, success: bool = True):
    """Record request metrics for monitoring."""
    connection_pool_manager.record_request(pool_name, duration, success)


def get_connection_stats(pool_name: str = None) -> Dict[str, Any]:
    """Get connection pool statistics."""
    return connection_pool_manager.get_pool_stats(pool_name)


def cleanup_connections():
    """Clean up idle connections."""
    return connection_pool_manager.cleanup_idle_pools()


# Periodic cleanup task
def start_cleanup_scheduler():
    """Start periodic cleanup of idle connections."""
    import threading
    import time
    
    def cleanup_task():
        while True:
            try:
                time.sleep(1800)  # Run every 30 minutes
                cleaned = cleanup_connections()
                if cleaned > 0:
                    logger.info(f"Cleaned up {cleaned} idle connection pools")
            except Exception as e:
                logger.error(f"Connection cleanup error: {e}")
    
    cleanup_thread = threading.Thread(target=cleanup_task, daemon=True)
    cleanup_thread.start()
    logger.info("Started connection pool cleanup scheduler")


# Initialize cleanup scheduler
start_cleanup_scheduler()