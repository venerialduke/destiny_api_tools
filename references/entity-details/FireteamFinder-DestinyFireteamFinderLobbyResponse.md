# FireteamFinder.DestinyFireteamFinderLobbyResponse

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderLobbyResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderlobbyresponse data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| lobbyId | integer (int64) |  | No |
| revision | integer (int32) |  | No |
| state | integer (int32) |  | No |
| owner | FireteamFinder.DestinyFireteamFinderPlayerId |  | No |
| settings | FireteamFinder.DestinyFireteamFinderLobbySettings |  | No |
| players | Array[FireteamFinder.DestinyFireteamFinderLobbyPlayer] |  | No |
| listingId | integer (int64) |  | No |
| createdDateTime | string (date-time) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderLobbyResponse object
const example = {
  lobbyId: 123,
  revision: 123,
  state: 123,
  owner: null,
  settings: null,
  // ... more properties
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderLobbyResponse object
example = {
    "lobbyId": 123,
    "revision": 123,
    "state": 123,
    "owner": None,
    "settings": None,
    # ... more properties
}
```

## Related Entities
- **FireteamFinder.DestinyFireteamFinderLobbyPlayer**: Referenced in this entity
- **FireteamFinder.DestinyFireteamFinderLobbySettings**: Referenced in this entity
- **FireteamFinder.DestinyFireteamFinderLobbyState**: Referenced in this entity
- **FireteamFinder.DestinyFireteamFinderPlayerId**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderLobbyResponse":   {
      "type": "object",
      "properties": {
          "lobbyId": {
              "format": "int64",
              "type": "integer"
          },
          "revision": {
              "format": "int32",
              "type": "integer"
          },
          "state": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/FireteamFinder.DestinyFireteamFinderLobbyState"
              }
          },
          "owner": {
              "$ref": "#/definitions/FireteamFinder.DestinyFireteamFinderPlayerId"
          },
          "settings": {
              "$ref": "#/definitions/FireteamFinder.DestinyFireteamFinderLobbySettings"
          },
          "players": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/FireteamFinder.DestinyFireteamFinderLobbyPlayer"
              }
          },
          "listingId": {
              "format": "int64",
              "type": "integer"
          },
          "createdDateTime": {
              "format": "date-time",
              "type": "string"
          }
      }
  }
}
```
