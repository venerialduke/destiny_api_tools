# FireteamFinder.DestinyFireteamFinderPlayerReadinessState

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderPlayerReadinessState
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing destinyfireteamfinderplayerreadinessstate data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Unknown |  |
| 1 | Reserved |  |
| 2 | Disconnected |  |
| 3 | InLobbyUnready |  |
| 4 | InLobbyReady |  |
| 5 | Summoned |  |

## Usage Examples

### JavaScript
```javascript
// FireteamFinder.DestinyFireteamFinderPlayerReadinessState enumeration values
const DestinyFireteamFinderPlayerReadinessState = {
  Unknown: 0,
  Reserved: 1,
  Disconnected: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyFireteamFinderPlayerReadinessState.Unknown;
```

### Python
```python
# FireteamFinder.DestinyFireteamFinderPlayerReadinessState enumeration values
class DestinyFireteamFinderPlayerReadinessState:
    UNKNOWN = 0
    RESERVED = 1
    DISCONNECTED = 2
    # ... more values

# Using the enumeration
value = DestinyFireteamFinderPlayerReadinessState.UNKNOWN
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderPlayerReadinessState":   {
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
