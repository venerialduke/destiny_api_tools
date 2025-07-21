"""
Enhanced Manifest Service for downloading and processing ALL Destiny 2 definition tables.
"""

import os
import json
import sqlite3
import requests
import zipfile
import tempfile
from datetime import datetime
from typing import Dict, List, Any, Optional
from ..config import Config
# Import json flattening functions from local copy
from .json_flattener import extract_key_value_pairs, infer_values


class EnhancedManifestService:
    """Service for downloading, storing, and processing the complete Destiny 2 manifest."""
    
    def __init__(self):
        self.base_url = Config.BUNGIE_API_BASE_URL
        self.api_key = Config.BUNGIE_API_KEY
        self.data_dir = os.path.join('data')
        self.raw_json_dir = os.path.join(self.data_dir, 'manifest_raw')
        self.manifest_db_path = os.path.join(self.data_dir, 'manifest_complete.db')
        self.flattened_db_path = os.path.join(self.data_dir, 'manifest_flattened.db')
        
        # Ensure directories exist
        os.makedirs(self.data_dir, exist_ok=True)
        os.makedirs(self.raw_json_dir, exist_ok=True)
    
    def get_manifest_info(self) -> Dict[str, Any]:
        """Get manifest metadata from Bungie API."""
        headers = {
            'X-API-Key': self.api_key
        }
        
        response = requests.get(f"{self.base_url}/Destiny2/Manifest/", headers=headers)
        response.raise_for_status()
        
        return response.json()
    
    def download_all_manifest_tables(self) -> Dict[str, str]:
        """Download all available manifest definition tables."""
        print("Getting manifest metadata...")
        manifest_info = self.get_manifest_info()
        
        if 'Response' not in manifest_info:
            raise Exception("Invalid manifest response")
        
        response = manifest_info['Response']
        
        # Get JSON world component content paths (English) - individual definition tables
        if 'jsonWorldComponentContentPaths' not in response:
            raise Exception("No JSON component content paths found")
        
        component_paths = response['jsonWorldComponentContentPaths']
        if 'en' not in component_paths:
            raise Exception("English component content not found")
        
        en_paths = component_paths['en']
        print(f"Found {len(en_paths)} definition tables to download")
        
        downloaded_files = {}
        headers = {'X-API-Key': self.api_key}
        
        for table_name, url in en_paths.items():
            print(f"Downloading {table_name}...")
            
            try:
                # Download the JSON file
                full_url = f"https://www.bungie.net{url}"
                response = requests.get(full_url, headers=headers)
                response.raise_for_status()
                
                # Save raw JSON file
                raw_file_path = os.path.join(self.raw_json_dir, f"{table_name}.json")
                with open(raw_file_path, 'w', encoding='utf-8') as f:
                    f.write(response.text)
                
                downloaded_files[table_name] = raw_file_path
                print(f"  OK Saved {table_name} ({len(response.text):,} characters)")
                
            except Exception as e:
                print(f"  ERROR Failed to download {table_name}: {e}")
                continue
        
        print(f"\nDownload complete: {len(downloaded_files)} tables saved")
        return downloaded_files
    
    def create_complete_manifest_db(self, downloaded_files: Dict[str, str]) -> None:
        """Create complete manifest database with all tables in normalized format."""
        print("\nCreating complete manifest database...")
        
        # Remove existing database
        if os.path.exists(self.manifest_db_path):
            os.remove(self.manifest_db_path)
        
        conn = sqlite3.connect(self.manifest_db_path)
        cursor = conn.cursor()
        
        # Create metadata table
        cursor.execute('''
            CREATE TABLE manifest_metadata (
                key TEXT PRIMARY KEY,
                value TEXT,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Insert version info
        cursor.execute('''
            INSERT INTO manifest_metadata (key, value) 
            VALUES ('version', ?), ('downloaded_at', ?)
        ''', ('enhanced_' + datetime.now().strftime('%Y%m%d_%H%M%S'), datetime.now().isoformat()))
        
        total_records = 0
        
        for table_name, file_path in downloaded_files.items():
            print(f"Processing {table_name}...")
            
            try:
                # Load JSON data
                with open(file_path, 'r', encoding='utf-8') as f:
                    table_data = json.load(f)
                
                if not isinstance(table_data, dict):
                    print(f"  ✗ Skipping {table_name}: not a dictionary")
                    continue
                
                # Create table for this definition type
                # Use a normalized structure that can handle any definition type
                cursor.execute(f'''
                    CREATE TABLE {table_name} (
                        hash INTEGER PRIMARY KEY,
                        display_name TEXT,
                        description TEXT,
                        raw_json TEXT
                    )
                ''')
                
                # Insert records
                records_inserted = 0
                for hash_key, definition in table_data.items():
                    if not isinstance(definition, dict):
                        continue
                    
                    # Extract display properties if they exist
                    display_props = definition.get('displayProperties', {})
                    display_name = display_props.get('name', '') if isinstance(display_props, dict) else ''
                    description = display_props.get('description', '') if isinstance(display_props, dict) else ''
                    
                    # Store complete raw JSON
                    raw_json = json.dumps(definition)
                    
                    cursor.execute(f'''
                        INSERT INTO {table_name} (hash, display_name, description, raw_json)
                        VALUES (?, ?, ?, ?)
                    ''', (int(hash_key), display_name, description, raw_json))
                    
                    records_inserted += 1
                
                total_records += records_inserted
                print(f"  OK Created {table_name} with {records_inserted:,} records")
                
            except Exception as e:
                print(f"  ERROR Failed to process {table_name}: {e}")
                continue
        
        conn.commit()
        conn.close()
        
        print(f"\nComplete manifest database created: {total_records:,} total records")
    
    def create_flattened_database(self, downloaded_files: Dict[str, str]) -> None:
        """Create flattened database using json_row_structure functions."""
        print("\nCreating flattened manifest database...")
        
        # Remove existing flattened database
        if os.path.exists(self.flattened_db_path):
            os.remove(self.flattened_db_path)
        
        conn = sqlite3.connect(self.flattened_db_path)
        cursor = conn.cursor()
        
        # Create single flattened table
        cursor.execute('''
            CREATE TABLE manifest_flattened (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source_table TEXT NOT NULL,
                entity_hash INTEGER NOT NULL,
                entity_name TEXT,
                key_path TEXT NOT NULL,
                data_type TEXT NOT NULL,
                boolean_value INTEGER,
                numeric_value REAL,
                string_value TEXT,
                key_link TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Create indexes for efficient searching
        cursor.execute('CREATE INDEX idx_source_table ON manifest_flattened(source_table)')
        cursor.execute('CREATE INDEX idx_entity_hash ON manifest_flattened(entity_hash)')
        cursor.execute('CREATE INDEX idx_key_path ON manifest_flattened(key_path)')
        cursor.execute('CREATE INDEX idx_data_type ON manifest_flattened(data_type)')
        cursor.execute('CREATE INDEX idx_string_value ON manifest_flattened(string_value)')
        cursor.execute('CREATE INDEX idx_numeric_value ON manifest_flattened(numeric_value)')
        
        # Create metadata table
        cursor.execute('''
            CREATE TABLE flattened_metadata (
                key TEXT PRIMARY KEY,
                value TEXT,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        cursor.execute('''
            INSERT INTO flattened_metadata (key, value) 
            VALUES ('version', ?), ('created_at', ?)
        ''', ('flattened_' + datetime.now().strftime('%Y%m%d_%H%M%S'), datetime.now().isoformat()))
        
        total_flattened_records = 0
        
        for table_name, file_path in downloaded_files.items():
            print(f"Flattening {table_name}...")
            
            try:
                # Load JSON data
                with open(file_path, 'r', encoding='utf-8') as f:
                    table_data = json.load(f)
                
                if not isinstance(table_data, dict):
                    print(f"  ✗ Skipping {table_name}: not a dictionary")
                    continue
                
                table_records = 0
                
                for hash_key, definition in table_data.items():
                    if not isinstance(definition, dict):
                        continue
                    
                    entity_hash = int(hash_key)
                    
                    # Get entity name if available
                    display_props = definition.get('displayProperties', {})
                    entity_name = display_props.get('name', '') if isinstance(display_props, dict) else ''
                    
                    # Extract all key-value pairs using json_row_structure functions
                    try:
                        key_value_pairs = extract_key_value_pairs(definition)
                        
                        # Insert flattened records
                        for kvp in key_value_pairs:
                            cursor.execute('''
                                INSERT INTO manifest_flattened 
                                (source_table, entity_hash, entity_name, key_path, data_type, 
                                 boolean_value, numeric_value, string_value, key_link)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                            ''', (
                                table_name,
                                entity_hash,
                                entity_name,
                                kvp['key_link'].rstrip('.'),  # Remove trailing dot
                                kvp['data_type'],
                                kvp['boolean_value'],
                                kvp['numeric_value'],
                                kvp['string_value'],
                                kvp['key_link']
                            ))
                            
                            table_records += 1
                    
                    except Exception as e:
                        print(f"    Warning: Failed to flatten entity {hash_key}: {e}")
                        continue
                
                total_flattened_records += table_records
                print(f"  OK Flattened {table_name}: {table_records:,} key-value pairs")
                
            except Exception as e:
                print(f"  ERROR Failed to flatten {table_name}: {e}")
                continue
        
        conn.commit()
        conn.close()
        
        print(f"\nFlattened database created: {total_flattened_records:,} total key-value records")
    
    def update_manifest(self) -> bool:
        """Complete manifest update process."""
        try:
            print("=== ENHANCED MANIFEST UPDATE ===")
            print(f"Started at: {datetime.now()}")
            
            # Step 1: Download all manifest tables
            downloaded_files = self.download_all_manifest_tables()
            
            if not downloaded_files:
                print("No files downloaded. Aborting.")
                return False
            
            # Step 2: Create complete manifest database
            self.create_complete_manifest_db(downloaded_files)
            
            # Step 3: Create flattened database
            self.create_flattened_database(downloaded_files)
            
            print(f"\n=== UPDATE COMPLETE ===")
            print(f"Finished at: {datetime.now()}")
            print(f"Raw JSON files: {self.raw_json_dir}")
            print(f"Complete database: {self.manifest_db_path}")
            print(f"Flattened database: {self.flattened_db_path}")
            
            return True
            
        except Exception as e:
            print(f"Manifest update failed: {e}")
            return False
    
    def get_available_tables(self) -> List[str]:
        """Get list of available definition tables."""
        if not os.path.exists(self.manifest_db_path):
            return []
        
        conn = sqlite3.connect(self.manifest_db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name != 'manifest_metadata'")
        tables = [row[0] for row in cursor.fetchall()]
        
        conn.close()
        return sorted(tables)
    
    def get_flattened_stats(self) -> Dict[str, Any]:
        """Get statistics about the flattened database."""
        if not os.path.exists(self.flattened_db_path):
            return {}
        
        conn = sqlite3.connect(self.flattened_db_path)
        cursor = conn.cursor()
        
        # Total records
        cursor.execute("SELECT COUNT(*) FROM manifest_flattened")
        total_records = cursor.fetchone()[0]
        
        # Records by source table
        cursor.execute("""
            SELECT source_table, COUNT(*) as count 
            FROM manifest_flattened 
            GROUP BY source_table 
            ORDER BY count DESC
        """)
        table_stats = dict(cursor.fetchall())
        
        # Data type distribution
        cursor.execute("""
            SELECT data_type, COUNT(*) as count 
            FROM manifest_flattened 
            GROUP BY data_type
        """)
        type_stats = dict(cursor.fetchall())
        
        conn.close()
        
        return {
            'total_records': total_records,
            'table_distribution': table_stats,
            'type_distribution': type_stats
        }


if __name__ == "__main__":
    # Test the service
    service = EnhancedManifestService()
    success = service.update_manifest()
    
    if success:
        print("\n=== RESULTS ===")
        tables = service.get_available_tables()
        print(f"Available tables: {len(tables)}")
        for table in tables:
            print(f"  - {table}")
        
        stats = service.get_flattened_stats()
        print(f"\nFlattened database stats:")
        print(f"  Total records: {stats.get('total_records', 0):,}")
        print(f"  Tables: {len(stats.get('table_distribution', {}))}")
        print(f"  Data types: {list(stats.get('type_distribution', {}).keys())}")