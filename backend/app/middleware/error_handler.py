"""
Centralized error handling middleware for Flask application.
"""

import logging
import traceback
from functools import wraps
from flask import Flask, request, g
from werkzeug.exceptions import HTTPException
from requests.exceptions import RequestException, ConnectionError, Timeout
import sqlite3

from ..utils.response import APIResponse, APIError, ErrorCodes


logger = logging.getLogger(__name__)


def register_error_handlers(app: Flask):
    """Register global error handlers for the Flask application."""
    
    @app.errorhandler(APIError)
    def handle_api_error(error: APIError):
        """Handle custom API errors."""
        logger.warning(f"API Error: {error.message} (Code: {error.code})")
        return error.to_response()
    
    @app.errorhandler(HTTPException)
    def handle_http_error(error: HTTPException):
        """Handle HTTP exceptions (404, 405, etc.)."""
        if error.code == 404:
            return APIResponse.error(
                message="Endpoint not found",
                code=ErrorCodes.RESOURCE_NOT_FOUND,
                status_code=404
            )
        elif error.code == 405:
            return APIResponse.error(
                message="Method not allowed",
                code=ErrorCodes.VALIDATION_ERROR,
                status_code=405
            )
        else:
            return APIResponse.error(
                message=error.description or "HTTP error",
                code=ErrorCodes.INTERNAL_ERROR,
                status_code=error.code
            )
    
    @app.errorhandler(ConnectionError)
    def handle_connection_error(error):
        """Handle network connection errors."""
        logger.error(f"Connection error: {str(error)}")
        return APIResponse.error(
            message="External service unavailable",
            code=ErrorCodes.NETWORK_ERROR,
            details=str(error),
            status_code=503
        )
    
    @app.errorhandler(Timeout)
    def handle_timeout_error(error):
        """Handle request timeout errors."""
        logger.error(f"Timeout error: {str(error)}")
        return APIResponse.error(
            message="Request timed out",
            code=ErrorCodes.NETWORK_ERROR,
            details=str(error),
            status_code=504
        )
    
    @app.errorhandler(RequestException)
    def handle_request_error(error):
        """Handle general request errors."""
        logger.error(f"Request error: {str(error)}")
        return APIResponse.error(
            message="External API error",
            code=ErrorCodes.BUNGIE_API_ERROR,
            details=str(error),
            status_code=503
        )
    
    @app.errorhandler(sqlite3.Error)
    def handle_database_error(error):
        """Handle database errors."""
        logger.error(f"Database error: {str(error)}")
        return APIResponse.error(
            message="Database error",
            code=ErrorCodes.DATABASE_ERROR,
            details=str(error),
            status_code=500
        )
    
    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        """Handle all other unexpected errors."""
        logger.error(f"Unexpected error: {str(error)}")
        logger.error(traceback.format_exc())
        
        # Don't expose internal error details in production
        if app.debug:
            details = {
                'error': str(error),
                'traceback': traceback.format_exc()
            }
        else:
            details = None
        
        return APIResponse.error(
            message="Internal server error",
            code=ErrorCodes.INTERNAL_ERROR,
            details=details,
            status_code=500
        )


def handle_errors(f):
    """
    Decorator for handling errors in route functions.
    Converts exceptions to standardized API responses.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except APIError as e:
            # Re-raise APIError to be handled by error handler
            raise e
        except Exception as e:
            # Convert unexpected errors to APIError
            logger.error(f"Error in {f.__name__}: {str(e)}")
            raise APIError(
                message="An error occurred while processing your request",
                code=ErrorCodes.INTERNAL_ERROR,
                details=str(e) if request.app.debug else None,
                status_code=500
            )
    
    return decorated_function


def validate_json_request(required_fields: list = None, optional_fields: list = None):
    """
    Decorator for validating JSON request data.
    
    Args:
        required_fields: List of required field names
        optional_fields: List of optional field names
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not request.is_json:
                raise APIError(
                    message="Request must be JSON",
                    code=ErrorCodes.VALIDATION_ERROR,
                    status_code=400
                )
            
            data = request.get_json()
            if data is None:
                raise APIError(
                    message="Invalid JSON data",
                    code=ErrorCodes.VALIDATION_ERROR,
                    status_code=400
                )
            
            # Check required fields
            if required_fields:
                missing_fields = [field for field in required_fields if field not in data]
                if missing_fields:
                    raise APIError(
                        message=f"Missing required fields: {', '.join(missing_fields)}",
                        code=ErrorCodes.MISSING_PARAMETER,
                        details={'missing_fields': missing_fields},
                        status_code=400
                    )
            
            # Store validated data in g for use in route
            g.json_data = data
            return f(*args, **kwargs)
        
        return decorated_function
    return decorator


def log_request_response():
    """Middleware to log requests and responses for debugging."""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # Log request
            logger.info(f"{request.method} {request.path} - IP: {request.remote_addr}")
            if request.is_json:
                # Don't log sensitive data
                sensitive_fields = ['password', 'token', 'secret', 'key']
                data = request.get_json() or {}
                filtered_data = {
                    k: '***' if any(sensitive in k.lower() for sensitive in sensitive_fields) else v
                    for k, v in data.items()
                }
                logger.debug(f"Request data: {filtered_data}")
            
            # Execute request
            response = f(*args, **kwargs)
            
            # Log response
            if hasattr(response, 'status_code'):
                logger.info(f"Response: {response.status_code}")
            
            return response
        
        return decorated_function
    return decorator