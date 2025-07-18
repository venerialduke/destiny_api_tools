# FireteamFinder.DestinyFireteamFinderLobbyListingReference

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderLobbyListingReference
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderlobbylistingreference data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| lobbyId | integer (int64) |  | No |
| listingId | integer (int64) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderLobbyListingReference object
const example = {
  lobbyId: 123,
  listingId: 123,
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderLobbyListingReference object
example = {
    "lobbyId": 123,
    "listingId": 123,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderLobbyListingReference":   {
      "type": "object",
      "properties": {
          "lobbyId": {
              "format": "int64",
              "type": "integer"
          },
          "listingId": {
              "format": "int64",
              "type": "integer"
          }
      }
  }
}
```
