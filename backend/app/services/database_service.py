"""
Database service for managing SQLite manifest storage.
"""

import sqlite3
import os
from typing import List, Dict, Any, Optional
from contextlib import contextmanager


class DatabaseService:
    """Service for SQLite database operations."""
    
    def __init__(self, db_path: str):
        """Initialize database service with path."""
        self.db_path = db_path
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    @contextmanager
    def get_connection(self):
        """Get database connection with automatic cleanup."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Enable dict-like access
        try:
            yield conn
        finally:
            conn.close()
    
    def initialize_database(self):
        """Create database schema."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # Create metadata table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS manifest_metadata (
                    key TEXT PRIMARY KEY,
                    value TEXT NOT NULL,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Create inventory item definition table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS destiny_inventory_item_definition (
                    hash INTEGER PRIMARY KEY,
                    display_name TEXT,
                    description TEXT,
                    icon TEXT,
                    item_type INTEGER,
                    item_sub_type INTEGER,
                    tier_type INTEGER,
                    class_type INTEGER,
                    damage_type INTEGER,
                    is_weapon BOOLEAN DEFAULT FALSE,
                    is_armor BOOLEAN DEFAULT FALSE,
                    is_consumable BOOLEAN DEFAULT FALSE,
                    is_mod BOOLEAN DEFAULT FALSE,
                    is_emblem BOOLEAN DEFAULT FALSE,
                    is_ghost BOOLEAN DEFAULT FALSE,
                    is_ship BOOLEAN DEFAULT FALSE,
                    is_sparrow BOOLEAN DEFAULT FALSE,
                    is_emote BOOLEAN DEFAULT FALSE,
                    is_shader BOOLEAN DEFAULT FALSE,
                    is_ornament BOOLEAN DEFAULT FALSE,
                    power_cap INTEGER,
                    default_damage_type INTEGER,
                    ammo_type INTEGER,
                    search_text TEXT,
                    raw_json TEXT
                )
            ''')
            
            # Create activity definition table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS destiny_activity_definition (
                    hash INTEGER PRIMARY KEY,
                    display_name TEXT,
                    description TEXT,
                    activity_type_hash INTEGER,
                    playlist_items TEXT,
                    modifiers TEXT,
                    is_pvp BOOLEAN DEFAULT FALSE,
                    is_pve BOOLEAN DEFAULT TRUE,
                    difficulty_tier INTEGER DEFAULT 0,
                    raw_json TEXT
                )
            ''')
            
            # Create vendor definition table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS destiny_vendor_definition (
                    hash INTEGER PRIMARY KEY,
                    display_name TEXT,
                    description TEXT,
                    icon TEXT,
                    vendor_banner TEXT,
                    enabled BOOLEAN DEFAULT FALSE,
                    vendor_category_hash INTEGER,
                    location_hash INTEGER,
                    raw_json TEXT
                )
            ''')
            
            # Create class definition table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS destiny_class_definition (
                    hash INTEGER PRIMARY KEY,
                    class_type INTEGER,
                    display_name TEXT,
                    description TEXT,
                    icon TEXT,
                    raw_json TEXT
                )
            ''')
            
            # Create race definition table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS destiny_race_definition (
                    hash INTEGER PRIMARY KEY,
                    race_type INTEGER,
                    display_name TEXT,
                    description TEXT,
                    icon TEXT,
                    raw_json TEXT
                )
            ''')
            
            # Create damage type definition table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS destiny_damage_type_definition (
                    hash INTEGER PRIMARY KEY,
                    damage_type INTEGER,
                    display_name TEXT,
                    description TEXT,
                    icon TEXT,
                    color TEXT,
                    raw_json TEXT
                )
            ''')
            
            # Create Full-Text Search virtual table
            cursor.execute('''
                CREATE VIRTUAL TABLE IF NOT EXISTS item_search_fts USING fts5(
                    hash,
                    display_name,
                    description,
                    search_text,
                    content='destiny_inventory_item_definition',
                    content_rowid='hash'
                )
            ''')
            
            # Create indexes for performance
            indexes = [
                'CREATE INDEX IF NOT EXISTS idx_item_type ON destiny_inventory_item_definition(item_type)',
                'CREATE INDEX IF NOT EXISTS idx_tier_type ON destiny_inventory_item_definition(tier_type)',
                'CREATE INDEX IF NOT EXISTS idx_class_type ON destiny_inventory_item_definition(class_type)',
                'CREATE INDEX IF NOT EXISTS idx_is_weapon ON destiny_inventory_item_definition(is_weapon)',
                'CREATE INDEX IF NOT EXISTS idx_is_armor ON destiny_inventory_item_definition(is_armor)',
                'CREATE INDEX IF NOT EXISTS idx_is_consumable ON destiny_inventory_item_definition(is_consumable)',
                'CREATE INDEX IF NOT EXISTS idx_is_mod ON destiny_inventory_item_definition(is_mod)',
                'CREATE INDEX IF NOT EXISTS idx_is_emblem ON destiny_inventory_item_definition(is_emblem)',
                'CREATE INDEX IF NOT EXISTS idx_is_ghost ON destiny_inventory_item_definition(is_ghost)',
                'CREATE INDEX IF NOT EXISTS idx_search_text ON destiny_inventory_item_definition(search_text)',
                'CREATE INDEX IF NOT EXISTS idx_display_name ON destiny_inventory_item_definition(display_name)',
                'CREATE INDEX IF NOT EXISTS idx_damage_type ON destiny_inventory_item_definition(damage_type)',
                'CREATE INDEX IF NOT EXISTS idx_power_cap ON destiny_inventory_item_definition(power_cap)',
                'CREATE INDEX IF NOT EXISTS idx_activity_type ON destiny_activity_definition(activity_type_hash)',
                'CREATE INDEX IF NOT EXISTS idx_activity_pvp ON destiny_activity_definition(is_pvp)',
                'CREATE INDEX IF NOT EXISTS idx_vendor_enabled ON destiny_vendor_definition(enabled)',
                'CREATE INDEX IF NOT EXISTS idx_vendor_category ON destiny_vendor_definition(vendor_category_hash)',
                # Composite indexes for common query patterns
                'CREATE INDEX IF NOT EXISTS idx_item_filter_composite ON destiny_inventory_item_definition(item_type, tier_type, class_type)',
                'CREATE INDEX IF NOT EXISTS idx_weapon_composite ON destiny_inventory_item_definition(is_weapon, tier_type, damage_type)',
                'CREATE INDEX IF NOT EXISTS idx_armor_composite ON destiny_inventory_item_definition(is_armor, tier_type, class_type)',
            ]
            
            for index_sql in indexes:
                cursor.execute(index_sql)
            
            conn.commit()
    
    def set_metadata(self, key: str, value: str):
        """Set metadata key-value pair."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT OR REPLACE INTO manifest_metadata (key, value, updated_at)
                VALUES (?, ?, datetime('now'))
            ''', (key, value))
            conn.commit()
    
    def get_metadata(self, key: str) -> Optional[str]:
        """Get metadata value by key."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT value FROM manifest_metadata WHERE key = ?', (key,))
            result = cursor.fetchone()
            return result['value'] if result else None
    
    def bulk_insert_items(self, items: List[Dict[str, Any]]):
        """Bulk insert inventory item definitions."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute('DELETE FROM destiny_inventory_item_definition')  # Clear existing data
            
            insert_sql = '''
                INSERT INTO destiny_inventory_item_definition (
                    hash, display_name, description, icon, item_type, item_sub_type,
                    tier_type, class_type, damage_type, is_weapon, is_armor, 
                    is_consumable, is_mod, is_emblem, is_ghost, is_ship, is_sparrow,
                    is_emote, is_shader, is_ornament, power_cap, default_damage_type,
                    ammo_type, search_text, raw_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            '''
            
            # Convert items to tuples for insertion
            item_tuples = []
            for item in items:
                item_tuples.append((
                    item['hash'],
                    item['display_name'],
                    item['description'],
                    item['icon'],
                    item['item_type'],
                    item['item_sub_type'],
                    item['tier_type'],
                    item['class_type'],
                    item['damage_type'],
                    item['is_weapon'],
                    item['is_armor'],
                    item['is_consumable'],
                    item['is_mod'],
                    item.get('is_emblem', False),
                    item.get('is_ghost', False),
                    item.get('is_ship', False),
                    item.get('is_sparrow', False),
                    item.get('is_emote', False),
                    item.get('is_shader', False),
                    item.get('is_ornament', False),
                    item.get('power_cap'),
                    item.get('default_damage_type'),
                    item.get('ammo_type'),
                    item['search_text'],
                    item['raw_json']
                ))
            
            cursor.executemany(insert_sql, item_tuples)
            
            # Rebuild FTS index after bulk insert
            cursor.execute('INSERT INTO item_search_fts(item_search_fts) VALUES("rebuild")')
            
            conn.commit()
    
    def bulk_insert_activities(self, activities: List[Dict[str, Any]]):
        """Bulk insert activity definitions."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute('DELETE FROM destiny_activity_definition')
            
            insert_sql = '''
                INSERT INTO destiny_activity_definition (
                    hash, display_name, description, activity_type_hash, playlist_items,
                    modifiers, is_pvp, is_pve, difficulty_tier, raw_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            '''
            
            activity_tuples = []
            for activity in activities:
                activity_tuples.append((
                    activity['hash'],
                    activity['display_name'],
                    activity['description'],
                    activity['activity_type_hash'],
                    activity.get('playlist_items', '[]'),
                    activity.get('modifiers', '[]'),
                    activity.get('is_pvp', False),
                    activity.get('is_pve', True),
                    activity.get('difficulty_tier', 0),
                    activity['raw_json']
                ))
            
            cursor.executemany(insert_sql, activity_tuples)
            conn.commit()
    
    def bulk_insert_vendors(self, vendors: List[Dict[str, Any]]):
        """Bulk insert vendor definitions."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute('DELETE FROM destiny_vendor_definition')
            
            insert_sql = '''
                INSERT INTO destiny_vendor_definition (
                    hash, display_name, description, icon, vendor_banner, enabled,
                    vendor_category_hash, location_hash, raw_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            '''
            
            vendor_tuples = []
            for vendor in vendors:
                vendor_tuples.append((
                    vendor['hash'],
                    vendor['display_name'],
                    vendor['description'],
                    vendor['icon'],
                    vendor.get('vendor_banner', ''),
                    vendor['enabled'],
                    vendor.get('vendor_category_hash', 0),
                    vendor.get('location_hash', 0),
                    vendor['raw_json']
                ))
            
            cursor.executemany(insert_sql, vendor_tuples)
            conn.commit()
    
    def bulk_insert_classes(self, classes: List[Dict[str, Any]]):
        """Bulk insert class definitions."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute('DELETE FROM destiny_class_definition')
            
            insert_sql = '''
                INSERT INTO destiny_class_definition (
                    hash, class_type, display_name, description, icon, raw_json
                ) VALUES (?, ?, ?, ?, ?, ?)
            '''
            
            class_tuples = []
            for class_def in classes:
                class_tuples.append((
                    class_def['hash'],
                    class_def['class_type'],
                    class_def['display_name'],
                    class_def['description'],
                    class_def['icon'],
                    class_def['raw_json']
                ))
            
            cursor.executemany(insert_sql, class_tuples)
            conn.commit()
    
    def bulk_insert_races(self, races: List[Dict[str, Any]]):
        """Bulk insert race definitions."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute('DELETE FROM destiny_race_definition')
            
            insert_sql = '''
                INSERT INTO destiny_race_definition (
                    hash, race_type, display_name, description, icon, raw_json
                ) VALUES (?, ?, ?, ?, ?, ?)
            '''
            
            race_tuples = []
            for race in races:
                race_tuples.append((
                    race['hash'],
                    race['race_type'],
                    race['display_name'],
                    race['description'],
                    race['icon'],
                    race['raw_json']
                ))
            
            cursor.executemany(insert_sql, race_tuples)
            conn.commit()
    
    def bulk_insert_damage_types(self, damage_types: List[Dict[str, Any]]):
        """Bulk insert damage type definitions."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute('DELETE FROM destiny_damage_type_definition')
            
            insert_sql = '''
                INSERT INTO destiny_damage_type_definition (
                    hash, damage_type, display_name, description, icon, color, raw_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            '''
            
            damage_type_tuples = []
            for damage_type in damage_types:
                damage_type_tuples.append((
                    damage_type['hash'],
                    damage_type['damage_type'],
                    damage_type['display_name'],
                    damage_type['description'],
                    damage_type['icon'],
                    str(damage_type['color']),  # Convert dict to string
                    damage_type['raw_json']
                ))
            
            cursor.executemany(insert_sql, damage_type_tuples)
            conn.commit()
    
    def get_item_by_hash(self, item_hash: int, include_raw: bool = False) -> Optional[Dict[str, Any]]:
        """Get item definition by hash."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            if include_raw:
                cursor.execute('''
                    SELECT * FROM destiny_inventory_item_definition WHERE hash = ?
                ''', (item_hash,))
            else:
                cursor.execute('''
                    SELECT hash, display_name, description, icon, item_type, item_sub_type,
                           tier_type, class_type, damage_type, is_weapon, is_armor,
                           is_consumable, is_mod
                    FROM destiny_inventory_item_definition WHERE hash = ?
                ''', (item_hash,))
            
            result = cursor.fetchone()
            return dict(result) if result else None
    
    def search_items_fts(self, query: str, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
        """Search items using Full-Text Search for better performance and relevance."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # Use FTS5 for fast text search
            fts_sql = '''
                SELECT d.hash, d.display_name, d.description, d.icon, d.item_type, d.tier_type,
                       d.class_type, d.damage_type, d.is_weapon, d.is_armor
                FROM item_search_fts f
                JOIN destiny_inventory_item_definition d ON f.hash = d.hash
                WHERE item_search_fts MATCH ?
                ORDER BY rank
                LIMIT ? OFFSET ?
            '''
            
            cursor.execute(fts_sql, (query, limit, offset))
            results = [dict(row) for row in cursor.fetchall()]
            
            # Get total count for FTS search
            count_sql = '''
                SELECT COUNT(*) FROM item_search_fts WHERE item_search_fts MATCH ?
            '''
            cursor.execute(count_sql, (query,))
            total_count = cursor.fetchone()[0]
            
            return {
                'items': results,
                'total': total_count,
                'has_more': (offset + limit) < total_count
            }
    
    def search_items(self, query: str = '', item_type: int = None, tier_type: int = None, 
                    class_type: int = None, is_weapon: bool = None, is_armor: bool = None,
                    is_consumable: bool = None, is_mod: bool = None, is_emblem: bool = None,
                    is_ghost: bool = None, is_ship: bool = None, is_sparrow: bool = None,
                    is_emote: bool = None, is_shader: bool = None, is_ornament: bool = None,
                    damage_type: int = None, power_cap_min: int = None, power_cap_max: int = None,
                    limit: int = 50, offset: int = 0) -> Dict[str, Any]:
        """Enhanced search with multiple filters and FTS optimization."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # Skip FTS for now - use regular search for all queries
            # Note: FTS table not available, using LIKE search instead
            
            # Build WHERE clause for complex queries
            where_conditions = []
            params = []
            
            if query:
                where_conditions.append('search_text LIKE ?')
                params.append(f'%{query.lower()}%')
            
            if item_type is not None:
                where_conditions.append('item_type = ?')
                params.append(item_type)
            
            if tier_type is not None:
                where_conditions.append('tier_type = ?')
                params.append(tier_type)
            
            if class_type is not None:
                where_conditions.append('class_type = ?')
                params.append(class_type)
            
            if damage_type is not None:
                where_conditions.append('damage_type = ?')
                params.append(damage_type)
            
            if is_weapon is not None:
                where_conditions.append('is_weapon = ?')
                params.append(is_weapon)
            
            if is_armor is not None:
                where_conditions.append('is_armor = ?')
                params.append(is_armor)
            
            if is_consumable is not None:
                where_conditions.append('is_consumable = ?')
                params.append(is_consumable)
            
            if is_mod is not None:
                where_conditions.append('is_mod = ?')
                params.append(is_mod)
            
            if is_emblem is not None:
                where_conditions.append('is_emblem = ?')
                params.append(is_emblem)
            
            if is_ghost is not None:
                where_conditions.append('is_ghost = ?')
                params.append(is_ghost)
            
            if is_ship is not None:
                where_conditions.append('is_ship = ?')
                params.append(is_ship)
            
            if is_sparrow is not None:
                where_conditions.append('is_sparrow = ?')
                params.append(is_sparrow)
            
            if is_emote is not None:
                where_conditions.append('is_emote = ?')
                params.append(is_emote)
            
            if is_shader is not None:
                where_conditions.append('is_shader = ?')
                params.append(is_shader)
            
            if is_ornament is not None:
                where_conditions.append('is_ornament = ?')
                params.append(is_ornament)
            
            if power_cap_min is not None:
                where_conditions.append('power_cap >= ?')
                params.append(power_cap_min)
            
            if power_cap_max is not None:
                where_conditions.append('power_cap <= ?')
                params.append(power_cap_max)
            
            where_clause = 'WHERE ' + ' AND '.join(where_conditions) if where_conditions else ''
            
            # Add pagination
            params.extend([limit, offset])
            
            sql = f'''
                SELECT hash, display_name, description, icon, item_type, tier_type,
                       class_type, damage_type, is_weapon, is_armor
                FROM destiny_inventory_item_definition
                {where_clause}
                ORDER BY tier_type DESC, display_name
                LIMIT ? OFFSET ?
            '''
            
            cursor.execute(sql, params)
            results = [dict(row) for row in cursor.fetchall()]
            
            # Get total count
            count_sql = f'''
                SELECT COUNT(*) FROM destiny_inventory_item_definition {where_clause}
            '''
            cursor.execute(count_sql, params[:-2])  # Remove limit/offset params
            total_count = cursor.fetchone()[0]
            
            return {
                'items': results,
                'total': total_count,
                'has_more': (offset + limit) < total_count
            }
    
    def get_class_name(self, class_type: int) -> str:
        """Get class name by type."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT display_name FROM destiny_class_definition WHERE class_type = ?
            ''', (class_type,))
            result = cursor.fetchone()
            return result['display_name'] if result else 'Unknown'
    
    def get_race_name(self, race_type: int) -> str:
        """Get race name by type."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT display_name FROM destiny_race_definition WHERE race_type = ?
            ''', (race_type,))
            result = cursor.fetchone()
            return result['display_name'] if result else 'Unknown'
    
    def get_damage_type_info(self, damage_type: int) -> Dict[str, Any]:
        """Get damage type information."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT display_name, icon, color FROM destiny_damage_type_definition 
                WHERE damage_type = ?
            ''', (damage_type,))
            result = cursor.fetchone()
            if result:
                return {
                    'name': result['display_name'],
                    'icon': result['icon'],
                    'color': result['color']
                }
            return {'name': 'Kinetic', 'icon': '', 'color': '{}'}