# Destiny.DestinyActivityNavPointType

## Entity Information
- **Entity Name**: Destiny.DestinyActivityNavPointType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing destinyactivitynavpointtype data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Inactive |  |
| 1 | PrimaryObjective |  |
| 2 | SecondaryObjective |  |
| 3 | TravelObjective |  |
| 4 | PublicEventObjective |  |
| 5 | AmmoCache |  |
| 6 | PointTypeFlag |  |
| 7 | CapturePoint |  |
| 8 | DefensiveEncounter |  |
| 9 | GhostInteraction |  |
| 10 | KillAi |  |
| 11 | QuestItem |  |
| 12 | PatrolMission |  |
| 13 | Incoming |  |
| 14 | ArenaObjective |  |
| 15 | AutomationHint |  |
| 16 | TrackedQuest |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyActivityNavPointType enumeration values
const DestinyActivityNavPointType = {
  Inactive: 0,
  PrimaryObjective: 1,
  SecondaryObjective: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyActivityNavPointType.Inactive;
```

### Python
```python
# Destiny.DestinyActivityNavPointType enumeration values
class DestinyActivityNavPointType:
    INACTIVE = 0
    PRIMARYOBJECTIVE = 1
    SECONDARYOBJECTIVE = 2
    # ... more values

# Using the enumeration
value = DestinyActivityNavPointType.INACTIVE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyActivityNavPointType":   {
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
          "13",
          "14",
          "15",
          "16"
      ],
      "type": "integer"
  }
}
```
