"""
Performance monitoring service for tracking application metrics and optimization insights.
Provides real-time monitoring, alerting, and performance analytics.
"""

import time
import logging
import threading
import psutil
import gc
from typing import Dict, List, Any, Optional, Callable
from dataclasses import dataclass, field
from collections import deque, defaultdict
from statistics import mean, median, stdev
from datetime import datetime, timedelta

from ..config import config
from .connection_pool import get_connection_stats
from .cache_service import get_cache
from .batch_service import get_optimized_client


logger = logging.getLogger(__name__)


@dataclass
class MetricSnapshot:
    """Represents a snapshot of metrics at a specific time."""
    timestamp: float
    values: Dict[str, Any]
    tags: Dict[str, str] = field(default_factory=dict)


@dataclass
class AlertRule:
    """Represents an alert rule for monitoring."""
    name: str
    metric: str
    threshold: float
    operator: str  # 'gt', 'lt', 'eq', 'gte', 'lte'
    duration: float  # How long condition must persist
    callback: Optional[Callable] = None
    enabled: bool = True
    last_triggered: Optional[float] = None
    cooldown: float = 300  # 5 minutes cooldown


class MetricsCollector:
    """Collects and stores performance metrics."""
    
    def __init__(self, max_history: int = 1000):
        self.max_history = max_history
        self.metrics: Dict[str, deque] = defaultdict(lambda: deque(maxlen=max_history))
        self.lock = threading.RLock()
        
        # Metric definitions
        self.metric_definitions = {
            'response_time': {'unit': 'ms', 'type': 'gauge'},
            'request_count': {'unit': 'count', 'type': 'counter'},
            'error_rate': {'unit': 'percent', 'type': 'gauge'},
            'cpu_usage': {'unit': 'percent', 'type': 'gauge'},
            'memory_usage': {'unit': 'MB', 'type': 'gauge'},
            'cache_hit_rate': {'unit': 'percent', 'type': 'gauge'},
            'active_connections': {'unit': 'count', 'type': 'gauge'},
            'queue_depth': {'unit': 'count', 'type': 'gauge'}
        }
    
    def record_metric(self, name: str, value: float, tags: Dict[str, str] = None):
        """Record a metric value."""
        with self.lock:
            snapshot = MetricSnapshot(
                timestamp=time.time(),
                values={name: value},
                tags=tags or {}
            )
            self.metrics[name].append(snapshot)
    
    def record_multiple(self, metrics: Dict[str, float], tags: Dict[str, str] = None):
        """Record multiple metrics at once."""
        timestamp = time.time()
        with self.lock:
            for name, value in metrics.items():
                snapshot = MetricSnapshot(
                    timestamp=timestamp,
                    values={name: value},
                    tags=tags or {}
                )
                self.metrics[name].append(snapshot)
    
    def get_metric_history(self, name: str, duration: float = 3600) -> List[MetricSnapshot]:
        """Get metric history for a specific duration."""
        cutoff_time = time.time() - duration
        with self.lock:
            if name in self.metrics:
                return [snapshot for snapshot in self.metrics[name] 
                       if snapshot.timestamp >= cutoff_time]
            return []
    
    def get_metric_stats(self, name: str, duration: float = 3600) -> Dict[str, Any]:
        """Get statistical summary of a metric."""
        history = self.get_metric_history(name, duration)
        if not history:
            return {}
        
        values = [snapshot.values[name] for snapshot in history]
        
        try:
            stats = {
                'count': len(values),
                'min': min(values),
                'max': max(values),
                'mean': mean(values),
                'median': median(values),
                'latest': values[-1] if values else None,
                'first': values[0] if values else None
            }
            
            if len(values) > 1:
                stats['stdev'] = stdev(values)
                stats['range'] = stats['max'] - stats['min']
            
            return stats
        except Exception as e:
            logger.error(f"Error calculating stats for {name}: {e}")
            return {'error': str(e)}
    
    def get_all_metrics(self, duration: float = 3600) -> Dict[str, Dict[str, Any]]:
        """Get statistics for all metrics."""
        with self.lock:
            result = {}
            for metric_name in self.metrics:
                result[metric_name] = self.get_metric_stats(metric_name, duration)
            return result


class SystemMonitor:
    """Monitors system-level performance metrics."""
    
    def __init__(self, collector: MetricsCollector):
        self.collector = collector
        self.process = psutil.Process()
        self.monitoring = False
        self.monitor_thread = None
        self.interval = 5.0  # 5 seconds
    
    def start_monitoring(self):
        """Start system monitoring in background thread."""
        if self.monitoring:
            return
        
        self.monitoring = True
        self.monitor_thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self.monitor_thread.start()
        logger.info("Started system monitoring")
    
    def stop_monitoring(self):
        """Stop system monitoring."""
        self.monitoring = False
        if self.monitor_thread:
            self.monitor_thread.join(timeout=5)
        logger.info("Stopped system monitoring")
    
    def _monitor_loop(self):
        """Main monitoring loop."""
        while self.monitoring:
            try:
                self._collect_system_metrics()
                time.sleep(self.interval)
            except Exception as e:
                logger.error(f"System monitoring error: {e}")
                time.sleep(self.interval)
    
    def _collect_system_metrics(self):
        """Collect system performance metrics."""
        try:
            # CPU metrics
            cpu_percent = psutil.cpu_percent(interval=None)
            cpu_count = psutil.cpu_count()
            load_avg = psutil.getloadavg()[0] if hasattr(psutil, 'getloadavg') else 0
            
            # Memory metrics
            memory = psutil.virtual_memory()
            swap = psutil.swap_memory()
            
            # Process-specific metrics
            process_memory = self.process.memory_info()
            process_cpu = self.process.cpu_percent()
            
            # Disk metrics
            disk = psutil.disk_usage('/')
            
            # Network metrics (if available)
            try:
                network = psutil.net_io_counters()
                network_metrics = {
                    'network_bytes_sent': network.bytes_sent,
                    'network_bytes_recv': network.bytes_recv,
                    'network_packets_sent': network.packets_sent,
                    'network_packets_recv': network.packets_recv
                }
            except:
                network_metrics = {}
            
            # Collect all metrics
            metrics = {
                # CPU
                'cpu_usage': cpu_percent,
                'cpu_count': cpu_count,
                'load_average': load_avg,
                
                # Memory
                'memory_total': memory.total / 1024 / 1024,  # MB
                'memory_available': memory.available / 1024 / 1024,  # MB
                'memory_usage': memory.percent,
                'swap_usage': swap.percent,
                
                # Process
                'process_memory_rss': process_memory.rss / 1024 / 1024,  # MB
                'process_memory_vms': process_memory.vms / 1024 / 1024,  # MB
                'process_cpu': process_cpu,
                
                # Disk
                'disk_usage': disk.percent,
                'disk_free': disk.free / 1024 / 1024 / 1024,  # GB
                
                # Python-specific
                'gc_collections': len(gc.get_stats()),
                'thread_count': threading.active_count(),
                
                **network_metrics
            }
            
            self.collector.record_multiple(metrics, {'source': 'system'})
            
        except Exception as e:
            logger.error(f"Error collecting system metrics: {e}")


class ApplicationMonitor:
    """Monitors application-specific performance metrics."""
    
    def __init__(self, collector: MetricsCollector):
        self.collector = collector
        self.request_times = deque(maxlen=1000)
        self.error_count = 0
        self.total_requests = 0
        self.lock = threading.Lock()
    
    def record_request(self, duration: float, success: bool = True, endpoint: str = None):
        """Record a request's performance."""
        with self.lock:
            self.total_requests += 1
            self.request_times.append(duration)
            
            if not success:
                self.error_count += 1
            
            # Calculate current metrics
            avg_response_time = mean(self.request_times) if self.request_times else 0
            error_rate = (self.error_count / self.total_requests * 100) if self.total_requests > 0 else 0
            
            tags = {'endpoint': endpoint} if endpoint else {}
            
            metrics = {
                'response_time': duration * 1000,  # Convert to ms
                'avg_response_time': avg_response_time * 1000,
                'error_rate': error_rate,
                'total_requests': self.total_requests
            }
            
            self.collector.record_multiple(metrics, tags)
    
    def get_current_stats(self) -> Dict[str, Any]:
        """Get current application statistics."""
        with self.lock:
            if not self.request_times:
                return {'total_requests': 0, 'error_count': 0}
            
            recent_times = list(self.request_times)
            
            return {
                'total_requests': self.total_requests,
                'error_count': self.error_count,
                'error_rate': (self.error_count / self.total_requests * 100) if self.total_requests > 0 else 0,
                'avg_response_time': mean(recent_times) * 1000,
                'min_response_time': min(recent_times) * 1000,
                'max_response_time': max(recent_times) * 1000,
                'median_response_time': median(recent_times) * 1000,
                'p95_response_time': sorted(recent_times)[int(len(recent_times) * 0.95)] * 1000 if recent_times else 0
            }


class AlertManager:
    """Manages performance alerts and notifications."""
    
    def __init__(self, collector: MetricsCollector):
        self.collector = collector
        self.rules: List[AlertRule] = []
        self.active_alerts: Dict[str, float] = {}  # rule_name -> triggered_time
        self.lock = threading.Lock()
        self.checking = False
        self.check_thread = None
        self.check_interval = 10.0  # 10 seconds
    
    def add_rule(self, rule: AlertRule):
        """Add an alert rule."""
        with self.lock:
            self.rules.append(rule)
        logger.info(f"Added alert rule: {rule.name}")
    
    def remove_rule(self, rule_name: str) -> bool:
        """Remove an alert rule."""
        with self.lock:
            for i, rule in enumerate(self.rules):
                if rule.name == rule_name:
                    del self.rules[i]
                    # Clear active alert if exists
                    if rule_name in self.active_alerts:
                        del self.active_alerts[rule_name]
                    logger.info(f"Removed alert rule: {rule_name}")
                    return True
        return False
    
    def start_checking(self):
        """Start alert checking in background thread."""
        if self.checking:
            return
        
        self.checking = True
        self.check_thread = threading.Thread(target=self._check_loop, daemon=True)
        self.check_thread.start()
        logger.info("Started alert checking")
    
    def stop_checking(self):
        """Stop alert checking."""
        self.checking = False
        if self.check_thread:
            self.check_thread.join(timeout=5)
        logger.info("Stopped alert checking")
    
    def _check_loop(self):
        """Main alert checking loop."""
        while self.checking:
            try:
                self._check_all_rules()
                time.sleep(self.check_interval)
            except Exception as e:
                logger.error(f"Alert checking error: {e}")
                time.sleep(self.check_interval)
    
    def _check_all_rules(self):
        """Check all alert rules."""
        current_time = time.time()
        
        with self.lock:
            for rule in self.rules:
                if not rule.enabled:
                    continue
                
                # Check cooldown
                if (rule.last_triggered and 
                    current_time - rule.last_triggered < rule.cooldown):
                    continue
                
                # Get recent metric values
                history = self.collector.get_metric_history(rule.metric, rule.duration)
                if not history:
                    continue
                
                # Check if condition is met
                if self._evaluate_condition(rule, history):
                    # Check if this is a new alert or ongoing
                    if rule.name not in self.active_alerts:
                        # New alert
                        self.active_alerts[rule.name] = current_time
                        self._trigger_alert(rule, history)
                    elif current_time - self.active_alerts[rule.name] >= rule.duration:
                        # Alert condition has persisted long enough
                        self._trigger_alert(rule, history)
                        rule.last_triggered = current_time
                else:
                    # Condition not met, clear active alert
                    if rule.name in self.active_alerts:
                        del self.active_alerts[rule.name]
    
    def _evaluate_condition(self, rule: AlertRule, history: List[MetricSnapshot]) -> bool:
        """Evaluate if alert condition is met."""
        if not history:
            return False
        
        # Get the latest value
        latest_value = history[-1].values[rule.metric]
        
        # Evaluate based on operator
        if rule.operator == 'gt':
            return latest_value > rule.threshold
        elif rule.operator == 'lt':
            return latest_value < rule.threshold
        elif rule.operator == 'gte':
            return latest_value >= rule.threshold
        elif rule.operator == 'lte':
            return latest_value <= rule.threshold
        elif rule.operator == 'eq':
            return latest_value == rule.threshold
        else:
            return False
    
    def _trigger_alert(self, rule: AlertRule, history: List[MetricSnapshot]):
        """Trigger an alert."""
        latest_value = history[-1].values[rule.metric]
        
        logger.warning(f"ALERT: {rule.name} - {rule.metric} {rule.operator} {rule.threshold}, current: {latest_value}")
        
        if rule.callback:
            try:
                rule.callback(rule, latest_value, history)
            except Exception as e:
                logger.error(f"Alert callback error for {rule.name}: {e}")
    
    def get_active_alerts(self) -> Dict[str, Dict[str, Any]]:
        """Get all active alerts."""
        with self.lock:
            result = {}
            current_time = time.time()
            
            for rule_name, triggered_time in self.active_alerts.items():
                rule = next((r for r in self.rules if r.name == rule_name), None)
                if rule:
                    result[rule_name] = {
                        'rule': rule,
                        'triggered_at': triggered_time,
                        'duration': current_time - triggered_time
                    }
            
            return result


class PerformanceMonitor:
    """Main performance monitoring service."""
    
    def __init__(self):
        self.collector = MetricsCollector()
        self.system_monitor = SystemMonitor(self.collector)
        self.app_monitor = ApplicationMonitor(self.collector)
        self.alert_manager = AlertManager(self.collector)
        
        self._setup_default_alerts()
        self.monitoring_enabled = False
    
    def start_monitoring(self):
        """Start all monitoring components."""
        if self.monitoring_enabled:
            return
        
        self.system_monitor.start_monitoring()
        self.alert_manager.start_checking()
        self.monitoring_enabled = True
        
        logger.info("Performance monitoring started")
    
    def stop_monitoring(self):
        """Stop all monitoring components."""
        if not self.monitoring_enabled:
            return
        
        self.system_monitor.stop_monitoring()
        self.alert_manager.stop_checking()
        self.monitoring_enabled = False
        
        logger.info("Performance monitoring stopped")
    
    def _setup_default_alerts(self):
        """Setup default alert rules."""
        default_rules = [
            AlertRule(
                name="high_cpu_usage",
                metric="cpu_usage",
                threshold=80.0,
                operator="gt",
                duration=60.0,  # 1 minute
                callback=lambda rule, value, history: logger.warning(f"High CPU usage: {value}%")
            ),
            AlertRule(
                name="high_memory_usage",
                metric="memory_usage",
                threshold=85.0,
                operator="gt",
                duration=120.0,  # 2 minutes
                callback=lambda rule, value, history: logger.warning(f"High memory usage: {value}%")
            ),
            AlertRule(
                name="high_error_rate",
                metric="error_rate",
                threshold=5.0,
                operator="gt",
                duration=30.0,  # 30 seconds
                callback=lambda rule, value, history: logger.error(f"High error rate: {value}%")
            ),
            AlertRule(
                name="slow_response_time",
                metric="avg_response_time",
                threshold=2000.0,  # 2 seconds
                operator="gt",
                duration=60.0,
                callback=lambda rule, value, history: logger.warning(f"Slow response time: {value}ms")
            )
        ]
        
        for rule in default_rules:
            self.alert_manager.add_rule(rule)
    
    def record_request(self, duration: float, success: bool = True, endpoint: str = None):
        """Record a request for monitoring."""
        self.app_monitor.record_request(duration, success, endpoint)
    
    def get_comprehensive_stats(self) -> Dict[str, Any]:
        """Get comprehensive performance statistics."""
        stats = {
            'timestamp': time.time(),
            'monitoring_enabled': self.monitoring_enabled,
            'application': self.app_monitor.get_current_stats(),
            'system': self.collector.get_all_metrics(3600),  # Last hour
            'alerts': {
                'active_count': len(self.alert_manager.get_active_alerts()),
                'total_rules': len(self.alert_manager.rules),
                'active_alerts': self.alert_manager.get_active_alerts()
            }
        }
        
        # Add external service stats
        try:
            stats['connection_pools'] = get_connection_stats()
        except Exception as e:
            logger.error(f"Error getting connection stats: {e}")
        
        try:
            stats['cache'] = get_cache().get_stats()
        except Exception as e:
            logger.error(f"Error getting cache stats: {e}")
        
        try:
            stats['batch_service'] = get_optimized_client().get_optimization_stats()
        except Exception as e:
            logger.error(f"Error getting batch stats: {e}")
        
        return stats
    
    def get_health_status(self) -> Dict[str, Any]:
        """Get overall health status."""
        stats = self.get_comprehensive_stats()
        
        # Determine health status based on key metrics
        health_score = 100
        issues = []
        
        # Check CPU usage
        cpu_stats = self.collector.get_metric_stats('cpu_usage', 300)  # Last 5 minutes
        if cpu_stats and cpu_stats.get('mean', 0) > 80:
            health_score -= 20
            issues.append("High CPU usage")
        
        # Check memory usage
        memory_stats = self.collector.get_metric_stats('memory_usage', 300)
        if memory_stats and memory_stats.get('mean', 0) > 85:
            health_score -= 25
            issues.append("High memory usage")
        
        # Check error rate
        error_stats = self.collector.get_metric_stats('error_rate', 300)
        if error_stats and error_stats.get('mean', 0) > 5:
            health_score -= 30
            issues.append("High error rate")
        
        # Check response time
        response_stats = self.collector.get_metric_stats('avg_response_time', 300)
        if response_stats and response_stats.get('mean', 0) > 2000:
            health_score -= 15
            issues.append("Slow response times")
        
        # Determine status
        if health_score >= 90:
            status = "healthy"
        elif health_score >= 70:
            status = "warning"
        else:
            status = "critical"
        
        return {
            'status': status,
            'health_score': max(0, health_score),
            'issues': issues,
            'active_alerts': len(self.alert_manager.get_active_alerts()),
            'uptime': time.time() - (stats.get('system', {}).get('process_cpu', {}).get('first', time.time())),
            'last_check': time.time()
        }


# Global performance monitor instance
performance_monitor = PerformanceMonitor()


def get_performance_monitor() -> PerformanceMonitor:
    """Get the global performance monitor instance."""
    return performance_monitor


def start_monitoring():
    """Start performance monitoring."""
    performance_monitor.start_monitoring()


def stop_monitoring():
    """Stop performance monitoring."""
    performance_monitor.stop_monitoring()


def record_request_performance(duration: float, success: bool = True, endpoint: str = None):
    """Record request performance metrics."""
    performance_monitor.record_request(duration, success, endpoint)


def get_performance_stats() -> Dict[str, Any]:
    """Get comprehensive performance statistics."""
    return performance_monitor.get_comprehensive_stats()


def get_health_status() -> Dict[str, Any]:
    """Get application health status."""
    return performance_monitor.get_health_status()


# Auto-start monitoring in development
if config.log_level == 'DEBUG':
    start_monitoring()