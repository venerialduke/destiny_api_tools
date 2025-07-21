"""
User profile service for handling user data management and character operations.
"""

from typing import Dict, Any, List, Optional
from .base_api_client import BaseBungieAPIClient


class UserService:
    """Service for managing user profiles and character data."""
    
    def __init__(self, access_token: str):
        """Initialize the user service with access token."""
        self.api_client = BaseBungieAPIClient(access_token)
        
    def get_user_memberships(self) -> Dict[str, Any]:
        """Get current user's platform memberships."""
        response = self.api_client.get('/User/GetMembershipsForCurrentUser/')
        return response['Response']
    
    def get_user_profile_with_characters(self, membership_type: int, 
                                       membership_id: str) -> Dict[str, Any]:
        """Get user profile with character data."""
        response = self.api_client.get(
            f'/Destiny2/{membership_type}/Profile/{membership_id}/',
            params={'components': '200'}
        )
        return response['Response']
    
    def get_character_details(self, membership_type: int, 
                            membership_id: str, character_id: str) -> Dict[str, Any]:
        """Get detailed character information."""
        response = self.api_client.get(
            f'/Destiny2/{membership_type}/Profile/{membership_id}/Character/{character_id}/',
            params={'components': '200,205'}
        )
        return response['Response']
    
    def format_character_data(self, characters_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Format raw character data for frontend consumption."""
        if 'data' not in characters_data:
            return []
        
        characters = []
        for character_id, character_data in characters_data['data'].items():
            # Map class types to readable names
            class_names = {0: "Titan", 1: "Hunter", 2: "Warlock"}
            race_names = {0: "Human", 1: "Awoken", 2: "Exo"}
            gender_names = {0: "Male", 1: "Female"}
            
            formatted_character = {
                'character_id': character_id,
                'membership_id': character_data['membershipId'],
                'membership_type': character_data['membershipType'],
                'character_class': character_data['classType'],
                'character_class_name': class_names.get(character_data['classType'], 'Unknown'),
                'race': character_data['raceType'],
                'race_name': race_names.get(character_data['raceType'], 'Unknown'),
                'gender': character_data['genderType'],
                'gender_name': gender_names.get(character_data['genderType'], 'Unknown'),
                'light_level': character_data['light'],
                'level': character_data['levelProgression']['level'],
                'emblem_path': character_data['emblemPath'],
                'emblem_background_path': character_data['emblemBackgroundPath'],
                'emblem_hash': character_data['emblemHash'],
                'base_character_level': character_data['baseCharacterLevel'],
                'percent_to_next_level': character_data['percentToNextLevel'],
                'date_last_played': character_data['dateLastPlayed'],
                'minutes_played_this_session': character_data['minutesPlayedThisSession'],
                'minutes_played_total': character_data['minutesPlayedTotal']
            }
            
            characters.append(formatted_character)
        
        # Sort characters by last played date (most recent first)
        characters.sort(key=lambda x: x['date_last_played'], reverse=True)
        
        return characters
    
    def get_user_profile_summary(self, access_token: str) -> Dict[str, Any]:
        """Get a complete user profile summary with all memberships and characters."""
        # Get user memberships
        memberships_data = self.get_user_memberships(access_token)
        
        # Get primary Destiny membership
        primary_membership = None
        if memberships_data['primaryMembershipId']:
            # Find the membership with the primary ID
            for membership in memberships_data['destinyMemberships']:
                if membership['membershipId'] == memberships_data['primaryMembershipId']:
                    primary_membership = membership
                    break
        
        # If no primary found, use the first available
        if not primary_membership and memberships_data['destinyMemberships']:
            primary_membership = memberships_data['destinyMemberships'][0]
        
        if not primary_membership:
            raise ValueError("No Destiny memberships found for user")
        
        # Get character data for the primary membership
        profile_data = self.get_user_profile_with_characters(
            access_token,
            primary_membership['membershipType'],
            primary_membership['membershipId']
        )
        
        # Format characters for frontend
        characters = []
        if 'characters' in profile_data:
            characters = self.format_character_data(profile_data['characters'])
        
        return {
            'bungie_net_user': memberships_data['bungieNetUser'],
            'destiny_memberships': memberships_data['destinyMemberships'],
            'primary_membership_id': memberships_data['primaryMembershipId'],
            'primary_membership': primary_membership,
            'characters': characters,
            'total_characters': len(characters)
        }
    
    def search_destiny_player(self, bungie_name: str, membership_type: int) -> Dict[str, Any]:
        """Search for a Destiny player by Bungie name (fallback method)."""
        headers = Config.get_bungie_headers()
        
        data = {
            'displayName': bungie_name
        }
        
        response = requests.post(
            f"{self.base_url}/Destiny2/SearchDestinyPlayerByBungieName/{membership_type}/",
            json=data,
            headers=headers
        )
        response.raise_for_status()
        
        return response.json()['Response']
    
    def get_character_equipment(self, access_token: str, membership_type: int,
                              membership_id: str, character_id: str) -> Dict[str, Any]:
        """Get character equipment data."""
        headers = Config.get_oauth_headers(access_token)
        
        response = requests.get(
            f"{self.base_url}/Destiny2/{membership_type}/Profile/{membership_id}/Character/{character_id}/?components=205",
            headers=headers
        )
        response.raise_for_status()
        
        return response.json()['Response']
    
    def validate_membership_access(self, access_token: str, membership_type: int,
                                 membership_id: str) -> bool:
        """Validate that the user has access to the specified membership."""
        try:
            memberships_data = self.get_user_memberships(access_token)
            
            # Check if the requested membership is in the user's memberships
            for membership in memberships_data['destinyMemberships']:
                if (membership['membershipType'] == membership_type and 
                    membership['membershipId'] == membership_id):
                    return True
            
            return False
        except Exception:
            return False