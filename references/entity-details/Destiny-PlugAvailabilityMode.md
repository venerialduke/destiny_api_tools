# Destiny.PlugAvailabilityMode

## Entity Information
- **Entity Name**: Destiny.PlugAvailabilityMode
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
This enum determines whether the plug is available to be inserted.
- Normal means that all existing rules for plug insertion apply.
- UnavailableIfSocketContainsMatchingPlugCategory means that the plug is only available if the socket does NOT match the plug category.
- AvailableIfSocketContainsMatchingPlugCategory means that the plug is only available if the socket DOES match the plug category.
For category matching, use the plug's "plugCategoryIdentifier" property, comparing it to

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Normal |  |
| 1 | UnavailableIfSocketContainsMatchingPlugCategory |  |
| 2 | AvailableIfSocketContainsMatchingPlugCategory |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.PlugAvailabilityMode enumeration values
const PlugAvailabilityMode = {
  Normal: 0,
  UnavailableIfSocketContainsMatchingPlugCategory: 1,
  AvailableIfSocketContainsMatchingPlugCategory: 2,
};

// Using the enumeration
const value = PlugAvailabilityMode.Normal;
```

### Python
```python
# Destiny.PlugAvailabilityMode enumeration values
class PlugAvailabilityMode:
    NORMAL = 0
    UNAVAILABLEIFSOCKETCONTAINSMATCHINGPLUGCATEGORY = 1
    AVAILABLEIFSOCKETCONTAINSMATCHINGPLUGCATEGORY = 2

# Using the enumeration
value = PlugAvailabilityMode.NORMAL
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.PlugAvailabilityMode":   {
      "format": "int32",
      "description": "This enum determines whether the plug is available to be inserted.\r\n- Normal means that all existing rules for plug insertion apply.\r\n- UnavailableIfSocketContainsMatchingPlugCategory means that the plug is only available if the socket does NOT match the plug category.\r\n- AvailableIfSocketContainsMatchingPlugCategory means that the plug is only available if the socket DOES match the plug category.\r\nFor category matching, use the plug's \"plugCategoryIdentifier\" property, comparing it to",
      "enum": [
          "0",
          "1",
          "2"
      ],
      "type": "integer"
  }
}
```
