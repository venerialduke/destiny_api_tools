"""
Background manifest update management service.
"""

import os
import time
import threading
import logging
from datetime import datetime, timedelta
from typing import Dict, Any, Optional, Callable
from .manifest_service import ManifestService
from .database_service import DatabaseService


class ManifestUpdater:
    """Service for managing automatic manifest updates."""
    
    def __init__(self, check_interval_hours: int = 6):
        """
        Initialize the manifest updater.
        
        Args:
            check_interval_hours: How often to check for updates (default: 6 hours)
        """
        self.manifest_service = ManifestService()
        self.check_interval = check_interval_hours * 3600  # Convert to seconds
        self.update_thread = None
        self.running = False
        self.last_check = None
        self.last_update = None
        self.update_status = 'idle'  # idle, checking, downloading, processing, complete, error
        self.error_message = None
        self.update_callbacks = []
        
        # Setup logging
        self.logger = logging.getLogger(__name__)
        
        # Update statistics
        self.stats = {
            'total_checks': 0,
            'total_updates': 0,
            'last_check_duration': 0,
            'last_update_duration': 0,
            'consecutive_errors': 0,
            'uptime_start': datetime.utcnow()
        }
    
    def add_update_callback(self, callback: Callable[[str, Dict[str, Any]], None]):
        """
        Add a callback function to be called during update events.
        
        Args:
            callback: Function that receives (event_type, data) parameters
        """
        self.update_callbacks.append(callback)
    
    def _notify_callbacks(self, event_type: str, data: Dict[str, Any]):
        """Notify all registered callbacks of an update event."""
        for callback in self.update_callbacks:
            try:
                callback(event_type, data)
            except Exception as e:
                self.logger.error(f"Error in update callback: {e}")
    
    def start_background_updates(self):
        """Start the background update thread."""
        if self.running:
            self.logger.warning("Background updates already running")
            return
        
        self.running = True
        self.update_thread = threading.Thread(target=self._background_update_loop, daemon=True)
        self.update_thread.start()
        self.logger.info(f"Started background manifest updates (checking every {self.check_interval/3600:.1f} hours)")
        
        self._notify_callbacks('updater_started', {
            'check_interval_hours': self.check_interval / 3600,
            'timestamp': datetime.utcnow().isoformat()
        })
    
    def stop_background_updates(self):
        """Stop the background update thread."""
        if not self.running:
            return
        
        self.running = False
        if self.update_thread and self.update_thread.is_alive():
            self.update_thread.join(timeout=5)
        
        self.logger.info("Stopped background manifest updates")
        self._notify_callbacks('updater_stopped', {
            'timestamp': datetime.utcnow().isoformat()
        })
    
    def _background_update_loop(self):
        """Main background update loop."""
        while self.running:
            try:
                self._check_and_update()
            except Exception as e:
                self.logger.error(f"Error in background update loop: {e}")
                self.stats['consecutive_errors'] += 1
                self.error_message = str(e)
                self.update_status = 'error'
                
                self._notify_callbacks('update_error', {
                    'error': str(e),
                    'consecutive_errors': self.stats['consecutive_errors'],
                    'timestamp': datetime.utcnow().isoformat()
                })
                
                # Exponential backoff for errors (max 1 hour)
                error_delay = min(300 * (2 ** min(self.stats['consecutive_errors'], 4)), 3600)
                time.sleep(error_delay)
                continue
            
            # Reset error count on successful check
            if self.stats['consecutive_errors'] > 0:
                self.stats['consecutive_errors'] = 0
                self.error_message = None
            
            # Wait for next check
            time.sleep(self.check_interval)
    
    def _check_and_update(self):
        """Check for updates and perform update if needed."""
        check_start = time.time()
        self.update_status = 'checking'
        self.last_check = datetime.utcnow()
        
        self.logger.info("Checking for manifest updates...")
        self._notify_callbacks('check_started', {
            'timestamp': self.last_check.isoformat()
        })
        
        try:
            # Check if update is needed
            needs_update = self.manifest_service.needs_update()
            check_duration = time.time() - check_start
            self.stats['last_check_duration'] = check_duration
            self.stats['total_checks'] += 1
            
            if needs_update:
                self.logger.info("Manifest update available, starting download...")
                self._perform_update()
            else:
                self.logger.info("Manifest is up to date")
                self.update_status = 'idle'
                
                self._notify_callbacks('check_complete', {
                    'needs_update': False,
                    'check_duration': check_duration,
                    'timestamp': datetime.utcnow().isoformat()
                })
        
        except Exception as e:
            self.update_status = 'error'
            self.error_message = str(e)
            raise
    
    def _perform_update(self):
        """Perform the actual manifest update."""
        update_start = time.time()
        self.update_status = 'downloading'
        
        self._notify_callbacks('update_started', {
            'timestamp': datetime.utcnow().isoformat()
        })
        
        try:
            # Create progress callback
            def progress_callback(percentage, downloaded, total):
                self._notify_callbacks('download_progress', {
                    'percentage': percentage,
                    'downloaded_mb': downloaded / (1024 * 1024),
                    'total_mb': total / (1024 * 1024),
                    'timestamp': datetime.utcnow().isoformat()
                })
            
            self.update_status = 'processing'
            success = self.manifest_service.update_manifest(progress_callback)
            
            update_duration = time.time() - update_start
            self.stats['last_update_duration'] = update_duration
            
            if success:
                self.stats['total_updates'] += 1
                self.last_update = datetime.utcnow()
                self.update_status = 'complete'
                
                # Get updated stats
                db_stats = self.manifest_service.get_database_stats()
                
                self.logger.info(f"Manifest update completed successfully in {update_duration:.1f}s")
                self._notify_callbacks('update_complete', {
                    'success': True,
                    'duration': update_duration,
                    'database_stats': db_stats,
                    'timestamp': self.last_update.isoformat()
                })
                
                # Reset to idle after successful update
                self.update_status = 'idle'
            else:
                raise Exception("Manifest update failed")
                
        except Exception as e:
            self.update_status = 'error'
            self.error_message = str(e)
            self.logger.error(f"Manifest update failed: {e}")
            
            self._notify_callbacks('update_failed', {
                'error': str(e),
                'duration': time.time() - update_start,
                'timestamp': datetime.utcnow().isoformat()
            })
            raise
    
    def force_update(self) -> Dict[str, Any]:
        """Force an immediate manifest update."""
        if self.update_status in ['downloading', 'processing']:
            return {
                'success': False,
                'error': 'Update already in progress',
                'status': self.update_status
            }
        
        try:
            self.logger.info("Force update requested")
            self._perform_update()
            return {
                'success': True,
                'message': 'Update completed successfully',
                'status': self.update_status,
                'timestamp': datetime.utcnow().isoformat()
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'status': self.update_status,
                'timestamp': datetime.utcnow().isoformat()
            }
    
    def get_status(self) -> Dict[str, Any]:
        """Get current updater status and statistics."""
        now = datetime.utcnow()
        uptime = now - self.stats['uptime_start']
        
        # Calculate next check time
        next_check = None
        if self.running and self.last_check:
            next_check = self.last_check + timedelta(seconds=self.check_interval)
        
        return {
            'running': self.running,
            'status': self.update_status,
            'error_message': self.error_message,
            'last_check': self.last_check.isoformat() if self.last_check else None,
            'last_update': self.last_update.isoformat() if self.last_update else None,
            'next_check': next_check.isoformat() if next_check else None,
            'check_interval_hours': self.check_interval / 3600,
            'uptime_hours': uptime.total_seconds() / 3600,
            'statistics': {
                'total_checks': self.stats['total_checks'],
                'total_updates': self.stats['total_updates'],
                'consecutive_errors': self.stats['consecutive_errors'],
                'last_check_duration_seconds': self.stats['last_check_duration'],
                'last_update_duration_seconds': self.stats['last_update_duration'],
                'average_checks_per_day': self.stats['total_checks'] / max(uptime.days, 1) if uptime.days > 0 else self.stats['total_checks'],
                'success_rate': (self.stats['total_checks'] - self.stats['consecutive_errors']) / max(self.stats['total_checks'], 1) * 100
            },
            'health': {
                'status': 'healthy' if self.stats['consecutive_errors'] == 0 else 'degraded' if self.stats['consecutive_errors'] < 3 else 'unhealthy',
                'consecutive_errors': self.stats['consecutive_errors'],
                'last_error': self.error_message
            }
        }
    
    def set_check_interval(self, hours: float):
        """Update the check interval."""
        old_interval = self.check_interval
        self.check_interval = int(hours * 3600)
        
        self.logger.info(f"Check interval updated from {old_interval/3600:.1f}h to {hours:.1f}h")
        self._notify_callbacks('interval_changed', {
            'old_hours': old_interval / 3600,
            'new_hours': hours,
            'timestamp': datetime.utcnow().isoformat()
        })
    
    def get_manifest_info(self) -> Dict[str, Any]:
        """Get current manifest information and version."""
        try:
            manifest_info = self.manifest_service.get_manifest_info()
            db_stats = self.manifest_service.get_database_stats()
            
            return {
                'success': True,
                'remote_info': {
                    'version': manifest_info.get('version', 'unknown'),
                    'json_world_content_paths': manifest_info.get('jsonWorldContentPaths', {}),
                    'mobile_world_content_paths': manifest_info.get('mobileWorldContentPaths', {})
                },
                'local_info': db_stats,
                'needs_update': self.manifest_service.needs_update(),
                'timestamp': datetime.utcnow().isoformat()
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'timestamp': datetime.utcnow().isoformat()
            }


# Global updater instance
_manifest_updater = None

def get_manifest_updater(check_interval_hours: int = 6) -> ManifestUpdater:
    """Get the global manifest updater instance."""
    global _manifest_updater
    if _manifest_updater is None:
        _manifest_updater = ManifestUpdater(check_interval_hours)
    return _manifest_updater