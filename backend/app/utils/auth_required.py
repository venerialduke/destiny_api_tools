"""
Authentication decorator for protecting API endpoints.
"""

from functools import wraps
from flask import request, jsonify


def auth_required(f):
    """Decorator to require authentication for API endpoints."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check for Authorization header
        auth_header = request.headers.get('Authorization')
        
        if not auth_header:
            return jsonify({'error': 'Authorization header required'}), 401
        
        # Check for Bearer token format
        if not auth_header.startswith('Bearer '):
            return jsonify({'error': 'Invalid authorization format'}), 401
        
        # Extract the token
        token = auth_header.split(' ')[1]
        
        if not token:
            return jsonify({'error': 'Access token required'}), 401
        
        # TODO: Add token validation logic here
        # For now, we'll assume the token is valid if it exists
        
        return f(*args, **kwargs)
    
    return decorated_function