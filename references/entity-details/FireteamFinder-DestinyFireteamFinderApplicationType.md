# FireteamFinder.DestinyFireteamFinderApplicationType

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderApplicationType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing destinyfireteamfinderapplicationtype data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Unknown |  |
| 1 | Creator |  |
| 2 | Search |  |
| 3 | Invite |  |
| 4 | Friend |  |
| 5 | Encounter |  |
| 6 | Public |  |

## Usage Examples

### JavaScript
```javascript
// FireteamFinder.DestinyFireteamFinderApplicationType enumeration values
const DestinyFireteamFinderApplicationType = {
  Unknown: 0,
  Creator: 1,
  Search: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyFireteamFinderApplicationType.Unknown;
```

### Python
```python
# FireteamFinder.DestinyFireteamFinderApplicationType enumeration values
class DestinyFireteamFinderApplicationType:
    UNKNOWN = 0
    CREATOR = 1
    SEARCH = 2
    # ... more values

# Using the enumeration
value = DestinyFireteamFinderApplicationType.UNKNOWN
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderApplicationType":   {
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
