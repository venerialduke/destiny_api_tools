"""
Error handlers for the Flask application.
"""

from flask import jsonify
import logging

logger = logging.getLogger(__name__)


def handle_api_error(error, default_message="An error occurred"):
    """Handle API errors and return appropriate JSON response."""
    logger.error(f"API error: {error}")
    
    if hasattr(error, 'response') and hasattr(error.response, 'status_code'):
        # Handle HTTP errors from requests
        status_code = error.response.status_code
        try:
            error_data = error.response.json()
            message = error_data.get('Message', str(error))
        except:
            message = str(error)
    else:
        # Handle other exceptions
        status_code = 500
        message = str(error) or default_message
    
    return jsonify({
        'success': False,
        'error': message
    }), status_code


def register_error_handlers(app):
    """Register error handlers for the Flask app."""
    
    @app.errorhandler(400)
    def bad_request(error):
        """Handle bad request errors."""
        return jsonify({
            'error': 'Bad request',
            'message': str(error.description)
        }), 400
    
    @app.errorhandler(401)
    def unauthorized(error):
        """Handle unauthorized errors."""
        return jsonify({
            'error': 'Unauthorized',
            'message': 'Authentication required'
        }), 401
    
    @app.errorhandler(403)
    def forbidden(error):
        """Handle forbidden errors."""
        return jsonify({
            'error': 'Forbidden',
            'message': 'Insufficient permissions'
        }), 403
    
    @app.errorhandler(404)
    def not_found(error):
        """Handle not found errors."""
        return jsonify({
            'error': 'Not found',
            'message': 'Resource not found'
        }), 404
    
    @app.errorhandler(429)
    def rate_limit_exceeded(error):
        """Handle rate limit errors."""
        return jsonify({
            'error': 'Rate limit exceeded',
            'message': 'Too many requests'
        }), 429
    
    @app.errorhandler(500)
    def internal_server_error(error):
        """Handle internal server errors."""
        logger.error(f"Internal server error: {error}")
        return jsonify({
            'error': 'Internal server error',
            'message': 'An unexpected error occurred'
        }), 500
    
    @app.errorhandler(Exception)
    def handle_exception(error):
        """Handle unexpected exceptions."""
        logger.error(f"Unexpected error: {error}")
        return jsonify({
            'error': 'Internal server error',
            'message': 'An unexpected error occurred'
        }), 500