# FireteamFinder.DestinyFireteamFinderOfferState

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderOfferState
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing destinyfireteamfinderofferstate data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Unknown |  |
| 1 | Pending |  |
| 2 | Accepted |  |
| 3 | Rejected |  |
| 4 | Deleted |  |
| 5 | Expired |  |

## Usage Examples

### JavaScript
```javascript
// FireteamFinder.DestinyFireteamFinderOfferState enumeration values
const DestinyFireteamFinderOfferState = {
  Unknown: 0,
  Pending: 1,
  Accepted: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyFireteamFinderOfferState.Unknown;
```

### Python
```python
# FireteamFinder.DestinyFireteamFinderOfferState enumeration values
class DestinyFireteamFinderOfferState:
    UNKNOWN = 0
    PENDING = 1
    ACCEPTED = 2
    # ... more values

# Using the enumeration
value = DestinyFireteamFinderOfferState.UNKNOWN
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderOfferState":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2",
          "3",
          "4",
          "5"
      ],
      "type": "integer"
  }
}
```
