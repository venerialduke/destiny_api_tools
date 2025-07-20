"""
Base API client for Bungie API interactions with consistent error handling,
retry logic, and performance monitoring.
"""

import time
import logging
from typing import Dict, Optional, Any, Union
from urllib.parse import urljoin
import requests

from ..config import config
from ..utils.response import APIError, ErrorCodes
from .connection_pool import get_optimized_session, record_request_metrics


logger = logging.getLogger(__name__)


class BaseBungieAPIClient:
    """
    Base class for Bungie API interactions with standardized error handling,
    retry logic, rate limiting, and performance monitoring.
    """
    
    def __init__(self, access_token: Optional[str] = None):
        """
        Initialize the Bungie API client.
        
        Args:
            access_token: OAuth access token for authenticated requests
        """
        self.access_token = access_token
        self.base_url = config.api.base_url
        
        # Use optimized connection pool
        self.session = get_optimized_session('bungie_api')
        self.pool_name = 'bungie_api'
        
        # Performance tracking
        self.request_count = 0
        self.total_request_time = 0.0
        self.last_request_time = None
        
        # Rate limiting from config
        self.min_request_interval = 1.0 / config.api.rate_limit_requests * config.api.rate_limit_window
    
    
    def _get_headers(self) -> Dict[str, str]:
        """Get request headers including API key and authorization."""
        if self.access_token:
            return config.get_oauth_headers(self.access_token)
        else:
            return config.get_bungie_headers()
    
    def _rate_limit(self):
        """Implement simple rate limiting."""
        if self.last_request_time:
            time_since_last = time.time() - self.last_request_time
            if time_since_last < self.min_request_interval:
                sleep_time = self.min_request_interval - time_since_last
                time.sleep(sleep_time)
    
    def _handle_response(self, response: requests.Response, endpoint: str) -> Dict[str, Any]:
        """
        Handle API response and convert errors to APIError exceptions.
        
        Args:
            response: The requests response object
            endpoint: The endpoint that was called for logging
            
        Returns:
            The JSON response data
            
        Raises:
            APIError: For various API error conditions
        """
        # Handle rate limiting
        if response.status_code == 429:
            retry_after = response.headers.get('Retry-After', '60')
            raise APIError(
                message=f"Rate limited. Retry after {retry_after} seconds",
                code=ErrorCodes.BUNGIE_RATE_LIMIT,
                details={'retry_after': retry_after, 'endpoint': endpoint},
                status_code=429
            )
        
        # Handle authentication errors
        if response.status_code == 401:
            raise APIError(
                message="Authentication required or token expired",
                code=ErrorCodes.INVALID_TOKEN,
                details={'endpoint': endpoint},
                status_code=401
            )
        
        # Handle forbidden access
        if response.status_code == 403:
            raise APIError(
                message="Insufficient permissions for this operation",
                code=ErrorCodes.INSUFFICIENT_PERMISSIONS,
                details={'endpoint': endpoint},
                status_code=403
            )
        
        # Handle not found
        if response.status_code == 404:
            raise APIError(
                message="Requested resource not found",
                code=ErrorCodes.RESOURCE_NOT_FOUND,
                details={'endpoint': endpoint},
                status_code=404
            )
        
        # Handle server errors
        if response.status_code >= 500:
            raise APIError(
                message="Bungie API server error",
                code=ErrorCodes.BUNGIE_API_UNAVAILABLE,
                details={
                    'endpoint': endpoint,
                    'status_code': response.status_code,
                    'response': response.text[:500]  # Limit response text
                },
                status_code=503
            )
        
        # Handle other client errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                message = error_data.get('Message', f'API error: {response.status_code}')
            except:
                message = f'API error: {response.status_code}'
            
            raise APIError(
                message=message,
                code=ErrorCodes.BUNGIE_API_ERROR,
                details={
                    'endpoint': endpoint,
                    'status_code': response.status_code,
                    'response': response.text[:500]
                },
                status_code=response.status_code
            )
        
        # Parse successful response
        try:
            data = response.json()
            
            # Check Bungie's error response format
            if isinstance(data, dict) and data.get('ErrorCode', 1) != 1:
                error_status = data.get('ErrorStatus', 'Unknown error')
                raise APIError(
                    message=f"Bungie API error: {error_status}",
                    code=ErrorCodes.BUNGIE_API_ERROR,
                    details={
                        'endpoint': endpoint,
                        'error_code': data.get('ErrorCode'),
                        'error_status': error_status,
                        'message': data.get('Message', '')
                    },
                    status_code=400
                )
            
            return data
            
        except ValueError as e:
            raise APIError(
                message="Invalid JSON response from Bungie API",
                code=ErrorCodes.BUNGIE_API_ERROR,
                details={'endpoint': endpoint, 'parse_error': str(e)},
                status_code=502
            )
    
    def request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        """
        Make a request to the Bungie API with error handling and monitoring.
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint (should start with /)
            **kwargs: Additional arguments for requests
            
        Returns:
            The API response data
            
        Raises:
            APIError: For various error conditions
        """
        # Rate limiting
        self._rate_limit()
        
        # Build URL
        url = urljoin(self.base_url, endpoint.lstrip('/'))
        
        # Prepare headers
        headers = self._get_headers()
        if 'headers' in kwargs:
            headers.update(kwargs.pop('headers'))
        
        # Track performance
        start_time = time.time()
        
        try:
            logger.debug(f"Making {method} request to {url}")
            
            response = self.session.request(
                method=method,
                url=url,
                headers=headers,
                timeout=config.api.timeout,
                **kwargs
            )
            
            # Update performance metrics
            request_time = time.time() - start_time
            self.request_count += 1
            self.total_request_time += request_time
            self.last_request_time = time.time()
            
            # Record metrics in connection pool
            record_request_metrics(self.pool_name, request_time, True)
            
            logger.debug(f"Request completed in {request_time:.3f}s with status {response.status_code}")
            
            return self._handle_response(response, endpoint)
            
        except requests.RequestException as e:
            request_time = time.time() - start_time
            
            # Record failed request metrics
            record_request_metrics(self.pool_name, request_time, False)
            
            logger.error(f"Request to {endpoint} failed after {request_time:.3f}s: {str(e)}")
            
            if isinstance(e, requests.Timeout):
                raise APIError(
                    message="Request to Bungie API timed out",
                    code=ErrorCodes.NETWORK_ERROR,
                    details={'endpoint': endpoint, 'timeout': config.api.timeout},
                    status_code=504
                )
            elif isinstance(e, requests.ConnectionError):
                raise APIError(
                    message="Unable to connect to Bungie API",
                    code=ErrorCodes.NETWORK_ERROR,
                    details={'endpoint': endpoint, 'error': str(e)},
                    status_code=503
                )
            else:
                raise APIError(
                    message="Network error while contacting Bungie API",
                    code=ErrorCodes.NETWORK_ERROR,
                    details={'endpoint': endpoint, 'error': str(e)},
                    status_code=502
                )
    
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """Make a GET request to the Bungie API."""
        return self.request('GET', endpoint, params=params)
    
    def post(self, endpoint: str, data: Optional[Dict] = None, json: Optional[Dict] = None) -> Dict[str, Any]:
        """Make a POST request to the Bungie API."""
        return self.request('POST', endpoint, data=data, json=json)
    
    def get_performance_stats(self) -> Dict[str, Any]:
        """Get performance statistics for this client."""
        if self.request_count > 0:
            avg_request_time = self.total_request_time / self.request_count
        else:
            avg_request_time = 0
        
        return {
            'request_count': self.request_count,
            'total_request_time': round(self.total_request_time, 3),
            'average_request_time': round(avg_request_time, 3),
            'last_request_time': self.last_request_time
        }
    
    def reset_performance_stats(self):
        """Reset performance tracking statistics."""
        self.request_count = 0
        self.total_request_time = 0.0
        self.last_request_time = None