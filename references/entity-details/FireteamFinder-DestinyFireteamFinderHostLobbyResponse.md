# FireteamFinder.DestinyFireteamFinderHostLobbyResponse

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderHostLobbyResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderhostlobbyresponse data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| lobbyId | integer (int64) |  | No |
| listingId | integer (int64) |  | No |
| applicationId | integer (int64) |  | No |
| offerId | integer (int64) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderHostLobbyResponse object
const example = {
  lobbyId: 123,
  listingId: 123,
  applicationId: 123,
  offerId: 123,
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderHostLobbyResponse object
example = {
    "lobbyId": 123,
    "listingId": 123,
    "applicationId": 123,
    "offerId": 123,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderHostLobbyResponse":   {
      "type": "object",
      "properties": {
          "lobbyId": {
              "format": "int64",
              "type": "integer"
          },
          "listingId": {
              "format": "int64",
              "type": "integer"
          },
          "applicationId": {
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
