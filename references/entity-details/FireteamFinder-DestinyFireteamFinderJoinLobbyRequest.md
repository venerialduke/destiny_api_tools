# FireteamFinder.DestinyFireteamFinderJoinLobbyRequest

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderJoinLobbyRequest
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderjoinlobbyrequest data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| lobbyId | integer (int64) |  | No |
| offerId | integer (int64) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderJoinLobbyRequest object
const example = {
  lobbyId: 123,
  offerId: 123,
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderJoinLobbyRequest object
example = {
    "lobbyId": 123,
    "offerId": 123,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderJoinLobbyRequest":   {
      "type": "object",
      "properties": {
          "lobbyId": {
              "format": "int64",
              "type": "integer"
          },
          "offerId": {
              "format": "int64",
              "type": "integer"
          }
      }
  }
}
```
