# Destiny.Advanced.AwaUserSelection

## Entity Information
- **Entity Name**: Destiny.Advanced.AwaUserSelection
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing awauserselection data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Rejected |  |
| 2 | Approved |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.Advanced.AwaUserSelection enumeration values
const AwaUserSelection = {
  None: 0,
  Rejected: 1,
  Approved: 2,
};

// Using the enumeration
const value = AwaUserSelection.None;
```

### Python
```python
# Destiny.Advanced.AwaUserSelection enumeration values
class AwaUserSelection:
    NONE = 0
    REJECTED = 1
    APPROVED = 2

# Using the enumeration
value = AwaUserSelection.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Advanced.AwaUserSelection":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2"
      ],
      "type": "integer"
  }
}
```
