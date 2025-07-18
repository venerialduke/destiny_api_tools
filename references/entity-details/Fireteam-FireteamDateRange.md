# Fireteam.FireteamDateRange

## Entity Information
- **Entity Name**: Fireteam.FireteamDateRange
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: byte

## Description
API entity for fireteamdaterange operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | All |  |
| 1 | Now |  |
| 2 | TwentyFourHours |  |
| 3 | FortyEightHours |  |
| 4 | ThisWeek |  |

## Usage Examples

### JavaScript
```javascript
// Fireteam.FireteamDateRange enumeration values
const FireteamDateRange = {
  All: 0,
  Now: 1,
  TwentyFourHours: 2,
  // ... more values
};

// Using the enumeration
const value = FireteamDateRange.All;
```

### Python
```python
# Fireteam.FireteamDateRange enumeration values
class FireteamDateRange:
    ALL = 0
    NOW = 1
    TWENTYFOURHOURS = 2
    # ... more values

# Using the enumeration
value = FireteamDateRange.ALL
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "Fireteam.FireteamDateRange":   {
      "format": "byte",
      "enum": [
          "0",
          "1",
          "2",
          "3",
          "4"
      ],
      "type": "integer"
  }
}
```
