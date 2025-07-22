"""
Standardized API response utilities for consistent error handling and response formatting.
"""

from datetime import datetime
from flask import jsonify
from typing import Any, Dict, Optional, Union


class APIResponse:
    """Standardized API response formatter."""
    
    @staticmethod
    def success(data: Any = None, message: Optional[str] = None, meta: Optional[Dict] = None, status_code: int = 200):
        """
        Create a successful API response.
        
        Args:
            data: The response data
            message: Optional success message
            meta: Optional metadata (pagination, etc.)
            status_code: HTTP status code (default: 200)
        """
        response = jsonify({
            'success': True,
            'data': data,
            'message': message,
            'meta': meta or {},
            'timestamp': datetime.utcnow().isoformat() + 'Z'
        })
        response.status_code = status_code
        return response
    
    @staticmethod
    def error(message: str, code: Optional[str] = None, details: Any = None, status_code: int = 400):
        """
        Create an error API response.
        
        Args:
            message: Error message
            code: Error code for programmatic handling
            details: Additional error details
            status_code: HTTP status code (default: 400)
        """
        response = jsonify({
            'success': False,
            'error': {
                'message': message,
                'code': code,
                'details': details
            },
            'timestamp': datetime.utcnow().isoformat() + 'Z'
        })
        response.status_code = status_code
        return response
    
    @staticmethod
    def paginated(items: list, total: int, limit: int, offset: int, has_more: bool = None, message: Optional[str] = None):
        """
        Create a paginated API response.
        
        Args:
            items: List of items for current page
            total: Total number of items
            limit: Items per page
            offset: Current offset
            has_more: Whether there are more items (calculated if not provided)
            message: Optional message
        """
        if has_more is None:
            has_more = offset + limit < total
        
        meta = {
            'pagination': {
                'total': total,
                'limit': limit,
                'offset': offset,
                'has_more': has_more,
                'next_offset': offset + limit if has_more else None,
                'current_page': (offset // limit) + 1 if limit > 0 else 1,
                'total_pages': (total + limit - 1) // limit if limit > 0 else 1
            }
        }
        
        return APIResponse.success(
            data=items,
            message=message,
            meta=meta
        )


class APIError(Exception):
    """Custom exception for API errors with structured error information."""
    
    def __init__(self, message: str, code: Optional[str] = None, details: Any = None, status_code: int = 400):
        super().__init__(message)
        self.message = message
        self.code = code
        self.details = details
        self.status_code = status_code
    
    def to_response(self):
        """Convert exception to API response."""
        return APIResponse.error(
            message=self.message,
            code=self.code,
            details=self.details,
            status_code=self.status_code
        )


# Common error codes for consistency
class ErrorCodes:
    """Standardized error codes for the application."""
    
    # Authentication errors (1000-1999)
    AUTHENTICATION_REQUIRED = "AUTH_001"
    INVALID_TOKEN = "AUTH_002"
    TOKEN_EXPIRED = "AUTH_003"
    INSUFFICIENT_PERMISSIONS = "AUTH_004"
    OAUTH_ERROR = "AUTH_005"
    SECURITY_VIOLATION = "AUTH_006"
    
    # Validation errors (2000-2999)
    VALIDATION_ERROR = "VAL_001"
    MISSING_PARAMETER = "VAL_002"
    INVALID_PARAMETER = "VAL_003"
    PARAMETER_OUT_OF_RANGE = "VAL_004"
    INVALID_REQUEST = "VAL_005"
    
    # Resource errors (3000-3999)
    RESOURCE_NOT_FOUND = "RES_001"
    RESOURCE_ALREADY_EXISTS = "RES_002"
    RESOURCE_LOCKED = "RES_003"
    RESOURCE_DELETED = "RES_004"
    
    # External API errors (4000-4999)
    BUNGIE_API_ERROR = "EXT_001"
    BUNGIE_API_UNAVAILABLE = "EXT_002"
    BUNGIE_RATE_LIMIT = "EXT_003"
    NETWORK_ERROR = "EXT_004"
    
    # Database errors (5000-5999)
    DATABASE_ERROR = "DB_001"
    DATABASE_CONNECTION_ERROR = "DB_002"
    DATABASE_TIMEOUT = "DB_003"
    
    # Internal errors (6000-6999)
    INTERNAL_ERROR = "INT_001"
    SERVICE_UNAVAILABLE = "INT_002"
    CONFIGURATION_ERROR = "INT_003"
    
    # Image service errors (7000-7999)
    IMAGE_NOT_FOUND = "IMG_001"
    IMAGE_PROCESSING_ERROR = "IMG_002"
    IMAGE_CACHE_ERROR = "IMG_003"


# Common error response helpers
def authentication_required():
    """Standard authentication required error."""
    return APIResponse.error(
        message="Authentication required",
        code=ErrorCodes.AUTHENTICATION_REQUIRED,
        status_code=401
    )


def invalid_token():
    """Standard invalid token error."""
    return APIResponse.error(
        message="Invalid or expired authentication token",
        code=ErrorCodes.INVALID_TOKEN,
        status_code=401
    )


def resource_not_found(resource_type: str = "Resource"):
    """Standard resource not found error."""
    return APIResponse.error(
        message=f"{resource_type} not found",
        code=ErrorCodes.RESOURCE_NOT_FOUND,
        status_code=404
    )


def validation_error(message: str, details: Any = None):
    """Standard validation error."""
    return APIResponse.error(
        message=message,
        code=ErrorCodes.VALIDATION_ERROR,
        details=details,
        status_code=400
    )


def bungie_api_error(message: str = "Bungie API error", details: Any = None):
    """Standard Bungie API error."""
    return APIResponse.error(
        message=message,
        code=ErrorCodes.BUNGIE_API_ERROR,
        details=details,
        status_code=503
    )


def internal_error(message: str = "Internal server error"):
    """Standard internal error."""
    return APIResponse.error(
        message=message,
        code=ErrorCodes.INTERNAL_ERROR,
        status_code=500
    )