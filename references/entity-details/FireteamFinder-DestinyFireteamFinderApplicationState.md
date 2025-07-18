# FireteamFinder.DestinyFireteamFinderApplicationState

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderApplicationState
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing destinyfireteamfinderapplicationstate data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Unknown |  |
| 1 | WaitingForApplicants |  |
| 2 | WaitingForLobbyOwner |  |
| 3 | Accepted |  |
| 4 | Rejected |  |
| 5 | Deleted |  |
| 6 | Expired |  |

## Usage Examples

### JavaScript
```javascript
// FireteamFinder.DestinyFireteamFinderApplicationState enumeration values
const DestinyFireteamFinderApplicationState = {
  Unknown: 0,
  WaitingForApplicants: 1,
  WaitingForLobbyOwner: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyFireteamFinderApplicationState.Unknown;
```

### Python
```python
# FireteamFinder.DestinyFireteamFinderApplicationState enumeration values
class DestinyFireteamFinderApplicationState:
    UNKNOWN = 0
    WAITINGFORAPPLICANTS = 1
    WAITINGFORLOBBYOWNER = 2
    # ... more values

# Using the enumeration
value = DestinyFireteamFinderApplicationState.UNKNOWN
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderApplicationState":   {
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
