"""
Destiny Manifest Service for downloading and managing game definition data.
"""

import os
import json
import requests
import sqlite3
from typing import Dict, Any, Optional, List
from datetime import datetime
import tempfile
import shutil
from ..config import Config
from .manifest_parser import ManifestParser


class ManifestService:
    """Service for managing Destiny 2 manifest data."""
    
    def __init__(self):
        """Initialize the manifest service."""
        self.manifest_url = f"{Config.BUNGIE_API_BASE_URL}/Destiny2/Manifest/"
        self.db_path = os.path.join('data', 'manifest.db')
        self.temp_db_path = os.path.join('data', 'manifest_temp.db')
        self.data_dir = 'data'
        self.parser = ManifestParser()
        
        # Ensure data directory exists
        os.makedirs(self.data_dir, exist_ok=True)
    
    def get_manifest_info(self) -> Dict[str, Any]:
        """Get current manifest information from Bungie API."""
        headers = Config.get_bungie_headers()
        
        response = requests.get(self.manifest_url, headers=headers)
        response.raise_for_status()
        
        manifest_data = response.json()
        
        if manifest_data.get('ErrorCode') != 1:
            raise Exception(f"Bungie API error: {manifest_data.get('Message', 'Unknown error')}")
        
        return manifest_data['Response']
    
    def get_current_version(self) -> Optional[str]:
        """Get the currently stored manifest version."""
        if not os.path.exists(self.db_path):
            return None
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT value FROM manifest_metadata WHERE key = ?", ('version',))
                result = cursor.fetchone()
                return result[0] if result else None
        except sqlite3.Error:
            return None
    
    def needs_update(self) -> bool:
        """Check if manifest needs to be updated."""
        try:
            remote_info = self.get_manifest_info()
            remote_version = remote_info.get('version')
            current_version = self.get_current_version()
            
            return remote_version != current_version
        except Exception as e:
            print(f"Error checking for manifest updates: {e}")
            return False
    
    def download_manifest(self, progress_callback=None) -> str:
        """
        Download the full manifest JSON file.
        
        Args:
            progress_callback: Optional function to call with download progress
            
        Returns:
            Path to the downloaded manifest file
        """
        manifest_info = self.get_manifest_info()
        
        # Get English manifest URL
        manifest_paths = manifest_info.get('jsonWorldContentPaths', {})
        if 'en' not in manifest_paths:
            raise Exception("English manifest not available")
        
        manifest_url = f"https://www.bungie.net{manifest_paths['en']}"
        
        # Download to temporary file
        temp_file = tempfile.NamedTemporaryFile(mode='wb', delete=False, suffix='.json')
        
        try:
            response = requests.get(manifest_url, stream=True)
            response.raise_for_status()
            
            total_size = int(response.headers.get('content-length', 0))
            downloaded = 0
            
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    temp_file.write(chunk)
                    downloaded += len(chunk)
                    
                    if progress_callback and total_size > 0:
                        progress = (downloaded / total_size) * 100
                        progress_callback(progress, downloaded, total_size)
            
            temp_file.close()
            return temp_file.name
            
        except Exception as e:
            temp_file.close()
            if os.path.exists(temp_file.name):
                os.unlink(temp_file.name)
            raise e
    
    def parse_manifest_file(self, manifest_file_path: str) -> Dict[str, Any]:
        """
        Parse downloaded manifest JSON file.
        
        Args:
            manifest_file_path: Path to downloaded manifest file
            
        Returns:
            Parsed manifest data
        """
        print(f"Parsing manifest file: {manifest_file_path}")
        
        with open(manifest_file_path, 'r', encoding='utf-8') as f:
            manifest_data = json.load(f)
        
        print(f"Loaded manifest with {len(manifest_data)} definition types")
        return manifest_data
    
    def update_manifest(self, progress_callback=None) -> bool:
        """
        Download and update the local manifest database.
        
        Args:
            progress_callback: Optional function to call with progress updates
            
        Returns:
            True if update was successful, False otherwise
        """
        try:
            print("Starting manifest update...")
            
            # Check if update is needed
            if not self.needs_update():
                print("Manifest is already up to date")
                return True
            
            # Get manifest info for version
            manifest_info = self.get_manifest_info()
            version = manifest_info.get('version')
            
            print(f"Downloading manifest version: {version}")
            
            # Download manifest
            manifest_file_path = self.download_manifest(progress_callback)
            
            try:
                # Parse manifest data
                manifest_data = self.parse_manifest_file(manifest_file_path)
                
                # Create new database
                from .database_service import DatabaseService
                db_service = DatabaseService(self.temp_db_path)
                
                # Initialize database schema
                db_service.initialize_database()
                
                # Populate database with manifest data
                self._populate_database(db_service, manifest_data, version)
                
                # Atomically replace old database
                if os.path.exists(self.db_path):
                    backup_path = f"{self.db_path}.backup"
                    shutil.move(self.db_path, backup_path)
                
                shutil.move(self.temp_db_path, self.db_path)
                
                # Clean up backup after successful update
                if os.path.exists(f"{self.db_path}.backup"):
                    os.remove(f"{self.db_path}.backup")
                
                print(f"Manifest updated successfully to version: {version}")
                return True
                
            finally:
                # Clean up downloaded file
                if os.path.exists(manifest_file_path):
                    os.unlink(manifest_file_path)
                
        except Exception as e:
            print(f"Error updating manifest: {e}")
            
            # Clean up temp database on error
            if os.path.exists(self.temp_db_path):
                os.remove(self.temp_db_path)
            
            return False
    
    def _populate_database(self, db_service, manifest_data: Dict[str, Any], version: str, progress_callback=None):
        """Populate database with manifest data using enhanced parser."""
        print("Populating database with manifest data...")
        
        # Store version metadata
        db_service.set_metadata('version', version)
        db_service.set_metadata('last_updated', datetime.utcnow().isoformat())
        
        # Use enhanced parser to process all manifest data
        def parser_progress_callback(percentage, completed, total):
            print(f"\rProcessing manifest data: {percentage:.1f}% ({completed:,}/{total:,})", end='', flush=True)
            if progress_callback:
                progress_callback(percentage, completed, total)
        
        processed_data = self.parser.process_manifest_data(manifest_data, parser_progress_callback)
        print("\nManifest data processed, inserting into database...")
        
        # Bulk insert all processed data
        if processed_data['items']:
            print(f"Inserting {len(processed_data['items']):,} items...")
            db_service.bulk_insert_items(processed_data['items'])
        
        if processed_data['activities']:
            print(f"Inserting {len(processed_data['activities']):,} activities...")
            db_service.bulk_insert_activities(processed_data['activities'])
        
        if processed_data['vendors']:
            print(f"Inserting {len(processed_data['vendors']):,} vendors...")
            db_service.bulk_insert_vendors(processed_data['vendors'])
        
        if processed_data['classes']:
            print(f"Inserting {len(processed_data['classes']):,} classes...")
            db_service.bulk_insert_classes(processed_data['classes'])
        
        if processed_data['races']:
            print(f"Inserting {len(processed_data['races']):,} races...")
            db_service.bulk_insert_races(processed_data['races'])
        
        if processed_data['damage_types']:
            print(f"Inserting {len(processed_data['damage_types']):,} damage types...")
            db_service.bulk_insert_damage_types(processed_data['damage_types'])
        
        print("Database population complete!")
    
    def _process_item_definitions(self, db_service, definitions: Dict[str, Any]):
        """Process inventory item definitions."""
        items = []
        
        for hash_str, item_data in definitions.items():
            hash_int = int(hash_str) & 0xFFFFFFFF  # Convert to unsigned 32-bit
            
            display_props = item_data.get('displayProperties', {})
            
            # Extract categorization data
            item_type = item_data.get('itemType', 0)
            item_sub_type = item_data.get('itemSubType', 0)
            tier_type = item_data.get('inventory', {}).get('tierType', 0)
            class_type = item_data.get('classType', 3)  # 3 = any class
            
            # Determine item category flags
            is_weapon = item_type == 3  # Weapon
            is_armor = item_type == 2   # Armor
            is_consumable = item_type == 9  # Consumable
            is_mod = item_type == 19    # Mod
            
            # Extract damage type for weapons
            damage_type = 0
            if is_weapon and 'defaultDamageType' in item_data:
                damage_type = item_data['defaultDamageType']
            
            # Build search text
            search_parts = [
                display_props.get('name', '').lower(),
                display_props.get('description', '').lower(),
                item_data.get('itemTypeDisplayName', '').lower(),
            ]
            search_text = ' '.join(filter(None, search_parts))
            
            items.append({
                'hash': hash_int,
                'display_name': display_props.get('name', ''),
                'description': display_props.get('description', ''),
                'icon': display_props.get('icon', ''),
                'item_type': item_type,
                'item_sub_type': item_sub_type,
                'tier_type': tier_type,
                'class_type': class_type,
                'damage_type': damage_type,
                'is_weapon': is_weapon,
                'is_armor': is_armor,
                'is_consumable': is_consumable,
                'is_mod': is_mod,
                'search_text': search_text,
                'raw_json': json.dumps(item_data)
            })
        
        db_service.bulk_insert_items(items)
    
    def _process_activity_definitions(self, db_service, definitions: Dict[str, Any]):
        """Process activity definitions."""
        activities = []
        
        for hash_str, activity_data in definitions.items():
            hash_int = int(hash_str) & 0xFFFFFFFF
            
            display_props = activity_data.get('displayProperties', {})
            
            activities.append({
                'hash': hash_int,
                'display_name': display_props.get('name', ''),
                'description': display_props.get('description', ''),
                'activity_type_hash': activity_data.get('activityTypeHash', 0),
                'raw_json': json.dumps(activity_data)
            })
        
        db_service.bulk_insert_activities(activities)
    
    def _process_vendor_definitions(self, db_service, definitions: Dict[str, Any]):
        """Process vendor definitions."""
        vendors = []
        
        for hash_str, vendor_data in definitions.items():
            hash_int = int(hash_str) & 0xFFFFFFFF
            
            display_props = vendor_data.get('displayProperties', {})
            
            vendors.append({
                'hash': hash_int,
                'display_name': display_props.get('name', ''),
                'description': display_props.get('description', ''),
                'icon': display_props.get('icon', ''),
                'enabled': vendor_data.get('enabled', False),
                'raw_json': json.dumps(vendor_data)
            })
        
        db_service.bulk_insert_vendors(vendors)
    
    def _process_class_definitions(self, db_service, definitions: Dict[str, Any]):
        """Process class definitions."""
        classes = []
        
        for hash_str, class_data in definitions.items():
            hash_int = int(hash_str) & 0xFFFFFFFF
            
            display_props = class_data.get('displayProperties', {})
            
            classes.append({
                'hash': hash_int,
                'class_type': class_data.get('classType', 0),
                'display_name': display_props.get('name', ''),
                'description': display_props.get('description', ''),
                'icon': display_props.get('icon', ''),
                'raw_json': json.dumps(class_data)
            })
        
        db_service.bulk_insert_classes(classes)
    
    def _process_race_definitions(self, db_service, definitions: Dict[str, Any]):
        """Process race definitions."""
        races = []
        
        for hash_str, race_data in definitions.items():
            hash_int = int(hash_str) & 0xFFFFFFFF
            
            display_props = race_data.get('displayProperties', {})
            
            races.append({
                'hash': hash_int,
                'race_type': race_data.get('raceType', 0),
                'display_name': display_props.get('name', ''),
                'description': display_props.get('description', ''),
                'icon': display_props.get('icon', ''),
                'raw_json': json.dumps(race_data)
            })
        
        db_service.bulk_insert_races(races)
    
    def _process_damage_type_definitions(self, db_service, definitions: Dict[str, Any]):
        """Process damage type definitions."""
        damage_types = []
        
        for hash_str, damage_data in definitions.items():
            hash_int = int(hash_str) & 0xFFFFFFFF
            
            display_props = damage_data.get('displayProperties', {})
            
            damage_types.append({
                'hash': hash_int,
                'damage_type': damage_data.get('enumValue', 0),
                'display_name': display_props.get('name', ''),
                'description': display_props.get('description', ''),
                'icon': display_props.get('icon', ''),
                'color': damage_data.get('color', {}),
                'raw_json': json.dumps(damage_data)
            })
        
        db_service.bulk_insert_damage_types(damage_types)
    
    def get_database_stats(self) -> Dict[str, Any]:
        """Get statistics about the manifest database."""
        if not os.path.exists(self.db_path):
            return {'status': 'no_database'}
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Get version and last update
                cursor.execute("SELECT key, value FROM manifest_metadata WHERE key IN ('version', 'last_updated')")
                metadata = dict(cursor.fetchall())
                
                # Get table counts
                tables = [
                    'destiny_inventory_item_definition',
                    'destiny_activity_definition', 
                    'destiny_vendor_definition',
                    'destiny_class_definition',
                    'destiny_race_definition',
                    'destiny_damage_type_definition'
                ]
                
                table_counts = {}
                for table in tables:
                    cursor.execute(f"SELECT COUNT(*) FROM {table}")
                    table_counts[table] = cursor.fetchone()[0]
                
                # Get database file size
                file_size = os.path.getsize(self.db_path)
                
                return {
                    'status': 'ready',
                    'version': metadata.get('version', 'unknown'),
                    'last_updated': metadata.get('last_updated', 'unknown'),
                    'file_size_mb': round(file_size / (1024 * 1024), 2),
                    'table_counts': table_counts,
                    'total_definitions': sum(table_counts.values())
                }
                
        except sqlite3.Error as e:
            return {'status': 'error', 'error': str(e)}