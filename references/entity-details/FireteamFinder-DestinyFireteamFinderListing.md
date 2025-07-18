# FireteamFinder.DestinyFireteamFinderListing

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderListing
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderlisting data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| listingId | integer (int64) |  | No |
| revision | integer (int32) |  | No |
| ownerId | FireteamFinder.DestinyFireteamFinderPlayerId |  | No |
| settings | FireteamFinder.DestinyFireteamFinderLobbySettings |  | No |
| availableSlots | integer (int32) |  | No |
| lobbyId | integer (int64) |  | No |
| lobbyState | integer (int32) |  | No |
| createdDateTime | string (date-time) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderListing object
const example = {
  listingId: 123,
  revision: 123,
  ownerId: null,
  settings: null,
  availableSlots: 123,
  // ... more properties
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderListing object
example = {
    "listingId": 123,
    "revision": 123,
    "ownerId": None,
    "settings": None,
    "availableSlots": 123,
    # ... more properties
}
```

## Related Entities
- **FireteamFinder.DestinyFireteamFinderLobbySettings**: Referenced in this entity
- **FireteamFinder.DestinyFireteamFinderLobbyState**: Referenced in this entity
- **FireteamFinder.DestinyFireteamFinderPlayerId**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderListing":   {
      "type": "object",
      "properties": {
          "listingId": {
              "format": "int64",
              "type": "integer"
          },
          "revision": {
              "format": "int32",
              "type": "integer"
          },
          "ownerId": {
              "$ref": "#/definitions/FireteamFinder.DestinyFireteamFinderPlayerId"
          },
          "settings": {
              "$ref": "#/definitions/FireteamFinder.DestinyFireteamFinderLobbySettings"
          },
          "availableSlots": {
              "format": "int32",
              "type": "integer"
          },
          "lobbyId": {
              "format": "int64",
              "type": "integer"
          },
          "lobbyState": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/FireteamFinder.DestinyFireteamFinderLobbyState"
              }
          },
          "createdDateTime": {
              "format": "date-time",
              "type": "string"
          }
      }
  }
}
```
