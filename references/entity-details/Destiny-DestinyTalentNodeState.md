# Destiny.DestinyTalentNodeState

## Entity Information
- **Entity Name**: Destiny.DestinyTalentNodeState
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing destinytalentnodestate data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Invalid |  |
| 1 | CanUpgrade |  |
| 2 | NoPoints |  |
| 3 | NoPrerequisites |  |
| 4 | NoSteps |  |
| 5 | NoUnlock |  |
| 6 | NoMaterial |  |
| 7 | NoGridLevel |  |
| 8 | SwappingLocked |  |
| 9 | MustSwap |  |
| 10 | Complete |  |
| 11 | Unknown |  |
| 12 | CreationOnly |  |
| 13 | Hidden |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyTalentNodeState enumeration values
const DestinyTalentNodeState = {
  Invalid: 0,
  CanUpgrade: 1,
  NoPoints: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyTalentNodeState.Invalid;
```

### Python
```python
# Destiny.DestinyTalentNodeState enumeration values
class DestinyTalentNodeState:
    INVALID = 0
    CANUPGRADE = 1
    NOPOINTS = 2
    # ... more values

# Using the enumeration
value = DestinyTalentNodeState.INVALID
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyTalentNodeState":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2",
          "3",
          "4",
          "5",
          "6",
          "7",
          "8",
          "9",
          "10",
          "11",
          "12",
          "13"
      ],
      "type": "integer"
  }
}
```
