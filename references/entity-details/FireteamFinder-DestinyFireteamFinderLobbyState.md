# FireteamFinder.DestinyFireteamFinderLobbyState

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderLobbyState
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing destinyfireteamfinderlobbystate data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Unknown |  |
| 1 | Inactive |  |
| 2 | Active |  |
| 3 | Expired |  |
| 4 | Closed |  |
| 5 | Canceled |  |
| 6 | Deleted |  |

## Usage Examples

### JavaScript
```javascript
// FireteamFinder.DestinyFireteamFinderLobbyState enumeration values
const DestinyFireteamFinderLobbyState = {
  Unknown: 0,
  Inactive: 1,
  Active: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyFireteamFinderLobbyState.Unknown;
```

### Python
```python
# FireteamFinder.DestinyFireteamFinderLobbyState enumeration values
class DestinyFireteamFinderLobbyState:
    UNKNOWN = 0
    INACTIVE = 1
    ACTIVE = 2
    # ... more values

# Using the enumeration
value = DestinyFireteamFinderLobbyState.UNKNOWN
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderLobbyState":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2",
          "3",
          "4",
          "5",
          "6"
      ],
      "type": "integer"
  }
}
```
