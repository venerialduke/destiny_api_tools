# Destiny.PlugUiStyles

## Entity Information
- **Entity Name**: Destiny.PlugUiStyles
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
If the plug has a specific custom style, this enumeration will represent that style/those styles.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Masterwork |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.PlugUiStyles enumeration values
const PlugUiStyles = {
  None: 0,
  Masterwork: 1,
};

// Using the enumeration
const value = PlugUiStyles.None;
```

### Python
```python
# Destiny.PlugUiStyles enumeration values
class PlugUiStyles:
    NONE = 0
    MASTERWORK = 1

# Using the enumeration
value = PlugUiStyles.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.PlugUiStyles":   {
      "format": "int32",
      "description": "If the plug has a specific custom style, this enumeration will represent that style/those styles.",
      "enum": [
          "0",
          "1"
      ],
      "type": "integer"
  }
}
```
