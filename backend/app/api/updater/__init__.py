"""
Update management API endpoints.
"""

from flask import Blueprint, jsonify, request
from ...services.manifest_updater import get_manifest_updater
from ...services.health_monitor import get_health_monitor
import json
from datetime import datetime

updater_bp = Blueprint('updater', __name__)


@updater_bp.route('/status', methods=['GET'])
def get_updater_status():
    """Get current updater status and statistics."""
    try:
        updater = get_manifest_updater()
        status = updater.get_status()
        return jsonify(status)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@updater_bp.route('/start', methods=['POST'])
def start_updater():
    """Start the background update service."""
    try:
        updater = get_manifest_updater()
        
        if updater.running:
            return jsonify({
                'success': False,
                'message': 'Updater is already running',
                'status': updater.update_status
            }), 400
        
        updater.start_background_updates()
        
        return jsonify({
            'success': True,
            'message': 'Background updater started successfully',
            'status': updater.update_status,
            'timestamp': datetime.utcnow().isoformat()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@updater_bp.route('/stop', methods=['POST'])
def stop_updater():
    """Stop the background update service."""
    try:
        updater = get_manifest_updater()
        
        if not updater.running:
            return jsonify({
                'success': False,
                'message': 'Updater is not running'
            }), 400
        
        updater.stop_background_updates()
        
        return jsonify({
            'success': True,
            'message': 'Background updater stopped successfully',
            'timestamp': datetime.utcnow().isoformat()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@updater_bp.route('/force-update', methods=['POST'])
def force_update():
    """Force an immediate manifest update."""
    try:
        updater = get_manifest_updater()
        result = updater.force_update()
        
        status_code = 200 if result['success'] else 400
        return jsonify(result), status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@updater_bp.route('/config', methods=['GET'])
def get_config():
    """Get current updater configuration."""
    try:
        updater = get_manifest_updater()
        status = updater.get_status()
        
        return jsonify({
            'check_interval_hours': status['check_interval_hours'],
            'running': status['running'],
            'status': status['status'],
            'configuration': {
                'auto_start': False,  # This could be configurable
                'max_retries': 3,
                'error_backoff_enabled': True,
                'callbacks_enabled': True
            }
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@updater_bp.route('/config', methods=['PUT'])
def update_config():
    """Update updater configuration."""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No configuration data provided'}), 400
        
        updater = get_manifest_updater()
        changes = []
        
        # Update check interval if provided
        if 'check_interval_hours' in data:
            new_interval = float(data['check_interval_hours'])
            if new_interval < 0.1:  # Minimum 6 minutes
                return jsonify({'error': 'Check interval must be at least 0.1 hours (6 minutes)'}), 400
            if new_interval > 168:  # Maximum 1 week
                return jsonify({'error': 'Check interval must be at most 168 hours (1 week)'}), 400
            
            old_interval = updater.check_interval / 3600
            updater.set_check_interval(new_interval)
            changes.append(f'Check interval: {old_interval:.1f}h → {new_interval:.1f}h')
        
        return jsonify({
            'success': True,
            'message': 'Configuration updated successfully',
            'changes': changes,
            'timestamp': datetime.utcnow().isoformat()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@updater_bp.route('/manifest-info', methods=['GET'])
def get_manifest_info():
    """Get current manifest version information."""
    try:
        updater = get_manifest_updater()
        info = updater.get_manifest_info()
        return jsonify(info)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@updater_bp.route('/health', methods=['GET'])
def get_health():
    """Get updater health status."""
    try:
        updater = get_manifest_updater()
        status = updater.get_status()
        
        health_info = {
            'status': status['health']['status'],
            'healthy': status['health']['status'] == 'healthy',
            'details': {
                'running': status['running'],
                'consecutive_errors': status['health']['consecutive_errors'],
                'last_error': status['health']['last_error'],
                'uptime_hours': status['uptime_hours'],
                'success_rate': status['statistics']['success_rate']
            },
            'recommendations': []
        }
        
        # Add health recommendations
        if not status['running']:
            health_info['recommendations'].append('Start the background updater service')
        
        if status['health']['consecutive_errors'] > 0:
            health_info['recommendations'].append('Check error logs and network connectivity')
        
        if status['statistics']['success_rate'] < 90:
            health_info['recommendations'].append('Review update frequency and error patterns')
        
        if status['uptime_hours'] > 720:  # 30 days
            health_info['recommendations'].append('Consider restarting the updater service')
        
        return jsonify(health_info)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@updater_bp.route('/events', methods=['GET'])
def get_events():
    """Get recent updater events (if event logging is implemented)."""
    try:
        # This would return recent events if we implement event logging
        # For now, return a placeholder
        return jsonify({
            'events': [],
            'note': 'Event logging not yet implemented',
            'available_endpoints': [
                'GET /status - Current status and statistics',
                'GET /health - Health check information',
                'GET /manifest-info - Manifest version information',
                'POST /start - Start background updates',
                'POST /stop - Stop background updates',
                'POST /force-update - Force immediate update'
            ]
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@updater_bp.route('/logs', methods=['GET'])
def get_logs():
    """Get recent updater logs."""
    try:
        # Get query parameters
        limit = min(request.args.get('limit', 100, type=int), 1000)
        level = request.args.get('level', '').upper()  # ERROR, WARN, INFO, DEBUG
        
        # This would return actual log entries if we implement log storage
        # For now, return a placeholder with current status
        updater = get_manifest_updater()
        status = updater.get_status()
        
        mock_logs = []
        if status['running']:
            mock_logs.append({
                'timestamp': datetime.utcnow().isoformat(),
                'level': 'INFO',
                'message': f'Background updater running (status: {status["status"]})'
            })
        
        if status['last_check']:
            mock_logs.append({
                'timestamp': status['last_check'],
                'level': 'INFO',
                'message': f'Last check completed in {status["statistics"]["last_check_duration_seconds"]:.1f}s'
            })
        
        if status['error_message']:
            mock_logs.append({
                'timestamp': datetime.utcnow().isoformat(),
                'level': 'ERROR',
                'message': status['error_message']
            })
        
        return jsonify({
            'logs': mock_logs[:limit],
            'total': len(mock_logs),
            'note': 'Log persistence not yet implemented - showing current status only'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@updater_bp.route('/metrics', methods=['GET'])
def get_metrics():
    """Get updater metrics in a format suitable for monitoring systems."""
    try:
        updater = get_manifest_updater()
        status = updater.get_status()
        
        # Format metrics for monitoring systems (Prometheus-style)
        metrics = {
            'manifest_updater_running': 1 if status['running'] else 0,
            'manifest_updater_uptime_hours': status['uptime_hours'],
            'manifest_updater_total_checks': status['statistics']['total_checks'],
            'manifest_updater_total_updates': status['statistics']['total_updates'],
            'manifest_updater_consecutive_errors': status['statistics']['consecutive_errors'],
            'manifest_updater_success_rate_percent': status['statistics']['success_rate'],
            'manifest_updater_last_check_duration_seconds': status['statistics']['last_check_duration_seconds'],
            'manifest_updater_last_update_duration_seconds': status['statistics']['last_update_duration_seconds'],
            'manifest_updater_check_interval_hours': status['check_interval_hours']
        }
        
        # Add health status as numeric
        health_status_map = {'healthy': 2, 'degraded': 1, 'unhealthy': 0}
        metrics['manifest_updater_health_status'] = health_status_map.get(status['health']['status'], 0)
        
        return jsonify({
            'metrics': metrics,
            'timestamp': datetime.utcnow().isoformat(),
            'format': 'prometheus_compatible'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@updater_bp.route('/system-health', methods=['GET'])
def get_system_health():
    """Get comprehensive system health status."""
    try:
        health_monitor = get_health_monitor()
        health_status = health_monitor.get_system_health()
        return jsonify(health_status)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@updater_bp.route('/performance', methods=['GET'])
def get_performance_metrics():
    """Get system performance metrics."""
    try:
        health_monitor = get_health_monitor()
        metrics = health_monitor.get_performance_metrics()
        return jsonify(metrics)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@updater_bp.route('/dashboard', methods=['GET'])
def get_dashboard_data():
    """Get comprehensive dashboard data combining all monitoring information."""
    try:
        # Get all monitoring data
        updater = get_manifest_updater()
        health_monitor = get_health_monitor()
        
        updater_status = updater.get_status()
        health_status = health_monitor.get_system_health()
        performance_metrics = health_monitor.get_performance_metrics()
        manifest_info = updater.get_manifest_info()
        
        dashboard = {
            'overview': {
                'status': health_status['status'],
                'healthy': health_status['healthy'],
                'uptime_hours': health_status['uptime_hours'],
                'last_update': updater_status['last_update'],
                'next_check': updater_status['next_check']
            },
            'updater': {
                'running': updater_status['running'],
                'status': updater_status['status'],
                'statistics': updater_status['statistics'],
                'health': updater_status['health']
            },
            'system': {
                'health_checks': health_status['checks'],
                'performance': performance_metrics.get('system', {}),
                'summary': health_status['summary']
            },
            'manifest': {
                'local_info': manifest_info.get('local_info', {}),
                'remote_info': manifest_info.get('remote_info', {}),
                'needs_update': manifest_info.get('needs_update', False)
            },
            'timestamp': datetime.utcnow().isoformat()
        }
        
        return jsonify(dashboard)
    except Exception as e:
        return jsonify({'error': str(e)}), 500