"""
Destiny API Tools Backend Application

A Flask-based backend service for the Destiny API Tools web application.
Provides RESTful API endpoints for various Destiny 2 tools and utilities.
"""

from flask import Flask
from flask_cors import CORS
from .config import config
from .api import api_bp
from .middleware import register_error_handlers
from .middleware.auth_middleware import init_security_middleware as init_auth_middleware
from .middleware.security_middleware import init_security_middleware


def create_app(config_instance=None):
    """Application factory pattern for Flask app creation."""
    app = Flask(__name__)
    
    # Use provided config or default
    if config_instance is None:
        config_instance = config
    
    # Configure Flask app from config instance
    app.config['SECRET_KEY'] = config_instance.security.secret_key
    app.config['DEBUG'] = getattr(config_instance, 'DEBUG', False)
    app.config['TESTING'] = getattr(config_instance, 'TESTING', False)
    
    # Initialize CORS with config-based origins
    CORS(app, 
         origins=config_instance.security.cors_origins,
         supports_credentials=True,
         methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
         allow_headers=['Content-Type', 'Authorization', 'X-Requested-With'])
    
    # Initialize security middleware - temporarily disabled for debugging
    # init_security_middleware(app)
    init_auth_middleware(app)
    
    # Register error handlers
    register_error_handlers(app)
    
    # Register blueprints
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # Store config instance for access throughout app
    app.config['APP_CONFIG'] = config_instance
    
    return app