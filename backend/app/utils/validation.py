"""
Request validation utilities for API endpoints.
"""

from typing import Dict, Any, List, Optional, Union


class ValidationError(Exception):
    """Custom validation error."""
    pass


def validate_request(data: Dict[str, Any], rules: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    """
    Validate request data against validation rules.
    
    Args:
        data: Request data to validate
        rules: Validation rules dictionary
        
    Returns:
        Validated and normalized data
        
    Raises:
        ValidationError: If validation fails
    """
    validated = {}
    errors = []
    
    for field, rule in rules.items():
        try:
            validated[field] = validate_field(data, field, rule)
        except ValidationError as e:
            errors.append(str(e))
    
    if errors:
        raise ValidationError(f"Validation failed: {'; '.join(errors)}")
    
    return validated


def validate_field(data: Dict[str, Any], field: str, rule: Dict[str, Any]) -> Any:
    """
    Validate a single field.
    
    Args:
        data: Request data
        field: Field name to validate
        rule: Validation rule for the field
        
    Returns:
        Validated field value
        
    Raises:
        ValidationError: If validation fails
    """
    value = data.get(field)
    required = rule.get('required', False)
    field_type = rule.get('type')
    default = rule.get('default')
    choices = rule.get('choices')
    min_val = rule.get('min')
    max_val = rule.get('max')
    min_length = rule.get('min_length')
    max_length = rule.get('max_length')
    pattern = rule.get('pattern')
    custom_validator = rule.get('validator')
    
    # Handle missing values
    if value is None:
        if required:
            raise ValidationError(f"Field '{field}' is required")
        if default is not None:
            return default
        return None
    
    # Type validation
    if field_type and not isinstance(value, field_type):
        if field_type == int and isinstance(value, str) and value.isdigit():
            value = int(value)
        elif field_type == float and isinstance(value, (str, int)):
            try:
                value = float(value)
            except ValueError:
                raise ValidationError(f"Field '{field}' must be a {field_type.__name__}")
        elif field_type == bool and isinstance(value, str):
            value = value.lower() in ('true', '1', 'yes', 'on')
        elif field_type == list and not isinstance(value, list):
            raise ValidationError(f"Field '{field}' must be a list")
        elif field_type == dict and not isinstance(value, dict):
            raise ValidationError(f"Field '{field}' must be a dictionary")
        else:
            raise ValidationError(f"Field '{field}' must be a {field_type.__name__}")
    
    # Choice validation
    if choices and value not in choices:
        raise ValidationError(f"Field '{field}' must be one of: {', '.join(map(str, choices))}")
    
    # Numeric range validation
    if isinstance(value, (int, float)):
        if min_val is not None and value < min_val:
            raise ValidationError(f"Field '{field}' must be >= {min_val}")
        if max_val is not None and value > max_val:
            raise ValidationError(f"Field '{field}' must be <= {max_val}")
    
    # String length validation
    if isinstance(value, str):
        if min_length is not None and len(value) < min_length:
            raise ValidationError(f"Field '{field}' must be at least {min_length} characters")
        if max_length is not None and len(value) > max_length:
            raise ValidationError(f"Field '{field}' must be at most {max_length} characters")
    
    # List length validation
    if isinstance(value, list):
        if min_length is not None and len(value) < min_length:
            raise ValidationError(f"Field '{field}' must have at least {min_length} items")
        if max_length is not None and len(value) > max_length:
            raise ValidationError(f"Field '{field}' must have at most {max_length} items")
    
    # Pattern validation
    if pattern and isinstance(value, str):
        import re
        if not re.match(pattern, value):
            raise ValidationError(f"Field '{field}' does not match required pattern")
    
    # Custom validation
    if custom_validator:
        try:
            if not custom_validator(value):
                raise ValidationError(f"Field '{field}' failed custom validation")
        except Exception as e:
            raise ValidationError(f"Field '{field}' validation error: {str(e)}")
    
    return value


def validate_pagination(data: Dict[str, Any], max_limit: int = 100) -> Dict[str, int]:
    """
    Validate pagination parameters.
    
    Args:
        data: Request data containing limit and offset
        max_limit: Maximum allowed limit
        
    Returns:
        Validated pagination parameters
    """
    rules = {
        'limit': {
            'type': int,
            'default': 20,
            'min': 1,
            'max': max_limit
        },
        'offset': {
            'type': int,
            'default': 0,
            'min': 0
        }
    }
    
    return validate_request(data, rules)


def validate_sort_params(data: Dict[str, Any], allowed_fields: List[str]) -> List[Dict[str, Any]]:
    """
    Validate sorting parameters.
    
    Args:
        data: Request data containing sort information
        allowed_fields: List of fields that can be sorted on
        
    Returns:
        Validated sort parameters
    """
    sort_param = data.get('sort', [])
    
    if not isinstance(sort_param, list):
        sort_param = [sort_param]
    
    validated_sorts = []
    
    for sort_item in sort_param:
        if isinstance(sort_item, str):
            # Handle simple string format: "field" or "-field"
            if sort_item.startswith('-'):
                field = sort_item[1:]
                order = 'desc'
            else:
                field = sort_item
                order = 'asc'
            
            sort_item = {'field': field, 'order': order}
        
        if not isinstance(sort_item, dict):
            raise ValidationError("Sort parameters must be objects or strings")
        
        field = sort_item.get('field')
        order = sort_item.get('order', 'asc')
        
        if not field:
            raise ValidationError("Sort field is required")
        
        if field not in allowed_fields:
            raise ValidationError(f"Cannot sort by field '{field}'. Allowed fields: {', '.join(allowed_fields)}")
        
        if order not in ['asc', 'desc']:
            raise ValidationError("Sort order must be 'asc' or 'desc'")
        
        validated_sorts.append({
            'field': field,
            'order': order,
            'priority': sort_item.get('priority', len(validated_sorts) + 1)
        })
    
    return validated_sorts


def validate_filter_params(data: Dict[str, Any], allowed_fields: List[str]) -> List[Dict[str, Any]]:
    """
    Validate filter parameters.
    
    Args:
        data: Request data containing filter information
        allowed_fields: List of fields that can be filtered on
        
    Returns:
        Validated filter parameters
    """
    filter_param = data.get('filters', [])
    
    if not isinstance(filter_param, list):
        raise ValidationError("Filters must be a list")
    
    validated_filters = []
    allowed_operators = ['eq', 'ne', 'gt', 'gte', 'lt', 'lte', 'in', 'not_in', 'contains', 'starts_with', 'ends_with']
    
    for filter_item in filter_param:
        if not isinstance(filter_item, dict):
            raise ValidationError("Filter items must be objects")
        
        field = filter_item.get('field')
        operator = filter_item.get('operator', 'eq')
        value = filter_item.get('value')
        
        if not field:
            raise ValidationError("Filter field is required")
        
        if field not in allowed_fields:
            raise ValidationError(f"Cannot filter by field '{field}'. Allowed fields: {', '.join(allowed_fields)}")
        
        if operator not in allowed_operators:
            raise ValidationError(f"Invalid filter operator '{operator}'. Allowed: {', '.join(allowed_operators)}")
        
        if value is None:
            raise ValidationError(f"Filter value is required for field '{field}'")
        
        validated_filters.append({
            'field': field,
            'operator': operator,
            'value': value,
            'case_sensitive': filter_item.get('case_sensitive', False)
        })
    
    return validated_filters


def validate_email(email: str) -> bool:
    """Validate email address format."""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_url(url: str) -> bool:
    """Validate URL format."""
    import re
    pattern = r'^https?://(?:[-\w.])+(?:\:[0-9]+)?(?:/[^?\s]*)?(?:\?[^#\s]*)?(?:#[^\s]*)?$'
    return re.match(pattern, url) is not None


def sanitize_html(text: str) -> str:
    """Basic HTML sanitization."""
    import re
    import html
    
    # Escape HTML entities
    text = html.escape(text)
    
    # Remove script tags
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.IGNORECASE | re.DOTALL)
    
    # Remove other potentially dangerous tags
    dangerous_tags = ['iframe', 'object', 'embed', 'form', 'input', 'button']
    for tag in dangerous_tags:
        text = re.sub(f'<{tag}[^>]*>.*?</{tag}>', '', text, flags=re.IGNORECASE | re.DOTALL)
        text = re.sub(f'<{tag}[^>]*/?>', '', text, flags=re.IGNORECASE)
    
    return text


def validate_json_schema(data: Any, schema: Dict[str, Any]) -> bool:
    """
    Basic JSON schema validation.
    
    Args:
        data: Data to validate
        schema: Schema definition
        
    Returns:
        True if valid, False otherwise
    """
    try:
        if 'type' in schema:
            expected_type = schema['type']
            if expected_type == 'string' and not isinstance(data, str):
                return False
            elif expected_type == 'number' and not isinstance(data, (int, float)):
                return False
            elif expected_type == 'integer' and not isinstance(data, int):
                return False
            elif expected_type == 'boolean' and not isinstance(data, bool):
                return False
            elif expected_type == 'array' and not isinstance(data, list):
                return False
            elif expected_type == 'object' and not isinstance(data, dict):
                return False
        
        if 'properties' in schema and isinstance(data, dict):
            for prop, prop_schema in schema['properties'].items():
                if prop in data:
                    if not validate_json_schema(data[prop], prop_schema):
                        return False
        
        if 'required' in schema and isinstance(data, dict):
            for required_prop in schema['required']:
                if required_prop not in data:
                    return False
        
        return True
        
    except Exception:
        return False