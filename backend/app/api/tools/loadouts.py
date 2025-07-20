"""
Loadout management API endpoints.
"""

from flask import request, jsonify
# from ...services.loadout_service import LoadoutService
from ...utils.auth_required import auth_required
from . import tools_bp


# Loadout endpoints temporarily disabled - service not implemented
# @tools_bp.route('/loadouts/<membership_type>/<membership_id>/<character_id>', methods=['GET'])
# @auth_required
# def get_loadouts(membership_type, membership_id, character_id):
#     """Get all loadouts for a character."""
#     try:
#         access_token = request.headers.get('Authorization').split(' ')[1]
#         loadout_service = LoadoutService(access_token)
#         
#         loadouts = loadout_service.get_character_loadouts(
#             membership_type, membership_id, character_id
#         )
#         return jsonify(loadouts)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500


# @tools_bp.route('/loadouts/equip', methods=['POST'])
# @auth_required
# def equip_loadout():
#     """Equip a loadout on a character."""
#     try:
#         data = request.get_json()
#         access_token = request.headers.get('Authorization').split(' ')[1]
#         loadout_service = LoadoutService(access_token)
#         
#         result = loadout_service.equip_loadout(
#             loadout_index=data['loadoutIndex'],
#             character_id=data['characterId'],
#             membership_type=data['membershipType']
#         )
#         
#         return jsonify(result)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500


# @tools_bp.route('/loadouts/snapshot', methods=['POST'])
# @auth_required
# def snapshot_loadout():
#     """Create a snapshot of current equipment as a loadout."""
#     try:
#         data = request.get_json()
#         access_token = request.headers.get('Authorization').split(' ')[1]
#         loadout_service = LoadoutService(access_token)
#         
#         result = loadout_service.snapshot_loadout(
#             loadout_index=data['loadoutIndex'],
#             character_id=data['characterId'],
#             membership_type=data['membershipType']
#         )
#         
#         return jsonify(result)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500