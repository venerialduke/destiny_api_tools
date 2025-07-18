# FireteamFinder.DestinyFireteamFinderListingFilterRangeType

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderListingFilterRangeType
- **Entity Type**: Enumeration
- **Base Type**: integer

## Description
Destiny API entity representing destinyfireteamfinderlistingfilterrangetype data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Unknown |  |
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
// FireteamFinder.DestinyFireteamFinderListingFilterRangeType enumeration values
const DestinyFireteamFinderListingFilterRangeType = {
  Unknown: 0,
  All: 1,
  Any: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyFireteamFinderListingFilterRangeType.Unknown;
```

### Python
```python
# FireteamFinder.DestinyFireteamFinderListingFilterRangeType enumeration values
class DestinyFireteamFinderListingFilterRangeType:
    UNKNOWN = 0
    ALL = 1
    ANY = 2
    # ... more values

# Using the enumeration
value = DestinyFireteamFinderListingFilterRangeType.UNKNOWN
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderListingFilterRangeType":   {
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
