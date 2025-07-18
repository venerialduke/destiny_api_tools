# Destiny.Advanced.AwaType

## Entity Information
- **Entity Name**: Destiny.Advanced.AwaType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing awatype data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | InsertPlugs | Insert plugs into sockets. |

## Usage Examples

### JavaScript
```javascript
// Destiny.Advanced.AwaType enumeration values
const AwaType = {
  None: 0,
  InsertPlugs: 1,
};

// Using the enumeration
const value = AwaType.None;
```

### Python
```python
# Destiny.Advanced.AwaType enumeration values
class AwaType:
    NONE = 0
    INSERTPLUGS = 1

# Using the enumeration
value = AwaType.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Advanced.AwaType":   {
      "format": "int32",
      "enum": [
          "0",
          "1"
      ],
      "type": "integer"
  }
}
```
