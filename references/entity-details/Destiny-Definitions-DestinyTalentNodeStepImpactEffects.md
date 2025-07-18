# Destiny.Definitions.DestinyTalentNodeStepImpactEffects

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyTalentNodeStepImpactEffects
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing destinytalentnodestepimpacteffects data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | ArmorPiercing |  |
| 2 | Ricochet |  |
| 4 | Flinch |  |
| 8 | CollateralDamage |  |
| 16 | Disorient |  |
| 32 | HighlightTarget |  |
| 63 | All |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.Definitions.DestinyTalentNodeStepImpactEffects enumeration values
const DestinyTalentNodeStepImpactEffects = {
  None: 0,
  ArmorPiercing: 1,
  Ricochet: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyTalentNodeStepImpactEffects.None;
```

### Python
```python
# Destiny.Definitions.DestinyTalentNodeStepImpactEffects enumeration values
class DestinyTalentNodeStepImpactEffects:
    NONE = 0
    ARMORPIERCING = 1
    RICOCHET = 2
    # ... more values

# Using the enumeration
value = DestinyTalentNodeStepImpactEffects.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyTalentNodeStepImpactEffects":   {
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
