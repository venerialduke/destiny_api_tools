# Destiny.DestinyAmmunitionType

## Entity Information
- **Entity Name**: Destiny.DestinyAmmunitionType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing destinyammunitiontype data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Primary |  |
| 2 | Special |  |
| 3 | Heavy |  |
| 4 | Unknown |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyAmmunitionType enumeration values
const DestinyAmmunitionType = {
  None: 0,
  Primary: 1,
  Special: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyAmmunitionType.None;
```

### Python
```python
# Destiny.DestinyAmmunitionType enumeration values
class DestinyAmmunitionType:
    NONE = 0
    PRIMARY = 1
    SPECIAL = 2
    # ... more values

# Using the enumeration
value = DestinyAmmunitionType.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyAmmunitionType":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2",
          "3",
          "4"
      ],
      "type": "integer"
  }
}
```
