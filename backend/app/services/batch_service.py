"""
Request batching service for optimizing API calls and reducing latency.
Combines related requests and implements intelligent batching strategies.
"""

import asyncio
import time
import logging
import threading
from typing import Dict, List, Any, Optional, Callable, Union, Awaitable
from dataclasses import dataclass, field
from collections import defaultdict
from enum import Enum
import concurrent.futures

from ..config import config
from .cache_service import cache_service


logger = logging.getLogger(__name__)


class BatchStrategy(Enum):
    """Different batching strategies for optimizing requests."""
    TIME_BASED = "time_based"        # Batch by time window
    SIZE_BASED = "size_based"        # Batch by number of requests
    ENDPOINT_BASED = "endpoint_based" # Batch by API endpoint
    ADAPTIVE = "adaptive"             # Dynamically choose strategy


@dataclass
class BatchRequest:
    """Represents a single request in a batch."""
    id: str
    endpoint: str
    method: str
    params: Dict[str, Any] = field(default_factory=dict)
    headers: Dict[str, str] = field(default_factory=dict)
    data: Any = None
    priority: int = 0  # Higher number = higher priority
    created_at: float = field(default_factory=time.time)
    timeout: float = 30.0
    cache_key: Optional[str] = None
    callback: Optional[Callable] = None


@dataclass
class BatchResponse:
    """Represents the response from a batched request."""
    request_id: str
    success: bool
    data: Any = None
    error: Optional[str] = None
    status_code: Optional[int] = None
    duration: float = 0.0
    from_cache: bool = False


class RequestBatcher:
    """Manages batching of API requests for optimal performance."""
    
    def __init__(self, 
                 strategy: BatchStrategy = BatchStrategy.ADAPTIVE,
                 max_batch_size: int = 10,
                 max_wait_time: float = 0.1,
                 max_concurrent_batches: int = 5):
        """
        Initialize request batcher.
        
        Args:
            strategy: Batching strategy to use
            max_batch_size: Maximum requests per batch
            max_wait_time: Maximum time to wait before processing batch
            max_concurrent_batches: Maximum concurrent batch operations
        """
        self.strategy = strategy
        self.max_batch_size = max_batch_size
        self.max_wait_time = max_wait_time
        self.max_concurrent_batches = max_concurrent_batches
        
        # Request queues organized by endpoint
        self.pending_requests: Dict[str, List[BatchRequest]] = defaultdict(list)
        self.pending_responses: Dict[str, BatchResponse] = {}
        
        # Threading and synchronization
        self.lock = threading.RLock()
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=max_concurrent_batches)
        self.timers: Dict[str, threading.Timer] = {}
        
        # Statistics
        self.stats = {
            'total_requests': 0,
            'batched_requests': 0,
            'cache_hits': 0,
            'batch_count': 0,
            'average_batch_size': 0,
            'total_time_saved': 0.0
        }
        
        # Adaptive strategy settings
        self.endpoint_stats: Dict[str, Dict[str, Any]] = defaultdict(lambda: {
            'request_count': 0,
            'average_response_time': 0.0,
            'last_batch_size': 0,
            'optimal_batch_size': 1
        })
    
    def add_request(self, request: BatchRequest) -> concurrent.futures.Future:
        """
        Add a request to the batch queue.
        
        Args:
            request: BatchRequest to add to queue
            
        Returns:
            Future that will contain the BatchResponse
        """
        with self.lock:
            # Check cache first
            if request.cache_key:
                cached_response = cache_service.get(request.cache_key)
                if cached_response:
                    self.stats['cache_hits'] += 1
                    future = concurrent.futures.Future()
                    future.set_result(BatchResponse(
                        request_id=request.id,
                        success=True,
                        data=cached_response,
                        from_cache=True
                    ))
                    return future
            
            # Add to appropriate queue based on strategy
            queue_key = self._get_queue_key(request)
            self.pending_requests[queue_key].append(request)
            self.stats['total_requests'] += 1
            
            # Create future for response
            future = concurrent.futures.Future()
            
            # Store future reference
            setattr(request, '_future', future)
            
            # Check if batch should be processed immediately
            if self._should_process_batch(queue_key):
                self._schedule_batch_processing(queue_key)
            elif queue_key not in self.timers:
                # Start timer for this queue
                self._start_batch_timer(queue_key)
            
            return future
    
    def _get_queue_key(self, request: BatchRequest) -> str:
        """Get the appropriate queue key based on batching strategy."""
        if self.strategy == BatchStrategy.ENDPOINT_BASED:
            return f"{request.method}:{request.endpoint}"
        elif self.strategy == BatchStrategy.TIME_BASED:
            # Group all requests together for time-based batching
            return "time_based"
        elif self.strategy == BatchStrategy.SIZE_BASED:
            # Group all requests together for size-based batching
            return "size_based"
        elif self.strategy == BatchStrategy.ADAPTIVE:
            # Use endpoint-based grouping for adaptive strategy
            return f"adaptive:{request.method}:{request.endpoint}"
        else:
            return "default"
    
    def _should_process_batch(self, queue_key: str) -> bool:
        """Determine if a batch should be processed immediately."""
        queue = self.pending_requests[queue_key]
        
        if self.strategy == BatchStrategy.SIZE_BASED:
            return len(queue) >= self.max_batch_size
        elif self.strategy == BatchStrategy.ADAPTIVE:
            # Use learned optimal batch size
            endpoint_stat = self.endpoint_stats[queue_key]
            optimal_size = endpoint_stat['optimal_batch_size']
            return len(queue) >= optimal_size
        else:
            # Default to max batch size
            return len(queue) >= self.max_batch_size
    
    def _start_batch_timer(self, queue_key: str):
        """Start a timer for batch processing."""
        def timer_callback():
            with self.lock:
                if queue_key in self.timers:
                    del self.timers[queue_key]
                self._schedule_batch_processing(queue_key)
        
        timer = threading.Timer(self.max_wait_time, timer_callback)
        self.timers[queue_key] = timer
        timer.start()
    
    def _schedule_batch_processing(self, queue_key: str):
        """Schedule batch processing for a queue."""
        with self.lock:
            # Cancel timer if running
            if queue_key in self.timers:
                self.timers[queue_key].cancel()
                del self.timers[queue_key]
            
            # Get requests to process
            requests = self.pending_requests[queue_key][:self.max_batch_size]
            self.pending_requests[queue_key] = self.pending_requests[queue_key][self.max_batch_size:]
            
            if not requests:
                return
            
            # Update statistics
            self.stats['batch_count'] += 1
            self.stats['batched_requests'] += len(requests)
            current_avg = self.stats['average_batch_size']
            batch_count = self.stats['batch_count']
            self.stats['average_batch_size'] = (current_avg * (batch_count - 1) + len(requests)) / batch_count
            
            # Process batch in executor
            self.executor.submit(self._process_batch, queue_key, requests)
    
    def _process_batch(self, queue_key: str, requests: List[BatchRequest]):
        """Process a batch of requests."""
        start_time = time.time()
        logger.debug(f"Processing batch of {len(requests)} requests for {queue_key}")
        
        try:
            # Group requests by endpoint for actual API calls
            endpoint_groups = defaultdict(list)
            for request in requests:
                endpoint_groups[request.endpoint].append(request)
            
            # Process each endpoint group
            responses = []
            for endpoint, endpoint_requests in endpoint_groups.items():
                group_responses = self._process_endpoint_group(endpoint, endpoint_requests)
                responses.extend(group_responses)
            
            # Update adaptive strategy statistics
            if self.strategy == BatchStrategy.ADAPTIVE:
                self._update_adaptive_stats(queue_key, requests, time.time() - start_time)
            
            # Set futures with responses
            for response in responses:
                request = next((r for r in requests if r.id == response.request_id), None)
                if request and hasattr(request, '_future'):
                    future = getattr(request, '_future')
                    if not future.done():
                        future.set_result(response)
                        
                        # Cache successful responses
                        if response.success and request.cache_key:
                            cache_service.set(request.cache_key, response.data, 
                                           ttl=config.cache.default_ttl)
        
        except Exception as e:
            logger.error(f"Batch processing error: {e}")
            # Set error on all futures
            for request in requests:
                if hasattr(request, '_future'):
                    future = getattr(request, '_future')
                    if not future.done():
                        future.set_result(BatchResponse(
                            request_id=request.id,
                            success=False,
                            error=str(e)
                        ))
    
    def _process_endpoint_group(self, endpoint: str, requests: List[BatchRequest]) -> List[BatchResponse]:
        """Process a group of requests for the same endpoint."""
        responses = []
        
        # Check if this endpoint supports batching
        if self._supports_batch_requests(endpoint):
            # Process as a single batch request
            response = self._execute_batch_request(endpoint, requests)
            responses.append(response)
        else:
            # Process requests individually but concurrently
            with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
                futures = [
                    executor.submit(self._execute_single_request, request)
                    for request in requests
                ]
                
                for future in concurrent.futures.as_completed(futures):
                    try:
                        response = future.result()
                        responses.append(response)
                    except Exception as e:
                        logger.error(f"Individual request failed: {e}")
        
        return responses
    
    def _supports_batch_requests(self, endpoint: str) -> bool:
        """Check if an endpoint supports batch requests."""
        # Define endpoints that support batching
        batch_endpoints = [
            '/Destiny2/Manifest/DestinyInventoryItemDefinition',
            '/Destiny2/GetProfile',
            '/User/GetBungieNetUserById'
        ]
        
        return any(batch_endpoint in endpoint for batch_endpoint in batch_endpoints)
    
    def _execute_batch_request(self, endpoint: str, requests: List[BatchRequest]) -> BatchResponse:
        """Execute a batch request to a supporting endpoint."""
        # This would implement actual batch API calls
        # For now, return a placeholder response
        
        start_time = time.time()
        
        try:
            # Simulate batch processing
            time.sleep(0.01)  # Simulate network delay
            
            # Create combined response
            batch_data = {
                'batch_size': len(requests),
                'endpoint': endpoint,
                'items': [{'request_id': req.id, 'data': f'batch_result_{req.id}'} for req in requests]
            }
            
            duration = time.time() - start_time
            
            return BatchResponse(
                request_id='batch_' + '_'.join(req.id for req in requests),
                success=True,
                data=batch_data,
                duration=duration
            )
            
        except Exception as e:
            return BatchResponse(
                request_id='batch_error',
                success=False,
                error=str(e),
                duration=time.time() - start_time
            )
    
    def _execute_single_request(self, request: BatchRequest) -> BatchResponse:
        """Execute a single request."""
        start_time = time.time()
        
        try:
            # This would implement actual API call
            # For now, simulate request processing
            time.sleep(0.05)  # Simulate network delay
            
            duration = time.time() - start_time
            
            return BatchResponse(
                request_id=request.id,
                success=True,
                data=f'result_for_{request.id}',
                duration=duration,
                status_code=200
            )
            
        except Exception as e:
            return BatchResponse(
                request_id=request.id,
                success=False,
                error=str(e),
                duration=time.time() - start_time
            )
    
    def _update_adaptive_stats(self, queue_key: str, requests: List[BatchRequest], duration: float):
        """Update statistics for adaptive batching strategy."""
        stats = self.endpoint_stats[queue_key]
        
        # Update request count and timing
        stats['request_count'] += len(requests)
        current_avg = stats['average_response_time']
        total_requests = stats['request_count']
        stats['average_response_time'] = (current_avg * (total_requests - len(requests)) + duration) / total_requests
        stats['last_batch_size'] = len(requests)
        
        # Adjust optimal batch size based on performance
        if duration < 0.05:  # Very fast response
            stats['optimal_batch_size'] = min(stats['optimal_batch_size'] + 1, self.max_batch_size)
        elif duration > 0.2:  # Slow response
            stats['optimal_batch_size'] = max(stats['optimal_batch_size'] - 1, 1)
    
    def get_stats(self) -> Dict[str, Any]:
        """Get comprehensive batching statistics."""
        with self.lock:
            time_saved = self.stats['total_time_saved']
            if self.stats['batched_requests'] > 0:
                efficiency = (self.stats['batched_requests'] - self.stats['batch_count']) / self.stats['batched_requests']
            else:
                efficiency = 0
            
            return {
                **self.stats,
                'strategy': self.strategy.value,
                'pending_queues': len(self.pending_requests),
                'total_pending': sum(len(queue) for queue in self.pending_requests.values()),
                'active_timers': len(self.timers),
                'efficiency_ratio': round(efficiency, 3),
                'cache_hit_rate': (self.stats['cache_hits'] / max(self.stats['total_requests'], 1)) * 100,
                'endpoint_stats': dict(self.endpoint_stats) if self.strategy == BatchStrategy.ADAPTIVE else {}
            }
    
    def shutdown(self):
        """Shutdown the batch service and process remaining requests."""
        with self.lock:
            # Cancel all timers
            for timer in self.timers.values():
                timer.cancel()
            self.timers.clear()
            
            # Process remaining requests
            for queue_key, requests in self.pending_requests.items():
                if requests:
                    self._schedule_batch_processing(queue_key)
            
            # Shutdown executor
            self.executor.shutdown(wait=True)


class OptimizedAPIClient:
    """API client with request optimization and batching capabilities."""
    
    def __init__(self, batcher: RequestBatcher = None):
        self.batcher = batcher or RequestBatcher()
        self.request_counter = 0
        self.lock = threading.Lock()
    
    def _generate_request_id(self) -> str:
        """Generate a unique request ID."""
        with self.lock:
            self.request_counter += 1
            return f"req_{int(time.time())}_{self.request_counter}"
    
    async def get(self, endpoint: str, params: Dict[str, Any] = None, 
                  headers: Dict[str, str] = None, cache_key: str = None,
                  priority: int = 0) -> BatchResponse:
        """Make an optimized GET request."""
        request = BatchRequest(
            id=self._generate_request_id(),
            endpoint=endpoint,
            method='GET',
            params=params or {},
            headers=headers or {},
            cache_key=cache_key,
            priority=priority
        )
        
        future = self.batcher.add_request(request)
        return future.result(timeout=30)  # Wait for result
    
    async def post(self, endpoint: str, data: Any = None, 
                   headers: Dict[str, str] = None, cache_key: str = None,
                   priority: int = 0) -> BatchResponse:
        """Make an optimized POST request."""
        request = BatchRequest(
            id=self._generate_request_id(),
            endpoint=endpoint,
            method='POST',
            data=data,
            headers=headers or {},
            cache_key=cache_key,
            priority=priority
        )
        
        future = self.batcher.add_request(request)
        return future.result(timeout=30)  # Wait for result
    
    def get_optimization_stats(self) -> Dict[str, Any]:
        """Get optimization statistics."""
        return self.batcher.get_stats()


# Global optimized client instance
optimized_client = OptimizedAPIClient()


def get_optimized_client() -> OptimizedAPIClient:
    """Get the global optimized API client."""
    return optimized_client


def shutdown_batch_service():
    """Shutdown the batch service."""
    optimized_client.batcher.shutdown()