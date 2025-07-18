# Destiny.FireteamFinderOptionSearchFilterType

## Entity Information
- **Entity Name**: Destiny.FireteamFinderOptionSearchFilterType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing fireteamfinderoptionsearchfiltertype data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | All |  |
| 2 | Any |  |
| 3 | InRangeInclusive |  |
| 4 | InRangeExclusive |  |
| 5 | GreaterThan |  |
| 6 | GreaterThanOrEqualTo |  |
| 7 | LessThan |  |
| 8 | LessThanOrEqualTo |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.FireteamFinderOptionSearchFilterType enumeration values
const FireteamFinderOptionSearchFilterType = {
  None: 0,
  All: 1,
  Any: 2,
  // ... more values
};

// Using the enumeration
const value = FireteamFinderOptionSearchFilterType.None;
```

### Python
```python
# Destiny.FireteamFinderOptionSearchFilterType enumeration values
class FireteamFinderOptionSearchFilterType:
    NONE = 0
    ALL = 1
    ANY = 2
    # ... more values

# Using the enumeration
value = FireteamFinderOptionSearchFilterType.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.FireteamFinderOptionSearchFilterType":   {
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
          "8"
      ],
      "type": "integer"
  }
}
```
