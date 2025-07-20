"""
Destiny API Tools Backend Application

A Flask-based backend service for the Destiny API Tools web application.
Provides RESTful API endpoints for various Destiny 2 tools and utilities.
"""

from flask import Flask
from flask_cors import CORS
from .config import Config
from .api import api_bp
from .utils.error_handlers import register_error_handlers


def create_app(config_class=Config):
    """Application factory pattern for Flask app creation."""
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions with explicit CORS configuration
    CORS(app, origins=["https://localhost:3000", "http://localhost:3000"], supports_credentials=True)
    
    # Register blueprints
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # Register error handlers
    register_error_handlers(app)
    
    return app