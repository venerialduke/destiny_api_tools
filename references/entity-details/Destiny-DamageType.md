# Destiny.DamageType

## Entity Information
- **Entity Name**: Destiny.DamageType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing damagetype data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Kinetic |  |
| 2 | Arc |  |
| 3 | Thermal |  |
| 4 | Void |  |
| 5 | Raid |  |
| 6 | Stasis |  |
| 7 | Strand |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DamageType enumeration values
const DamageType = {
  None: 0,
  Kinetic: 1,
  Arc: 2,
  // ... more values
};

// Using the enumeration
const value = DamageType.None;
```

### Python
```python
# Destiny.DamageType enumeration values
class DamageType:
    NONE = 0
    KINETIC = 1
    ARC = 2
    # ... more values

# Using the enumeration
value = DamageType.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DamageType":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2",
          "3",
          "4",
          "5",
          "6",
          "7"
      ],
      "type": "integer"
  }
}
```
