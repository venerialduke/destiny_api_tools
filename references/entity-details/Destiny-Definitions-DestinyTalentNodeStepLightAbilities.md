# Destiny.Definitions.DestinyTalentNodeStepLightAbilities

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyTalentNodeStepLightAbilities
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing destinytalentnodesteplightabilities data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Grenades |  |
| 2 | Melee |  |
| 4 | MovementModes |  |
| 8 | Orbs |  |
| 16 | SuperEnergy |  |
| 32 | SuperMods |  |
| 63 | All |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.Definitions.DestinyTalentNodeStepLightAbilities enumeration values
const DestinyTalentNodeStepLightAbilities = {
  None: 0,
  Grenades: 1,
  Melee: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyTalentNodeStepLightAbilities.None;
```

### Python
```python
# Destiny.Definitions.DestinyTalentNodeStepLightAbilities enumeration values
class DestinyTalentNodeStepLightAbilities:
    NONE = 0
    GRENADES = 1
    MELEE = 2
    # ... more values

# Using the enumeration
value = DestinyTalentNodeStepLightAbilities.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyTalentNodeStepLightAbilities":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2",
          "4",
          "8",
          "16",
          "32",
          "63"
      ],
      "type": "integer"
  }
}
```
