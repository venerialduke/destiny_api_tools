"""
Application startup service for initializing background services.
"""

import logging
import os
from .manifest_updater import get_manifest_updater
from .manifest_service import ManifestService


class StartupService:
    """Service for handling application startup tasks."""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def initialize_application(self, auto_start_updater: bool = True):
        """
        Initialize the application and start background services.
        
        Args:
            auto_start_updater: Whether to automatically start the manifest updater
        """
        self.logger.info("Initializing Destiny API Tools application...")
        
        # Initialize manifest database if it doesn't exist
        self._initialize_manifest_database()
        
        # Initialize and optionally start the updater
        if auto_start_updater:
            self._initialize_updater()
        
        self.logger.info("Application initialization complete")
    
    def _initialize_manifest_database(self):
        """Initialize the manifest database if it doesn't exist."""
        manifest_service = ManifestService()
        db_stats = manifest_service.get_database_stats()
        
        if db_stats.get('status') == 'no_database':
            self.logger.info("No manifest database found, checking for initial download...")
            
            try:
                # Check if an update is needed (this will also create the DB if needed)
                needs_update = manifest_service.needs_update()
                if needs_update:
                    self.logger.info("Performing initial manifest download...")
                    success = manifest_service.update_manifest()
                    if success:
                        self.logger.info("Initial manifest download completed successfully")
                    else:
                        self.logger.warning("Initial manifest download failed")
                else:
                    self.logger.info("Manifest database initialized")
            except Exception as e:
                self.logger.error(f"Failed to initialize manifest database: {e}")
        else:
            self.logger.info(f"Manifest database found (status: {db_stats.get('status')})")
    
    def _initialize_updater(self):
        """Initialize and start the manifest updater."""
        try:
            updater = get_manifest_updater()
            
            # Add logging callback
            def log_callback(event_type: str, data: dict):
                if event_type == 'updater_started':
                    self.logger.info("Manifest updater started")
                elif event_type == 'check_complete':
                    if data.get('needs_update'):
                        self.logger.info("Manifest update available")
                    else:
                        self.logger.debug("Manifest check complete - no update needed")
                elif event_type == 'update_complete':
                    self.logger.info(f"Manifest update completed in {data.get('duration', 0):.1f}s")
                elif event_type == 'update_error':
                    self.logger.error(f"Manifest update error: {data.get('error')}")
                elif event_type == 'download_progress':
                    percentage = data.get('percentage', 0)
                    if percentage % 10 == 0:  # Log every 10%
                        self.logger.info(f"Download progress: {percentage:.1f}%")
            
            updater.add_update_callback(log_callback)
            
            # Start the background updater
            if not updater.running:
                updater.start_background_updates()
                self.logger.info("Background manifest updater started")
            else:
                self.logger.info("Background manifest updater already running")
                
        except Exception as e:
            self.logger.error(f"Failed to initialize manifest updater: {e}")
    
    def shutdown_application(self):
        """Gracefully shutdown background services."""
        self.logger.info("Shutting down application services...")
        
        try:
            updater = get_manifest_updater()
            if updater.running:
                updater.stop_background_updates()
                self.logger.info("Manifest updater stopped")
        except Exception as e:
            self.logger.error(f"Error stopping manifest updater: {e}")
        
        self.logger.info("Application shutdown complete")


# Global startup service instance
_startup_service = None

def get_startup_service() -> StartupService:
    """Get the global startup service instance."""
    global _startup_service
    if _startup_service is None:
        _startup_service = StartupService()
    return _startup_service