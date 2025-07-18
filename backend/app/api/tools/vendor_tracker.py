"""
Vendor tracking API endpoints.
"""

from flask import request, jsonify
from ...services.vendor_service import VendorService
from ...utils.auth_required import auth_required
from . import tools_bp


@tools_bp.route('/vendors/<membership_type>/<membership_id>/<character_id>', methods=['GET'])
@auth_required
def get_vendors(membership_type, membership_id, character_id):
    """Get all vendors for a character."""
    try:
        access_token = request.headers.get('Authorization').split(' ')[1]
        vendor_service = VendorService(access_token)
        
        vendors = vendor_service.get_character_vendors(
            membership_type, membership_id, character_id
        )
        return jsonify(vendors)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@tools_bp.route('/vendors/<membership_type>/<membership_id>/<character_id>/<vendor_hash>', methods=['GET'])
@auth_required
def get_vendor_details(membership_type, membership_id, character_id, vendor_hash):
    """Get detailed information for a specific vendor."""
    try:
        access_token = request.headers.get('Authorization').split(' ')[1]
        vendor_service = VendorService(access_token)
        
        vendor = vendor_service.get_vendor_details(
            membership_type, membership_id, character_id, vendor_hash
        )
        return jsonify(vendor)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@tools_bp.route('/vendors/public', methods=['GET'])
def get_public_vendors():
    """Get public vendor information (no auth required)."""
    try:
        vendor_service = VendorService()
        vendors = vendor_service.get_public_vendors()
        return jsonify(vendors)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@tools_bp.route('/vendors/track', methods=['POST'])
@auth_required
def track_vendor_item():
    """Track a vendor item for notifications."""
    try:
        data = request.get_json()
        access_token = request.headers.get('Authorization').split(' ')[1]
        vendor_service = VendorService(access_token)
        
        result = vendor_service.track_item(
            vendor_hash=data['vendorHash'],
            item_hash=data['itemHash'],
            membership_type=data['membershipType'],
            membership_id=data['membershipId'],
            notification_settings=data.get('notificationSettings', {})
        )
        
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500