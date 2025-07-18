"""
Validation utilities for API inputs.
"""

import re
from typing import Any, Dict, List, Optional


def validate_oauth_code(code: str) -> bool:
    """Validate OAuth authorization code format."""
    if not code or not isinstance(code, str):
        return False
    
    # Basic validation - OAuth codes are typically alphanumeric
    if not re.match(r'^[a-zA-Z0-9]+$', code):
        return False
    
    # Check length (typical OAuth codes are 20-100 characters)
    if len(code) < 20 or len(code) > 100:
        return False
    
    return True


def validate_membership_type(membership_type: Any) -> bool:
    """Validate Bungie membership type."""
    valid_types = [1, 2, 3, 4, 5, 10, 254]  # Bungie membership types
    
    try:
        membership_type = int(membership_type)
        return membership_type in valid_types
    except (ValueError, TypeError):
        return False


def validate_membership_id(membership_id: str) -> bool:
    """Validate Bungie membership ID format."""
    if not membership_id or not isinstance(membership_id, str):
        return False
    
    # Membership IDs are typically numeric strings
    if not re.match(r'^\d+$', membership_id):
        return False
    
    # Check reasonable length
    if len(membership_id) < 10 or len(membership_id) > 20:
        return False
    
    return True


def validate_character_id(character_id: str) -> bool:
    """Validate Destiny character ID format."""
    if not character_id or not isinstance(character_id, str):
        return False
    
    # Character IDs are typically numeric strings
    if not re.match(r'^\d+$', character_id):
        return False
    
    # Check reasonable length
    if len(character_id) < 15 or len(character_id) > 25:
        return False
    
    return True


def validate_item_hash(item_hash: Any) -> bool:
    """Validate item hash."""
    try:
        item_hash = int(item_hash)
        return item_hash > 0
    except (ValueError, TypeError):
        return False


def validate_required_fields(data: Dict[str, Any], required_fields: List[str]) -> Optional[str]:
    """Validate that required fields are present in data."""
    missing_fields = []
    
    for field in required_fields:
        if field not in data or data[field] is None:
            missing_fields.append(field)
    
    if missing_fields:
        return f"Missing required fields: {', '.join(missing_fields)}"
    
    return None