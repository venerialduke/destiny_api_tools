"""
Test suite for health monitoring functionality.
"""

import pytest
import time
from unittest.mock import Mock, patch
from app.services.health_monitor import get_health_monitor, HealthMonitor


class TestHealthMonitor:
    """Test health monitoring functionality."""
    
    def setup_method(self):
        """Setup test environment."""
        self.health_monitor = HealthMonitor()
    
    def test_health_monitor_initialization(self):
        """Test health monitor initializes correctly."""
        assert self.health_monitor is not None
        assert hasattr(self.health_monitor, 'start_time')
        assert self.health_monitor.start_time is not None
    
    def test_register_health_check(self):
        """Test registering a custom health check."""
        def test_check():
            return {'status': 'healthy', 'message': 'Test check passed'}
        
        result = self.health_monitor.register_health_check(
            name="test_check",
            description="Test health check",
            check_function=test_check
        )
        
        assert result is True
        assert "test_check" in self.health_monitor.health_checks
    
    def test_run_health_check(self):
        """Test running a health check."""
        def test_check():
            return {'status': 'healthy', 'message': 'Test passed'}
        
        self.health_monitor.register_health_check(
            name="test_check",
            description="Test check",
            check_function=test_check
        )
        
        result = self.health_monitor.run_health_check("test_check")
        
        assert result['status'] == 'healthy'
        assert result['name'] == 'test_check'
        assert 'duration_ms' in result
    
    def test_run_nonexistent_health_check(self):
        """Test running a non-existent health check."""
        result = self.health_monitor.run_health_check("nonexistent")
        
        assert result['status'] == 'unknown'
        assert 'error' in result
    
    def test_run_all_health_checks(self):
        """Test running all health checks."""
        def healthy_check():
            return {'status': 'healthy'}
        
        def warning_check():
            return {'status': 'warning'}
        
        self.health_monitor.register_health_check(
            name="healthy_check",
            description="Healthy check",
            check_function=healthy_check
        )
        
        self.health_monitor.register_health_check(
            name="warning_check",
            description="Warning check",
            check_function=warning_check
        )
        
        result = self.health_monitor.run_all_health_checks()
        
        assert 'overall_status' in result
        assert 'checks' in result
        assert len(result['checks']) >= 2
    
    def test_health_check_error_handling(self):
        """Test health check error handling."""
        def failing_check():
            raise Exception("Test error")
        
        self.health_monitor.register_health_check(
            name="failing_check",
            description="Failing check",
            check_function=failing_check
        )
        
        result = self.health_monitor.run_health_check("failing_check")
        
        assert result['status'] == 'critical'
        assert 'error' in result
        assert 'Test error' in result['error']
    
    @patch('app.services.health_monitor.get_cache')
    def test_cache_health_check(self, mock_get_cache):
        """Test cache service health check."""
        # Mock cache operations
        mock_cache = Mock()
        mock_cache.set.return_value = None
        mock_cache.get.return_value = "health_check_value"
        mock_cache.delete.return_value = None
        mock_get_cache.return_value = mock_cache
        
        result = self.health_monitor._check_cache_service()
        
        assert result['status'] == 'healthy'
        assert 'operational' in result['message']
    
    @patch('app.services.health_monitor.get_cache')
    def test_cache_health_check_failure(self, mock_get_cache):
        """Test cache service health check failure."""
        # Mock cache failure
        mock_cache = Mock()
        mock_cache.set.side_effect = Exception("Cache error")
        mock_get_cache.return_value = mock_cache
        
        result = self.health_monitor._check_cache_service()
        
        assert result['status'] == 'critical'
        assert 'error' in result
    
    def test_application_status(self):
        """Test getting comprehensive application status."""
        status = self.health_monitor.get_application_status()
        
        assert 'overall_status' in status
        assert 'timestamp' in status
        assert 'uptime_seconds' in status
        assert 'version' in status
        assert 'environment' in status
        assert 'health_checks' in status
        assert 'performance_metrics' in status
    
    def test_disabled_health_check(self):
        """Test disabled health check is not executed."""
        def test_check():
            return {'status': 'healthy'}
        
        self.health_monitor.register_health_check(
            name="disabled_check",
            description="Disabled check",
            check_function=test_check,
            enabled=False
        )
        
        result = self.health_monitor.run_health_check("disabled_check")
        
        assert result['status'] == 'unknown'
        assert 'disabled' in result['message']
    
    def test_monitoring_start_stop(self):
        """Test starting and stopping health monitoring."""
        assert not self.health_monitor.monitoring
        
        self.health_monitor.start_monitoring()
        assert self.health_monitor.monitoring
        assert self.health_monitor.monitor_thread is not None
        
        self.health_monitor.stop_monitoring()
        assert not self.health_monitor.monitoring
    
    def test_global_health_monitor_instance(self):
        """Test global health monitor instance."""
        monitor1 = get_health_monitor()
        monitor2 = get_health_monitor()
        
        # Should be the same instance
        assert monitor1 is monitor2
    
    def test_health_check_timing(self):
        """Test health check execution timing."""
        def slow_check():
            time.sleep(0.1)  # 100ms delay
            return {'status': 'healthy'}
        
        self.health_monitor.register_health_check(
            name="slow_check",
            description="Slow check",
            check_function=slow_check
        )
        
        result = self.health_monitor.run_health_check("slow_check")
        
        assert result['duration_ms'] >= 100
        assert result['status'] == 'healthy'
    
    def test_critical_health_check_marking(self):
        """Test critical health check marking affects overall status."""
        def critical_failing_check():
            return {'status': 'critical'}
        
        def non_critical_failing_check():
            return {'status': 'critical'}
        
        self.health_monitor.register_health_check(
            name="critical_check",
            description="Critical check",
            check_function=critical_failing_check,
            critical=True
        )
        
        self.health_monitor.register_health_check(
            name="non_critical_check",
            description="Non-critical check",
            check_function=non_critical_failing_check,
            critical=False
        )
        
        result = self.health_monitor.run_all_health_checks()
        
        # Should be critical due to critical check failure
        assert result['overall_status'] == 'critical'
        assert result['critical_failures'] >= 1


class TestHealthAPI:
    """Test health check API endpoints."""
    
    @pytest.fixture
    def client(self):
        """Create test client."""
        from app import create_app
        app = create_app(testing=True)
        with app.test_client() as client:
            yield client
    
    def test_basic_health_endpoint(self, client):
        """Test basic health check endpoint."""
        response = client.get('/api/core/health/health')
        
        assert response.status_code in [200, 503]
        data = response.get_json()
        assert 'status' in data
        assert 'healthy' in data
        assert 'timestamp' in data
    
    def test_detailed_health_endpoint(self, client):
        """Test detailed health check endpoint."""
        response = client.get('/api/core/health/detailed')
        
        assert response.status_code in [200, 503]
        data = response.get_json()
        assert 'success' in data
        if data['success']:
            assert 'data' in data
            assert 'checks' in data['data']
    
    def test_readiness_check_endpoint(self, client):
        """Test readiness check endpoint."""
        response = client.get('/api/core/health/ready')
        
        assert response.status_code in [200, 503]
        data = response.get_json()
        assert 'ready' in data
        assert 'message' in data
    
    def test_liveness_check_endpoint(self, client):
        """Test liveness check endpoint."""
        response = client.get('/api/core/health/live')
        
        assert response.status_code == 200
        data = response.get_json()
        assert 'alive' in data
        assert data['alive'] is True
    
    def test_performance_metrics_endpoint(self, client):
        """Test performance metrics endpoint."""
        response = client.get('/api/core/health/performance')
        
        assert response.status_code == 200
        data = response.get_json()
        assert 'success' in data
        if data['success']:
            assert 'data' in data
            assert 'timestamp' in data['data']
    
    def test_service_status_endpoint(self, client):
        """Test service status endpoint."""
        response = client.get('/api/core/health/services')
        
        assert response.status_code == 200
        data = response.get_json()
        assert 'success' in data
        if data['success']:
            assert 'data' in data
            assert 'overall_status' in data['data']
            assert 'services' in data['data']
    
    def test_prometheus_metrics_export(self, client):
        """Test Prometheus metrics export."""
        response = client.get('/api/core/health/metrics/export')
        
        assert response.status_code in [200, 500]
        assert response.content_type.startswith('text/plain')
        
        if response.status_code == 200:
            content = response.get_data(as_text=True)
            assert 'app_health_status' in content
            assert 'TYPE' in content
            assert 'HELP' in content
    
    def test_database_health_endpoint(self, client):
        """Test database-specific health check."""
        response = client.get('/api/core/health/database')
        
        assert response.status_code in [200, 503]
        data = response.get_json()
        assert 'success' in data
    
    def test_dependency_health_endpoint(self, client):
        """Test dependency health check."""
        response = client.get('/api/core/health/dependencies')
        
        assert response.status_code == 200
        data = response.get_json()
        assert 'success' in data
        if data['success']:
            assert 'data' in data
            assert 'dependencies' in data['data']


if __name__ == '__main__':
    pytest.main([__file__])