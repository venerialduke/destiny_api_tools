"""
Core Bungie API service for making authenticated requests.
"""

import requests
from typing import Dict, Any, Optional
from ..config import Config


class BungieAPIService:
    """Service for interacting with the Bungie API."""
    
    def __init__(self, access_token: Optional[str] = None):
        """Initialize the Bungie API service."""
        self.base_url = Config.BUNGIE_API_BASE_URL
        self.access_token = access_token
        self.session = requests.Session()
        
    def _get_headers(self, authenticated: bool = False) -> Dict[str, str]:
        """Get headers for API requests."""
        if authenticated and self.access_token:
            return Config.get_oauth_headers(self.access_token)
        return Config.get_bungie_headers()
    
    def _make_request(self, method: str, endpoint: str, authenticated: bool = False, 
                     params: Optional[Dict] = None, data: Optional[Dict] = None) -> Dict[str, Any]:
        """Make a request to the Bungie API."""
        url = f"{self.base_url}{endpoint}"
        headers = self._get_headers(authenticated)
        
        response = self.session.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=data
        )
        
        response.raise_for_status()
        return response.json()
    
    def get_manifest(self) -> Dict[str, Any]:
        """Get the current Destiny 2 manifest."""
        return self._make_request('GET', '/Destiny2/Manifest/')
    
    def get_profile(self, membership_type: int, membership_id: str, 
                   components: Optional[str] = None) -> Dict[str, Any]:
        """Get a player's profile."""
        params = {}
        if components:
            params['components'] = components
            
        return self._make_request(
            'GET', 
            f'/Destiny2/{membership_type}/Profile/{membership_id}/',
            authenticated=True,
            params=params
        )
    
    def get_character(self, membership_type: int, membership_id: str, 
                     character_id: str, components: Optional[str] = None) -> Dict[str, Any]:
        """Get character information."""
        params = {}
        if components:
            params['components'] = components
            
        return self._make_request(
            'GET',
            f'/Destiny2/{membership_type}/Profile/{membership_id}/Character/{character_id}/',
            authenticated=True,
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
        
        return self._make_request(
            'POST',
            '/Destiny2/Actions/Items/TransferItem/',
            authenticated=True,
            data=data
        )
    
    def equip_item(self, item_id: str, character_id: str, 
                  membership_type: int) -> Dict[str, Any]:
        """Equip an item on a character."""
        data = {
            'itemId': item_id,
            'characterId': character_id,
            'membershipType': membership_type
        }
        
        return self._make_request(
            'POST',
            '/Destiny2/Actions/Items/EquipItem/',
            authenticated=True,
            data=data
        )