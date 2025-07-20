"""
Authentication service for handling OAuth flow with Bungie API.
"""

import requests
import secrets
from typing import Dict, Any
from urllib.parse import urlencode
from ..config import Config


class AuthService:
    """Service for handling OAuth authentication."""
    
    def __init__(self):
        """Initialize the authentication service."""
        self.auth_url = 'https://www.bungie.net/en/OAuth/Authorize'
        self.token_url = 'https://www.bungie.net/Platform/App/OAuth/token/'
        
    def get_authorization_url(self, state: str = None) -> Dict[str, str]:
        """Generate the OAuth authorization URL with required scopes."""
        if not state:
            state = secrets.token_urlsafe(32)
            
        params = {
            'client_id': Config.BUNGIE_CLIENT_ID,
            'response_type': 'code',
            'state': state,
            'redirect_uri': Config.OAUTH_REDIRECT_URI
        }
        
        auth_url = f"{self.auth_url}?{urlencode(params)}"
        print(f"DEBUG: Generated OAuth URL: {auth_url}")
        return {
            'auth_url': auth_url,
            'state': state
        }
    
    def exchange_code_for_tokens(self, code: str) -> Dict[str, Any]:
        """Exchange authorization code for access tokens and retrieve user data."""
        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': Config.OAUTH_REDIRECT_URI,
            'client_id': Config.BUNGIE_CLIENT_ID,
            'client_secret': Config.BUNGIE_CLIENT_SECRET
        }
        
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-API-Key': Config.BUNGIE_API_KEY
        }
        
        print(f"DEBUG: Token exchange request data: {data}")
        print(f"DEBUG: Token exchange headers: {headers}")
        
        response = requests.post(self.token_url, data=data, headers=headers)
        print(f"DEBUG: Token response status: {response.status_code}")
        print(f"DEBUG: Token response content: {response.text}")
        
        if not response.ok:
            print(f"DEBUG: Token exchange failed with status {response.status_code}: {response.text}")
            raise Exception(f"Token exchange failed: {response.text}")
        
        token_data = response.json()
        
        # Get user memberships and character data
        user_data = self._get_user_data_with_characters(token_data['access_token'])
        
        return {
            'access_token': token_data['access_token'],
            'refresh_token': token_data['refresh_token'],
            'expires_in': token_data['expires_in'],
            'user_data': user_data
        }
    
    def refresh_access_token(self, refresh_token: str) -> Dict[str, Any]:
        """Refresh the access token using the refresh token."""
        data = {
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
            'client_id': Config.BUNGIE_CLIENT_ID,
            'client_secret': Config.BUNGIE_CLIENT_SECRET
        }
        
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-API-Key': Config.BUNGIE_API_KEY
        }
        
        response = requests.post(self.token_url, data=data, headers=headers)
        response.raise_for_status()
        
        token_data = response.json()
        
        return {
            'access_token': token_data['access_token'],
            'refresh_token': token_data['refresh_token'],
            'expires_in': token_data['expires_in']
        }
    
    def _get_user_data_with_characters(self, access_token: str) -> Dict[str, Any]:
        """Get user memberships and character data."""
        headers = Config.get_oauth_headers(access_token)
        
        # Get user memberships
        response = requests.get(
            f"{Config.BUNGIE_API_BASE_URL}/User/GetMembershipsForCurrentUser/",
            headers=headers
        )
        response.raise_for_status()
        
        memberships_data = response.json()
        user_membership_data = memberships_data['Response']
        
        # Get primary Destiny membership
        primary_membership = None
        if user_membership_data['primaryMembershipId']:
            # Find the membership with the primary ID
            for membership in user_membership_data['destinyMemberships']:
                if membership['membershipId'] == user_membership_data['primaryMembershipId']:
                    primary_membership = membership
                    break
        
        # If no primary found, use the first available
        if not primary_membership and user_membership_data['destinyMemberships']:
            primary_membership = user_membership_data['destinyMemberships'][0]
        
        if not primary_membership:
            raise ValueError("No Destiny memberships found for user")
        
        # Get character data for the primary membership
        characters = self._get_characters(
            access_token, 
            primary_membership['membershipType'], 
            primary_membership['membershipId']
        )
        
        return {
            'bungie_net_user': user_membership_data['bungieNetUser'],
            'destiny_memberships': user_membership_data['destinyMemberships'],
            'primary_membership_id': user_membership_data['primaryMembershipId'],
            'primary_membership': primary_membership,
            'characters': characters
        }
    
    def _get_characters(self, access_token: str, membership_type: int, membership_id: str) -> list:
        """Get character data for a specific membership."""
        headers = Config.get_oauth_headers(access_token)
        
        response = requests.get(
            f"{Config.BUNGIE_API_BASE_URL}/Destiny2/{membership_type}/Profile/{membership_id}/?components=200",
            headers=headers
        )
        response.raise_for_status()
        
        profile_data = response.json()
        
        if 'characters' not in profile_data['Response'] or 'data' not in profile_data['Response']['characters']:
            return []
        
        characters_data = profile_data['Response']['characters']['data']
        
        # Format character data for frontend
        characters = []
        for character_id, character_data in characters_data.items():
            characters.append({
                'character_id': character_id,
                'membership_id': character_data['membershipId'],
                'membership_type': character_data['membershipType'],
                'character_class': character_data['classType'],
                'race': character_data['raceType'],
                'gender': character_data['genderType'],
                'light_level': character_data['light'],
                'level': character_data['levelProgression']['level'],
                'emblem_path': character_data['emblemPath'],
                'emblem_background_path': character_data['emblemBackgroundPath'],
                'emblem_hash': character_data['emblemHash'],
                'base_character_level': character_data['baseCharacterLevel'],
                'percent_to_next_level': character_data['percentToNextLevel']
            })
        
        return characters