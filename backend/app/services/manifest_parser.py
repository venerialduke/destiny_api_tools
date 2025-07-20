"""
Enhanced manifest parser for data processing and enrichment.
"""

import json
import re
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime


class ManifestParser:
    """Enhanced parser for processing manifest data with relationship mapping."""
    
    def __init__(self):
        """Initialize parser with processing configurations."""
        self.item_type_mappings = {
            0: 'None',
            1: 'Currency',
            2: 'Armor',
            3: 'Weapon',
            7: 'Message',
            8: 'Emblem',
            9: 'Consumable',
            10: 'ExchangeMaterial',
            11: 'MissionReward',
            12: 'QuestStep',
            13: 'QuestStepComplete',
            14: 'Emblem',
            15: 'Subclass',
            16: 'ClanBanner',
            17: 'Aura',
            18: 'Mod',
            19: 'Dummy',
            20: 'Ship',
            21: 'Vehicle',
            22: 'Emote',
            23: 'Ghost',
            24: 'Package',
            25: 'Bounty',
            26: 'Wrapper',
            27: 'SeasonalArtifact',
            28: 'Finisher',
            29: 'Pattern'
        }
        
        self.tier_type_mappings = {
            0: 'Unknown',
            1: 'Currency',
            2: 'Basic',
            3: 'Common',
            4: 'Rare',
            5: 'Superior',
            6: 'Exotic'
        }
        
        self.class_type_mappings = {
            0: 'Titan',
            1: 'Hunter', 
            2: 'Warlock',
            3: 'Any'
        }
        
        self.damage_type_mappings = {
            0: 'None',
            1: 'Kinetic',
            2: 'Arc',
            3: 'Solar',
            4: 'Void',
            5: 'Raid',
            6: 'Stasis',
            7: 'Strand'
        }
        
        # Track relationships for enhanced data
        self.perk_relationships = {}
        self.socket_relationships = {}
        self.activity_relationships = {}
    
    def clean_text(self, text: str) -> str:
        """Clean and normalize text for search."""
        if not text:
            return ""
        
        # Remove HTML tags
        text = re.sub(r'<[^>]+>', '', text)
        
        # Remove special characters but keep alphanumeric and basic punctuation
        text = re.sub(r'[^\w\s\-\.\,\!\?]', ' ', text)
        
        # Normalize whitespace
        text = re.sub(r'\s+', ' ', text)
        
        return text.strip()
    
    def build_search_text(self, item_data: Dict[str, Any]) -> str:
        """Build optimized search text for full-text search."""
        search_parts = []
        
        # Display properties
        display_props = item_data.get('displayProperties', {})
        name = display_props.get('name', '')
        description = display_props.get('description', '')
        
        if name:
            search_parts.append(name)
        if description:
            search_parts.append(description)
        
        # Item type name
        item_type = item_data.get('itemType', 0)
        if item_type in self.item_type_mappings:
            search_parts.append(self.item_type_mappings[item_type])
        
        # Tier type name
        tier_type = item_data.get('inventory', {}).get('tierType', 0)
        if tier_type in self.tier_type_mappings:
            search_parts.append(self.tier_type_mappings[tier_type])
        
        # Class type name
        class_type = item_data.get('classType', 3)
        if class_type in self.class_type_mappings:
            search_parts.append(self.class_type_mappings[class_type])
        
        # Damage type name
        damage_type = item_data.get('defaultDamageType', 0)
        if damage_type in self.damage_type_mappings:
            search_parts.append(self.damage_type_mappings[damage_type])
        
        # Socket perks and traits (if available)
        sockets = item_data.get('sockets', {})
        socket_entries = sockets.get('socketEntries', [])
        for socket_entry in socket_entries:
            # This would need perk definitions to be fully implemented
            # For now, we'll skip this to avoid circular dependencies
            pass
        
        # Combine and clean
        combined_text = ' '.join(search_parts)
        return self.clean_text(combined_text).lower()
    
    def categorize_item(self, item_data: Dict[str, Any]) -> Dict[str, bool]:
        """Categorize item into different types."""
        item_type = item_data.get('itemType', 0)
        item_sub_type = item_data.get('itemSubType', 0)
        
        categories = {
            'is_weapon': item_type == 3,
            'is_armor': item_type == 2,
            'is_consumable': item_type == 9,
            'is_mod': item_type == 18,
            'is_emblem': item_type == 14,
            'is_ghost': item_type == 23,
            'is_ship': item_type == 20,
            'is_sparrow': item_type == 21,
            'is_emote': item_type == 22,
            'is_shader': False,  # Shaders are typically item_type 2 with specific sub_type
            'is_ornament': False  # Ornaments need special detection
        }
        
        # Special cases for shaders and ornaments
        if item_type == 2 and item_sub_type == 20:  # Shader
            categories['is_shader'] = True
            categories['is_armor'] = False
        
        # Detect ornaments (usually in item_type 2 or 3 with specific properties)
        if 'plug' in item_data and item_data.get('plug', {}).get('plugCategoryIdentifier') == 'ornaments':
            categories['is_ornament'] = True
        
        return categories
    
    def extract_power_info(self, item_data: Dict[str, Any]) -> Dict[str, Optional[int]]:
        """Extract power and progression information."""
        quality = item_data.get('quality', {})
        inventory = item_data.get('inventory', {})
        
        return {
            'power_cap': quality.get('currentVersion', 0) if quality else None,
            'default_damage_type': item_data.get('defaultDamageType', 0),
            'ammo_type': inventory.get('bucketTypeHash', 0) if inventory else None
        }
    
    def parse_item_definition(self, hash_value: int, item_data: Dict[str, Any]) -> Dict[str, Any]:
        """Parse a single item definition with enrichment."""
        display_props = item_data.get('displayProperties', {})
        inventory = item_data.get('inventory', {})
        
        # Basic properties
        parsed_item = {
            'hash': hash_value,
            'display_name': display_props.get('name', ''),
            'description': display_props.get('description', ''),
            'icon': display_props.get('icon', ''),
            'item_type': item_data.get('itemType', 0),
            'item_sub_type': item_data.get('itemSubType', 0),
            'tier_type': inventory.get('tierType', 0),
            'class_type': item_data.get('classType', 3),
            'damage_type': item_data.get('defaultDamageType', 0),
            'raw_json': json.dumps(item_data)
        }
        
        # Add categorization
        categories = self.categorize_item(item_data)
        parsed_item.update(categories)
        
        # Add power information
        power_info = self.extract_power_info(item_data)
        parsed_item.update(power_info)
        
        # Build search text
        parsed_item['search_text'] = self.build_search_text(item_data)
        
        return parsed_item
    
    def parse_activity_definition(self, hash_value: int, activity_data: Dict[str, Any]) -> Dict[str, Any]:
        """Parse activity definition with enhanced data."""
        display_props = activity_data.get('displayProperties', {})
        
        parsed_activity = {
            'hash': hash_value,
            'display_name': display_props.get('name', ''),
            'description': display_props.get('description', ''),
            'activity_type_hash': activity_data.get('activityTypeHash', 0),
            'playlist_items': json.dumps(activity_data.get('playlistItems', [])),
            'modifiers': json.dumps(activity_data.get('modifiers', [])),
            'is_pvp': activity_data.get('isPvP', False),
            'is_pve': not activity_data.get('isPvP', False),
            'difficulty_tier': activity_data.get('tier', 0),
            'raw_json': json.dumps(activity_data)
        }
        
        return parsed_activity
    
    def parse_vendor_definition(self, hash_value: int, vendor_data: Dict[str, Any]) -> Dict[str, Any]:
        """Parse vendor definition with enhanced data."""
        display_props = vendor_data.get('displayProperties', {})
        
        parsed_vendor = {
            'hash': hash_value,
            'display_name': display_props.get('name', ''),
            'description': display_props.get('description', ''),
            'icon': display_props.get('icon', ''),
            'vendor_banner': display_props.get('largeIcon', ''),
            'enabled': vendor_data.get('enabled', False),
            'vendor_category_hash': vendor_data.get('vendorCategoryHash', 0),
            'location_hash': vendor_data.get('locationHash', 0),
            'raw_json': json.dumps(vendor_data)
        }
        
        return parsed_vendor
    
    def parse_class_definition(self, hash_value: int, class_data: Dict[str, Any]) -> Dict[str, Any]:
        """Parse class definition."""
        display_props = class_data.get('displayProperties', {})
        
        return {
            'hash': hash_value,
            'class_type': class_data.get('classType', 3),
            'display_name': display_props.get('name', ''),
            'description': display_props.get('description', ''),
            'icon': display_props.get('icon', ''),
            'raw_json': json.dumps(class_data)
        }
    
    def parse_race_definition(self, hash_value: int, race_data: Dict[str, Any]) -> Dict[str, Any]:
        """Parse race definition."""
        display_props = race_data.get('displayProperties', {})
        
        return {
            'hash': hash_value,
            'race_type': race_data.get('raceType', 0),
            'display_name': display_props.get('name', ''),
            'description': display_props.get('description', ''),
            'icon': display_props.get('icon', ''),
            'raw_json': json.dumps(race_data)
        }
    
    def parse_damage_type_definition(self, hash_value: int, damage_type_data: Dict[str, Any]) -> Dict[str, Any]:
        """Parse damage type definition."""
        display_props = damage_type_data.get('displayProperties', {})
        
        return {
            'hash': hash_value,
            'damage_type': damage_type_data.get('enumValue', 0),
            'display_name': display_props.get('name', ''),
            'description': display_props.get('description', ''),
            'icon': display_props.get('icon', ''),
            'color': json.dumps(damage_type_data.get('color', {})),
            'raw_json': json.dumps(damage_type_data)
        }
    
    def build_relationships(self, manifest_data: Dict[str, Any]) -> Dict[str, Dict]:
        """Build relationship mappings between different definition types."""
        relationships = {
            'item_to_perks': {},
            'item_to_sockets': {},
            'activity_to_rewards': {},
            'vendor_to_items': {}
        }
        
        # Build item to perk relationships
        item_definitions = manifest_data.get('DestinyInventoryItemDefinition', {})
        for item_hash, item_data in item_definitions.items():
            sockets = item_data.get('sockets', {})
            if sockets:
                socket_entries = sockets.get('socketEntries', [])
                item_perks = []
                for socket_entry in socket_entries:
                    reusable_plugs = socket_entry.get('reusablePlugItems', [])
                    for plug in reusable_plugs:
                        plug_hash = plug.get('plugItemHash')
                        if plug_hash:
                            item_perks.append(plug_hash)
                
                if item_perks:
                    relationships['item_to_perks'][item_hash] = item_perks
        
        # Build activity to reward relationships
        activity_definitions = manifest_data.get('DestinyActivityDefinition', {})
        for activity_hash, activity_data in activity_definitions.items():
            rewards = activity_data.get('rewards', [])
            if rewards:
                activity_rewards = []
                for reward in rewards:
                    reward_items = reward.get('rewardItems', [])
                    for item in reward_items:
                        item_hash = item.get('itemHash')
                        if item_hash:
                            activity_rewards.append(item_hash)
                
                if activity_rewards:
                    relationships['activity_to_rewards'][activity_hash] = activity_rewards
        
        return relationships
    
    def process_manifest_data(self, manifest_data: Dict[str, Any], progress_callback=None) -> Dict[str, List[Dict]]:
        """Process complete manifest data with progress tracking."""
        processed_data = {
            'items': [],
            'activities': [],
            'vendors': [],
            'classes': [],
            'races': [],
            'damage_types': []
        }
        
        total_operations = 0
        completed_operations = 0
        
        # Count total operations
        for definition_type in manifest_data:
            if definition_type in ['DestinyInventoryItemDefinition', 'DestinyActivityDefinition', 
                                   'DestinyVendorDefinition', 'DestinyClassDefinition',
                                   'DestinyRaceDefinition', 'DestinyDamageTypeDefinition']:
                total_operations += len(manifest_data[definition_type])
        
        # Process item definitions
        item_definitions = manifest_data.get('DestinyInventoryItemDefinition', {})
        for item_hash_str, item_data in item_definitions.items():
            try:
                item_hash = int(item_hash_str)
                # Convert signed to unsigned if negative
                if item_hash < 0:
                    item_hash = item_hash + 2**32
                
                parsed_item = self.parse_item_definition(item_hash, item_data)
                processed_data['items'].append(parsed_item)
                
                completed_operations += 1
                if progress_callback and completed_operations % 1000 == 0:
                    progress = (completed_operations / total_operations) * 100
                    progress_callback(progress, completed_operations, total_operations)
                    
            except Exception as e:
                print(f"Error processing item {item_hash_str}: {e}")
                continue
        
        # Process activity definitions
        activity_definitions = manifest_data.get('DestinyActivityDefinition', {})
        for activity_hash_str, activity_data in activity_definitions.items():
            try:
                activity_hash = int(activity_hash_str)
                if activity_hash < 0:
                    activity_hash = activity_hash + 2**32
                
                parsed_activity = self.parse_activity_definition(activity_hash, activity_data)
                processed_data['activities'].append(parsed_activity)
                
                completed_operations += 1
                if progress_callback and completed_operations % 100 == 0:
                    progress = (completed_operations / total_operations) * 100
                    progress_callback(progress, completed_operations, total_operations)
                    
            except Exception as e:
                print(f"Error processing activity {activity_hash_str}: {e}")
                continue
        
        # Process vendor definitions
        vendor_definitions = manifest_data.get('DestinyVendorDefinition', {})
        for vendor_hash_str, vendor_data in vendor_definitions.items():
            try:
                vendor_hash = int(vendor_hash_str)
                if vendor_hash < 0:
                    vendor_hash = vendor_hash + 2**32
                
                parsed_vendor = self.parse_vendor_definition(vendor_hash, vendor_data)
                processed_data['vendors'].append(parsed_vendor)
                
                completed_operations += 1
                
            except Exception as e:
                print(f"Error processing vendor {vendor_hash_str}: {e}")
                continue
        
        # Process class definitions
        class_definitions = manifest_data.get('DestinyClassDefinition', {})
        for class_hash_str, class_data in class_definitions.items():
            try:
                class_hash = int(class_hash_str)
                if class_hash < 0:
                    class_hash = class_hash + 2**32
                
                parsed_class = self.parse_class_definition(class_hash, class_data)
                processed_data['classes'].append(parsed_class)
                
                completed_operations += 1
                
            except Exception as e:
                print(f"Error processing class {class_hash_str}: {e}")
                continue
        
        # Process race definitions
        race_definitions = manifest_data.get('DestinyRaceDefinition', {})
        for race_hash_str, race_data in race_definitions.items():
            try:
                race_hash = int(race_hash_str)
                if race_hash < 0:
                    race_hash = race_hash + 2**32
                
                parsed_race = self.parse_race_definition(race_hash, race_data)
                processed_data['races'].append(parsed_race)
                
                completed_operations += 1
                
            except Exception as e:
                print(f"Error processing race {race_hash_str}: {e}")
                continue
        
        # Process damage type definitions
        damage_type_definitions = manifest_data.get('DestinyDamageTypeDefinition', {})
        for damage_type_hash_str, damage_type_data in damage_type_definitions.items():
            try:
                damage_type_hash = int(damage_type_hash_str)
                if damage_type_hash < 0:
                    damage_type_hash = damage_type_hash + 2**32
                
                parsed_damage_type = self.parse_damage_type_definition(damage_type_hash, damage_type_data)
                processed_data['damage_types'].append(parsed_damage_type)
                
                completed_operations += 1
                
            except Exception as e:
                print(f"Error processing damage type {damage_type_hash_str}: {e}")
                continue
        
        # Final progress update
        if progress_callback:
            progress_callback(100, completed_operations, total_operations)
        
        return processed_data