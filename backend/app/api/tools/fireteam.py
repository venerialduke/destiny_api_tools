"""
Fireteam and LFG API endpoints.
"""

from flask import request, jsonify
# from ...services.fireteam_service import FireteamService
from ...utils.auth_required import auth_required
from . import tools_bp


# Fireteam endpoints temporarily disabled - service not implemented
# @tools_bp.route('/fireteam/search', methods=['POST'])
# @auth_required
# def search_fireteams():
#     """Search for available fireteams."""
#     try:
#         data = request.get_json()
#         access_token = request.headers.get('Authorization').split(' ')[1]
#         fireteam_service = FireteamService(access_token)
#         
#         fireteams = fireteam_service.search_fireteams(
#             membership_type=data['membershipType'],
#             membership_id=data['membershipId'],
#             character_id=data['characterId'],
#             activity_type=data.get('activityType'),
#             platform=data.get('platform'),
#             date_range=data.get('dateRange', 0),
#             slot_filter=data.get('slotFilter', 0)
#         )
#         
#         return jsonify(fireteams)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500


# @tools_bp.route('/fireteam/create', methods=['POST'])
# @auth_required
# def create_fireteam():
#     """Create a new fireteam listing."""
#     try:
#         data = request.get_json()
#         access_token = request.headers.get('Authorization').split(' ')[1]
#         fireteam_service = FireteamService(access_token)
#         
#         result = fireteam_service.create_fireteam(
#             membership_type=data['membershipType'],
#             membership_id=data['membershipId'],
#             character_id=data['characterId'],
#             activity_type=data['activityType'],
#             platform=data['platform'],
#             settings=data.get('settings', {})
#         )
#         
#         return jsonify(result)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500


# @tools_bp.route('/fireteam/join', methods=['POST'])
# @auth_required
# def join_fireteam():
#     """Join an existing fireteam."""
#     try:
#         data = request.get_json()
#         access_token = request.headers.get('Authorization').split(' ')[1]
#         fireteam_service = FireteamService(access_token)
#         
#         result = fireteam_service.join_fireteam(
#             fireteam_id=data['fireteamId'],
#             membership_type=data['membershipType'],
#             membership_id=data['membershipId'],
#             character_id=data['characterId']
#         )
#         
#         return jsonify(result)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500


# @tools_bp.route('/fireteam/my-fireteams/<membership_type>/<membership_id>', methods=['GET'])
# @auth_required
# def get_my_fireteams(membership_type, membership_id):
#     """Get user's fireteam listings."""
#     try:
#         access_token = request.headers.get('Authorization').split(' ')[1]
#         fireteam_service = FireteamService(access_token)
#         
#         platform = request.args.get('platform', 0)
#         include_closed = request.args.get('includeClosed', 'false').lower() == 'true'
#         
#         fireteams = fireteam_service.get_my_fireteams(
#             membership_type, membership_id, platform, include_closed
#         )
#         
#         return jsonify(fireteams)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500