# Destiny.Definitions.DestinyTalentNodeStepGuardianAttributes

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyTalentNodeStepGuardianAttributes
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing destinytalentnodestepguardianattributes data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Stats |  |
| 2 | Shields |  |
| 4 | Health |  |
| 8 | Revive |  |
| 16 | AimUnderFire |  |
| 32 | Radar |  |
| 64 | Invisibility |  |
| 128 | Reputations |  |
| 255 | All |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.Definitions.DestinyTalentNodeStepGuardianAttributes enumeration values
const DestinyTalentNodeStepGuardianAttributes = {
  None: 0,
  Stats: 1,
  Shields: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyTalentNodeStepGuardianAttributes.None;
```

### Python
```python
# Destiny.Definitions.DestinyTalentNodeStepGuardianAttributes enumeration values
class DestinyTalentNodeStepGuardianAttributes:
    NONE = 0
    STATS = 1
    SHIELDS = 2
    # ... more values

# Using the enumeration
value = DestinyTalentNodeStepGuardianAttributes.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyTalentNodeStepGuardianAttributes":   {
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
          "255"
      ],
      "type": "integer"
  }
}
```
