"""
WebSocket manager for real-time data synchronization and live updates.
Provides bidirectional communication for character data, inventory changes, and activity updates.
"""

import json
import time
import asyncio
import logging
import threading
from typing import Dict, List, Set, Any, Optional, Callable
from dataclasses import dataclass, field
from collections import defaultdict
from enum import Enum

from ..config import config
from .cache_service import get_cache
from .performance_monitor import get_performance_monitor


logger = logging.getLogger(__name__)


class MessageType(Enum):
    """WebSocket message types for different data channels."""
    HEARTBEAT = "heartbeat"
    SUBSCRIBE = "subscribe"
    UNSUBSCRIBE = "unsubscribe"
    CHARACTER_UPDATE = "character_update"
    INVENTORY_UPDATE = "inventory_update"
    ACTIVITY_UPDATE = "activity_update"
    MANIFEST_UPDATE = "manifest_update"
    ERROR = "error"
    NOTIFICATION = "notification"


@dataclass
class WebSocketMessage:
    """Represents a WebSocket message."""
    type: str
    payload: Dict[str, Any]
    timestamp: float = field(default_factory=time.time)
    id: Optional[str] = None
    user_id: Optional[str] = None
    channel: Optional[str] = None


@dataclass
class WebSocketClient:
    """Represents a connected WebSocket client."""
    id: str
    user_id: Optional[str]
    subscriptions: Set[str] = field(default_factory=set)
    last_heartbeat: float = field(default_factory=time.time)
    metadata: Dict[str, Any] = field(default_factory=dict)
    connected_at: float = field(default_factory=time.time)


class SubscriptionManager:
    """Manages client subscriptions to different data channels."""
    
    def __init__(self):
        # Channel -> Set of client IDs
        self.channel_subscribers: Dict[str, Set[str]] = defaultdict(set)
        # Client ID -> Set of channels
        self.client_subscriptions: Dict[str, Set[str]] = defaultdict(set)
        self.lock = threading.RLock()
    
    def subscribe(self, client_id: str, channel: str) -> bool:
        """Subscribe a client to a channel."""
        with self.lock:
            self.channel_subscribers[channel].add(client_id)
            self.client_subscriptions[client_id].add(channel)
            logger.debug(f"Client {client_id} subscribed to {channel}")
            return True
    
    def unsubscribe(self, client_id: str, channel: str) -> bool:
        """Unsubscribe a client from a channel."""
        with self.lock:
            self.channel_subscribers[channel].discard(client_id)
            self.client_subscriptions[client_id].discard(channel)
            logger.debug(f"Client {client_id} unsubscribed from {channel}")
            return True
    
    def unsubscribe_all(self, client_id: str) -> Set[str]:
        """Unsubscribe a client from all channels."""
        with self.lock:
            channels = self.client_subscriptions[client_id].copy()
            for channel in channels:
                self.channel_subscribers[channel].discard(client_id)
            del self.client_subscriptions[client_id]
            logger.debug(f"Client {client_id} unsubscribed from all channels")
            return channels
    
    def get_subscribers(self, channel: str) -> Set[str]:
        """Get all subscribers for a channel."""
        with self.lock:
            return self.channel_subscribers[channel].copy()
    
    def get_subscriptions(self, client_id: str) -> Set[str]:
        """Get all subscriptions for a client."""
        with self.lock:
            return self.client_subscriptions[client_id].copy()
    
    def get_stats(self) -> Dict[str, Any]:
        """Get subscription statistics."""
        with self.lock:
            return {
                'total_channels': len(self.channel_subscribers),
                'total_subscriptions': sum(len(subs) for subs in self.channel_subscribers.values()),
                'channels': {
                    channel: len(subscribers) 
                    for channel, subscribers in self.channel_subscribers.items()
                }
            }


class DataSynchronizer:
    """Handles data synchronization and change detection."""
    
    def __init__(self, websocket_manager):
        self.websocket_manager = websocket_manager
        self.cache = get_cache()
        self.last_sync_times: Dict[str, float] = {}
        self.sync_intervals = {
            'character_data': 30,  # 30 seconds
            'inventory_data': 60,  # 1 minute
            'activity_data': 15,   # 15 seconds
            'manifest_data': 3600  # 1 hour
        }
        self.lock = threading.RLock()
        self.running = False
        self.sync_thread = None
    
    def start_sync(self):
        """Start the data synchronization background process."""
        if self.running:
            return
        
        self.running = True
        self.sync_thread = threading.Thread(target=self._sync_loop, daemon=True)
        self.sync_thread.start()
        logger.info("Data synchronization started")
    
    def stop_sync(self):
        """Stop the data synchronization process."""
        self.running = False
        if self.sync_thread:
            self.sync_thread.join(timeout=5)
        logger.info("Data synchronization stopped")
    
    def _sync_loop(self):
        """Main synchronization loop."""
        while self.running:
            try:
                current_time = time.time()
                
                # Check each data type for sync
                for data_type, interval in self.sync_intervals.items():
                    last_sync = self.last_sync_times.get(data_type, 0)
                    if current_time - last_sync >= interval:
                        self._sync_data_type(data_type)
                        self.last_sync_times[data_type] = current_time
                
                # Sleep for 5 seconds before next check
                time.sleep(5)
                
            except Exception as e:
                logger.error(f"Sync loop error: {e}")
                time.sleep(10)  # Wait longer on error
    
    def _sync_data_type(self, data_type: str):
        """Synchronize a specific type of data."""
        try:
            if data_type == 'character_data':
                self._sync_character_data()
            elif data_type == 'inventory_data':
                self._sync_inventory_data()
            elif data_type == 'activity_data':
                self._sync_activity_data()
            elif data_type == 'manifest_data':
                self._sync_manifest_data()
                
        except Exception as e:
            logger.error(f"Error syncing {data_type}: {e}")
    
    def _sync_character_data(self):
        """Sync character data for active users."""
        # Get users with character subscriptions
        subscribers = self.websocket_manager.subscription_manager.get_subscribers('character_updates')
        
        for client_id in subscribers:
            client = self.websocket_manager.clients.get(client_id)
            if client and client.user_id:
                # Fetch fresh character data and compare with cached
                self._check_character_changes(client.user_id)
    
    def _sync_inventory_data(self):
        """Sync inventory data for active users."""
        subscribers = self.websocket_manager.subscription_manager.get_subscribers('inventory_updates')
        
        for client_id in subscribers:
            client = self.websocket_manager.clients.get(client_id)
            if client and client.user_id:
                self._check_inventory_changes(client.user_id)
    
    def _sync_activity_data(self):
        """Sync activity data for active users."""
        subscribers = self.websocket_manager.subscription_manager.get_subscribers('activity_updates')
        
        for client_id in subscribers:
            client = self.websocket_manager.clients.get(client_id)
            if client and client.user_id:
                self._check_activity_changes(client.user_id)
    
    def _sync_manifest_data(self):
        """Check for manifest updates."""
        # This would check for new manifest versions
        # For now, simulate a periodic check
        logger.debug("Checking for manifest updates")
        
        # If manifest updated, notify all subscribers
        subscribers = self.websocket_manager.subscription_manager.get_subscribers('manifest_updates')
        if subscribers:
            message = WebSocketMessage(
                type=MessageType.MANIFEST_UPDATE.value,
                payload={'status': 'checked', 'updated': False}
            )
            self.websocket_manager.broadcast_to_subscribers('manifest_updates', message)
    
    def _check_character_changes(self, user_id: str):
        """Check for character data changes."""
        try:
            # This would fetch current character data and compare with cached version
            # For now, simulate character data changes
            cache_key = f"character_sync:{user_id}"
            last_data = self.cache.get(cache_key)
            
            # Simulate new character data
            current_data = {
                'user_id': user_id,
                'characters': [
                    {
                        'character_id': '123456',
                        'light_level': 1800 + int(time.time()) % 10,  # Simulate light level changes
                        'last_played': time.time(),
                        'location': 'Tower'
                    }
                ],
                'timestamp': time.time()
            }
            
            # Check if data changed
            if last_data != current_data:
                self.cache.set(cache_key, current_data, ttl=300)
                
                # Notify subscribers
                message = WebSocketMessage(
                    type=MessageType.CHARACTER_UPDATE.value,
                    payload=current_data,
                    user_id=user_id
                )
                self.websocket_manager.send_to_user(user_id, message)
                
        except Exception as e:
            logger.error(f"Error checking character changes for {user_id}: {e}")
    
    def _check_inventory_changes(self, user_id: str):
        """Check for inventory changes."""
        # Similar implementation for inventory data
        logger.debug(f"Checking inventory changes for {user_id}")
    
    def _check_activity_changes(self, user_id: str):
        """Check for activity status changes."""
        # Similar implementation for activity data
        logger.debug(f"Checking activity changes for {user_id}")


class WebSocketManager:
    """Main WebSocket manager for handling real-time connections."""
    
    def __init__(self):
        self.clients: Dict[str, WebSocketClient] = {}
        self.subscription_manager = SubscriptionManager()
        self.data_synchronizer = DataSynchronizer(self)
        self.message_handlers: Dict[str, Callable] = {}
        self.lock = threading.RLock()
        
        # Statistics
        self.stats = {
            'total_connections': 0,
            'active_connections': 0,
            'messages_sent': 0,
            'messages_received': 0,
            'errors': 0
        }
        
        # Setup default message handlers
        self._setup_default_handlers()
        
        # Heartbeat monitoring
        self.heartbeat_interval = 30  # 30 seconds
        self.heartbeat_thread = None
        self.monitoring_heartbeats = False
    
    def _setup_default_handlers(self):
        """Setup default message handlers."""
        self.message_handlers = {
            MessageType.HEARTBEAT.value: self._handle_heartbeat,
            MessageType.SUBSCRIBE.value: self._handle_subscribe,
            MessageType.UNSUBSCRIBE.value: self._handle_unsubscribe,
        }
    
    def add_client(self, client_id: str, user_id: Optional[str] = None, metadata: Dict = None) -> WebSocketClient:
        """Add a new WebSocket client."""
        with self.lock:
            client = WebSocketClient(
                id=client_id,
                user_id=user_id,
                metadata=metadata or {}
            )
            self.clients[client_id] = client
            self.stats['total_connections'] += 1
            self.stats['active_connections'] += 1
            
            logger.info(f"WebSocket client connected: {client_id} (user: {user_id})")
            return client
    
    def remove_client(self, client_id: str) -> bool:
        """Remove a WebSocket client."""
        with self.lock:
            if client_id in self.clients:
                # Unsubscribe from all channels
                self.subscription_manager.unsubscribe_all(client_id)
                
                # Remove client
                del self.clients[client_id]
                self.stats['active_connections'] -= 1
                
                logger.info(f"WebSocket client disconnected: {client_id}")
                return True
            return False
    
    def handle_message(self, client_id: str, message_data: str) -> bool:
        """Handle incoming WebSocket message."""
        try:
            # Parse message
            data = json.loads(message_data)
            message = WebSocketMessage(
                type=data.get('type'),
                payload=data.get('payload', {}),
                id=data.get('id'),
                channel=data.get('channel')
            )
            
            self.stats['messages_received'] += 1
            
            # Get message handler
            handler = self.message_handlers.get(message.type)
            if handler:
                return handler(client_id, message)
            else:
                logger.warning(f"No handler for message type: {message.type}")
                self._send_error(client_id, f"Unknown message type: {message.type}")
                return False
                
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON from client {client_id}: {e}")
            self._send_error(client_id, "Invalid JSON format")
            return False
        except Exception as e:
            logger.error(f"Error handling message from {client_id}: {e}")
            self._send_error(client_id, "Message processing error")
            self.stats['errors'] += 1
            return False
    
    def send_message(self, client_id: str, message: WebSocketMessage) -> bool:
        """Send a message to a specific client."""
        try:
            client = self.clients.get(client_id)
            if not client:
                return False
            
            # Format message for transmission
            data = {
                'type': message.type,
                'payload': message.payload,
                'timestamp': message.timestamp
            }
            
            if message.id:
                data['id'] = message.id
            if message.channel:
                data['channel'] = message.channel
            
            # This would be implemented by the actual WebSocket library
            # For now, we'll just log the message
            logger.debug(f"Sending message to {client_id}: {message.type}")
            
            self.stats['messages_sent'] += 1
            return True
            
        except Exception as e:
            logger.error(f"Error sending message to {client_id}: {e}")
            self.stats['errors'] += 1
            return False
    
    def send_to_user(self, user_id: str, message: WebSocketMessage) -> int:
        """Send a message to all clients for a specific user."""
        sent_count = 0
        
        with self.lock:
            for client in self.clients.values():
                if client.user_id == user_id:
                    if self.send_message(client.id, message):
                        sent_count += 1
        
        return sent_count
    
    def broadcast_to_subscribers(self, channel: str, message: WebSocketMessage) -> int:
        """Broadcast a message to all subscribers of a channel."""
        subscribers = self.subscription_manager.get_subscribers(channel)
        sent_count = 0
        
        for client_id in subscribers:
            if self.send_message(client_id, message):
                sent_count += 1
        
        return sent_count
    
    def broadcast_to_all(self, message: WebSocketMessage) -> int:
        """Broadcast a message to all connected clients."""
        sent_count = 0
        
        with self.lock:
            for client_id in self.clients:
                if self.send_message(client_id, message):
                    sent_count += 1
        
        return sent_count
    
    def _handle_heartbeat(self, client_id: str, message: WebSocketMessage) -> bool:
        """Handle heartbeat message."""
        with self.lock:
            client = self.clients.get(client_id)
            if client:
                client.last_heartbeat = time.time()
                
                # Send heartbeat response
                response = WebSocketMessage(
                    type=MessageType.HEARTBEAT.value,
                    payload={'status': 'alive', 'server_time': time.time()}
                )
                return self.send_message(client_id, response)
        return False
    
    def _handle_subscribe(self, client_id: str, message: WebSocketMessage) -> bool:
        """Handle subscription request."""
        channel = message.payload.get('channel')
        if not channel:
            self._send_error(client_id, "Channel required for subscription")
            return False
        
        success = self.subscription_manager.subscribe(client_id, channel)
        
        # Send confirmation
        response = WebSocketMessage(
            type=MessageType.SUBSCRIBE.value,
            payload={'channel': channel, 'subscribed': success}
        )
        return self.send_message(client_id, response)
    
    def _handle_unsubscribe(self, client_id: str, message: WebSocketMessage) -> bool:
        """Handle unsubscription request."""
        channel = message.payload.get('channel')
        if not channel:
            self._send_error(client_id, "Channel required for unsubscription")
            return False
        
        success = self.subscription_manager.unsubscribe(client_id, channel)
        
        # Send confirmation
        response = WebSocketMessage(
            type=MessageType.UNSUBSCRIBE.value,
            payload={'channel': channel, 'unsubscribed': success}
        )
        return self.send_message(client_id, response)
    
    def _send_error(self, client_id: str, error_message: str):
        """Send an error message to a client."""
        error_msg = WebSocketMessage(
            type=MessageType.ERROR.value,
            payload={'error': error_message}
        )
        self.send_message(client_id, error_msg)
    
    def start_heartbeat_monitoring(self):
        """Start heartbeat monitoring for client health."""
        if self.monitoring_heartbeats:
            return
        
        self.monitoring_heartbeats = True
        self.heartbeat_thread = threading.Thread(target=self._heartbeat_monitor, daemon=True)
        self.heartbeat_thread.start()
        logger.info("WebSocket heartbeat monitoring started")
    
    def stop_heartbeat_monitoring(self):
        """Stop heartbeat monitoring."""
        self.monitoring_heartbeats = False
        if self.heartbeat_thread:
            self.heartbeat_thread.join(timeout=5)
        logger.info("WebSocket heartbeat monitoring stopped")
    
    def _heartbeat_monitor(self):
        """Monitor client heartbeats and remove stale connections."""
        while self.monitoring_heartbeats:
            try:
                current_time = time.time()
                stale_clients = []
                
                with self.lock:
                    for client_id, client in self.clients.items():
                        if current_time - client.last_heartbeat > self.heartbeat_interval * 2:
                            stale_clients.append(client_id)
                
                # Remove stale clients
                for client_id in stale_clients:
                    logger.warning(f"Removing stale WebSocket client: {client_id}")
                    self.remove_client(client_id)
                
                time.sleep(self.heartbeat_interval)
                
            except Exception as e:
                logger.error(f"Heartbeat monitor error: {e}")
                time.sleep(10)
    
    def get_stats(self) -> Dict[str, Any]:
        """Get WebSocket manager statistics."""
        with self.lock:
            subscription_stats = self.subscription_manager.get_stats()
            
            return {
                **self.stats,
                'subscriptions': subscription_stats,
                'clients': {
                    'total': len(self.clients),
                    'by_user': len(set(c.user_id for c in self.clients.values() if c.user_id))
                }
            }
    
    def start(self):
        """Start all WebSocket services."""
        self.start_heartbeat_monitoring()
        self.data_synchronizer.start_sync()
        logger.info("WebSocket manager started")
    
    def stop(self):
        """Stop all WebSocket services."""
        self.stop_heartbeat_monitoring()
        self.data_synchronizer.stop_sync()
        
        # Disconnect all clients
        with self.lock:
            client_ids = list(self.clients.keys())
            for client_id in client_ids:
                self.remove_client(client_id)
        
        logger.info("WebSocket manager stopped")


# Global WebSocket manager instance
websocket_manager = WebSocketManager()


def get_websocket_manager() -> WebSocketManager:
    """Get the global WebSocket manager instance."""
    return websocket_manager


def start_websocket_services():
    """Start WebSocket services."""
    websocket_manager.start()


def stop_websocket_services():
    """Stop WebSocket services."""
    websocket_manager.stop()


def notify_character_update(user_id: str, character_data: Dict[str, Any]):
    """Notify clients of character data updates."""
    message = WebSocketMessage(
        type=MessageType.CHARACTER_UPDATE.value,
        payload=character_data,
        user_id=user_id
    )
    return websocket_manager.send_to_user(user_id, message)


def notify_inventory_update(user_id: str, inventory_data: Dict[str, Any]):
    """Notify clients of inventory updates."""
    message = WebSocketMessage(
        type=MessageType.INVENTORY_UPDATE.value,
        payload=inventory_data,
        user_id=user_id
    )
    return websocket_manager.send_to_user(user_id, message)


def broadcast_notification(notification: Dict[str, Any], channel: str = None):
    """Broadcast a notification to all clients or specific channel."""
    message = WebSocketMessage(
        type=MessageType.NOTIFICATION.value,
        payload=notification
    )
    
    if channel:
        return websocket_manager.broadcast_to_subscribers(channel, message)
    else:
        return websocket_manager.broadcast_to_all(message)