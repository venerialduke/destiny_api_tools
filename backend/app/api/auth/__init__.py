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
    print("🔐 AUTH: /login endpoint called")
    print(f"🔐 AUTH: Request method: {request.method}")
    print(f"🔐 AUTH: Request headers: {dict(request.headers)}")
    
    try:
        print("🔐 AUTH: Creating AuthService instance...")
        auth_service = AuthService()
        print("🔐 AUTH: Getting authorization URL...")
        auth_data = auth_service.get_authorization_url()
        
        response_data = {
            'auth_url': auth_data['auth_url'],
            'state': auth_data['state'],
            'status': 'redirect_required'
        }
        print(f"🔐 AUTH: Sending response: {response_data}")
        return jsonify(response_data)
    except Exception as e:
        print(f"❌ AUTH ERROR: {str(e)}")
        import traceback
        print(f"❌ AUTH TRACEBACK: {traceback.format_exc()}")
        return jsonify({'error': str(e)}), 500


@auth_bp.route('/callback', methods=['POST'])
def oauth_callback():
    """Handle OAuth callback and exchange code for tokens."""
    print("🔐 AUTH: /callback endpoint called")
    try:
        data = request.get_json()
        print(f"🔐 AUTH: Callback request data: {data}")
        
        code = data.get('code')
        print(f"🔐 AUTH: Authorization code: {code}")
        
        if not code:
            print("❌ AUTH: No authorization code provided")
            return jsonify({'error': 'Authorization code required'}), 400
        
        print("🔐 AUTH: Validating OAuth code...")
        if not validate_oauth_code(code):
            print("❌ AUTH: OAuth code validation failed")
            return jsonify({'error': 'Invalid authorization code'}), 400
        
        print("🔐 AUTH: Creating AuthService and exchanging code for tokens...")
        auth_service = AuthService()
        tokens = auth_service.exchange_code_for_tokens(code)
        
        print(f"🔐 AUTH: Token exchange successful, got tokens: {list(tokens.keys())}")
        
        response_data = {
            'access_token': tokens['access_token'],
            'refresh_token': tokens['refresh_token'],
            'expires_in': tokens['expires_in'],
            'user_data': tokens['user_data']
        }
        print(f"🔐 AUTH: Sending callback response with user_data keys: {list(tokens.get('user_data', {}).keys())}")
        
        return jsonify(response_data)
    except Exception as e:
        print(f"❌ AUTH CALLBACK ERROR: {str(e)}")
        import traceback
        print(f"❌ AUTH CALLBACK TRACEBACK: {traceback.format_exc()}")
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