# FireteamFinder.DestinyFireteamFinderLobbyPrivacyScope

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderLobbyPrivacyScope
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing destinyfireteamfinderlobbyprivacyscope data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Unknown |  |
| 1 | Open |  |
| 2 | Applications |  |
| 3 | Clan |  |
| 4 | Friends |  |

## Usage Examples

### JavaScript
```javascript
// FireteamFinder.DestinyFireteamFinderLobbyPrivacyScope enumeration values
const DestinyFireteamFinderLobbyPrivacyScope = {
  Unknown: 0,
  Open: 1,
  Applications: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyFireteamFinderLobbyPrivacyScope.Unknown;
```

### Python
```python
# FireteamFinder.DestinyFireteamFinderLobbyPrivacyScope enumeration values
class DestinyFireteamFinderLobbyPrivacyScope:
    UNKNOWN = 0
    OPEN = 1
    APPLICATIONS = 2
    # ... more values

# Using the enumeration
value = DestinyFireteamFinderLobbyPrivacyScope.UNKNOWN
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderLobbyPrivacyScope":   {
      "format": "int32",
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
