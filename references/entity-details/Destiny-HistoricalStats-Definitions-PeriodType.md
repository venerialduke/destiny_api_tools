# Destiny.HistoricalStats.Definitions.PeriodType

## Entity Information
- **Entity Name**: Destiny.HistoricalStats.Definitions.PeriodType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing periodtype data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Daily |  |
| 2 | AllTime |  |
| 3 | Activity |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.HistoricalStats.Definitions.PeriodType enumeration values
const PeriodType = {
  None: 0,
  Daily: 1,
  AllTime: 2,
  // ... more values
};

// Using the enumeration
const value = PeriodType.None;
```

### Python
```python
# Destiny.HistoricalStats.Definitions.PeriodType enumeration values
class PeriodType:
    NONE = 0
    DAILY = 1
    ALLTIME = 2
    # ... more values

# Using the enumeration
value = PeriodType.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.HistoricalStats.Definitions.PeriodType":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2",
          "3"
      ],
      "type": "integer"
  }
}
```
