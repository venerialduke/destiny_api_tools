# FireteamFinder.DestinyFireteamFinderListingFilterMatchType

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderListingFilterMatchType
- **Entity Type**: Enumeration
- **Base Type**: integer

## Description
Destiny API entity representing destinyfireteamfinderlistingfiltermatchtype data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Unknown |  |
| 1 | MustNot |  |
| 2 | Should |  |
| 3 | Filter |  |

## Usage Examples

### JavaScript
```javascript
// FireteamFinder.DestinyFireteamFinderListingFilterMatchType enumeration values
const DestinyFireteamFinderListingFilterMatchType = {
  Unknown: 0,
  MustNot: 1,
  Should: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyFireteamFinderListingFilterMatchType.Unknown;
```

### Python
```python
# FireteamFinder.DestinyFireteamFinderListingFilterMatchType enumeration values
class DestinyFireteamFinderListingFilterMatchType:
    UNKNOWN = 0
    MUSTNOT = 1
    SHOULD = 2
    # ... more values

# Using the enumeration
value = DestinyFireteamFinderListingFilterMatchType.UNKNOWN
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderListingFilterMatchType":   {
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
