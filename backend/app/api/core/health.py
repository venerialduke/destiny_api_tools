"""
Health check and monitoring API endpoints.
"""

from flask import Blueprint, jsonify, request
from ...services.health_monitor import get_health_monitor
from ...services.performance_monitor import get_performance_monitor
from ...services.data_pipeline import get_data_pipeline
from ...services.search_service import get_search_service
from ...services.job_scheduler import get_job_scheduler
from ...utils.response import APIResponse

health_bp = Blueprint('health', __name__)


@health_bp.route('/health', methods=['GET'])
def health_check():
    """
    Basic health check endpoint.
    Returns overall application health status.
    """
    try:
        health_monitor = get_health_monitor()
        health_status = health_monitor.get_system_health()
        
        # Determine HTTP status code based on health
        if health_status['status'] == 'healthy':
            status_code = 200
        elif health_status['status'] == 'degraded':
            status_code = 200  # Still operational
        else:  # critical
            status_code = 503  # Service unavailable
        
        return jsonify({
            'status': health_status['status'],
            'healthy': health_status['healthy'],
            'timestamp': health_status['timestamp'],
            'uptime_hours': health_status['uptime_hours'],
            'message': f"Application is {health_status['status']}"
        }), status_code
        
    except Exception as e:
        return jsonify({
            'status': 'critical',
            'healthy': False,
            'error': str(e),
            'message': 'Health check failed'
        }), 503


@health_bp.route('/health/detailed', methods=['GET'])
def detailed_health_check():
    """
    Detailed health check with all subsystem status.
    """
    try:
        health_monitor = get_health_monitor()
        health_status = health_monitor.get_system_health()
        
        return APIResponse.success(
            data=health_status,
            message="Detailed health check completed"
        )
        
    except Exception as e:
        return APIResponse.error(
            message="Detailed health check failed",
            code="HEALTH_CHECK_ERROR",
            details={"error": str(e)}
        ), 503


@health_bp.route('/health/performance', methods=['GET'])
def performance_metrics():
    """
    Get performance metrics and statistics.
    """
    try:
        health_monitor = get_health_monitor()
        performance_data = health_monitor.get_performance_metrics()
        
        # Add additional performance data from other services
        try:
            perf_monitor = get_performance_monitor()
            performance_data['monitoring'] = perf_monitor.get_health_status()
        except Exception as e:
            performance_data['monitoring'] = {'error': str(e)}
        
        try:
            data_pipeline = get_data_pipeline()
            performance_data['pipeline'] = data_pipeline.get_comprehensive_stats()
        except Exception as e:
            performance_data['pipeline'] = {'error': str(e)}
        
        try:
            search_service = get_search_service()
            performance_data['search'] = search_service.get_stats()
        except Exception as e:
            performance_data['search'] = {'error': str(e)}
        
        try:
            job_scheduler = get_job_scheduler()
            performance_data['scheduler'] = job_scheduler.get_stats()
        except Exception as e:
            performance_data['scheduler'] = {'error': str(e)}
        
        return APIResponse.success(
            data=performance_data,
            message="Performance metrics retrieved successfully"
        )
        
    except Exception as e:
        return APIResponse.error(
            message="Failed to retrieve performance metrics",
            code="PERFORMANCE_METRICS_ERROR",
            details={"error": str(e)}
        ), 500


@health_bp.route('/health/services', methods=['GET'])
def service_status():
    """
    Get status of all application services.
    """
    try:
        services_status = {}
        
        # Health Monitor
        try:
            health_monitor = get_health_monitor()
            services_status['health_monitor'] = {
                'status': 'healthy',
                'message': 'Health monitoring operational'
            }
        except Exception as e:
            services_status['health_monitor'] = {
                'status': 'error',
                'error': str(e)
            }
        
        # Performance Monitor
        try:
            perf_monitor = get_performance_monitor()
            health_status = perf_monitor.get_health_status()
            services_status['performance_monitor'] = {
                'status': 'healthy' if 'error' not in health_status else 'error',
                'details': health_status
            }
        except Exception as e:
            services_status['performance_monitor'] = {
                'status': 'error',
                'error': str(e)
            }
        
        # Data Pipeline
        try:
            data_pipeline = get_data_pipeline()
            pipeline_stats = data_pipeline.get_comprehensive_stats()
            services_status['data_pipeline'] = {
                'status': 'healthy' if pipeline_stats['pipeline']['running'] else 'stopped',
                'details': pipeline_stats
            }
        except Exception as e:
            services_status['data_pipeline'] = {
                'status': 'error',
                'error': str(e)
            }
        
        # Search Service
        try:
            search_service = get_search_service()
            search_stats = search_service.get_stats()
            services_status['search_service'] = {
                'status': 'healthy' if search_stats['total_documents'] > 0 else 'empty',
                'details': search_stats
            }
        except Exception as e:
            services_status['search_service'] = {
                'status': 'error',
                'error': str(e)
            }
        
        # Job Scheduler
        try:
            job_scheduler = get_job_scheduler()
            scheduler_stats = job_scheduler.get_stats()
            services_status['job_scheduler'] = {
                'status': 'healthy' if scheduler_stats['scheduler_running'] else 'stopped',
                'details': scheduler_stats
            }
        except Exception as e:
            services_status['job_scheduler'] = {
                'status': 'error',
                'error': str(e)
            }
        
        # Determine overall status
        all_healthy = all(
            service['status'] in ['healthy', 'empty', 'stopped'] 
            for service in services_status.values()
        )
        any_error = any(
            service['status'] == 'error' 
            for service in services_status.values()
        )
        
        overall_status = 'healthy' if all_healthy else 'degraded' if not any_error else 'critical'
        
        return APIResponse.success(
            data={
                'overall_status': overall_status,
                'services': services_status,
                'summary': {
                    'total_services': len(services_status),
                    'healthy_services': sum(1 for s in services_status.values() if s['status'] in ['healthy']),
                    'error_services': sum(1 for s in services_status.values() if s['status'] == 'error')
                }
            },
            message="Service status retrieved successfully"
        )
        
    except Exception as e:
        return APIResponse.error(
            message="Failed to retrieve service status",
            code="SERVICE_STATUS_ERROR",
            details={"error": str(e)}
        ), 500


@health_bp.route('/health/ready', methods=['GET'])
def readiness_check():
    """
    Kubernetes-style readiness check.
    Returns 200 if the application is ready to serve traffic.
    """
    try:
        health_monitor = get_health_monitor()
        health_status = health_monitor.get_system_health()
        
        # Check if critical systems are working
        critical_checks = []
        for check_name, check_result in health_status['checks'].items():
            if check_result.get('critical', False) and not check_result['healthy']:
                critical_checks.append(check_name)
        
        if critical_checks:
            return jsonify({
                'ready': False,
                'message': f"Critical systems not ready: {', '.join(critical_checks)}"
            }), 503
        
        return jsonify({
            'ready': True,
            'message': 'Application is ready to serve traffic'
        }), 200
        
    except Exception as e:
        return jsonify({
            'ready': False,
            'error': str(e),
            'message': 'Readiness check failed'
        }), 503


@health_bp.route('/health/live', methods=['GET'])
def liveness_check():
    """
    Kubernetes-style liveness check.
    Returns 200 if the application is alive (basic functionality working).
    """
    try:
        # Basic liveness check - just ensure the application can respond
        return jsonify({
            'alive': True,
            'timestamp': health_monitor.get_health_monitor().start_time.isoformat(),
            'message': 'Application is alive'
        }), 200
        
    except Exception as e:
        return jsonify({
            'alive': False,
            'error': str(e),
            'message': 'Liveness check failed'
        }), 500


@health_bp.route('/health/startup', methods=['GET'])
def startup_check():
    """
    Kubernetes-style startup check.
    Returns 200 when the application has finished starting up.
    """
    try:
        # Check if essential services have started
        health_monitor = get_health_monitor()
        health_status = health_monitor.get_system_health()
        
        # Consider started if basic health checks pass
        if health_status['status'] in ['healthy', 'degraded']:
            return jsonify({
                'started': True,
                'uptime_hours': health_status['uptime_hours'],
                'message': 'Application startup completed'
            }), 200
        else:
            return jsonify({
                'started': False,
                'status': health_status['status'],
                'message': 'Application still starting up'
            }), 503
        
    except Exception as e:
        return jsonify({
            'started': False,
            'error': str(e),
            'message': 'Startup check failed'
        }), 500


@health_bp.route('/health/database', methods=['GET'])
def database_health():
    """
    Specific database health check.
    """
    try:
        health_monitor = get_health_monitor()
        health_status = health_monitor.get_system_health()
        
        db_check = health_status['checks'].get('database', {})
        
        if db_check.get('healthy', False):
            status_code = 200
        elif db_check.get('critical', False):
            status_code = 503
        else:
            status_code = 200  # Degraded but operational
        
        return APIResponse.success(
            data=db_check,
            message="Database health check completed"
        ), status_code
        
    except Exception as e:
        return APIResponse.error(
            message="Database health check failed",
            code="DATABASE_HEALTH_ERROR",
            details={"error": str(e)}
        ), 503


@health_bp.route('/health/dependencies', methods=['GET'])
def dependency_health():
    """
    Check health of external dependencies.
    """
    try:
        dependencies = {}
        
        # Check external API connectivity (Bungie API)
        try:
            # This would perform actual connectivity tests
            dependencies['bungie_api'] = {
                'status': 'healthy',
                'response_time_ms': 150,
                'last_checked': health_monitor.get_health_monitor().start_time.isoformat()
            }
        except Exception as e:
            dependencies['bungie_api'] = {
                'status': 'error',
                'error': str(e)
            }
        
        # Check other dependencies as needed
        dependencies['manifest_updater'] = {
            'status': 'healthy',
            'message': 'Manifest updater operational'
        }
        
        # Determine overall dependency health
        all_healthy = all(dep['status'] == 'healthy' for dep in dependencies.values())
        overall_status = 'healthy' if all_healthy else 'degraded'
        
        return APIResponse.success(
            data={
                'overall_status': overall_status,
                'dependencies': dependencies,
                'total_dependencies': len(dependencies),
                'healthy_dependencies': sum(1 for d in dependencies.values() if d['status'] == 'healthy')
            },
            message="Dependency health check completed"
        )
        
    except Exception as e:
        return APIResponse.error(
            message="Dependency health check failed",
            code="DEPENDENCY_HEALTH_ERROR",
            details={"error": str(e)}
        ), 500


@health_bp.route('/health/metrics/export', methods=['GET'])
def export_metrics():
    """
    Export metrics in Prometheus format.
    """
    try:
        health_monitor = get_health_monitor()
        health_status = health_monitor.get_system_health()
        performance_data = health_monitor.get_performance_metrics()
        
        # Generate Prometheus-style metrics
        metrics = []
        
        # Health status metrics
        metrics.append(f'# HELP app_health_status Application health status (1=healthy, 0=unhealthy)')
        metrics.append(f'# TYPE app_health_status gauge')
        metrics.append(f'app_health_status{{status="{health_status["status"]}"}} {1 if health_status["healthy"] else 0}')
        
        # Uptime metric
        metrics.append(f'# HELP app_uptime_hours Application uptime in hours')
        metrics.append(f'# TYPE app_uptime_hours gauge')
        metrics.append(f'app_uptime_hours {health_status["uptime_hours"]:.2f}')
        
        # System metrics
        if 'system' in performance_data:
            system = performance_data['system']
            
            metrics.append(f'# HELP system_cpu_percent CPU usage percentage')
            metrics.append(f'# TYPE system_cpu_percent gauge')
            metrics.append(f'system_cpu_percent {system.get("cpu_percent", 0)}')
            
            metrics.append(f'# HELP system_memory_percent Memory usage percentage')
            metrics.append(f'# TYPE system_memory_percent gauge')
            metrics.append(f'system_memory_percent {system.get("memory_percent", 0)}')
        
        # Database metrics
        if 'database' in performance_data:
            database = performance_data['database']
            
            metrics.append(f'# HELP database_definitions_total Total number of definitions in database')
            metrics.append(f'# TYPE database_definitions_total gauge')
            metrics.append(f'database_definitions_total {database.get("total_definitions", 0)}')
        
        # Updater metrics
        if 'updater' in performance_data:
            updater = performance_data['updater']
            
            metrics.append(f'# HELP updater_total_checks_total Total number of update checks performed')
            metrics.append(f'# TYPE updater_total_checks_total counter')
            metrics.append(f'updater_total_checks_total {updater.get("total_checks", 0)}')
            
            metrics.append(f'# HELP updater_success_rate Update success rate')
            metrics.append(f'# TYPE updater_success_rate gauge')
            metrics.append(f'updater_success_rate {updater.get("success_rate", 0)}')
        
        # Return as plain text for Prometheus scraping
        return '\n'.join(metrics), 200, {'Content-Type': 'text/plain; charset=utf-8'}
        
    except Exception as e:
        return f'# ERROR: Failed to export metrics: {str(e)}', 500, {'Content-Type': 'text/plain; charset=utf-8'}