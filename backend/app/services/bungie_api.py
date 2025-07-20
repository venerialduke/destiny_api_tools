"""
Core Bungie API service for making authenticated requests.
"""

from typing import Dict, Any, Optional
from .base_api_client import BaseBungieAPIClient


class BungieAPIService(BaseBungieAPIClient):
    """Service for interacting with the Bungie API using the base client."""
    
    def __init__(self, access_token: Optional[str] = None):
        """Initialize the Bungie API service."""
        super().__init__(access_token)
    
    def get_manifest(self) -> Dict[str, Any]:
        """Get the current Destiny 2 manifest."""
        return self.get('/Destiny2/Manifest/')
    
    def get_profile(self, membership_type: int, membership_id: str, 
                   components: Optional[str] = None) -> Dict[str, Any]:
        """Get a player's profile."""
        params = {}
        if components:
            params['components'] = components
            
        return self.get(
            f'/Destiny2/{membership_type}/Profile/{membership_id}/',
            params=params
        )
    
    def get_character(self, membership_type: int, membership_id: str, 
                     character_id: str, components: Optional[str] = None) -> Dict[str, Any]:
        """Get character information."""
        params = {}
        if components:
            params['components'] = components
            
        return self.get(
            f'/Destiny2/{membership_type}/Profile/{membership_id}/Character/{character_id}/',
            params=params
        )
    
    def transfer_item(self, item_reference_hash: int, stack_size: int, 
                     transfer_to_vault: bool, item_id: str, 
                     character_id: str, membership_type: int) -> Dict[str, Any]:
        """Transfer an item between characters or vault."""
        data = {
            'itemReferenceHash': item_reference_hash,
            'stackSize': stack_size,
            'transferToVault': transfer_to_vault,
            'itemId': item_id,
            'characterId': character_id,
            'membershipType': membership_type
        }
        
        return self.post('/Destiny2/Actions/Items/TransferItem/', json=data)
    
    def equip_item(self, item_id: str, character_id: str, 
                  membership_type: int) -> Dict[str, Any]:
        """Equip an item on a character."""
        data = {
            'itemId': item_id,
            'characterId': character_id,
            'membershipType': membership_type
        }
        
        return self.post('/Destiny2/Actions/Items/EquipItem/', json=data)