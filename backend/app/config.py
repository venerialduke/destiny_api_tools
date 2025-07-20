"""
Configuration settings for the Destiny API Tools backend.
Centralizes all configuration management with environment variable validation.
"""

import os
import logging
from typing import Dict, Any, List
from dataclasses import dataclass


@dataclass
class APISettings:
    """API-related configuration settings."""
    key: str
    client_id: str
    client_secret: str
    base_url: str = 'https://www.bungie.net/Platform'
    timeout: int = 30
    rate_limit_requests: int = 25
    rate_limit_window: int = 10  # seconds
    retry_attempts: int = 3
    retry_backoff_factor: float = 1.0


@dataclass
class SecuritySettings:
    """Security-related configuration settings."""
    secret_key: str
    oauth_redirect_uri: str
    cors_origins: List[str]
    csrf_enabled: bool = True
    session_timeout: int = 3600  # seconds
    token_expiry_buffer: int = 300  # seconds before token expires to refresh


@dataclass
class DatabaseSettings:
    """Database configuration settings."""
    url: str
    pool_size: int = 10
    max_overflow: int = 20
    pool_timeout: int = 30
    pool_recycle: int = 3600


@dataclass
class CacheSettings:
    """Cache configuration settings."""
    redis_url: str
    default_ttl: int = 300  # 5 minutes
    max_size: int = 1000
    manifest_ttl: int = 86400  # 24 hours
    user_data_ttl: int = 1800  # 30 minutes


@dataclass
class LoggingSettings:
    """Logging configuration settings."""
    directory: str
    level: str = 'INFO'
    max_file_size: int = 10485760  # 10MB
    backup_count: int = 5
    enable_json: bool = True
    enable_console: bool = True
    enable_file: bool = True


class Config:
    """Base configuration class with validation and defaults."""
    
    def __init__(self):
        """Initialize configuration with validation."""
        self._validate_required_env_vars()
        self._setup_api_settings()
        self._setup_security_settings()
        self._setup_database_settings()
        self._setup_cache_settings()
        self._setup_logging()
        self._setup_directories()
    
    def _validate_required_env_vars(self):
        """Validate that required environment variables are set."""
        required_vars = [
            'BUNGIE_API_KEY',
            'BUNGIE_CLIENT_ID', 
            'BUNGIE_CLIENT_SECRET'
        ]
        
        missing_vars = [var for var in required_vars if not os.environ.get(var)]
        if missing_vars:
            # In development, log warnings instead of failing
            env = os.environ.get('FLASK_ENV', 'development')
            if env == 'development':
                logging.warning(f"Missing environment variables (using defaults): {', '.join(missing_vars)}")
                # Set default values for development
                for var in missing_vars:
                    os.environ.setdefault(var, f'dev-{var.lower().replace("_", "-")}')
            else:
                raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
    
    def _setup_api_settings(self):
        """Setup API-related settings."""
        self.api = APISettings(
            key=os.environ.get('BUNGIE_API_KEY'),
            client_id=os.environ.get('BUNGIE_CLIENT_ID'),
            client_secret=os.environ.get('BUNGIE_CLIENT_SECRET'),
            base_url=os.environ.get('BUNGIE_API_BASE_URL', 'https://www.bungie.net/Platform'),
            timeout=int(os.environ.get('API_TIMEOUT', '30')),
            rate_limit_requests=int(os.environ.get('RATE_LIMIT_REQUESTS', '25')),
            rate_limit_window=int(os.environ.get('RATE_LIMIT_WINDOW', '10')),
            retry_attempts=int(os.environ.get('RETRY_ATTEMPTS', '3')),
            retry_backoff_factor=float(os.environ.get('RETRY_BACKOFF_FACTOR', '1.0'))
        )
    
    def _setup_security_settings(self):
        """Setup security-related settings."""
        self.security = SecuritySettings(
            secret_key=os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production',
            oauth_redirect_uri=os.environ.get('OAUTH_REDIRECT_URI', 'https://localhost:3000/auth/callback'),
            cors_origins=os.environ.get('CORS_ORIGINS', '*').split(','),
            csrf_enabled=os.environ.get('CSRF_ENABLED', 'true').lower() == 'true',
            session_timeout=int(os.environ.get('SESSION_TIMEOUT', '3600')),
            token_expiry_buffer=int(os.environ.get('TOKEN_EXPIRY_BUFFER', '300'))
        )
    
    def _setup_database_settings(self):
        """Setup database configuration."""
        self.database = DatabaseSettings(
            url=os.environ.get('DATABASE_URL', 'sqlite:///destiny_tools.db'),
            pool_size=int(os.environ.get('DB_POOL_SIZE', '10')),
            max_overflow=int(os.environ.get('DB_MAX_OVERFLOW', '20')),
            pool_timeout=int(os.environ.get('DB_POOL_TIMEOUT', '30')),
            pool_recycle=int(os.environ.get('DB_POOL_RECYCLE', '3600'))
        )
    
    def _setup_cache_settings(self):
        """Setup cache configuration."""
        self.cache = CacheSettings(
            redis_url=os.environ.get('REDIS_URL', 'redis://localhost:6379'),
            default_ttl=int(os.environ.get('CACHE_DEFAULT_TTL', '300')),
            max_size=int(os.environ.get('CACHE_MAX_SIZE', '1000')),
            manifest_ttl=int(os.environ.get('MANIFEST_CACHE_TTL', '86400')),
            user_data_ttl=int(os.environ.get('USER_DATA_CACHE_TTL', '1800'))
        )
    
    def _setup_logging(self):
        """Setup logging configuration."""
        self.logs = LoggingSettings(
            directory=os.environ.get('LOGS_DIR', 'logs'),
            level=os.environ.get('LOG_LEVEL', 'INFO'),
            max_file_size=int(os.environ.get('LOG_MAX_FILE_SIZE', '10485760')),
            backup_count=int(os.environ.get('LOG_BACKUP_COUNT', '5')),
            enable_json=os.environ.get('LOG_ENABLE_JSON', 'true').lower() == 'true',
            enable_console=os.environ.get('LOG_ENABLE_CONSOLE', 'true').lower() == 'true',
            enable_file=os.environ.get('LOG_ENABLE_FILE', 'true').lower() == 'true'
        )
        
        # Legacy properties
        self.log_level = self.logs.level
        self.log_format = os.environ.get('LOG_FORMAT', 
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.log_file = os.environ.get('LOG_FILE')
    
    def _setup_directories(self):
        """Setup directory paths."""
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.data_dir = os.environ.get('DATA_DIR', os.path.join(base_dir, 'data'))
        self.logs_dir = os.environ.get('LOGS_DIR', os.path.join(base_dir, 'logs'))
        self.temp_dir = os.environ.get('TEMP_DIR', os.path.join(base_dir, 'temp'))
        
        # Update logs directory in logging settings
        self.logs.directory = self.logs_dir
        
        # Ensure directories exist
        for directory in [self.data_dir, self.logs_dir, self.temp_dir]:
            os.makedirs(directory, exist_ok=True)
    
    @property
    def environment(self) -> str:
        """Get the current environment."""
        return os.environ.get('FLASK_ENV', 'development')
    
    # Legacy compatibility properties
    @property
    def SECRET_KEY(self) -> str:
        return self.security.secret_key
    
    @property
    def BUNGIE_API_KEY(self) -> str:
        return self.api.key
    
    @property
    def BUNGIE_CLIENT_ID(self) -> str:
        return self.api.client_id
    
    @property
    def BUNGIE_CLIENT_SECRET(self) -> str:
        return self.api.client_secret
    
    @property
    def BUNGIE_API_BASE_URL(self) -> str:
        return self.api.base_url
    
    @property
    def OAUTH_REDIRECT_URI(self) -> str:
        return self.security.oauth_redirect_uri
    
    def get_bungie_headers(self) -> Dict[str, str]:
        """Get headers for Bungie API requests."""
        return {
            'X-API-Key': self.api.key,
            'Content-Type': 'application/json',
            'User-Agent': 'Destiny-API-Tools/1.0'
        }
    
    def get_oauth_headers(self, access_token: str) -> Dict[str, str]:
        """Get headers for authenticated Bungie API requests."""
        headers = self.get_bungie_headers()
        headers['Authorization'] = f'Bearer {access_token}'
        return headers
    
    def get_settings_dict(self) -> Dict[str, Any]:
        """Get all settings as a dictionary for debugging/monitoring."""
        return {
            'api': {
                'base_url': self.api.base_url,
                'timeout': self.api.timeout,
                'rate_limit_requests': self.api.rate_limit_requests,
                'rate_limit_window': self.api.rate_limit_window,
                'retry_attempts': self.api.retry_attempts,
                'retry_backoff_factor': self.api.retry_backoff_factor
            },
            'security': {
                'oauth_redirect_uri': self.security.oauth_redirect_uri,
                'cors_origins': self.security.cors_origins,
                'csrf_enabled': self.security.csrf_enabled,
                'session_timeout': self.security.session_timeout,
                'token_expiry_buffer': self.security.token_expiry_buffer
            },
            'cache': {
                'default_ttl': self.cache.default_ttl,
                'max_size': self.cache.max_size,
                'manifest_ttl': self.cache.manifest_ttl,
                'user_data_ttl': self.cache.user_data_ttl
            },
            'logging': {
                'level': self.log_level,
                'format': self.log_format,
                'file': self.log_file
            }
        }


class DevelopmentConfig(Config):
    """Development configuration."""
    
    def __init__(self):
        super().__init__()
        self.DEBUG = True
        self.TESTING = False
        
        # Override security settings for development
        if self.security.secret_key == 'dev-secret-key-change-in-production':
            logging.warning("Using default development secret key. Set SECRET_KEY environment variable.")


class ProductionConfig(Config):
    """Production configuration."""
    
    def __init__(self):
        super().__init__()
        self.DEBUG = False
        self.TESTING = False
        
        # Validate production requirements
        if self.security.secret_key == 'dev-secret-key-change-in-production':
            raise ValueError("Production environment must set a custom SECRET_KEY")
        
        # Tighten security settings for production
        self.security.csrf_enabled = True
        
        # Reduce cache TTL for production
        self.cache.default_ttl = min(self.cache.default_ttl, 300)


class TestingConfig(Config):
    """Testing configuration."""
    
    def __init__(self):
        # Skip environment validation for testing
        self._setup_test_settings()
        self._setup_api_settings()
        self._setup_security_settings()
        self._setup_database_settings()
        self._setup_cache_settings()
        self._setup_logging()
        
        self.DEBUG = True
        self.TESTING = True
        
        # Override for testing
        self.security.csrf_enabled = False
        self.cache.default_ttl = 1  # Very short cache for testing
        
    def _setup_test_settings(self):
        """Setup test environment variables."""
        os.environ.setdefault('BUNGIE_API_KEY', 'test-api-key')
        os.environ.setdefault('BUNGIE_CLIENT_ID', 'test-client-id')
        os.environ.setdefault('BUNGIE_CLIENT_SECRET', 'test-client-secret')
    
    def _validate_required_env_vars(self):
        """Skip validation for testing."""
        pass


def get_config(env: str = None) -> Config:
    """Get configuration instance based on environment."""
    if env is None:
        env = os.environ.get('FLASK_ENV', 'development')
    
    config_map = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'testing': TestingConfig
    }
    
    config_class = config_map.get(env, DevelopmentConfig)
    return config_class()


# Global configuration instance
config = get_config()

# Legacy compatibility
Config = config