"""
User API endpoints for profile and character data.
"""

from flask import Blueprint, request, jsonify
from ...services.user_service import UserService
from ...utils.auth_required import auth_required
from ...utils.error_handlers import handle_api_error

user_bp = Blueprint('user', __name__)


@user_bp.route('/profile', methods=['GET'])
@auth_required
def get_user_profile():
    """Get the current user's profile with characters."""
    try:
        access_token = request.headers.get('Authorization').replace('Bearer ', '')
        user_service = UserService(access_token)
        
        # Get user memberships first to find primary membership
        memberships_data = user_service.get_user_memberships()
        primary_membership = None
        
        # Find primary membership
        if memberships_data.get('primaryMembershipId'):
            for membership in memberships_data.get('destinyMemberships', []):
                if membership['membershipId'] == memberships_data['primaryMembershipId']:
                    primary_membership = membership
                    break
        
        if not primary_membership and memberships_data.get('destinyMemberships'):
            primary_membership = memberships_data['destinyMemberships'][0]
        
        if not primary_membership:
            raise ValueError("No Destiny memberships found")
        
        # Get character data
        profile_data = user_service.get_user_profile_with_characters(
            primary_membership['membershipType'],
            primary_membership['membershipId']
        )
        
        return jsonify({
            'success': True,
            'data': profile_data
        }), 200
        
    except ValueError as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
        
    except Exception as e:
        return handle_api_error(e, 'Failed to retrieve user profile')


@user_bp.route('/memberships', methods=['GET'])
@auth_required
def get_user_memberships():
    """Get the current user's platform memberships."""
    try:
        access_token = request.headers.get('Authorization').replace('Bearer ', '')
        user_service = UserService(access_token)
        
        memberships_data = user_service.get_user_memberships()
        
        return jsonify({
            'success': True,
            'data': memberships_data
        }), 200
        
    except Exception as e:
        return handle_api_error(e, 'Failed to retrieve user memberships')


@user_bp.route('/characters/<int:membership_type>/<membership_id>', methods=['GET'])
@auth_required
def get_characters(membership_type, membership_id):
    """Get characters for a specific membership."""
    try:
        access_token = request.headers.get('Authorization').replace('Bearer ', '')
        user_service = UserService(access_token)
        
        # TODO: Add membership access validation
        
        profile_data = user_service.get_user_profile_with_characters(
            membership_type, membership_id
        )
        
        characters = []
        if 'characters' in profile_data:
            characters = user_service.format_character_data(profile_data['characters'])
        
        return jsonify({
            'success': True,
            'data': {
                'characters': characters,
                'membership_type': membership_type,
                'membership_id': membership_id
            }
        }), 200
        
    except Exception as e:
        return handle_api_error(e, 'Failed to retrieve characters')


@user_bp.route('/character/<int:membership_type>/<membership_id>/<character_id>', methods=['GET'])
@auth_required
def get_character_details(membership_type, membership_id, character_id):
    """Get detailed information for a specific character."""
    try:
        access_token = request.headers.get('Authorization').replace('Bearer ', '')
        user_service = UserService(access_token)
        
        # TODO: Add membership access validation
        
        character_data = user_service.get_character_details(
            membership_type, membership_id, character_id
        )
        
        return jsonify({
            'success': True,
            'data': character_data
        }), 200
        
    except Exception as e:
        return handle_api_error(e, 'Failed to retrieve character details')


@user_bp.route('/character/<int:membership_type>/<membership_id>/<character_id>/equipment', methods=['GET'])
@auth_required
def get_character_equipment(membership_type, membership_id, character_id):
    """Get equipment data for a specific character."""
    try:
        access_token = request.headers.get('Authorization').replace('Bearer ', '')
        user_service = UserService(access_token)
        
        # TODO: Add membership access validation
        
        # For now, return character details as equipment data since get_character_equipment doesn't exist yet
        equipment_data = user_service.get_character_details(
            membership_type, membership_id, character_id
        )
        
        return jsonify({
            'success': True,
            'data': equipment_data
        }), 200
        
    except Exception as e:
        return handle_api_error(e, 'Failed to retrieve character equipment')


@user_bp.route('/search/<int:membership_type>', methods=['POST'])
def search_player():
    """Search for a Destiny player by Bungie name."""
    try:
        data = request.get_json()
        bungie_name = data.get('bungie_name')
        
        if not bungie_name:
            return jsonify({
                'success': False,
                'error': 'Bungie name is required'
            }), 400
        
        membership_type = request.view_args['membership_type']
        
        # Create user service without token since search doesn't require auth
        from ...services.bungie_api import BungieAPIService
        api_service = BungieAPIService()
        
        # TODO: Implement search functionality
        search_results = {'message': 'Search functionality not yet implemented'}
        
        return jsonify({
            'success': True,
            'data': search_results
        }), 200
        
    except Exception as e:
        return handle_api_error(e, 'Failed to search for player')