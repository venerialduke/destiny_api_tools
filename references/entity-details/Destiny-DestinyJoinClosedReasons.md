# Destiny.DestinyJoinClosedReasons

## Entity Information
- **Entity Name**: Destiny.DestinyJoinClosedReasons
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
A Flags enumeration representing the reasons why a person can't join this user's fireteam.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | InMatchmaking | The user is currently in matchmaking. |
| 2 | Loading | The user is currently in a loading screen. |
| 4 | SoloMode | The user is in an activity that requires solo play. |
| 8 | InternalReasons | The user can't be joined for one of a variety of internal reasons. Basically, the game can't let you join at this time, but for reasons that aren't under the control of this user. |
| 16 | DisallowedByGameState | The user's current activity/quest/other transitory game state is preventing joining. |
| 32768 | Offline | The user appears to be offline. |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyJoinClosedReasons enumeration values
const DestinyJoinClosedReasons = {
  None: 0,
  InMatchmaking: 1,
  Loading: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyJoinClosedReasons.None;
```

### Python
```python
# Destiny.DestinyJoinClosedReasons enumeration values
class DestinyJoinClosedReasons:
    NONE = 0
    INMATCHMAKING = 1
    LOADING = 2
    # ... more values

# Using the enumeration
value = DestinyJoinClosedReasons.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyJoinClosedReasons":   {
      "format": "int32",
      "description": "A Flags enumeration representing the reasons why a person can't join this user's fireteam.",
      "enum": [
          "0",
          "1",
          "2",
          "4",
          "8",
          "16",
          "32768"
      ],
      "type": "integer"
  }
}
```
