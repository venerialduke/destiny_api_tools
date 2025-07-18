# Destiny.Definitions.DestinyTalentNodeStepWeaponPerformances

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyTalentNodeStepWeaponPerformances
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing destinytalentnodestepweaponperformances data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | RateOfFire |  |
| 2 | Damage |  |
| 4 | Accuracy |  |
| 8 | Range |  |
| 16 | Zoom |  |
| 32 | Recoil |  |
| 64 | Ready |  |
| 128 | Reload |  |
| 256 | HairTrigger |  |
| 512 | AmmoAndMagazine |  |
| 1024 | TrackingAndDetonation |  |
| 2048 | ShotgunSpread |  |
| 4096 | ChargeTime |  |
| 8191 | All |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.Definitions.DestinyTalentNodeStepWeaponPerformances enumeration values
const DestinyTalentNodeStepWeaponPerformances = {
  None: 0,
  RateOfFire: 1,
  Damage: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyTalentNodeStepWeaponPerformances.None;
```

### Python
```python
# Destiny.Definitions.DestinyTalentNodeStepWeaponPerformances enumeration values
class DestinyTalentNodeStepWeaponPerformances:
    NONE = 0
    RATEOFFIRE = 1
    DAMAGE = 2
    # ... more values

# Using the enumeration
value = DestinyTalentNodeStepWeaponPerformances.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyTalentNodeStepWeaponPerformances":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2",
          "4",
          "8",
          "16",
          "32",
          "64",
          "128",
          "256",
          "512",
          "1024",
          "2048",
          "4096",
          "8191"
      ],
      "type": "integer"
  }
}
```
