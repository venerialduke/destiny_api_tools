"""
Service for processing and serving Destiny 2 Equipable Item Sets data.
Combines data from DestinyEquipableItemSetDefinition, DestinyInventoryItemDefinition, 
and DestinySandboxPerkDefinition to create rich set information.
"""

import sqlite3
import json
import os
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from ..config import Config


@dataclass
class ArmorPiece:
    """Represents an individual armor piece in a set."""
    hash: int
    name: str
    description: str
    icon: str
    item_type: str
    item_sub_type: str
    class_type: int
    class_name: str
    tier_type: int


@dataclass 
class SetPerk:
    """Represents a set perk with required count."""
    required_count: int
    hash: int
    name: str
    description: str
    icon: str
    is_displayable: bool


@dataclass
class EquipableSet:
    """Complete equipable set with items and perks."""
    hash: int
    name: str
    description: str
    icon: Optional[str]
    has_icon: bool
    armor_pieces: List[ArmorPiece]
    set_perks: List[SetPerk]
    class_type: int
    class_name: str
    total_pieces: int


class EquipableSetsService:
    """Service for retrieving and processing equipable sets data."""
    
    def __init__(self):
        # Use absolute path to root data directory
        # From backend/app/services/ go up to project root
        root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
        self.data_dir = os.path.join(root_dir, 'data')
        self.complete_db_path = os.path.join(self.data_dir, 'manifest_complete.db')
        
        # Class type mappings
        self.class_types = {
            0: "Titan",
            1: "Hunter", 
            2: "Warlock",
            3: "Unknown"
        }
        
        # Item sub type mappings for armor
        self.armor_sub_types = {
            26: "Helmet",
            27: "Gauntlets", 
            28: "Chest Armor",
            29: "Leg Armor",
            30: "Class Armor"
        }

    def get_all_sets(self, class_filter: Optional[int] = None) -> List[EquipableSet]:
        """Get all equipable sets, optionally filtered by class type."""
        if not os.path.exists(self.complete_db_path):
            return []
            
        conn = sqlite3.connect(self.complete_db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        try:
            # Get all equipable sets
            cursor.execute("""
                SELECT hash, display_name, description, raw_json
                FROM DestinyEquipableItemSetDefinition
                WHERE display_name != '' AND display_name IS NOT NULL
            """)
            
            rows = cursor.fetchall()
            
            sets = []
            for row in rows:
                try:
                    raw_data = json.loads(row['raw_json'])
                    processed_set = self._process_set_data(cursor, row['hash'], raw_data)
                    
                    if processed_set and (class_filter is None or processed_set.class_type == class_filter):
                        sets.append(processed_set)
                        
                except Exception as e:
                    print(f"Error processing set {row['hash']}: {e}")
                    continue
            return sorted(sets, key=lambda s: s.name)
            
        finally:
            conn.close()
    
    def get_set_by_hash(self, set_hash: int) -> Optional[EquipableSet]:
        """Get a specific equipable set by hash."""
        if not os.path.exists(self.complete_db_path):
            return None
            
        conn = sqlite3.connect(self.complete_db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                SELECT hash, display_name, description, raw_json
                FROM DestinyEquipableItemSetDefinition
                WHERE hash = ?
            """, (set_hash,))
            
            row = cursor.fetchone()
            if not row:
                return None
                
            raw_data = json.loads(row['raw_json'])
            return self._process_set_data(cursor, row['hash'], raw_data)
            
        except Exception as e:
            print(f"Error retrieving set {set_hash}: {e}")
            return None
        finally:
            conn.close()
    
    def _process_set_data(self, cursor, set_hash: int, raw_data: Dict) -> Optional[EquipableSet]:
        """Process raw set data into EquipableSet object."""
        try:
            display_props = raw_data.get('displayProperties', {})
            set_items = raw_data.get('setItems', [])
            set_perks_data = raw_data.get('setPerks', [])
            
            if not set_items:  # Skip sets with no items
                return None
            
            # Process armor pieces
            armor_pieces = []
            set_class_type = None
            
            for item_hash in set_items:
                armor_piece = self._get_armor_piece(cursor, item_hash)
                if armor_piece:
                    armor_pieces.append(armor_piece)
                    # Determine set class from first armor piece
                    if set_class_type is None:
                        set_class_type = armor_piece.class_type
            
            if not armor_pieces or set_class_type is None:
                return None
            
            # Process set perks
            set_perks = []
            for perk_data in set_perks_data:
                perk = self._get_set_perk(cursor, perk_data)
                if perk:
                    set_perks.append(perk)
            
            # Create equipable set
            return EquipableSet(
                hash=set_hash,
                name=display_props.get('name', 'Unknown Set'),
                description=display_props.get('description', ''),
                icon=display_props.get('icon', None),
                has_icon=display_props.get('hasIcon', False),
                armor_pieces=armor_pieces,
                set_perks=sorted(set_perks, key=lambda p: p.required_count),
                class_type=set_class_type,
                class_name=self.class_types.get(set_class_type, 'Unknown'),
                total_pieces=len(armor_pieces)
            )
            
        except Exception as e:
            print(f"Error processing set data for {set_hash}: {e}")
            return None
    
    def _get_armor_piece(self, cursor, item_hash: int) -> Optional[ArmorPiece]:
        """Get armor piece details from DestinyInventoryItemDefinition."""
        try:
            cursor.execute("""
                SELECT hash, display_name, description, raw_json
                FROM DestinyInventoryItemDefinition
                WHERE hash = ?
            """, (item_hash,))
            
            row = cursor.fetchone()
            if not row:
                return None
                
            raw_data = json.loads(row['raw_json'])
            display_props = raw_data.get('displayProperties', {})
            
            # Extract relevant fields
            item_type = raw_data.get('itemType', 0)
            item_sub_type = raw_data.get('itemSubType', 0) 
            class_type = raw_data.get('classType', 3)
            tier_type = raw_data.get('inventory', {}).get('tierType', 0)
            
            # Only process armor items
            if item_type != 2:  # itemType 2 = Armor
                return None
                
            return ArmorPiece(
                hash=item_hash,
                name=display_props.get('name', 'Unknown Item'),
                description=display_props.get('description', ''),
                icon=display_props.get('icon', ''),
                item_type='Armor',
                item_sub_type=self.armor_sub_types.get(item_sub_type, 'Unknown'),
                class_type=class_type,
                class_name=self.class_types.get(class_type, 'Unknown'),
                tier_type=tier_type
            )
            
        except Exception as e:
            print(f"Error getting armor piece {item_hash}: {e}")
            return None
    
    def _get_set_perk(self, cursor, perk_data: Dict) -> Optional[SetPerk]:
        """Get set perk details from DestinySandboxPerkDefinition."""
        try:
            required_count = perk_data.get('requiredSetCount', 0)
            perk_hash = perk_data.get('sandboxPerkHash', 0)
            
            if not perk_hash:
                return None
                
            cursor.execute("""
                SELECT hash, display_name, description, raw_json
                FROM DestinySandboxPerkDefinition
                WHERE hash = ?
            """, (perk_hash,))
            
            row = cursor.fetchone()
            if not row:
                return None
                
            raw_data = json.loads(row['raw_json'])
            display_props = raw_data.get('displayProperties', {})
            is_displayable = raw_data.get('isDisplayable', False)
            
            # Skip non-displayable perks
            if not is_displayable:
                return None
                
            return SetPerk(
                required_count=required_count,
                hash=perk_hash,
                name=display_props.get('name', 'Unknown Perk'),
                description=display_props.get('description', ''),
                icon=display_props.get('icon', ''),
                is_displayable=is_displayable
            )
            
        except Exception as e:
            print(f"Error getting set perk {perk_data}: {e}")
            return None
    
    def get_sets_summary(self) -> Dict[str, Any]:
        """Get summary statistics about equipable sets."""
        sets = self.get_all_sets()
        
        class_counts = {}
        total_perks = 0
        sets_with_perks = 0
        
        for equipable_set in sets:
            class_name = equipable_set.class_name
            class_counts[class_name] = class_counts.get(class_name, 0) + 1
            
            if equipable_set.set_perks:
                sets_with_perks += 1
                total_perks += len(equipable_set.set_perks)
        
        return {
            'total_sets': len(sets),
            'sets_by_class': class_counts,
            'sets_with_perks': sets_with_perks,
            'total_perks': total_perks,
            'average_perks_per_set': round(total_perks / max(sets_with_perks, 1), 2)
        }


# Create singleton instance
equipable_sets_service = EquipableSetsService()