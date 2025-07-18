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
        
    def get_authorization_url(self, state: str = None) -> str:
        """Generate the OAuth authorization URL."""
        if not state:
            state = secrets.token_urlsafe(32)
            
        params = {
            'client_id': Config.BUNGIE_CLIENT_ID,
            'response_type': 'code',
            'state': state,
            'redirect_uri': Config.OAUTH_REDIRECT_URI
        }
        
        return f"{self.auth_url}?{urlencode(params)}"
    
    def exchange_code_for_tokens(self, code: str) -> Dict[str, Any]:
        """Exchange authorization code for access tokens."""
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
        
        response = requests.post(self.token_url, data=data, headers=headers)
        response.raise_for_status()
        
        token_data = response.json()
        
        # Get membership ID from the token
        membership_id = self._get_membership_id(token_data['access_token'])
        
        return {
            'access_token': token_data['access_token'],
            'refresh_token': token_data['refresh_token'],
            'expires_in': token_data['expires_in'],
            'membership_id': membership_id
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
    
    def _get_membership_id(self, access_token: str) -> str:
        """Get the membership ID from the access token."""
        headers = Config.get_oauth_headers(access_token)
        
        response = requests.get(
            f"{Config.BUNGIE_API_BASE_URL}/User/GetMembershipsForCurrentUser/",
            headers=headers
        )
        response.raise_for_status()
        
        data = response.json()
        
        # Get the primary membership ID
        if data['Response']['destinyMemberships']:
            return data['Response']['destinyMemberships'][0]['membershipId']
        elif data['Response']['bungieNetUser']:
            return data['Response']['bungieNetUser']['membershipId']
        else:
            raise ValueError("Could not determine membership ID")