"""
API Blueprint initialization for Destiny API Tools.
"""

from flask import Blueprint
from .core import core_bp
from .auth import auth_bp
from .tools import tools_bp

# Main API blueprint
api_bp = Blueprint('api', __name__)

# Register sub-blueprints
api_bp.register_blueprint(core_bp, url_prefix='/core')
api_bp.register_blueprint(auth_bp, url_prefix='/auth')
api_bp.register_blueprint(tools_bp, url_prefix='/tools')