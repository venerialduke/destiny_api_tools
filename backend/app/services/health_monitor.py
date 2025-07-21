"""
Health monitoring service for the application.
"""

import os
import time
import psutil
from datetime import datetime, timedelta
from typing import Dict, Any, List
from .manifest_updater import get_manifest_updater
from .manifest_service import ManifestService
from .database_service import DatabaseService


class HealthMonitor:
    """Service for monitoring application health."""
    
    def __init__(self):
        self.start_time = datetime.utcnow()
    
    def get_system_health(self) -> Dict[str, Any]:
        """Get overall system health status."""
        health_checks = [
            self._check_database_health(),
            self._check_updater_health(),
            self._check_system_resources(),
            self._check_disk_space(),
            self._check_api_health()
        ]
        
        # Determine overall health
        all_healthy = all(check['healthy'] for check in health_checks)
        any_critical = any(check.get('critical', False) for check in health_checks)
        
        overall_status = 'healthy' if all_healthy else 'critical' if any_critical else 'degraded'
        
        return {
            'status': overall_status,
            'healthy': all_healthy,
            'timestamp': datetime.utcnow().isoformat(),
            'uptime_hours': (datetime.utcnow() - self.start_time).total_seconds() / 3600,
            'checks': {
                'database': health_checks[0],
                'updater': health_checks[1],
                'system_resources': health_checks[2],
                'disk_space': health_checks[3],
                'api': health_checks[4]
            },
            'summary': {
                'total_checks': len(health_checks),
                'healthy_checks': sum(1 for check in health_checks if check['healthy']),
                'critical_issues': sum(1 for check in health_checks if check.get('critical', False))
            }
        }
    
    def _check_database_health(self) -> Dict[str, Any]:
        """Check manifest database health."""
        try:
            manifest_service = ManifestService()
            db_stats = manifest_service.get_database_stats()
            
            if db_stats.get('status') == 'no_database':
                return {
                    'healthy': False,
                    'critical': True,
                    'status': 'no_database',
                    'message': 'Manifest database not found',
                    'details': db_stats
                }
            elif db_stats.get('status') == 'error':
                return {
                    'healthy': False,
                    'critical': True,
                    'status': 'error',
                    'message': f"Database error: {db_stats.get('error')}",
                    'details': db_stats
                }
            elif db_stats.get('status') == 'ready':
                # Check if database is too old
                last_updated = db_stats.get('last_updated')
                if last_updated:
                    try:
                        last_update_time = datetime.fromisoformat(last_updated.replace('Z', '+00:00'))
                        age_hours = (datetime.utcnow() - last_update_time.replace(tzinfo=None)).total_seconds() / 3600
                        
                        if age_hours > 168:  # 1 week
                            return {
                                'healthy': False,
                                'critical': False,
                                'status': 'outdated',
                                'message': f'Database is {age_hours:.1f} hours old',
                                'details': {**db_stats, 'age_hours': age_hours}
                            }
                    except ValueError:
                        pass  # Continue with healthy status if date parsing fails
                
                return {
                    'healthy': True,
                    'status': 'ready',
                    'message': f"Database ready with {db_stats.get('total_definitions', 0):,} definitions",
                    'details': db_stats
                }
            else:
                return {
                    'healthy': False,
                    'critical': False,
                    'status': 'unknown',
                    'message': f"Unknown database status: {db_stats.get('status')}",
                    'details': db_stats
                }
        except Exception as e:
            return {
                'healthy': False,
                'critical': True,
                'status': 'error',
                'message': f'Database health check failed: {str(e)}',
                'details': {'error': str(e)}
            }
    
    def _check_updater_health(self) -> Dict[str, Any]:
        """Check manifest updater health."""
        try:
            updater = get_manifest_updater()
            status = updater.get_status()
            
            health_status = status['health']['status']
            consecutive_errors = status['health']['consecutive_errors']
            
            if health_status == 'unhealthy':
                return {
                    'healthy': False,
                    'critical': True,
                    'status': 'unhealthy',
                    'message': f'Updater unhealthy with {consecutive_errors} consecutive errors',
                    'details': {
                        'running': status['running'],
                        'consecutive_errors': consecutive_errors,
                        'last_error': status['error_message'],
                        'success_rate': status['statistics']['success_rate']
                    }
                }
            elif health_status == 'degraded':
                return {
                    'healthy': False,
                    'critical': False,
                    'status': 'degraded',
                    'message': f'Updater degraded with {consecutive_errors} recent errors',
                    'details': {
                        'running': status['running'],
                        'consecutive_errors': consecutive_errors,
                        'success_rate': status['statistics']['success_rate']
                    }
                }
            else:
                return {
                    'healthy': True,
                    'status': 'healthy',
                    'message': f"Updater healthy (running: {status['running']})",
                    'details': {
                        'running': status['running'],
                        'total_checks': status['statistics']['total_checks'],
                        'total_updates': status['statistics']['total_updates'],
                        'success_rate': status['statistics']['success_rate']
                    }
                }
        except Exception as e:
            return {
                'healthy': False,
                'critical': True,
                'status': 'error',
                'message': f'Updater health check failed: {str(e)}',
                'details': {'error': str(e)}
            }
    
    def _check_system_resources(self) -> Dict[str, Any]:
        """Check system resource usage."""
        try:
            # Get CPU and memory usage
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            
            # Check thresholds
            cpu_critical = cpu_percent > 90
            memory_critical = memory.percent > 90
            
            cpu_warning = cpu_percent > 70
            memory_warning = memory.percent > 70
            
            is_critical = cpu_critical or memory_critical
            is_warning = cpu_warning or memory_warning
            
            issues = []
            if cpu_critical:
                issues.append(f'CPU usage critical: {cpu_percent:.1f}%')
            elif cpu_warning:
                issues.append(f'CPU usage high: {cpu_percent:.1f}%')
            
            if memory_critical:
                issues.append(f'Memory usage critical: {memory.percent:.1f}%')
            elif memory_warning:
                issues.append(f'Memory usage high: {memory.percent:.1f}%')
            
            if is_critical:
                status = 'critical'
                message = '; '.join(issues)
            elif is_warning:
                status = 'warning'
                message = '; '.join(issues)
            else:
                status = 'good'
                message = f'Resources normal (CPU: {cpu_percent:.1f}%, Memory: {memory.percent:.1f}%)'
            
            return {
                'healthy': not is_critical,
                'critical': is_critical,
                'status': status,
                'message': message,
                'details': {
                    'cpu_percent': cpu_percent,
                    'memory_percent': memory.percent,
                    'memory_available_gb': memory.available / (1024**3),
                    'memory_total_gb': memory.total / (1024**3)
                }
            }
        except Exception as e:
            return {
                'healthy': False,
                'critical': False,
                'status': 'error',
                'message': f'Resource check failed: {str(e)}',
                'details': {'error': str(e)}
            }
    
    def _check_disk_space(self) -> Dict[str, Any]:
        """Check disk space for data directory."""
        try:
            data_dir = os.path.join(os.getcwd(), 'data')
            if not os.path.exists(data_dir):
                data_dir = os.getcwd()
            
            disk_usage = psutil.disk_usage(data_dir)
            free_percent = (disk_usage.free / disk_usage.total) * 100
            used_percent = 100 - free_percent
            
            # Check thresholds
            critical = free_percent < 5  # Less than 5% free
            warning = free_percent < 15  # Less than 15% free
            
            if critical:
                status = 'critical'
                message = f'Disk space critical: {free_percent:.1f}% free'
            elif warning:
                status = 'warning'
                message = f'Disk space low: {free_percent:.1f}% free'
            else:
                status = 'good'
                message = f'Disk space sufficient: {free_percent:.1f}% free'
            
            return {
                'healthy': not critical,
                'critical': critical,
                'status': status,
                'message': message,
                'details': {
                    'path': data_dir,
                    'total_gb': disk_usage.total / (1024**3),
                    'used_gb': disk_usage.used / (1024**3),
                    'free_gb': disk_usage.free / (1024**3),
                    'used_percent': used_percent,
                    'free_percent': free_percent
                }
            }
        except Exception as e:
            return {
                'healthy': False,
                'critical': False,
                'status': 'error',
                'message': f'Disk space check failed: {str(e)}',
                'details': {'error': str(e)}
            }
    
    def _check_api_health(self) -> Dict[str, Any]:
        """Check API health by testing manifest endpoints."""
        try:
            # Test basic database operations
            db_path = os.path.join('data', 'manifest.db')
            if not os.path.exists(db_path):
                return {
                    'healthy': False,
                    'critical': True,
                    'status': 'no_database',
                    'message': 'Database file not found',
                    'details': {'db_path': db_path}
                }
            
            db_service = DatabaseService(db_path)
            
            # Test a simple query
            results = db_service.search_items(limit=1)
            
            if results['total'] > 0:
                return {
                    'healthy': True,
                    'status': 'operational',
                    'message': f'API operational with {results["total"]:,} items available',
                    'details': {
                        'total_items': results['total'],
                        'database_responsive': True
                    }
                }
            else:
                return {
                    'healthy': False,
                    'critical': False,
                    'status': 'empty_database',
                    'message': 'Database is empty',
                    'details': {'total_items': 0}
                }
                
        except Exception as e:
            return {
                'healthy': False,
                'critical': True,
                'status': 'error',
                'message': f'API health check failed: {str(e)}',
                'details': {'error': str(e)}
            }
    
    def get_performance_metrics(self) -> Dict[str, Any]:
        """Get performance metrics for monitoring."""
        try:
            # System metrics
            cpu_percent = psutil.cpu_percent(interval=0.1)
            memory = psutil.virtual_memory()
            
            # Application metrics
            updater = get_manifest_updater()
            updater_status = updater.get_status()
            
            manifest_service = ManifestService()
            db_stats = manifest_service.get_database_stats()
            
            return {
                'timestamp': datetime.utcnow().isoformat(),
                'system': {
                    'cpu_percent': cpu_percent,
                    'memory_percent': memory.percent,
                    'memory_used_gb': (memory.total - memory.available) / (1024**3),
                    'uptime_hours': (datetime.utcnow() - self.start_time).total_seconds() / 3600
                },
                'updater': {
                    'running': updater_status['running'],
                    'total_checks': updater_status['statistics']['total_checks'],
                    'total_updates': updater_status['statistics']['total_updates'],
                    'success_rate': updater_status['statistics']['success_rate'],
                    'consecutive_errors': updater_status['statistics']['consecutive_errors']
                },
                'database': {
                    'status': db_stats.get('status', 'unknown'),
                    'total_definitions': db_stats.get('total_definitions', 0),
                    'file_size_mb': db_stats.get('file_size_mb', 0),
                    'version': db_stats.get('version', 'unknown')
                }
            }
        except Exception as e:
            return {
                'timestamp': datetime.utcnow().isoformat(),
                'error': str(e)
            }


# Global health monitor instance
_health_monitor = None

def get_health_monitor() -> HealthMonitor:
    """Get the global health monitor instance."""
    global _health_monitor
    if _health_monitor is None:
        _health_monitor = HealthMonitor()
    return _health_monitor