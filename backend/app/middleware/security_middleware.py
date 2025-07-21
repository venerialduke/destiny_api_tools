"""
Security middleware for request validation, rate limiting, and attack prevention.
Provides comprehensive security features for the API.
"""

import time
import hashlib
import logging
from typing import Dict, Any, Optional
from collections import defaultdict, deque
from flask import request, current_app, g
from ipaddress import ip_address, ip_network

from ..config import config
from ..utils.response import APIError, ErrorCodes, APIResponse


logger = logging.getLogger(__name__)


class RateLimiter:
    """
    Simple in-memory rate limiter with sliding window.
    In production, this should use Redis for distributed rate limiting.
    """
    
    def __init__(self):
        self.requests = defaultdict(deque)
        self.blocked_ips = {}
    
    def is_allowed(self, identifier: str, limit: int = None, window: int = None) -> tuple[bool, Dict[str, Any]]:
        """
        Check if request is allowed based on rate limits.
        
        Args:
            identifier: Unique identifier (IP, user ID, etc.)
            limit: Request limit (default from config)
            window: Time window in seconds (default from config)
            
        Returns:
            Tuple of (is_allowed, rate_limit_info)
        """
        if limit is None:
            limit = config.api.rate_limit_requests
        if window is None:
            window = config.api.rate_limit_window
        
        current_time = time.time()
        
        # Check if IP is temporarily blocked
        if identifier in self.blocked_ips:
            if current_time < self.blocked_ips[identifier]:
                return False, {
                    'limit': limit,
                    'remaining': 0,
                    'reset': self.blocked_ips[identifier],
                    'blocked': True
                }
            else:
                # Unblock IP
                del self.blocked_ips[identifier]
        
        # Clean old requests outside the window
        request_times = self.requests[identifier]
        while request_times and request_times[0] < current_time - window:
            request_times.popleft()
        
        # Check if under limit
        if len(request_times) < limit:
            request_times.append(current_time)
            return True, {
                'limit': limit,
                'remaining': limit - len(request_times),
                'reset': current_time + window,
                'blocked': False
            }
        else:
            # Rate limit exceeded - temporarily block for repeated violations
            violation_count = getattr(self, f'_violations_{identifier}', 0)
            violation_count += 1
            setattr(self, f'_violations_{identifier}', violation_count)
            
            if violation_count >= 5:  # Block after 5 violations
                self.blocked_ips[identifier] = current_time + 300  # Block for 5 minutes
                logger.warning(f"IP {identifier} temporarily blocked for repeated rate limit violations")
            
            return False, {
                'limit': limit,
                'remaining': 0,
                'reset': current_time + window,
                'blocked': violation_count >= 5
            }
    
    def clear_violations(self, identifier: str):
        """Clear violation count for identifier."""
        if hasattr(self, f'_violations_{identifier}'):
            delattr(self, f'_violations_{identifier}')


class RequestValidator:
    """Validates incoming requests for security threats."""
    
    # Common SQL injection patterns
    SQL_INJECTION_PATTERNS = [
        r'union\s+select', r'or\s+1\s*=\s*1', r'drop\s+table',
        r'insert\s+into', r'delete\s+from', r'update\s+.*\s+set',
        r'exec\s*\(', r'script\s*:', r'javascript\s*:'
    ]
    
    # Common XSS patterns
    XSS_PATTERNS = [
        r'<script', r'javascript:', r'onload\s*=', r'onerror\s*=',
        r'<iframe', r'<object', r'<embed'
    ]
    
    @staticmethod
    def validate_request_size(max_size: int = 10 * 1024 * 1024):  # 10MB default
        """
        Validate request size to prevent memory exhaustion attacks.
        
        Args:
            max_size: Maximum request size in bytes
            
        Raises:
            APIError: If request is too large
        """
        content_length = request.content_length
        if content_length and content_length > max_size:
            raise APIError(
                message="Request too large",
                code=ErrorCodes.REQUEST_TOO_LARGE,
                status_code=413
            )
    
    @staticmethod
    def validate_content_type(allowed_types: list = None):
        """
        Validate request content type.
        
        Args:
            allowed_types: List of allowed content types
            
        Raises:
            APIError: If content type is not allowed
        """
        if allowed_types is None:
            allowed_types = ['application/json', 'application/x-www-form-urlencoded']
        
        content_type = request.content_type
        if content_type and not any(allowed in content_type for allowed in allowed_types):
            raise APIError(
                message="Unsupported content type",
                code=ErrorCodes.INVALID_REQUEST,
                status_code=415
            )
    
    @classmethod
    def scan_for_threats(cls, data: str) -> list:
        """
        Scan data for common attack patterns.
        
        Args:
            data: String data to scan
            
        Returns:
            List of detected threat types
        """
        import re
        
        threats = []
        data_lower = data.lower()
        
        # Check for SQL injection
        for pattern in cls.SQL_INJECTION_PATTERNS:
            if re.search(pattern, data_lower):
                threats.append('sql_injection')
                break
        
        # Check for XSS
        for pattern in cls.XSS_PATTERNS:
            if re.search(pattern, data_lower):
                threats.append('xss')
                break
        
        # Check for path traversal
        if '../' in data or '..\\' in data:
            threats.append('path_traversal')
        
        return threats
    
    @classmethod
    def validate_request_data(cls):
        """
        Validate request data for security threats.
        
        Raises:
            APIError: If threats are detected
        """
        # Validate query parameters
        for key, value in request.args.items():
            threats = cls.scan_for_threats(f"{key}={value}")
            if threats:
                logger.warning(f"Security threat detected in query params: {threats}")
                raise APIError(
                    message="Invalid request parameters",
                    code=ErrorCodes.SECURITY_VIOLATION,
                    status_code=400
                )
        
        # Validate JSON body if present
        if request.is_json:
            try:
                json_data = request.get_json()
                if json_data:
                    json_str = str(json_data)
                    threats = cls.scan_for_threats(json_str)
                    if threats:
                        logger.warning(f"Security threat detected in JSON body: {threats}")
                        raise APIError(
                            message="Invalid request data",
                            code=ErrorCodes.SECURITY_VIOLATION,
                            status_code=400
                        )
            except Exception as e:
                logger.error(f"Error validating JSON: {str(e)}")
                raise APIError(
                    message="Invalid JSON data",
                    code=ErrorCodes.INVALID_REQUEST,
                    status_code=400
                )


class IPWhitelist:
    """Manages IP whitelisting for sensitive endpoints."""
    
    def __init__(self):
        # Default allowed networks (can be configured via environment)
        self.allowed_networks = [
            ip_network('127.0.0.0/8'),    # Localhost
            ip_network('10.0.0.0/8'),     # Private network
            ip_network('172.16.0.0/12'),  # Private network
            ip_network('192.168.0.0/16'), # Private network
        ]
        
        # Add custom networks from config if available
        custom_networks = getattr(config, 'allowed_ip_networks', [])
        for network in custom_networks:
            try:
                self.allowed_networks.append(ip_network(network))
            except Exception as e:
                logger.error(f"Invalid IP network in config: {network} - {e}")
    
    def is_allowed(self, ip_addr: str) -> bool:
        """
        Check if IP address is in whitelist.
        
        Args:
            ip_addr: IP address to check
            
        Returns:
            True if IP is allowed
        """
        try:
            ip = ip_address(ip_addr)
            return any(ip in network for network in self.allowed_networks)
        except Exception as e:
            logger.error(f"Error checking IP {ip_addr}: {e}")
            return False


# Global instances
rate_limiter = RateLimiter()
ip_whitelist = IPWhitelist()


def apply_rate_limiting():
    """Apply rate limiting to current request."""
    # Get client identifier (IP address primarily)
    client_ip = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    if client_ip and ',' in client_ip:
        client_ip = client_ip.split(',')[0].strip()
    
    # Check rate limit
    is_allowed, rate_info = rate_limiter.is_allowed(client_ip)
    
    # Store rate limit info in g for use in response headers
    g.rate_limit_info = rate_info
    
    if not is_allowed:
        logger.warning(f"Rate limit exceeded for IP: {client_ip}")
        
        error_message = "Rate limit exceeded"
        if rate_info.get('blocked'):
            error_message = "IP temporarily blocked due to repeated violations"
        
        raise APIError(
            message=error_message,
            code=ErrorCodes.RATE_LIMIT_EXCEEDED,
            details={
                'limit': rate_info['limit'],
                'reset': rate_info['reset']
            },
            status_code=429
        )


def apply_security_validation():
    """Apply security validation to current request."""
    try:
        # Validate request size
        RequestValidator.validate_request_size()
        
        # Validate content type for POST/PUT requests
        if request.method in ['POST', 'PUT', 'PATCH']:
            RequestValidator.validate_content_type()
        
        # Scan for security threats
        RequestValidator.validate_request_data()
        
    except APIError:
        raise
    except Exception as e:
        logger.error(f"Security validation error: {str(e)}")
        raise APIError(
            message="Security validation failed",
            code=ErrorCodes.SECURITY_VIOLATION,
            status_code=400
        )


def require_ip_whitelist():
    """Require request to come from whitelisted IP."""
    client_ip = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    if client_ip and ',' in client_ip:
        client_ip = client_ip.split(',')[0].strip()
    
    if not ip_whitelist.is_allowed(client_ip):
        logger.warning(f"Unauthorized IP access attempt: {client_ip}")
        raise APIError(
            message="Access denied",
            code=ErrorCodes.ACCESS_DENIED,
            status_code=403
        )


def init_security_middleware(app):
    """
    Initialize security middleware for Flask app.
    
    Args:
        app: Flask application instance
    """
    @app.before_request
    def apply_security():
        """Apply security measures to all requests."""
        # Skip security for health check endpoints
        if request.path in ['/api/core/health', '/health']:
            return
        
        try:
            # Apply rate limiting
            apply_rate_limiting()
            
            # Apply security validation
            apply_security_validation()
            
        except APIError as e:
            return e.to_response()
        except Exception as e:
            logger.error(f"Security middleware error: {str(e)}")
            return APIResponse.error(
                message="Security validation failed",
                code=ErrorCodes.SECURITY_VIOLATION,
                status_code=500
            )
    
    @app.after_request
    def add_rate_limit_headers(response):
        """Add rate limit headers to response."""
        if hasattr(g, 'rate_limit_info'):
            info = g.rate_limit_info
            response.headers['X-RateLimit-Limit'] = str(info['limit'])
            response.headers['X-RateLimit-Remaining'] = str(info['remaining'])
            response.headers['X-RateLimit-Reset'] = str(int(info['reset']))
        
        return response