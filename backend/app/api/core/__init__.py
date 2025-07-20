"""
Core API endpoints for basic functionality.
"""

from flask import Blueprint, jsonify
from ...services.bungie_api import BungieAPIService
from .user import user_bp
from .performance import performance_bp
from .search import search_bp
from .health import health_bp

core_bp = Blueprint('core', __name__)

# Register sub-blueprints
core_bp.register_blueprint(user_bp, url_prefix='/user')
core_bp.register_blueprint(performance_bp, url_prefix='/performance')
core_bp.register_blueprint(search_bp, url_prefix='/search')
core_bp.register_blueprint(health_bp, url_prefix='/health')




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