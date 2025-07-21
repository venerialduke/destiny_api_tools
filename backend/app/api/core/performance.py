"""
Performance monitoring API endpoints for system health and metrics.
"""

from flask import Blueprint, jsonify, request
from ...services.performance_monitor import (
    get_performance_monitor, get_performance_stats, get_health_status
)
from ...services.connection_pool import get_connection_stats, cleanup_connections
from ...services.cache_service import get_cache
from ...services.batch_service import get_optimized_client
from ...utils.response import APIResponse
from ...middleware.auth_middleware import require_auth

performance_bp = Blueprint('performance', __name__)


@performance_bp.route('/health', methods=['GET'])
def health_check():
    """Get application health status."""
    try:
        health = get_health_status()
        
        # Return appropriate status code based on health
        status_code = 200
        if health['status'] == 'warning':
            status_code = 200  # Still OK but with warnings
        elif health['status'] == 'critical':
            status_code = 503  # Service unavailable
        
        return APIResponse.success(
            data=health,
            message=f"Application is {health['status']}",
            status_code=status_code
        )
        
    except Exception as e:
        return APIResponse.error(
            message="Health check failed",
            details={'error': str(e)},
            status_code=500
        )


@performance_bp.route('/stats', methods=['GET'])
@require_auth(optional=True)  # Allow both authenticated and anonymous access
def get_stats():
    """Get comprehensive performance statistics."""
    try:
        # Check if detailed stats are requested (requires auth)
        detailed = request.args.get('detailed', 'false').lower() == 'true'
        
        if detailed and not hasattr(request, 'current_user'):
            return APIResponse.error(
                message="Authentication required for detailed statistics",
                status_code=401
            )
        
        stats = get_performance_stats()
        
        # Filter sensitive information for non-authenticated requests
        if not detailed:
            # Return only basic stats for anonymous users
            filtered_stats = {
                'timestamp': stats['timestamp'],
                'health': get_health_status(),
                'application': {
                    'total_requests': stats.get('application', {}).get('total_requests', 0),
                    'avg_response_time': stats.get('application', {}).get('avg_response_time', 0),
                    'error_rate': stats.get('application', {}).get('error_rate', 0)
                },
                'cache': {
                    'hit_rate_percent': stats.get('cache', {}).get('hit_rate_percent', 0)
                }
            }
            stats = filtered_stats
        
        return APIResponse.success(
            data=stats,
            message="Performance statistics retrieved successfully"
        )
        
    except Exception as e:
        return APIResponse.error(
            message="Failed to retrieve performance statistics",
            details={'error': str(e)},
            status_code=500
        )


@performance_bp.route('/metrics', methods=['GET'])
@require_auth()  # Requires authentication
def get_metrics():
    """Get detailed performance metrics."""
    try:
        monitor = get_performance_monitor()
        
        # Get query parameters
        duration = float(request.args.get('duration', 3600))  # Default 1 hour
        metric_name = request.args.get('metric')
        
        if metric_name:
            # Get specific metric
            stats = monitor.collector.get_metric_stats(metric_name, duration)
            history = monitor.collector.get_metric_history(metric_name, duration)
            
            result = {
                'metric': metric_name,
                'duration': duration,
                'stats': stats,
                'history_count': len(history),
                'history': [
                    {
                        'timestamp': snapshot.timestamp,
                        'value': snapshot.values[metric_name],
                        'tags': snapshot.tags
                    }
                    for snapshot in history[-100:]  # Last 100 points
                ] if len(history) <= 100 else []
            }
        else:
            # Get all metrics
            all_stats = monitor.collector.get_all_metrics(duration)
            result = {
                'duration': duration,
                'metrics': all_stats,
                'available_metrics': list(monitor.collector.metric_definitions.keys())
            }
        
        return APIResponse.success(
            data=result,
            message="Metrics retrieved successfully"
        )
        
    except Exception as e:
        return APIResponse.error(
            message="Failed to retrieve metrics",
            details={'error': str(e)},
            status_code=500
        )


@performance_bp.route('/connections', methods=['GET'])
@require_auth()
def get_connection_stats_endpoint():
    """Get connection pool statistics."""
    try:
        pool_name = request.args.get('pool')
        stats = get_connection_stats(pool_name)
        
        return APIResponse.success(
            data=stats,
            message="Connection statistics retrieved successfully"
        )
        
    except Exception as e:
        return APIResponse.error(
            message="Failed to retrieve connection statistics",
            details={'error': str(e)},
            status_code=500
        )


@performance_bp.route('/connections/cleanup', methods=['POST'])
@require_auth()
def cleanup_connections_endpoint():
    """Clean up idle connections."""
    try:
        cleaned_count = cleanup_connections()
        
        return APIResponse.success(
            data={'cleaned_pools': cleaned_count},
            message=f"Cleaned up {cleaned_count} idle connection pools"
        )
        
    except Exception as e:
        return APIResponse.error(
            message="Failed to cleanup connections",
            details={'error': str(e)},
            status_code=500
        )


@performance_bp.route('/cache', methods=['GET'])
@require_auth()
def get_cache_stats():
    """Get cache statistics."""
    try:
        cache = get_cache()
        stats = cache.get_stats()
        
        return APIResponse.success(
            data=stats,
            message="Cache statistics retrieved successfully"
        )
        
    except Exception as e:
        return APIResponse.error(
            message="Failed to retrieve cache statistics",
            details={'error': str(e)},
            status_code=500
        )


@performance_bp.route('/cache/clear', methods=['POST'])
@require_auth()
def clear_cache():
    """Clear cache data."""
    try:
        cache = get_cache()
        success = cache.clear()
        
        return APIResponse.success(
            data={'cleared': success},
            message="Cache cleared successfully" if success else "Failed to clear cache"
        )
        
    except Exception as e:
        return APIResponse.error(
            message="Failed to clear cache",
            details={'error': str(e)},
            status_code=500
        )


@performance_bp.route('/batch', methods=['GET'])
@require_auth()
def get_batch_stats():
    """Get request batching statistics."""
    try:
        client = get_optimized_client()
        stats = client.get_optimization_stats()
        
        return APIResponse.success(
            data=stats,
            message="Batch statistics retrieved successfully"
        )
        
    except Exception as e:
        return APIResponse.error(
            message="Failed to retrieve batch statistics",
            details={'error': str(e)},
            status_code=500
        )


@performance_bp.route('/alerts', methods=['GET'])
@require_auth()
def get_alerts():
    """Get active performance alerts."""
    try:
        monitor = get_performance_monitor()
        active_alerts = monitor.alert_manager.get_active_alerts()
        
        # Format alerts for response
        formatted_alerts = {}
        for name, alert_info in active_alerts.items():
            rule = alert_info['rule']
            formatted_alerts[name] = {
                'name': rule.name,
                'metric': rule.metric,
                'threshold': rule.threshold,
                'operator': rule.operator,
                'triggered_at': alert_info['triggered_at'],
                'duration': alert_info['duration'],
                'enabled': rule.enabled
            }
        
        return APIResponse.success(
            data={
                'active_alerts': formatted_alerts,
                'total_rules': len(monitor.alert_manager.rules),
                'active_count': len(active_alerts)
            },
            message="Alerts retrieved successfully"
        )
        
    except Exception as e:
        return APIResponse.error(
            message="Failed to retrieve alerts",
            details={'error': str(e)},
            status_code=500
        )


@performance_bp.route('/system', methods=['GET'])
@require_auth()
def get_system_info():
    """Get system information and resource usage."""
    try:
        import psutil
        import platform
        import sys
        
        # System information
        system_info = {
            'platform': {
                'system': platform.system(),
                'release': platform.release(),
                'version': platform.version(),
                'machine': platform.machine(),
                'processor': platform.processor()
            },
            'python': {
                'version': sys.version,
                'executable': sys.executable,
                'path': sys.path[:5]  # First 5 paths only
            },
            'resources': {
                'cpu_count': psutil.cpu_count(),
                'cpu_freq': psutil.cpu_freq()._asdict() if psutil.cpu_freq() else None,
                'memory': psutil.virtual_memory()._asdict(),
                'disk': psutil.disk_usage('/')._asdict(),
                'boot_time': psutil.boot_time()
            }
        }
        
        # Network interfaces (limited info)
        try:
            network_info = {}
            for interface, addresses in psutil.net_if_addrs().items():
                network_info[interface] = len(addresses)
            system_info['network_interfaces'] = network_info
        except:
            pass
        
        return APIResponse.success(
            data=system_info,
            message="System information retrieved successfully"
        )
        
    except Exception as e:
        return APIResponse.error(
            message="Failed to retrieve system information",
            details={'error': str(e)},
            status_code=500
        )


@performance_bp.route('/monitor/start', methods=['POST'])
@require_auth()
def start_monitoring():
    """Start performance monitoring."""
    try:
        monitor = get_performance_monitor()
        if monitor.monitoring_enabled:
            return APIResponse.success(
                data={'already_running': True},
                message="Performance monitoring is already running"
            )
        
        monitor.start_monitoring()
        
        return APIResponse.success(
            data={'started': True},
            message="Performance monitoring started successfully"
        )
        
    except Exception as e:
        return APIResponse.error(
            message="Failed to start monitoring",
            details={'error': str(e)},
            status_code=500
        )


@performance_bp.route('/monitor/stop', methods=['POST'])
@require_auth()
def stop_monitoring():
    """Stop performance monitoring."""
    try:
        monitor = get_performance_monitor()
        if not monitor.monitoring_enabled:
            return APIResponse.success(
                data={'already_stopped': True},
                message="Performance monitoring is not running"
            )
        
        monitor.stop_monitoring()
        
        return APIResponse.success(
            data={'stopped': True},
            message="Performance monitoring stopped successfully"
        )
        
    except Exception as e:
        return APIResponse.error(
            message="Failed to stop monitoring",
            details={'error': str(e)},
            status_code=500
        )


@performance_bp.route('/export', methods=['GET'])
@require_auth()
def export_metrics():
    """Export metrics in various formats."""
    try:
        format_type = request.args.get('format', 'json').lower()
        duration = float(request.args.get('duration', 3600))
        
        monitor = get_performance_monitor()
        stats = monitor.collector.get_all_metrics(duration)
        
        if format_type == 'prometheus':
            # Export in Prometheus format
            lines = []
            for metric_name, metric_stats in stats.items():
                if 'latest' in metric_stats:
                    lines.append(f"# TYPE {metric_name} gauge")
                    lines.append(f"{metric_name} {metric_stats['latest']}")
            
            response_text = '\n'.join(lines)
            
            from flask import Response
            return Response(response_text, mimetype='text/plain')
        
        else:
            # Default JSON export
            export_data = {
                'format': format_type,
                'exported_at': time.time(),
                'duration': duration,
                'metrics': stats
            }
            
            return APIResponse.success(
                data=export_data,
                message="Metrics exported successfully"
            )
        
    except Exception as e:
        return APIResponse.error(
            message="Failed to export metrics",
            details={'error': str(e)},
            status_code=500
        )