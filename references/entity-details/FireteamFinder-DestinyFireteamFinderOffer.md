# FireteamFinder.DestinyFireteamFinderOffer

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderOffer
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderoffer data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| offerId | integer (int64) |  | No |
| lobbyId | integer (int64) |  | No |
| revision | integer (int32) |  | No |
| state | integer (int32) |  | No |
| targetId | FireteamFinder.DestinyFireteamFinderPlayerId |  | No |
| applicationId | integer (int64) |  | No |
| createdDateTime | string (date-time) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderOffer object
const example = {
  offerId: 123,
  lobbyId: 123,
  revision: 123,
  state: 123,
  targetId: null,
  // ... more properties
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderOffer object
example = {
    "offerId": 123,
    "lobbyId": 123,
    "revision": 123,
    "state": 123,
    "targetId": None,
    # ... more properties
}
```

## Related Entities
- **FireteamFinder.DestinyFireteamFinderOfferState**: Referenced in this entity
- **FireteamFinder.DestinyFireteamFinderPlayerId**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderOffer":   {
      "type": "object",
      "properties": {
          "offerId": {
              "format": "int64",
              "type": "integer"
          },
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
                  "$ref": "#/components/schemas/FireteamFinder.DestinyFireteamFinderOfferState"
              }
          },
          "targetId": {
              "$ref": "#/definitions/FireteamFinder.DestinyFireteamFinderPlayerId"
          },
          "applicationId": {
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
