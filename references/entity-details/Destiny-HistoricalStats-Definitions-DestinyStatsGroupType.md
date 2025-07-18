# Destiny.HistoricalStats.Definitions.DestinyStatsGroupType

## Entity Information
- **Entity Name**: Destiny.HistoricalStats.Definitions.DestinyStatsGroupType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
If the enum value is > 100, it is a "special" group that cannot be queried for directly (special cases apply to when they are returned, and are not relevant in general cases)

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | General |  |
| 2 | Weapons |  |
| 3 | Medals |  |
| 100 | ReservedGroups | This is purely to serve as the dividing line between filterable and un-filterable groups. Below this number is a group you can pass as a filter. Above it are groups used in very specific circumstances and not relevant for filtering. |
| 101 | Leaderboard | Only applicable while generating leaderboards. |
| 102 | Activity | These will *only* be consumed by GetAggregateStatsByActivity |
| 103 | UniqueWeapon | These are only consumed and returned by GetUniqueWeaponHistory |
| 104 | Internal |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.HistoricalStats.Definitions.DestinyStatsGroupType enumeration values
const DestinyStatsGroupType = {
  None: 0,
  General: 1,
  Weapons: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyStatsGroupType.None;
```

### Python
```python
# Destiny.HistoricalStats.Definitions.DestinyStatsGroupType enumeration values
class DestinyStatsGroupType:
    NONE = 0
    GENERAL = 1
    WEAPONS = 2
    # ... more values

# Using the enumeration
value = DestinyStatsGroupType.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.HistoricalStats.Definitions.DestinyStatsGroupType":   {
      "format": "int32",
      "description": "If the enum value is > 100, it is a \"special\" group that cannot be queried for directly (special cases apply to when they are returned, and are not relevant in general cases)",
      "enum": [
          "0",
          "1",
          "2",
          "3",
          "100",
          "101",
          "102",
          "103",
          "104"
      ],
      "type": "integer"
  }
}
```
