"""
JSON flattening functions extracted from json_row_structure.py
"""

def infer_values(key, value):
    """Infer the data type and extract corresponding values."""
    if isinstance(value, dict):
        return {'data_type': 'dict', 'boolean_value': None, 'numeric_value': None, 'string_value': None, 'key_link': key}
    
    if isinstance(value, list):
        return {'data_type': 'array', 'boolean_value': None, 'numeric_value': None, 'string_value': None, 'key_link': key}
    
    data_type, boolean_value, numeric_value, string_value = "String", None, None, None
    
    if isinstance(value, bool):
        data_type, boolean_value = "Boolean", value
    elif isinstance(value, (int, float)):
        data_type, numeric_value = "Numeric", value
    elif isinstance(value, str):
        if value.lower() in ('true', 'false'):
            data_type, boolean_value = "Boolean", value.lower() == 'true'
        else:
            try:
                numeric_value = float(value)
                data_type = "Numeric"
            except ValueError:
                string_value = value
    
    return {'data_type': data_type, 'boolean_value': boolean_value, 'numeric_value': numeric_value, 'string_value': string_value, 'key_link': key}

def extract_key_value_pairs(dictionary, parent_key=''):
    """Recursively extract key-value pairs from a nested dictionary."""
    key_value_pairs = []
    
    for key, value in dictionary.items():
        full_key = f"{parent_key}{key}."
        if isinstance(value, dict):
            key_value_pairs.extend(extract_key_value_pairs(value, full_key))
            key_value_pairs.append(infer_values(full_key, value))
        elif isinstance(value, list):
            key_value_pairs.append(infer_values(full_key, value))
            for idx, item in enumerate(value):
                indexed_key = f"{parent_key}{key}[{idx}]"
                if isinstance(item, dict):
                    key_value_pairs.extend(extract_key_value_pairs(item, f"{indexed_key}."))
                key_value_pairs.append(infer_values(indexed_key, item))
        else:
            key_value_pairs.append(infer_values(full_key, value))
    
    return key_value_pairs