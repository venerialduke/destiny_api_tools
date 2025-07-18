# Destiny.DestinyActivitySkullDynamicUse

## Entity Information
- **Entity Name**: Destiny.DestinyActivitySkullDynamicUse
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing destinyactivityskulldynamicuse data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Unknown |  |
| 1 | Allowed |  |
| 2 | Disallowed |  |
| 3 | Count |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyActivitySkullDynamicUse enumeration values
const DestinyActivitySkullDynamicUse = {
  Unknown: 0,
  Allowed: 1,
  Disallowed: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyActivitySkullDynamicUse.Unknown;
```

### Python
```python
# Destiny.DestinyActivitySkullDynamicUse enumeration values
class DestinyActivitySkullDynamicUse:
    UNKNOWN = 0
    ALLOWED = 1
    DISALLOWED = 2
    # ... more values

# Using the enumeration
value = DestinyActivitySkullDynamicUse.UNKNOWN
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyActivitySkullDynamicUse":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2",
          "3"
      ],
      "type": "integer"
  }
}
```
