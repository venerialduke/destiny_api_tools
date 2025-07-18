# Destiny.Definitions.DestinyTalentNodeStepDamageTypes

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyTalentNodeStepDamageTypes
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing destinytalentnodestepdamagetypes data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Kinetic |  |
| 2 | Arc |  |
| 4 | Solar |  |
| 8 | Void |  |
| 15 | All |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.Definitions.DestinyTalentNodeStepDamageTypes enumeration values
const DestinyTalentNodeStepDamageTypes = {
  None: 0,
  Kinetic: 1,
  Arc: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyTalentNodeStepDamageTypes.None;
```

### Python
```python
# Destiny.Definitions.DestinyTalentNodeStepDamageTypes enumeration values
class DestinyTalentNodeStepDamageTypes:
    NONE = 0
    KINETIC = 1
    ARC = 2
    # ... more values

# Using the enumeration
value = DestinyTalentNodeStepDamageTypes.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyTalentNodeStepDamageTypes":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2",
          "4",
          "8",
          "15"
      ],
      "type": "integer"
  }
}
```
