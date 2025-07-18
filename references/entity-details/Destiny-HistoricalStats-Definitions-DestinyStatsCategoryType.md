# Destiny.HistoricalStats.Definitions.DestinyStatsCategoryType

## Entity Information
- **Entity Name**: Destiny.HistoricalStats.Definitions.DestinyStatsCategoryType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing destinystatscategorytype data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Kills |  |
| 2 | Assists |  |
| 3 | Deaths |  |
| 4 | Criticals |  |
| 5 | KDa |  |
| 6 | KD |  |
| 7 | Score |  |
| 8 | Entered |  |
| 9 | TimePlayed |  |
| 10 | MedalWins |  |
| 11 | MedalGame |  |
| 12 | MedalSpecialKills |  |
| 13 | MedalSprees |  |
| 14 | MedalMultiKills |  |
| 15 | MedalAbilities |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.HistoricalStats.Definitions.DestinyStatsCategoryType enumeration values
const DestinyStatsCategoryType = {
  None: 0,
  Kills: 1,
  Assists: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyStatsCategoryType.None;
```

### Python
```python
# Destiny.HistoricalStats.Definitions.DestinyStatsCategoryType enumeration values
class DestinyStatsCategoryType:
    NONE = 0
    KILLS = 1
    ASSISTS = 2
    # ... more values

# Using the enumeration
value = DestinyStatsCategoryType.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.HistoricalStats.Definitions.DestinyStatsCategoryType":   {
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
          "15"
      ],
      "type": "integer"
  }
}
```
