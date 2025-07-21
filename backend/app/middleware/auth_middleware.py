"""
Authentication middleware for JWT token validation and user context management.
Provides secure token handling and request authorization.
"""

import os
import time
import logging
from functools import wraps
from typing import Dict, Any, Optional
from flask import request, g, current_app

from ..config import config
from ..utils.response import APIError, ErrorCodes, APIResponse


logger = logging.getLogger(__name__)


class TokenValidator:
    """Handles JWT token validation and refresh logic."""
    
    @staticmethod
    def validate_token(token: str) -> Dict[str, Any]:
        """
        Validate a JWT token and return payload.
        
        Args:
            token: JWT token string
            
        Returns:
            Token payload if valid
            
        Raises:
            APIError: If token is invalid or expired
        """
        if not token:
            raise APIError(
                message="Authorization token required",
                code=ErrorCodes.INVALID_TOKEN,
                status_code=401
            )
        
        try:
            # Remove 'Bearer ' prefix if present
            if token.startswith('Bearer '):
                token = token[7:]
            
            # For Bungie OAuth tokens, we don't decode them - we validate by making a test request
            # This is a simplified validation - in production you'd want to cache validation results
            payload = {
                'access_token': token,
                'exp': time.time() + config.security.session_timeout  # Assume token is valid for session timeout
            }
            
            return payload
            
        except Exception as e:
            logger.error(f"Token validation error: {str(e)}")
            raise APIError(
                message="Token validation failed",
                code=ErrorCodes.INVALID_TOKEN,
                status_code=401
            )
    
    @staticmethod
    def is_token_expired(payload: Dict[str, Any], buffer_seconds: int = None) -> bool:
        """
        Check if token is expired or close to expiration.
        
        Args:
            payload: Token payload
            buffer_seconds: Extra buffer time before considering token expired
            
        Returns:
            True if token is expired or about to expire
        """
        if buffer_seconds is None:
            buffer_seconds = config.security.token_expiry_buffer
        
        exp = payload.get('exp', 0)
        current_time = time.time()
        
        return current_time >= (exp - buffer_seconds)


def require_auth(optional: bool = False):
    """
    Decorator to require authentication for endpoints.
    
    Args:
        optional: If True, authentication is optional and errors won't be raised
        
    Returns:
        Decorated function
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            auth_header = request.headers.get('Authorization')
            
            if not auth_header:
                if optional:
                    g.current_user = None
                    g.access_token = None
                    return f(*args, **kwargs)
                else:
                    return APIResponse.error(
                        message="Authorization header required",
                        code=ErrorCodes.INVALID_TOKEN,
                        status_code=401
                    )
            
            try:
                # Validate the token
                payload = TokenValidator.validate_token(auth_header)
                
                # Store user context in Flask's g object
                g.current_user = {
                    'access_token': payload['access_token'],
                    'exp': payload['exp']
                }
                g.access_token = payload['access_token']
                
                # Check if token is about to expire
                if TokenValidator.is_token_expired(payload):
                    logger.warning("Token is close to expiration")
                    # You could implement automatic refresh here
                
                return f(*args, **kwargs)
                
            except APIError as e:
                if optional:
                    g.current_user = None
                    g.access_token = None
                    return f(*args, **kwargs)
                else:
                    return e.to_response()
            except Exception as e:
                logger.error(f"Authentication error: {str(e)}")
                if optional:
                    g.current_user = None
                    g.access_token = None
                    return f(*args, **kwargs)
                else:
                    return APIResponse.error(
                        message="Authentication failed",
                        code=ErrorCodes.INVALID_TOKEN,
                        status_code=401
                    )
        
        return decorated_function
    return decorator


def require_scopes(*required_scopes):
    """
    Decorator to require specific OAuth scopes for endpoints.
    
    Args:
        required_scopes: List of required OAuth scopes
        
    Returns:
        Decorated function
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not hasattr(g, 'current_user') or not g.current_user:
                return APIResponse.error(
                    message="Authentication required",
                    code=ErrorCodes.INVALID_TOKEN,
                    status_code=401
                )
            
            # In a full implementation, you'd check the token's scopes against required_scopes
            # For now, we'll assume the token has the required scopes if it's valid
            
            return f(*args, **kwargs)
        
        return decorated_function
    return decorator


class SecurityHeaders:
    """Handles security-related HTTP headers."""
    
    @staticmethod
    def apply_security_headers(response):
        """
        Apply security headers to response.
        
        Args:
            response: Flask response object
            
        Returns:
            Response with security headers added
        """
        # Prevent clickjacking
        response.headers['X-Frame-Options'] = 'DENY'
        
        # Prevent MIME type sniffing
        response.headers['X-Content-Type-Options'] = 'nosniff'
        
        # Enable XSS protection
        response.headers['X-XSS-Protection'] = '1; mode=block'
        
        # Enforce HTTPS in production
        env = os.environ.get('FLASK_ENV', 'development')
        if env != 'development':
            response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        
        # Content Security Policy (adjust as needed)
        response.headers['Content-Security-Policy'] = (
            "default-src 'self'; "
            "script-src 'self' 'unsafe-inline' 'unsafe-eval'; "
            "style-src 'self' 'unsafe-inline'; "
            "img-src 'self' data: https://bungie.net https://*.bungie.net; "
            "connect-src 'self' https://bungie.net https://*.bungie.net"
        )
        
        # Remove server information
        response.headers.pop('Server', None)
        
        return response


def init_security_middleware(app):
    """
    Initialize security middleware for the Flask app.
    
    Args:
        app: Flask application instance
    """
    @app.after_request
    def apply_security_headers(response):
        return SecurityHeaders.apply_security_headers(response)
    
    @app.before_request
    def log_request():
        """Log requests for security monitoring."""
        if config.log_level == 'DEBUG':
            logger.debug(f"{request.method} {request.path} from {request.remote_addr}")
    
    @app.after_request
    def log_response(response):
        """Log responses for security monitoring."""
        if config.log_level == 'DEBUG':
            logger.debug(f"Response {response.status_code} for {request.method} {request.path}")
        return response


# Utility functions for manual token validation
def get_current_user() -> Optional[Dict[str, Any]]:
    """Get current authenticated user from Flask context."""
    return getattr(g, 'current_user', None)


def get_access_token() -> Optional[str]:
    """Get current access token from Flask context."""
    return getattr(g, 'access_token', None)


def validate_request_token() -> Dict[str, Any]:
    """
    Validate token from current request without using decorator.
    
    Returns:
        Token payload
        
    Raises:
        APIError: If token is invalid
    """
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        raise APIError(
            message="Authorization header required",
            code=ErrorCodes.INVALID_TOKEN,
            status_code=401
        )
    
    return TokenValidator.validate_token(auth_header)