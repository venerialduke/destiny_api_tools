# Destiny.HistoricalStats.Definitions.UnitType

## Entity Information
- **Entity Name**: Destiny.HistoricalStats.Definitions.UnitType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing unittype data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Count | Indicates the statistic is a simple count of something. |
| 2 | PerGame | Indicates the statistic is a per game average. |
| 3 | Seconds | Indicates the number of seconds |
| 4 | Points | Indicates the number of points earned |
| 5 | Team | Values represents a team ID |
| 6 | Distance | Values represents a distance (units to-be-determined) |
| 7 | Percent | Ratio represented as a whole value from 0 to 100. |
| 8 | Ratio | Ratio of something, shown with decimal places |
| 9 | Boolean | True or false |
| 10 | WeaponType | The stat is actually a weapon type. |
| 11 | Standing | Indicates victory, defeat, or something in between. |
| 12 | Milliseconds | Number of milliseconds some event spanned. For example, race time, or lap time. |
| 13 | CompletionReason | The value is a enumeration of the Completion Reason type. |

## Usage Examples

### JavaScript
```javascript
// Destiny.HistoricalStats.Definitions.UnitType enumeration values
const UnitType = {
  None: 0,
  Count: 1,
  PerGame: 2,
  // ... more values
};

// Using the enumeration
const value = UnitType.None;
```

### Python
```python
# Destiny.HistoricalStats.Definitions.UnitType enumeration values
class UnitType:
    NONE = 0
    COUNT = 1
    PERGAME = 2
    # ... more values

# Using the enumeration
value = UnitType.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.HistoricalStats.Definitions.UnitType":   {
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
