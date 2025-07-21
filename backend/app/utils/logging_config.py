"""
Comprehensive logging configuration with structured logging, multiple handlers,
and production-ready features like log rotation, filtering, and centralized collection.
"""

import os
import sys
import json
import logging
import logging.handlers
from datetime import datetime
from typing import Dict, Any, Optional

from ..config import config


class StructuredFormatter(logging.Formatter):
    """Custom JSON formatter with additional context fields."""
    
    def format(self, record):
        # Create log record dictionary
        log_record = {
            'timestamp': datetime.utcnow().isoformat() + 'Z',
            'level': record.levelname,
            'logger': record.name,
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno,
            'message': record.getMessage(),
            'process_id': record.process,
            'thread_id': record.thread,
            'thread_name': record.threadName,
            'application': 'destiny-api-tools',
            'environment': config.environment,
            'version': getattr(config, 'version', '1.0.0')
        }
        
        # Add exception info if present
        if record.exc_info:
            log_record['exception'] = self.formatException(record.exc_info)
        
        # Add request context if available
        try:
            from flask import g, request
            if request:
                log_record['request_id'] = getattr(g, 'request_id', None)
                log_record['user_id'] = getattr(g, 'user_id', None)
                log_record['endpoint'] = request.endpoint
                log_record['method'] = request.method
                log_record['path'] = request.path
                log_record['remote_addr'] = request.remote_addr
        except (ImportError, RuntimeError):
            # Flask context not available
            pass
        
        # Add any extra fields from the record
        if hasattr(record, 'structured_data'):
            log_record.update(record.structured_data)
        
        return json.dumps(log_record)


class ColoredConsoleFormatter(logging.Formatter):
    """Colored console formatter for development."""
    
    COLORS = {
        'DEBUG': '\033[36m',     # Cyan
        'INFO': '\033[32m',      # Green
        'WARNING': '\033[33m',   # Yellow
        'ERROR': '\033[31m',     # Red
        'CRITICAL': '\033[35m',  # Magenta
        'RESET': '\033[0m'       # Reset
    }
    
    def format(self, record):
        # Add color to level name
        level_color = self.COLORS.get(record.levelname, self.COLORS['RESET'])
        record.colored_levelname = f"{level_color}{record.levelname}{self.COLORS['RESET']}"
        
        # Format the message
        formatted = super().format(record)
        
        return formatted


class RequestContextFilter(logging.Filter):
    """Filter to add request context to log records."""
    
    def filter(self, record):
        try:
            from flask import g, request
            if request:
                record.request_id = getattr(g, 'request_id', None)
                record.user_id = getattr(g, 'user_id', None)
                record.endpoint = request.endpoint
                record.method = request.method
                record.path = request.path
            else:
                record.request_id = None
                record.user_id = None
                record.endpoint = None
                record.method = None
                record.path = None
        except (ImportError, RuntimeError):
            # Flask context not available
            record.request_id = None
            record.user_id = None
            record.endpoint = None
            record.method = None
            record.path = None
        
        return True


class PerformanceFilter(logging.Filter):
    """Filter to add performance metrics to log records."""
    
    def filter(self, record):
        # Add memory usage if available
        try:
            import psutil
            process = psutil.Process()
            record.memory_usage_mb = process.memory_info().rss / 1024 / 1024
            record.cpu_percent = process.cpu_percent()
        except ImportError:
            record.memory_usage_mb = None
            record.cpu_percent = None
        
        return True


class SensitiveDataFilter(logging.Filter):
    """Filter to remove sensitive data from log messages."""
    
    SENSITIVE_PATTERNS = [
        'password', 'token', 'key', 'secret', 'auth', 'credential',
        'private', 'confidential', 'sensitive'
    ]
    
    def filter(self, record):
        # Check message for sensitive data
        if hasattr(record, 'msg') and isinstance(record.msg, str):
            msg = record.msg.lower()
            for pattern in self.SENSITIVE_PATTERNS:
                if pattern in msg:
                    record.msg = '[SENSITIVE DATA REDACTED]'
                    break
        
        # Check args for sensitive data
        if hasattr(record, 'args') and record.args:
            filtered_args = []
            for arg in record.args:
                if isinstance(arg, str) and any(pattern in arg.lower() for pattern in self.SENSITIVE_PATTERNS):
                    filtered_args.append('[REDACTED]')
                else:
                    filtered_args.append(arg)
            record.args = tuple(filtered_args)
        
        return True


class LoggingConfig:
    """Centralized logging configuration."""
    
    def __init__(self):
        self.log_dir = config.logs.directory
        self.log_level = getattr(logging, config.logs.level.upper())
        self.max_file_size = config.logs.max_file_size
        self.backup_count = config.logs.backup_count
        self.enable_json_logging = config.logs.enable_json
        self.enable_console_logging = config.logs.enable_console
        self.enable_file_logging = config.logs.enable_file
        
        # Ensure log directory exists
        os.makedirs(self.log_dir, exist_ok=True)
    
    def setup_logging(self):
        """Setup comprehensive logging configuration."""
        # Get root logger
        root_logger = logging.getLogger()
        root_logger.setLevel(self.log_level)
        
        # Clear existing handlers
        root_logger.handlers.clear()
        
        # Add console handler for development
        if self.enable_console_logging:
            self._add_console_handler(root_logger)
        
        # Add file handlers for production
        if self.enable_file_logging:
            self._add_file_handlers(root_logger)
        
        # Setup application-specific loggers
        self._setup_application_loggers()
        
        # Add filters
        self._add_filters(root_logger)
        
        logging.info("Logging system initialized")
    
    def _add_console_handler(self, logger):
        """Add colored console handler."""
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(self.log_level)
        
        if config.environment == 'development':
            # Colored format for development
            console_format = (
                "%(asctime)s | %(colored_levelname)s | %(name)s:%(lineno)d | "
                "%(message)s"
            )
            console_formatter = ColoredConsoleFormatter(console_format)
        else:
            # Simple format for production console
            console_format = (
                "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
            )
            console_formatter = logging.Formatter(console_format)
        
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)
    
    def _add_file_handlers(self, logger):
        """Add rotating file handlers."""
        # Main application log
        app_log_path = os.path.join(self.log_dir, 'app.log')
        app_handler = logging.handlers.RotatingFileHandler(
            app_log_path,
            maxBytes=self.max_file_size,
            backupCount=self.backup_count,
            encoding='utf-8'
        )
        app_handler.setLevel(logging.INFO)
        
        # Error log (errors and critical only)
        error_log_path = os.path.join(self.log_dir, 'error.log')
        error_handler = logging.handlers.RotatingFileHandler(
            error_log_path,
            maxBytes=self.max_file_size,
            backupCount=self.backup_count,
            encoding='utf-8'
        )
        error_handler.setLevel(logging.ERROR)
        
        # Access log for HTTP requests
        access_log_path = os.path.join(self.log_dir, 'access.log')
        access_handler = logging.handlers.RotatingFileHandler(
            access_log_path,
            maxBytes=self.max_file_size,
            backupCount=self.backup_count,
            encoding='utf-8'
        )
        access_handler.setLevel(logging.INFO)
        
        # Performance log
        perf_log_path = os.path.join(self.log_dir, 'performance.log')
        perf_handler = logging.handlers.RotatingFileHandler(
            perf_log_path,
            maxBytes=self.max_file_size,
            backupCount=self.backup_count,
            encoding='utf-8'
        )
        perf_handler.setLevel(logging.DEBUG)
        
        # Use JSON formatting if enabled
        if self.enable_json_logging:
            json_formatter = StructuredFormatter()
            
            app_handler.setFormatter(json_formatter)
            error_handler.setFormatter(json_formatter)
            access_handler.setFormatter(json_formatter)
            perf_handler.setFormatter(json_formatter)
        else:
            # Standard text formatting
            text_format = (
                "%(asctime)s | %(levelname)s | %(name)s:%(lineno)d | "
                "%(funcName)s() | %(message)s"
            )
            text_formatter = logging.Formatter(text_format)
            
            app_handler.setFormatter(text_formatter)
            error_handler.setFormatter(text_formatter)
            access_handler.setFormatter(text_formatter)
            perf_handler.setFormatter(text_formatter)
        
        # Add handlers to logger
        logger.addHandler(app_handler)
        logger.addHandler(error_handler)
        
        # Add specialized handlers to specific loggers
        access_logger = logging.getLogger('access')
        access_logger.addHandler(access_handler)
        access_logger.propagate = False
        
        perf_logger = logging.getLogger('performance')
        perf_logger.addHandler(perf_handler)
        perf_logger.propagate = False
    
    def _setup_application_loggers(self):
        """Setup application-specific loggers."""
        # API logger
        api_logger = logging.getLogger('api')
        api_logger.setLevel(logging.INFO)
        
        # Security logger
        security_logger = logging.getLogger('security')
        security_logger.setLevel(logging.INFO)
        
        # Database logger
        db_logger = logging.getLogger('database')
        db_logger.setLevel(logging.INFO)
        
        # Background jobs logger
        jobs_logger = logging.getLogger('jobs')
        jobs_logger.setLevel(logging.INFO)
        
        # External API logger (Bungie API)
        external_logger = logging.getLogger('external_api')
        external_logger.setLevel(logging.INFO)
        
        # Performance logger
        perf_logger = logging.getLogger('performance')
        perf_logger.setLevel(logging.DEBUG)
        
        # WebSocket logger
        ws_logger = logging.getLogger('websocket')
        ws_logger.setLevel(logging.INFO)
        
        # Cache logger
        cache_logger = logging.getLogger('cache')
        cache_logger.setLevel(logging.INFO)
    
    def _add_filters(self, logger):
        """Add logging filters."""
        # Add request context filter
        request_filter = RequestContextFilter()
        
        # Add performance filter
        performance_filter = PerformanceFilter()
        
        # Add sensitive data filter
        sensitive_filter = SensitiveDataFilter()
        
        # Apply filters to all handlers
        for handler in logger.handlers:
            handler.addFilter(request_filter)
            handler.addFilter(performance_filter)
            handler.addFilter(sensitive_filter)
    
    def get_logger(self, name: str) -> logging.Logger:
        """Get a configured logger by name."""
        return logging.getLogger(name)


class StructuredLogger:
    """Helper class for structured logging with consistent formatting."""
    
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
    
    def debug(self, message: str, **kwargs):
        """Log debug message with structured data."""
        self._log(logging.DEBUG, message, **kwargs)
    
    def info(self, message: str, **kwargs):
        """Log info message with structured data."""
        self._log(logging.INFO, message, **kwargs)
    
    def warning(self, message: str, **kwargs):
        """Log warning message with structured data."""
        self._log(logging.WARNING, message, **kwargs)
    
    def error(self, message: str, **kwargs):
        """Log error message with structured data."""
        self._log(logging.ERROR, message, **kwargs)
    
    def critical(self, message: str, **kwargs):
        """Log critical message with structured data."""
        self._log(logging.CRITICAL, message, **kwargs)
    
    def _log(self, level: int, message: str, **kwargs):
        """Internal logging method with structured data."""
        if kwargs:
            # Add structured data as extra fields
            extra = {'structured_data': kwargs}
            self.logger.log(level, message, extra=extra)
        else:
            self.logger.log(level, message)
    
    def log_request(self, method: str, path: str, status_code: int, 
                   duration: float, user_id: str = None, **kwargs):
        """Log HTTP request with structured data."""
        self._log(logging.INFO, f"{method} {path} {status_code}", 
                 method=method, path=path, status_code=status_code,
                 duration_ms=duration, user_id=user_id, **kwargs)
    
    def log_api_call(self, service: str, endpoint: str, duration: float,
                    success: bool, **kwargs):
        """Log external API call with structured data."""
        self._log(logging.INFO, f"API call to {service} {endpoint}",
                 service=service, endpoint=endpoint, duration_ms=duration,
                 success=success, **kwargs)
    
    def log_performance(self, operation: str, duration: float, **kwargs):
        """Log performance metrics with structured data."""
        perf_logger = logging.getLogger('performance')
        if kwargs:
            extra = {'structured_data': kwargs}
            perf_logger.info(f"Performance: {operation} took {duration:.2f}ms", 
                           extra=extra)
        else:
            perf_logger.info(f"Performance: {operation} took {duration:.2f}ms")
    
    def log_security_event(self, event_type: str, user_id: str = None, 
                          ip_address: str = None, **kwargs):
        """Log security event with structured data."""
        security_logger = logging.getLogger('security')
        extra = {
            'structured_data': {
                'event_type': event_type,
                'user_id': user_id,
                'ip_address': ip_address,
                **kwargs
            }
        }
        security_logger.warning(f"Security event: {event_type}", extra=extra)


# Global logging configuration
logging_config = LoggingConfig()


def setup_logging():
    """Setup the logging system."""
    logging_config.setup_logging()


def get_logger(name: str) -> logging.Logger:
    """Get a configured logger."""
    return logging_config.get_logger(name)


def get_structured_logger(name: str) -> StructuredLogger:
    """Get a structured logger."""
    return StructuredLogger(name)


# Application-specific logger instances
api_logger = get_structured_logger('api')
security_logger = get_structured_logger('security')
db_logger = get_structured_logger('database')
jobs_logger = get_structured_logger('jobs')
external_api_logger = get_structured_logger('external_api')
performance_logger = get_structured_logger('performance')
websocket_logger = get_structured_logger('websocket')
cache_logger = get_structured_logger('cache')


def log_request(method: str, path: str, status_code: int, duration: float, **kwargs):
    """Log HTTP request."""
    access_logger = logging.getLogger('access')
    access_logger.info(f"{method} {path} {status_code} {duration:.2f}ms")


def log_api_call(service: str, endpoint: str, duration: float, success: bool, **kwargs):
    """Log external API call."""
    external_api_logger.log_api_call(service, endpoint, duration, success, **kwargs)


def log_performance(operation: str, duration: float, **kwargs):
    """Log performance metric."""
    performance_logger.log_performance(operation, duration, **kwargs)


def log_security_event(event_type: str, **kwargs):
    """Log security event."""
    security_logger.log_security_event(event_type, **kwargs)