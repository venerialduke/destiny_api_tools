"""
Authentication API endpoints for OAuth flow.
"""

from flask import Blueprint, request, jsonify, redirect, url_for
from ...services.auth_service import AuthService
from ...utils.validators import validate_oauth_code

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET'])
def login():
    """Initiate OAuth login flow."""
    try:
        auth_service = AuthService()
        auth_data = auth_service.get_authorization_url()
        return jsonify({
            'auth_url': auth_data['auth_url'],
            'state': auth_data['state'],
            'status': 'redirect_required'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@auth_bp.route('/callback', methods=['POST'])
def oauth_callback():
    """Handle OAuth callback and exchange code for tokens."""
    try:
        data = request.get_json()
        code = data.get('code')
        
        if not code:
            return jsonify({'error': 'Authorization code required'}), 400
        
        if not validate_oauth_code(code):
            return jsonify({'error': 'Invalid authorization code'}), 400
        
        auth_service = AuthService()
        tokens = auth_service.exchange_code_for_tokens(code)
        
        return jsonify({
            'access_token': tokens['access_token'],
            'refresh_token': tokens['refresh_token'],
            'expires_in': tokens['expires_in'],
            'user_data': tokens['user_data']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@auth_bp.route('/refresh', methods=['POST'])
def refresh_token():
    """Refresh access token using refresh token."""
    try:
        data = request.get_json()
        refresh_token = data.get('refresh_token')
        
        if not refresh_token:
            return jsonify({'error': 'Refresh token required'}), 400
        
        auth_service = AuthService()
        tokens = auth_service.refresh_access_token(refresh_token)
        
        return jsonify({
            'access_token': tokens['access_token'],
            'refresh_token': tokens['refresh_token'],
            'expires_in': tokens['expires_in']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@auth_bp.route('/logout', methods=['POST'])
def logout():
    """Logout user (client-side token cleanup)."""
    return jsonify({'status': 'logged_out'})