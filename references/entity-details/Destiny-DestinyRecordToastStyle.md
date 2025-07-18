# Destiny.DestinyRecordToastStyle

## Entity Information
- **Entity Name**: Destiny.DestinyRecordToastStyle
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing destinyrecordtoaststyle data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Record |  |
| 2 | Lore |  |
| 3 | Badge |  |
| 4 | MetaRecord |  |
| 5 | MedalComplete |  |
| 6 | SeasonChallengeComplete |  |
| 7 | GildedTitleComplete |  |
| 8 | CraftingRecipeUnlocked |  |
| 9 | ToastGuardianRankDetails |  |
| 10 | PathfinderObjectiveCompleteRituals |  |
| 11 | PathfinderObjectiveCompleteSchism |  |
| 12 | PathfinderObjectiveCompletePvp |  |
| 13 | PathfinderObjectiveCompleteStrikes |  |
| 14 | PathfinderObjectiveCompleteGambit |  |
| 15 | SeasonWeeklyComplete |  |
| 16 | SeasonDailyComplete |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyRecordToastStyle enumeration values
const DestinyRecordToastStyle = {
  None: 0,
  Record: 1,
  Lore: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyRecordToastStyle.None;
```

### Python
```python
# Destiny.DestinyRecordToastStyle enumeration values
class DestinyRecordToastStyle:
    NONE = 0
    RECORD = 1
    LORE = 2
    # ... more values

# Using the enumeration
value = DestinyRecordToastStyle.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyRecordToastStyle":   {
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
