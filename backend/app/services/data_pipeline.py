"""
Data pipeline service for processing manifest data, bulk operations, and ETL tasks.
Handles large-scale data processing with queuing, batching, and parallel execution.
"""

import time
import json
import logging
import threading
import hashlib
from typing import Dict, List, Any, Optional, Callable, Union
from dataclasses import dataclass, field
from collections import deque
from enum import Enum
import concurrent.futures

from ..config import config
from .cache_service import get_cache
from .performance_monitor import get_performance_monitor


logger = logging.getLogger(__name__)


class JobStatus(Enum):
    """Job execution statuses."""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    RETRYING = "retrying"


class JobPriority(Enum):
    """Job priority levels."""
    LOW = 1
    NORMAL = 2
    HIGH = 3
    CRITICAL = 4


@dataclass
class Job:
    """Represents a data processing job."""
    id: str
    name: str
    type: str
    payload: Dict[str, Any]
    priority: JobPriority = JobPriority.NORMAL
    status: JobStatus = JobStatus.PENDING
    created_at: float = field(default_factory=time.time)
    started_at: Optional[float] = None
    completed_at: Optional[float] = None
    error: Optional[str] = None
    result: Optional[Any] = None
    retry_count: int = 0
    max_retries: int = 3
    timeout: float = 300  # 5 minutes default
    callback: Optional[Callable] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Pipeline:
    """Represents a data processing pipeline."""
    id: str
    name: str
    steps: List[Dict[str, Any]]
    config: Dict[str, Any] = field(default_factory=dict)
    enabled: bool = True
    schedule: Optional[str] = None  # Cron-like schedule
    last_run: Optional[float] = None
    next_run: Optional[float] = None


class JobQueue:
    """Priority-based job queue with thread-safe operations."""
    
    def __init__(self, max_size: int = 10000):
        self.max_size = max_size
        self.queues = {
            JobPriority.CRITICAL: deque(),
            JobPriority.HIGH: deque(),
            JobPriority.NORMAL: deque(),
            JobPriority.LOW: deque()
        }
        self.lock = threading.RLock()
        self.condition = threading.Condition(self.lock)
        
        # Statistics
        self.stats = {
            'total_jobs': 0,
            'completed_jobs': 0,
            'failed_jobs': 0,
            'current_size': 0
        }
    
    def add_job(self, job: Job) -> bool:
        """Add a job to the appropriate priority queue."""
        with self.condition:
            if self.stats['current_size'] >= self.max_size:
                logger.warning(f"Job queue full, rejecting job: {job.id}")
                return False
            
            self.queues[job.priority].append(job)
            self.stats['total_jobs'] += 1
            self.stats['current_size'] += 1
            
            logger.debug(f"Added job {job.id} with priority {job.priority.name}")
            self.condition.notify()
            return True
    
    def get_job(self, timeout: float = None) -> Optional[Job]:
        """Get the next highest priority job."""
        with self.condition:
            # Wait for a job to be available
            if not self._has_jobs() and timeout is not None:
                self.condition.wait(timeout=timeout)
            
            # Get job from highest priority queue
            for priority in [JobPriority.CRITICAL, JobPriority.HIGH, JobPriority.NORMAL, JobPriority.LOW]:
                if self.queues[priority]:
                    job = self.queues[priority].popleft()
                    self.stats['current_size'] -= 1
                    return job
            
            return None
    
    def _has_jobs(self) -> bool:
        """Check if any jobs are available."""
        return any(queue for queue in self.queues.values())
    
    def get_stats(self) -> Dict[str, Any]:
        """Get queue statistics."""
        with self.lock:
            queue_sizes = {
                priority.name: len(queue) 
                for priority, queue in self.queues.items()
            }
            
            return {
                **self.stats,
                'queue_sizes': queue_sizes
            }


class ManifestProcessor:
    """Processes Destiny 2 manifest data."""
    
    def __init__(self):
        self.cache = get_cache()
        self.processed_hashes = set()
    
    def process_manifest_update(self, manifest_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process a manifest update."""
        logger.info("Processing manifest update")
        
        try:
            # Extract key data structures
            result = {
                'processed_items': 0,
                'new_items': 0,
                'updated_items': 0,
                'processing_time': 0
            }
            
            start_time = time.time()
            
            # Process different manifest tables
            if 'DestinyInventoryItemDefinition' in manifest_data:
                item_result = self._process_inventory_items(
                    manifest_data['DestinyInventoryItemDefinition']
                )
                result.update(item_result)
            
            if 'DestinyActivityDefinition' in manifest_data:
                activity_result = self._process_activities(
                    manifest_data['DestinyActivityDefinition']
                )
                result.update(activity_result)
            
            if 'DestinyClassDefinition' in manifest_data:
                class_result = self._process_classes(
                    manifest_data['DestinyClassDefinition']
                )
                result.update(class_result)
            
            result['processing_time'] = time.time() - start_time
            
            # Cache processed manifest
            self.cache.set(
                'processed_manifest', 
                result, 
                ttl=config.cache.manifest_ttl,
                tags=['manifest']
            )
            
            logger.info(f"Manifest processing completed in {result['processing_time']:.2f}s")
            return result
            
        except Exception as e:
            logger.error(f"Manifest processing failed: {e}")
            raise
    
    def _process_inventory_items(self, items: Dict[str, Any]) -> Dict[str, Any]:
        """Process inventory item definitions."""
        processed = 0
        new_items = 0
        updated_items = 0
        
        for item_hash, item_data in items.items():
            try:
                # Create searchable item data
                searchable_item = {
                    'hash': item_hash,
                    'name': item_data.get('displayProperties', {}).get('name', ''),
                    'description': item_data.get('displayProperties', {}).get('description', ''),
                    'type': item_data.get('itemTypeDisplayName', ''),
                    'tier': item_data.get('inventory', {}).get('tierTypeName', ''),
                    'category': item_data.get('itemCategoryHashes', []),
                    'tags': self._extract_item_tags(item_data),
                    'searchable_text': self._create_searchable_text(item_data)
                }
                
                # Check if item is new or updated
                cache_key = f"item:{item_hash}"
                existing_item = self.cache.get(cache_key)
                
                if not existing_item:
                    new_items += 1
                elif existing_item != searchable_item:
                    updated_items += 1
                
                # Cache the processed item
                self.cache.set(
                    cache_key, 
                    searchable_item, 
                    ttl=config.cache.manifest_ttl,
                    tags=['manifest', 'items']
                )
                
                processed += 1
                
            except Exception as e:
                logger.error(f"Error processing item {item_hash}: {e}")
        
        return {
            'items_processed': processed,
            'new_items': new_items,
            'updated_items': updated_items
        }
    
    def _process_activities(self, activities: Dict[str, Any]) -> Dict[str, Any]:
        """Process activity definitions."""
        processed = 0
        
        for activity_hash, activity_data in activities.items():
            try:
                # Process activity data
                searchable_activity = {
                    'hash': activity_hash,
                    'name': activity_data.get('displayProperties', {}).get('name', ''),
                    'description': activity_data.get('displayProperties', {}).get('description', ''),
                    'type': activity_data.get('activityTypeHash'),
                    'destination': activity_data.get('destinationHash'),
                    'place': activity_data.get('placeHash')
                }
                
                cache_key = f"activity:{activity_hash}"
                self.cache.set(
                    cache_key, 
                    searchable_activity, 
                    ttl=config.cache.manifest_ttl,
                    tags=['manifest', 'activities']
                )
                
                processed += 1
                
            except Exception as e:
                logger.error(f"Error processing activity {activity_hash}: {e}")
        
        return {'activities_processed': processed}
    
    def _process_classes(self, classes: Dict[str, Any]) -> Dict[str, Any]:
        """Process class definitions."""
        processed = 0
        
        for class_hash, class_data in classes.items():
            try:
                # Process class data
                searchable_class = {
                    'hash': class_hash,
                    'name': class_data.get('displayProperties', {}).get('name', ''),
                    'description': class_data.get('displayProperties', {}).get('description', ''),
                    'type': class_data.get('classType')
                }
                
                cache_key = f"class:{class_hash}"
                self.cache.set(
                    cache_key, 
                    searchable_class, 
                    ttl=config.cache.manifest_ttl,
                    tags=['manifest', 'classes']
                )
                
                processed += 1
                
            except Exception as e:
                logger.error(f"Error processing class {class_hash}: {e}")
        
        return {'classes_processed': processed}
    
    def _extract_item_tags(self, item_data: Dict[str, Any]) -> List[str]:
        """Extract searchable tags from item data."""
        tags = []
        
        # Add item type tags
        if 'itemType' in item_data:
            tags.append(f"type:{item_data['itemType']}")
        
        # Add tier tags
        tier = item_data.get('inventory', {}).get('tierTypeName', '')
        if tier:
            tags.append(f"tier:{tier.lower()}")
        
        # Add category tags
        categories = item_data.get('itemCategoryHashes', [])
        for category in categories:
            tags.append(f"category:{category}")
        
        # Add damage type tags
        damage_type = item_data.get('damageTypeHashes', [])
        for damage in damage_type:
            tags.append(f"damage:{damage}")
        
        return tags
    
    def _create_searchable_text(self, item_data: Dict[str, Any]) -> str:
        """Create searchable text index for item."""
        text_parts = []
        
        # Add name and description
        display_props = item_data.get('displayProperties', {})
        text_parts.append(display_props.get('name', ''))
        text_parts.append(display_props.get('description', ''))
        
        # Add type and tier information
        text_parts.append(item_data.get('itemTypeDisplayName', ''))
        text_parts.append(item_data.get('inventory', {}).get('tierTypeName', ''))
        
        # Add flavor text
        flavor_text = item_data.get('flavorText', '')
        if flavor_text:
            text_parts.append(flavor_text)
        
        return ' '.join(text_parts).lower()


class JobProcessor:
    """Processes jobs from the job queue."""
    
    def __init__(self, job_queue: JobQueue, max_workers: int = 4):
        self.job_queue = job_queue
        self.max_workers = max_workers
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=max_workers)
        self.active_jobs: Dict[str, Job] = {}
        self.completed_jobs: Dict[str, Job] = {}
        self.lock = threading.RLock()
        self.running = False
        self.worker_threads = []
        
        # Job handlers
        self.job_handlers = {
            'manifest_update': self._handle_manifest_update,
            'user_data_sync': self._handle_user_data_sync,
            'cache_warmup': self._handle_cache_warmup,
            'data_export': self._handle_data_export,
            'cleanup': self._handle_cleanup
        }
        
        # Manifest processor
        self.manifest_processor = ManifestProcessor()
    
    def start(self):
        """Start job processing."""
        if self.running:
            return
        
        self.running = True
        
        # Start worker threads
        for i in range(self.max_workers):
            worker = threading.Thread(target=self._worker_loop, daemon=True)
            worker.start()
            self.worker_threads.append(worker)
        
        logger.info(f"Job processor started with {self.max_workers} workers")
    
    def stop(self):
        """Stop job processing."""
        self.running = False
        
        # Shutdown executor
        self.executor.shutdown(wait=True)
        
        # Wait for worker threads
        for worker in self.worker_threads:
            worker.join(timeout=5)
        
        logger.info("Job processor stopped")
    
    def _worker_loop(self):
        """Main worker loop for processing jobs."""
        while self.running:
            try:
                # Get next job
                job = self.job_queue.get_job(timeout=1.0)
                if not job:
                    continue
                
                # Process the job
                self._process_job(job)
                
            except Exception as e:
                logger.error(f"Worker error: {e}")
                time.sleep(1)
    
    def _process_job(self, job: Job):
        """Process a single job."""
        job.status = JobStatus.RUNNING
        job.started_at = time.time()
        
        with self.lock:
            self.active_jobs[job.id] = job
        
        logger.info(f"Processing job {job.id} ({job.type})")
        
        try:
            # Get job handler
            handler = self.job_handlers.get(job.type)
            if not handler:
                raise ValueError(f"No handler for job type: {job.type}")
            
            # Execute job with timeout
            future = self.executor.submit(handler, job)
            result = future.result(timeout=job.timeout)
            
            # Job completed successfully
            job.status = JobStatus.COMPLETED
            job.completed_at = time.time()
            job.result = result
            
            self.job_queue.stats['completed_jobs'] += 1
            
            # Call callback if provided
            if job.callback:
                try:
                    job.callback(job)
                except Exception as e:
                    logger.error(f"Job callback error for {job.id}: {e}")
            
            logger.info(f"Job {job.id} completed in {job.completed_at - job.started_at:.2f}s")
            
        except concurrent.futures.TimeoutError:
            job.status = JobStatus.FAILED
            job.error = f"Job timed out after {job.timeout}s"
            self.job_queue.stats['failed_jobs'] += 1
            logger.error(f"Job {job.id} timed out")
            
        except Exception as e:
            job.status = JobStatus.FAILED
            job.error = str(e)
            self.job_queue.stats['failed_jobs'] += 1
            logger.error(f"Job {job.id} failed: {e}")
            
            # Retry logic
            if job.retry_count < job.max_retries:
                job.retry_count += 1
                job.status = JobStatus.RETRYING
                
                # Add back to queue for retry with exponential backoff
                retry_delay = 2 ** job.retry_count
                threading.Timer(retry_delay, lambda: self.job_queue.add_job(job)).start()
                
                logger.info(f"Job {job.id} will be retried in {retry_delay}s (attempt {job.retry_count + 1})")
        
        finally:
            # Move to completed jobs
            with self.lock:
                if job.id in self.active_jobs:
                    del self.active_jobs[job.id]
                self.completed_jobs[job.id] = job
                
                # Limit completed jobs history
                if len(self.completed_jobs) > 1000:
                    oldest_jobs = sorted(
                        self.completed_jobs.items(), 
                        key=lambda x: x[1].completed_at or 0
                    )[:100]
                    for old_job_id, _ in oldest_jobs:
                        del self.completed_jobs[old_job_id]
    
    def _handle_manifest_update(self, job: Job) -> Dict[str, Any]:
        """Handle manifest update job."""
        manifest_data = job.payload.get('manifest_data')
        if not manifest_data:
            raise ValueError("No manifest data provided")
        
        return self.manifest_processor.process_manifest_update(manifest_data)
    
    def _handle_user_data_sync(self, job: Job) -> Dict[str, Any]:
        """Handle user data synchronization job."""
        user_id = job.payload.get('user_id')
        if not user_id:
            raise ValueError("No user ID provided")
        
        # Simulate user data sync
        time.sleep(1)  # Simulate processing time
        
        return {
            'user_id': user_id,
            'synced_characters': 3,
            'synced_at': time.time()
        }
    
    def _handle_cache_warmup(self, job: Job) -> Dict[str, Any]:
        """Handle cache warmup job."""
        cache_keys = job.payload.get('cache_keys', [])
        
        warmed_count = 0
        for key in cache_keys:
            # Simulate cache warming
            time.sleep(0.1)
            warmed_count += 1
        
        return {
            'warmed_keys': warmed_count,
            'total_keys': len(cache_keys)
        }
    
    def _handle_data_export(self, job: Job) -> Dict[str, Any]:
        """Handle data export job."""
        export_type = job.payload.get('export_type')
        user_id = job.payload.get('user_id')
        
        # Simulate data export
        time.sleep(2)
        
        return {
            'export_type': export_type,
            'user_id': user_id,
            'file_size': 1024 * 1024,  # 1MB
            'exported_at': time.time()
        }
    
    def _handle_cleanup(self, job: Job) -> Dict[str, Any]:
        """Handle cleanup job."""
        cleanup_type = job.payload.get('cleanup_type', 'cache')
        
        if cleanup_type == 'cache':
            # Clean expired cache entries
            cache = get_cache()
            # This would implement actual cleanup logic
            cleaned_count = 10  # Simulated
            
        elif cleanup_type == 'logs':
            # Clean old log files
            cleaned_count = 5  # Simulated
            
        else:
            cleaned_count = 0
        
        return {
            'cleanup_type': cleanup_type,
            'cleaned_items': cleaned_count
        }
    
    def get_stats(self) -> Dict[str, Any]:
        """Get job processor statistics."""
        with self.lock:
            return {
                'active_jobs': len(self.active_jobs),
                'completed_jobs': len(self.completed_jobs),
                'worker_count': self.max_workers,
                'running': self.running,
                'queue_stats': self.job_queue.get_stats()
            }


class DataPipeline:
    """Main data pipeline orchestrator."""
    
    def __init__(self):
        self.job_queue = JobQueue()
        self.job_processor = JobProcessor(self.job_queue)
        self.pipelines: Dict[str, Pipeline] = {}
        self.scheduler_thread = None
        self.scheduling = False
    
    def start(self):
        """Start the data pipeline."""
        self.job_processor.start()
        self._start_scheduler()
        logger.info("Data pipeline started")
    
    def stop(self):
        """Stop the data pipeline."""
        self.job_processor.stop()
        self._stop_scheduler()
        logger.info("Data pipeline stopped")
    
    def submit_job(self, job: Job) -> bool:
        """Submit a job to the pipeline."""
        return self.job_queue.add_job(job)
    
    def create_job(self, name: str, job_type: str, payload: Dict[str, Any], 
                   priority: JobPriority = JobPriority.NORMAL, **kwargs) -> Job:
        """Create a new job."""
        job_id = self._generate_job_id(name, job_type)
        
        return Job(
            id=job_id,
            name=name,
            type=job_type,
            payload=payload,
            priority=priority,
            **kwargs
        )
    
    def schedule_manifest_update(self, manifest_data: Dict[str, Any]) -> str:
        """Schedule a manifest update job."""
        job = self.create_job(
            name="Manifest Update",
            job_type="manifest_update",
            payload={'manifest_data': manifest_data},
            priority=JobPriority.HIGH
        )
        
        if self.submit_job(job):
            return job.id
        else:
            raise RuntimeError("Failed to schedule manifest update job")
    
    def schedule_user_sync(self, user_id: str) -> str:
        """Schedule a user data sync job."""
        job = self.create_job(
            name=f"User Sync - {user_id}",
            job_type="user_data_sync",
            payload={'user_id': user_id},
            priority=JobPriority.NORMAL
        )
        
        if self.submit_job(job):
            return job.id
        else:
            raise RuntimeError("Failed to schedule user sync job")
    
    def schedule_cleanup(self, cleanup_type: str = 'cache') -> str:
        """Schedule a cleanup job."""
        job = self.create_job(
            name=f"Cleanup - {cleanup_type}",
            job_type="cleanup",
            payload={'cleanup_type': cleanup_type},
            priority=JobPriority.LOW
        )
        
        if self.submit_job(job):
            return job.id
        else:
            raise RuntimeError("Failed to schedule cleanup job")
    
    def _generate_job_id(self, name: str, job_type: str) -> str:
        """Generate a unique job ID."""
        timestamp = str(int(time.time() * 1000))
        content = f"{name}:{job_type}:{timestamp}"
        return hashlib.md5(content.encode()).hexdigest()[:16]
    
    def _start_scheduler(self):
        """Start the pipeline scheduler."""
        if self.scheduling:
            return
        
        self.scheduling = True
        self.scheduler_thread = threading.Thread(target=self._scheduler_loop, daemon=True)
        self.scheduler_thread.start()
    
    def _stop_scheduler(self):
        """Stop the pipeline scheduler."""
        self.scheduling = False
        if self.scheduler_thread:
            self.scheduler_thread.join(timeout=5)
    
    def _scheduler_loop(self):
        """Main scheduler loop."""
        while self.scheduling:
            try:
                # Check for scheduled pipelines
                current_time = time.time()
                
                for pipeline in self.pipelines.values():
                    if (pipeline.enabled and 
                        pipeline.next_run and 
                        current_time >= pipeline.next_run):
                        self._execute_pipeline(pipeline)
                
                time.sleep(60)  # Check every minute
                
            except Exception as e:
                logger.error(f"Scheduler error: {e}")
                time.sleep(60)
    
    def _execute_pipeline(self, pipeline: Pipeline):
        """Execute a scheduled pipeline."""
        logger.info(f"Executing pipeline: {pipeline.name}")
        
        try:
            for step in pipeline.steps:
                job = self.create_job(
                    name=f"{pipeline.name} - {step['name']}",
                    job_type=step['type'],
                    payload=step.get('payload', {}),
                    priority=JobPriority(step.get('priority', 2))
                )
                
                self.submit_job(job)
            
            pipeline.last_run = time.time()
            # Calculate next run time based on schedule
            # This would implement cron-like scheduling
            
        except Exception as e:
            logger.error(f"Pipeline execution error for {pipeline.name}: {e}")
    
    def get_comprehensive_stats(self) -> Dict[str, Any]:
        """Get comprehensive pipeline statistics."""
        processor_stats = self.job_processor.get_stats()
        
        return {
            'pipeline': {
                'running': self.scheduling,
                'registered_pipelines': len(self.pipelines)
            },
            'jobs': processor_stats,
            'performance': get_performance_monitor().get_health_status()
        }


# Global data pipeline instance
data_pipeline = DataPipeline()


def get_data_pipeline() -> DataPipeline:
    """Get the global data pipeline instance."""
    return data_pipeline


def start_data_pipeline():
    """Start the data pipeline services."""
    data_pipeline.start()


def stop_data_pipeline():
    """Stop the data pipeline services."""
    data_pipeline.stop()


def schedule_manifest_update(manifest_data: Dict[str, Any]) -> str:
    """Schedule a manifest update job."""
    return data_pipeline.schedule_manifest_update(manifest_data)


def schedule_user_sync(user_id: str) -> str:
    """Schedule a user data synchronization job."""
    return data_pipeline.schedule_user_sync(user_id)


def schedule_cleanup(cleanup_type: str = 'cache') -> str:
    """Schedule a cleanup job."""
    return data_pipeline.schedule_cleanup(cleanup_type)