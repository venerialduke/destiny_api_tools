"""
Core API endpoints for basic functionality.
"""

from flask import Blueprint, jsonify
from ...services.bungie_api import BungieAPIService

core_bp = Blueprint('core', __name__)


@core_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'service': 'destiny-api-tools-backend',
        'version': '1.0.0'
    })


@core_bp.route('/manifest', methods=['GET'])
def get_manifest():
    """Get the current Destiny 2 manifest information."""
    try:
        bungie_service = BungieAPIService()
        manifest = bungie_service.get_manifest()
        return jsonify(manifest)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@core_bp.route('/settings', methods=['GET'])
def get_settings():
    """Get application settings for the frontend."""
    return jsonify({
        'bungie_api_available': True,
        'oauth_enabled': True,
        'version': '1.0.0'
    })