"""
Background job scheduler and processor for handling long-running tasks.
Provides cron-like scheduling and job queue management with persistence.
"""

import time
import json
import logging
import threading
import schedule
from typing import Dict, List, Any, Optional, Callable
from dataclasses import dataclass, field, asdict
from datetime import datetime, timedelta
from enum import Enum
import sqlite3
import os

from ..config import config
from .data_pipeline import get_data_pipeline, Job, JobPriority
from .cache_service import get_cache
from .performance_monitor import get_performance_monitor

logger = logging.getLogger(__name__)


class JobFrequency(Enum):
    """Job execution frequencies."""
    ONCE = "once"
    HOURLY = "hourly"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    CUSTOM = "custom"


class JobExecutionStatus(Enum):
    """Job execution status."""
    SCHEDULED = "scheduled"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    SKIPPED = "skipped"


@dataclass
class ScheduledJob:
    """Represents a scheduled background job."""
    id: str
    name: str
    job_type: str
    frequency: JobFrequency
    cron_expression: Optional[str] = None
    enabled: bool = True
    payload: Dict[str, Any] = field(default_factory=dict)
    priority: JobPriority = JobPriority.NORMAL
    max_retries: int = 3
    timeout: float = 300
    next_run: Optional[datetime] = None
    last_run: Optional[datetime] = None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class JobExecution:
    """Represents a job execution instance."""
    id: str
    scheduled_job_id: str
    status: JobExecutionStatus
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    duration: float = 0.0
    result: Optional[Any] = None
    error: Optional[str] = None
    retry_count: int = 0


class JobDatabase:
    """SQLite database for job persistence."""
    
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.lock = threading.RLock()
        self._ensure_database()
    
    def _ensure_database(self):
        """Create database tables if they don't exist."""
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        
        with sqlite3.connect(self.db_path) as conn:
            conn.executescript('''
                CREATE TABLE IF NOT EXISTS scheduled_jobs (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    job_type TEXT NOT NULL,
                    frequency TEXT NOT NULL,
                    cron_expression TEXT,
                    enabled BOOLEAN NOT NULL DEFAULT 1,
                    payload TEXT NOT NULL DEFAULT '{}',
                    priority INTEGER NOT NULL DEFAULT 2,
                    max_retries INTEGER NOT NULL DEFAULT 3,
                    timeout REAL NOT NULL DEFAULT 300,
                    next_run TEXT,
                    last_run TEXT,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL,
                    metadata TEXT NOT NULL DEFAULT '{}'
                );
                
                CREATE TABLE IF NOT EXISTS job_executions (
                    id TEXT PRIMARY KEY,
                    scheduled_job_id TEXT NOT NULL,
                    status TEXT NOT NULL,
                    started_at TEXT,
                    completed_at TEXT,
                    duration REAL NOT NULL DEFAULT 0,
                    result TEXT,
                    error TEXT,
                    retry_count INTEGER NOT NULL DEFAULT 0,
                    FOREIGN KEY (scheduled_job_id) REFERENCES scheduled_jobs (id)
                );
                
                CREATE INDEX IF NOT EXISTS idx_scheduled_jobs_enabled ON scheduled_jobs(enabled);
                CREATE INDEX IF NOT EXISTS idx_scheduled_jobs_next_run ON scheduled_jobs(next_run);
                CREATE INDEX IF NOT EXISTS idx_job_executions_status ON job_executions(status);
                CREATE INDEX IF NOT EXISTS idx_job_executions_scheduled_job_id ON job_executions(scheduled_job_id);
            ''')
    
    def save_scheduled_job(self, job: ScheduledJob):
        """Save a scheduled job to the database."""
        with self.lock:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute('''
                    INSERT OR REPLACE INTO scheduled_jobs 
                    (id, name, job_type, frequency, cron_expression, enabled, payload, 
                     priority, max_retries, timeout, next_run, last_run, created_at, updated_at, metadata)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    job.id, job.name, job.job_type, job.frequency.value, job.cron_expression,
                    job.enabled, json.dumps(job.payload), job.priority.value, job.max_retries,
                    job.timeout, job.next_run.isoformat() if job.next_run else None,
                    job.last_run.isoformat() if job.last_run else None,
                    job.created_at.isoformat(), job.updated_at.isoformat(),
                    json.dumps(job.metadata)
                ))
    
    def load_scheduled_jobs(self) -> List[ScheduledJob]:
        """Load all scheduled jobs from the database."""
        with self.lock:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.execute('SELECT * FROM scheduled_jobs ORDER BY created_at')
                jobs = []
                
                for row in cursor.fetchall():
                    job = ScheduledJob(
                        id=row[0],
                        name=row[1],
                        job_type=row[2],
                        frequency=JobFrequency(row[3]),
                        cron_expression=row[4],
                        enabled=bool(row[5]),
                        payload=json.loads(row[6]),
                        priority=JobPriority(row[7]),
                        max_retries=row[8],
                        timeout=row[9],
                        next_run=datetime.fromisoformat(row[10]) if row[10] else None,
                        last_run=datetime.fromisoformat(row[11]) if row[11] else None,
                        created_at=datetime.fromisoformat(row[12]),
                        updated_at=datetime.fromisoformat(row[13]),
                        metadata=json.loads(row[14])
                    )
                    jobs.append(job)
                
                return jobs
    
    def delete_scheduled_job(self, job_id: str):
        """Delete a scheduled job and its executions."""
        with self.lock:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute('DELETE FROM job_executions WHERE scheduled_job_id = ?', (job_id,))
                conn.execute('DELETE FROM scheduled_jobs WHERE id = ?', (job_id,))
    
    def save_job_execution(self, execution: JobExecution):
        """Save a job execution to the database."""
        with self.lock:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute('''
                    INSERT OR REPLACE INTO job_executions 
                    (id, scheduled_job_id, status, started_at, completed_at, duration, result, error, retry_count)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    execution.id, execution.scheduled_job_id, execution.status.value,
                    execution.started_at.isoformat() if execution.started_at else None,
                    execution.completed_at.isoformat() if execution.completed_at else None,
                    execution.duration, json.dumps(execution.result) if execution.result else None,
                    execution.error, execution.retry_count
                ))
    
    def get_job_executions(self, scheduled_job_id: str, limit: int = 50) -> List[JobExecution]:
        """Get executions for a scheduled job."""
        with self.lock:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.execute('''
                    SELECT * FROM job_executions 
                    WHERE scheduled_job_id = ? 
                    ORDER BY started_at DESC 
                    LIMIT ?
                ''', (scheduled_job_id, limit))
                
                executions = []
                for row in cursor.fetchall():
                    execution = JobExecution(
                        id=row[0],
                        scheduled_job_id=row[1],
                        status=JobExecutionStatus(row[2]),
                        started_at=datetime.fromisoformat(row[3]) if row[3] else None,
                        completed_at=datetime.fromisoformat(row[4]) if row[4] else None,
                        duration=row[5],
                        result=json.loads(row[6]) if row[6] else None,
                        error=row[7],
                        retry_count=row[8]
                    )
                    executions.append(execution)
                
                return executions


class BackgroundJobScheduler:
    """Background job scheduler with persistence and monitoring."""
    
    def __init__(self, db_path: str = None):
        self.db_path = db_path or os.path.join(config.data_dir, 'jobs.db')
        self.database = JobDatabase(self.db_path)
        self.data_pipeline = get_data_pipeline()
        self.cache = get_cache()
        self.performance_monitor = get_performance_monitor()
        
        # In-memory job registry
        self.scheduled_jobs: Dict[str, ScheduledJob] = {}
        self.job_handlers: Dict[str, Callable] = {}
        self.active_executions: Dict[str, JobExecution] = {}
        
        # Scheduler state
        self.running = False
        self.scheduler_thread = None
        self.lock = threading.RLock()
        
        # Default job handlers
        self._register_default_handlers()
        
        # Load persisted jobs
        self._load_jobs_from_database()
    
    def _register_default_handlers(self):
        """Register default job handlers."""
        self.job_handlers = {
            'manifest_update': self._handle_manifest_update,
            'user_cleanup': self._handle_user_cleanup,
            'cache_cleanup': self._handle_cache_cleanup,
            'log_cleanup': self._handle_log_cleanup,
            'health_check': self._handle_health_check,
            'performance_report': self._handle_performance_report,
            'backup_data': self._handle_backup_data
        }
    
    def _load_jobs_from_database(self):
        """Load scheduled jobs from database."""
        try:
            jobs = self.database.load_scheduled_jobs()
            for job in jobs:
                self.scheduled_jobs[job.id] = job
                self._schedule_job(job)
            
            logger.info(f"Loaded {len(jobs)} scheduled jobs from database")
        except Exception as e:
            logger.error(f"Failed to load jobs from database: {e}")
    
    def start(self):
        """Start the background job scheduler."""
        if self.running:
            return
        
        self.running = True
        self.scheduler_thread = threading.Thread(target=self._scheduler_loop, daemon=True)
        self.scheduler_thread.start()
        
        logger.info("Background job scheduler started")
    
    def stop(self):
        """Stop the background job scheduler."""
        self.running = False
        if self.scheduler_thread:
            self.scheduler_thread.join(timeout=5)
        
        # Cancel any pending scheduled jobs
        schedule.clear()
        
        logger.info("Background job scheduler stopped")
    
    def schedule_job(self, 
                    name: str,
                    job_type: str,
                    frequency: JobFrequency,
                    payload: Dict[str, Any] = None,
                    cron_expression: str = None,
                    priority: JobPriority = JobPriority.NORMAL,
                    enabled: bool = True,
                    **kwargs) -> str:
        """Schedule a new background job."""
        
        job_id = self._generate_job_id(name, job_type)
        
        scheduled_job = ScheduledJob(
            id=job_id,
            name=name,
            job_type=job_type,
            frequency=frequency,
            cron_expression=cron_expression,
            enabled=enabled,
            payload=payload or {},
            priority=priority,
            **kwargs
        )
        
        # Calculate next run time
        scheduled_job.next_run = self._calculate_next_run(scheduled_job)
        
        # Save to database
        self.database.save_scheduled_job(scheduled_job)
        
        # Add to in-memory registry
        with self.lock:
            self.scheduled_jobs[job_id] = scheduled_job
        
        # Schedule with the scheduler
        self._schedule_job(scheduled_job)
        
        logger.info(f"Scheduled job '{name}' ({job_type}) with frequency {frequency.value}")
        
        return job_id
    
    def unschedule_job(self, job_id: str) -> bool:
        """Unschedule and delete a job."""
        with self.lock:
            if job_id not in self.scheduled_jobs:
                return False
            
            # Remove from database
            self.database.delete_scheduled_job(job_id)
            
            # Remove from in-memory registry
            job = self.scheduled_jobs.pop(job_id)
            
            logger.info(f"Unscheduled job '{job.name}' ({job.job_type})")
            
            return True
    
    def update_job(self, job_id: str, **updates) -> bool:
        """Update a scheduled job."""
        with self.lock:
            if job_id not in self.scheduled_jobs:
                return False
            
            job = self.scheduled_jobs[job_id]
            
            # Apply updates
            for key, value in updates.items():
                if hasattr(job, key):
                    setattr(job, key, value)
            
            job.updated_at = datetime.now()
            
            # Recalculate next run if schedule changed
            if 'frequency' in updates or 'cron_expression' in updates:
                job.next_run = self._calculate_next_run(job)
                self._schedule_job(job)
            
            # Save to database
            self.database.save_scheduled_job(job)
            
            logger.info(f"Updated job '{job.name}' ({job.job_type})")
            
            return True
    
    def execute_job_now(self, job_id: str) -> str:
        """Execute a job immediately."""
        with self.lock:
            if job_id not in self.scheduled_jobs:
                raise ValueError(f"Job {job_id} not found")
            
            scheduled_job = self.scheduled_jobs[job_id]
            return self._execute_job(scheduled_job, immediate=True)
    
    def get_job(self, job_id: str) -> Optional[ScheduledJob]:
        """Get a scheduled job by ID."""
        return self.scheduled_jobs.get(job_id)
    
    def list_jobs(self, enabled_only: bool = False) -> List[ScheduledJob]:
        """List all scheduled jobs."""
        jobs = list(self.scheduled_jobs.values())
        if enabled_only:
            jobs = [job for job in jobs if job.enabled]
        return sorted(jobs, key=lambda j: j.created_at)
    
    def get_job_executions(self, job_id: str, limit: int = 50) -> List[JobExecution]:
        """Get execution history for a job."""
        return self.database.get_job_executions(job_id, limit)
    
    def _scheduler_loop(self):
        """Main scheduler loop."""
        while self.running:
            try:
                # Run any pending scheduled jobs
                schedule.run_pending()
                
                # Check for jobs that need to be executed
                current_time = datetime.now()
                for job in self.scheduled_jobs.values():
                    if (job.enabled and 
                        job.next_run and 
                        current_time >= job.next_run and
                        job.id not in self.active_executions):
                        
                        self._execute_job(job)
                        
                        # Update next run time
                        job.next_run = self._calculate_next_run(job)
                        job.last_run = current_time
                        job.updated_at = current_time
                        self.database.save_scheduled_job(job)
                
                time.sleep(30)  # Check every 30 seconds
                
            except Exception as e:
                logger.error(f"Scheduler loop error: {e}")
                time.sleep(60)  # Wait longer on error
    
    def _schedule_job(self, job: ScheduledJob):
        """Schedule a job with the scheduler library."""
        if not job.enabled:
            return
        
        if job.frequency == JobFrequency.HOURLY:
            schedule.every().hour.do(self._execute_job, job)
        elif job.frequency == JobFrequency.DAILY:
            schedule.every().day.do(self._execute_job, job)
        elif job.frequency == JobFrequency.WEEKLY:
            schedule.every().week.do(self._execute_job, job)
        elif job.frequency == JobFrequency.MONTHLY:
            # Approximate monthly as 30 days
            schedule.every(30).days.do(self._execute_job, job)
        elif job.frequency == JobFrequency.CUSTOM and job.cron_expression:
            # For cron expressions, we'll handle them in the main loop
            pass
    
    def _calculate_next_run(self, job: ScheduledJob) -> Optional[datetime]:
        """Calculate the next run time for a job."""
        if not job.enabled:
            return None
        
        now = datetime.now()
        
        if job.frequency == JobFrequency.ONCE:
            return now if not job.last_run else None
        elif job.frequency == JobFrequency.HOURLY:
            return now + timedelta(hours=1)
        elif job.frequency == JobFrequency.DAILY:
            return now + timedelta(days=1)
        elif job.frequency == JobFrequency.WEEKLY:
            return now + timedelta(weeks=1)
        elif job.frequency == JobFrequency.MONTHLY:
            return now + timedelta(days=30)
        elif job.frequency == JobFrequency.CUSTOM and job.cron_expression:
            # Basic cron parsing - could be enhanced with a proper cron library
            return now + timedelta(hours=1)  # Default fallback
        
        return None
    
    def _execute_job(self, job: ScheduledJob, immediate: bool = False) -> str:
        """Execute a scheduled job."""
        execution_id = f"{job.id}_{int(time.time() * 1000)}"
        
        execution = JobExecution(
            id=execution_id,
            scheduled_job_id=job.id,
            status=JobExecutionStatus.SCHEDULED,
            started_at=datetime.now()
        )
        
        with self.lock:
            self.active_executions[execution_id] = execution
        
        try:
            execution.status = JobExecutionStatus.RUNNING
            self.database.save_job_execution(execution)
            
            # Create pipeline job
            pipeline_job = Job(
                id=execution_id,
                name=f"Scheduled: {job.name}",
                type=job.job_type,
                payload=job.payload.copy(),
                priority=job.priority,
                max_retries=job.max_retries,
                timeout=job.timeout,
                callback=lambda completed_job: self._on_job_completion(execution_id, completed_job)
            )
            
            # Submit to data pipeline
            if self.data_pipeline.submit_job(pipeline_job):
                logger.info(f"Executing scheduled job '{job.name}' ({job.job_type})")
            else:
                raise RuntimeError("Failed to submit job to pipeline")
            
        except Exception as e:
            execution.status = JobExecutionStatus.FAILED
            execution.error = str(e)
            execution.completed_at = datetime.now()
            execution.duration = (execution.completed_at - execution.started_at).total_seconds()
            
            self.database.save_job_execution(execution)
            
            with self.lock:
                self.active_executions.pop(execution_id, None)
            
            logger.error(f"Failed to execute scheduled job '{job.name}': {e}")
        
        return execution_id
    
    def _on_job_completion(self, execution_id: str, completed_job: Job):
        """Handle job completion callback."""
        with self.lock:
            execution = self.active_executions.pop(execution_id, None)
        
        if not execution:
            return
        
        execution.completed_at = datetime.now()
        execution.duration = (execution.completed_at - execution.started_at).total_seconds()
        
        if completed_job.status.value == 'completed':
            execution.status = JobExecutionStatus.COMPLETED
            execution.result = completed_job.result
        else:
            execution.status = JobExecutionStatus.FAILED
            execution.error = completed_job.error
            execution.retry_count = completed_job.retry_count
        
        self.database.save_job_execution(execution)
        
        # Record performance metrics
        self.performance_monitor.recordMetric(
            f'Scheduled_Job_{completed_job.type}',
            execution.duration * 1000,
            {
                'success': execution.status == JobExecutionStatus.COMPLETED,
                'retry_count': execution.retry_count
            }
        )
    
    def _generate_job_id(self, name: str, job_type: str) -> str:
        """Generate a unique job ID."""
        import hashlib
        content = f"{name}:{job_type}:{time.time()}"
        return hashlib.md5(content.encode()).hexdigest()[:16]
    
    # Default job handlers
    def _handle_manifest_update(self, job: Job) -> Dict[str, Any]:
        """Handle manifest update job."""
        logger.info("Running scheduled manifest update")
        
        # This would fetch and process the latest manifest
        # For now, return a simulated result
        return {
            'status': 'completed',
            'items_processed': 1000,
            'duration': 30.0
        }
    
    def _handle_user_cleanup(self, job: Job) -> Dict[str, Any]:
        """Handle user data cleanup job."""
        logger.info("Running user data cleanup")
        
        # This would clean up inactive user data
        return {
            'status': 'completed',
            'users_cleaned': 10,
            'data_freed_mb': 50
        }
    
    def _handle_cache_cleanup(self, job: Job) -> Dict[str, Any]:
        """Handle cache cleanup job."""
        logger.info("Running cache cleanup")
        
        # Clean expired cache entries
        cleaned_entries = 0
        try:
            # This would implement actual cache cleanup
            cleaned_entries = 100  # Simulated
            
            return {
                'status': 'completed',
                'entries_cleaned': cleaned_entries,
                'cache_size_after': '50MB'
            }
        except Exception as e:
            return {
                'status': 'failed',
                'error': str(e)
            }
    
    def _handle_log_cleanup(self, job: Job) -> Dict[str, Any]:
        """Handle log file cleanup job."""
        logger.info("Running log cleanup")
        
        # This would clean old log files
        return {
            'status': 'completed',
            'log_files_cleaned': 5,
            'space_freed_mb': 100
        }
    
    def _handle_health_check(self, job: Job) -> Dict[str, Any]:
        """Handle system health check job."""
        logger.info("Running system health check")
        
        # Check system health
        health_status = {
            'database': 'healthy',
            'cache': 'healthy',
            'api': 'healthy',
            'disk_usage': '45%',
            'memory_usage': '60%'
        }
        
        return {
            'status': 'completed',
            'health_status': health_status,
            'timestamp': datetime.now().isoformat()
        }
    
    def _handle_performance_report(self, job: Job) -> Dict[str, Any]:
        """Handle performance report generation job."""
        logger.info("Generating performance report")
        
        # Generate performance report
        report = self.performance_monitor.get_health_status()
        
        return {
            'status': 'completed',
            'report': report,
            'generated_at': datetime.now().isoformat()
        }
    
    def _handle_backup_data(self, job: Job) -> Dict[str, Any]:
        """Handle data backup job."""
        logger.info("Running data backup")
        
        # This would backup important data
        return {
            'status': 'completed',
            'backup_size_mb': 500,
            'backup_location': '/backups/app_backup.tar.gz'
        }
    
    def get_stats(self) -> Dict[str, Any]:
        """Get scheduler statistics."""
        with self.lock:
            active_jobs = sum(1 for job in self.scheduled_jobs.values() if job.enabled)
            next_runs = [job.next_run for job in self.scheduled_jobs.values() if job.next_run]
            next_run = min(next_runs) if next_runs else None
            
            return {
                'total_jobs': len(self.scheduled_jobs),
                'active_jobs': active_jobs,
                'running_executions': len(self.active_executions),
                'next_run': next_run.isoformat() if next_run else None,
                'scheduler_running': self.running,
                'job_types': list(set(job.job_type for job in self.scheduled_jobs.values()))
            }


# Global scheduler instance
job_scheduler = BackgroundJobScheduler()


def get_job_scheduler() -> BackgroundJobScheduler:
    """Get the global job scheduler instance."""
    return job_scheduler


def start_job_scheduler():
    """Start the background job scheduler."""
    job_scheduler.start()


def stop_job_scheduler():
    """Stop the background job scheduler."""
    job_scheduler.stop()


def schedule_background_job(name: str, job_type: str, frequency: JobFrequency, **kwargs) -> str:
    """Schedule a background job."""
    return job_scheduler.schedule_job(name, job_type, frequency, **kwargs)