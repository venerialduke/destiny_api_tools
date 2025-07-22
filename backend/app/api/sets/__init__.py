"""
API endpoints for Destiny 2 Equipable Item Sets.
Provides comprehensive set information including armor pieces and set perks.
"""

from flask import Blueprint, jsonify, request
from ...services.equipable_sets_service import equipable_sets_service
from ...utils.response import APIResponse, ErrorCodes


sets_bp = Blueprint('sets', __name__)


@sets_bp.route('/', methods=['GET'])
def get_all_sets():
    """Get all equipable sets with optional class filtering."""
    try:
        # Get query parameters
        class_filter = request.args.get('class', type=int)
        include_items = request.args.get('include_items', 'false').lower() == 'true'
        include_perks = request.args.get('include_perks', 'false').lower() == 'true'
        
        # Validate class filter
        if class_filter is not None and class_filter not in [0, 1, 2]:
            return APIResponse.error(
                message="Invalid class type. Must be 0 (Titan), 1 (Hunter), or 2 (Warlock)",
                code=ErrorCodes.INVALID_PARAMETER,
                status_code=400
            )
        
        # Get sets data
        sets = equipable_sets_service.get_all_sets(class_filter)
        
        # Format response based on query parameters
        formatted_sets = []
        for equipable_set in sets:
            set_data = {
                'hash': equipable_set.hash,
                'name': equipable_set.name,
                'description': equipable_set.description,
                'icon': equipable_set.icon,
                'hasIcon': equipable_set.has_icon,
                'classType': equipable_set.class_type,
                'className': equipable_set.class_name,
                'totalPieces': equipable_set.total_pieces,
                'perkCount': len(equipable_set.set_perks)
            }
            
            # Include detailed armor pieces if requested
            if include_items:
                set_data['armorPieces'] = [
                    {
                        'hash': piece.hash,
                        'name': piece.name,
                        'description': piece.description,
                        'icon': piece.icon,
                        'itemType': piece.item_type,
                        'itemSubType': piece.item_sub_type,
                        'classType': piece.class_type,
                        'className': piece.class_name,
                        'tierType': piece.tier_type
                    }
                    for piece in equipable_set.armor_pieces
                ]
            
            # Include detailed set perks if requested  
            if include_perks:
                set_data['setPerks'] = [
                    {
                        'requiredCount': perk.required_count,
                        'hash': perk.hash,
                        'name': perk.name,
                        'description': perk.description,
                        'icon': perk.icon,
                        'isDisplayable': perk.is_displayable
                    }
                    for perk in equipable_set.set_perks
                ]
            
            formatted_sets.append(set_data)
        
        return APIResponse.success(formatted_sets, meta={
            'total': len(formatted_sets),
            'classFilter': class_filter,
            'includeItems': include_items,
            'includePerks': include_perks
        })
        
    except Exception as e:
        return APIResponse.error(
            message="Failed to retrieve equipable sets",
            code=ErrorCodes.INTERNAL_ERROR,
            details=str(e),
            status_code=500
        )


@sets_bp.route('/<int:set_hash>', methods=['GET'])
def get_set_details(set_hash):
    """Get detailed information for a specific equipable set."""
    try:
        equipable_set = equipable_sets_service.get_set_by_hash(set_hash)
        
        if not equipable_set:
            return APIResponse.error(
                message=f"Equipable set {set_hash} not found",
                code=ErrorCodes.RESOURCE_NOT_FOUND,
                status_code=404
            )
        
        # Format complete set details
        set_data = {
            'hash': equipable_set.hash,
            'name': equipable_set.name,
            'description': equipable_set.description,
            'icon': equipable_set.icon,
            'hasIcon': equipable_set.has_icon,
            'classType': equipable_set.class_type,
            'className': equipable_set.class_name,
            'totalPieces': equipable_set.total_pieces,
            'armorPieces': [
                {
                    'hash': piece.hash,
                    'name': piece.name,
                    'description': piece.description,
                    'icon': piece.icon,
                    'itemType': piece.item_type,
                    'itemSubType': piece.item_sub_type,
                    'classType': piece.class_type,
                    'className': piece.class_name,
                    'tierType': piece.tier_type
                }
                for piece in equipable_set.armor_pieces
            ],
            'setPerks': [
                {
                    'requiredCount': perk.required_count,
                    'hash': perk.hash,
                    'name': perk.name,
                    'description': perk.description,
                    'icon': perk.icon,
                    'isDisplayable': perk.is_displayable
                }
                for perk in equipable_set.set_perks
            ]
        }
        
        return APIResponse.success(set_data)
        
    except Exception as e:
        return APIResponse.error(
            message=f"Failed to retrieve set {set_hash}",
            code=ErrorCodes.INTERNAL_ERROR,
            details=str(e),
            status_code=500
        )


@sets_bp.route('/by-class/<int:class_type>', methods=['GET'])
def get_sets_by_class(class_type):
    """Get all equipable sets for a specific class."""
    try:
        # Validate class type
        if class_type not in [0, 1, 2]:
            return APIResponse.error(
                message="Invalid class type. Must be 0 (Titan), 1 (Hunter), or 2 (Warlock)",
                code=ErrorCodes.INVALID_PARAMETER,
                status_code=400
            )
        
        # Get query parameters for detail level
        include_items = request.args.get('include_items', 'false').lower() == 'true'
        include_perks = request.args.get('include_perks', 'false').lower() == 'true'
        
        # Get sets for class
        sets = equipable_sets_service.get_all_sets(class_type)
        
        # Format response
        formatted_sets = []
        for equipable_set in sets:
            set_data = {
                'hash': equipable_set.hash,
                'name': equipable_set.name,
                'description': equipable_set.description,
                'icon': equipable_set.icon,
                'hasIcon': equipable_set.has_icon,
                'classType': equipable_set.class_type,
                'className': equipable_set.class_name,
                'totalPieces': equipable_set.total_pieces,
                'perkCount': len(equipable_set.set_perks)
            }
            
            if include_items:
                set_data['armorPieces'] = [
                    {
                        'hash': piece.hash,
                        'name': piece.name,
                        'description': piece.description,
                        'icon': piece.icon,
                        'itemType': piece.item_type,
                        'itemSubType': piece.item_sub_type,
                        'tierType': piece.tier_type
                    }
                    for piece in equipable_set.armor_pieces
                ]
            
            if include_perks:
                set_data['setPerks'] = [
                    {
                        'requiredCount': perk.required_count,
                        'hash': perk.hash,
                        'name': perk.name,
                        'description': perk.description,
                        'icon': perk.icon
                    }
                    for perk in equipable_set.set_perks
                ]
            
            formatted_sets.append(set_data)
        
        class_names = {0: "Titan", 1: "Hunter", 2: "Warlock"}
        
        return APIResponse.success(formatted_sets, meta={
            'classType': class_type,
            'className': class_names[class_type],
            'total': len(formatted_sets),
            'includeItems': include_items,
            'includePerks': include_perks
        })
        
    except Exception as e:
        return APIResponse.error(
            message=f"Failed to retrieve sets for class {class_type}",
            code=ErrorCodes.INTERNAL_ERROR,
            details=str(e),
            status_code=500
        )


@sets_bp.route('/summary', methods=['GET'])
def get_sets_summary():
    """Get summary statistics about equipable sets."""
    try:
        summary = equipable_sets_service.get_sets_summary()
        return APIResponse.success(summary)
        
    except Exception as e:
        return APIResponse.error(
            message="Failed to retrieve sets summary",
            code=ErrorCodes.INTERNAL_ERROR,
            details=str(e),
            status_code=500
        )