# FireteamFinder.DestinyFireteamFinderLobbyPlayer

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderLobbyPlayer
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderlobbyplayer data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| playerId | FireteamFinder.DestinyFireteamFinderPlayerId |  | No |
| referralToken | integer (int64) |  | No |
| state | integer (int32) |  | No |
| offerId | integer (int64) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderLobbyPlayer object
const example = {
  playerId: null,
  referralToken: 123,
  state: 123,
  offerId: 123,
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderLobbyPlayer object
example = {
    "playerId": None,
    "referralToken": 123,
    "state": 123,
    "offerId": 123,
}
```

## Related Entities
- **FireteamFinder.DestinyFireteamFinderPlayerId**: Referenced in this entity
- **FireteamFinder.DestinyFireteamFinderPlayerReadinessState**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderLobbyPlayer":   {
      "type": "object",
      "properties": {
          "playerId": {
              "$ref": "#/definitions/FireteamFinder.DestinyFireteamFinderPlayerId"
          },
          "referralToken": {
              "format": "int64",
              "type": "integer"
          },
          "state": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/FireteamFinder.DestinyFireteamFinderPlayerReadinessState"
              }
          },
          "offerId": {
              "format": "int64",
              "type": "integer"
          }
      }
  }
}
```
