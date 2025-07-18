"""
Configuration settings for the Destiny API Tools backend.
"""

import os
from typing import Dict, Any


class Config:
    """Base configuration class."""
    
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Bungie API settings
    BUNGIE_API_KEY = os.environ.get('BUNGIE_API_KEY')
    BUNGIE_CLIENT_ID = os.environ.get('BUNGIE_CLIENT_ID')
    BUNGIE_CLIENT_SECRET = os.environ.get('BUNGIE_CLIENT_SECRET')
    BUNGIE_API_BASE_URL = 'https://www.bungie.net/Platform'
    
    # OAuth settings
    OAUTH_REDIRECT_URI = os.environ.get('OAUTH_REDIRECT_URI') or 'http://localhost:3000/auth/callback'
    
    # Database settings (if needed later)
    DATABASE_URL = os.environ.get('DATABASE_URL') or 'sqlite:///destiny_tools.db'
    
    # Rate limiting settings
    RATE_LIMIT_STORAGE_URL = os.environ.get('REDIS_URL') or 'redis://localhost:6379'
    
    # CORS settings
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS', '*').split(',')
    
    # Logging settings
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
    
    @classmethod
    def get_bungie_headers(cls) -> Dict[str, str]:
        """Get headers for Bungie API requests."""
        return {
            'X-API-Key': cls.BUNGIE_API_KEY,
            'Content-Type': 'application/json'
        }
    
    @classmethod
    def get_oauth_headers(cls, access_token: str) -> Dict[str, str]:
        """Get headers for authenticated Bungie API requests."""
        headers = cls.get_bungie_headers()
        headers['Authorization'] = f'Bearer {access_token}'
        return headers


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}