# FireteamFinder.DestinyFireteamFinderGetPlayerLobbiesResponse

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderGetPlayerLobbiesResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfindergetplayerlobbiesresponse data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| lobbies | Array[FireteamFinder.DestinyFireteamFinderLobbyResponse] | All available lobbies that this player has created or is a member of. | No |
| pageSize | integer (int32) | The number of results requested. | No |
| nextPageToken | string | A string token required to get the next page of results. This will be null or empty if there are no more results. | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderGetPlayerLobbiesResponse object
const example = {
  lobbies: [],
  pageSize: 123,
  nextPageToken: "example value",
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderGetPlayerLobbiesResponse object
example = {
    "lobbies": [],
    "pageSize": 123,
    "nextPageToken": "example value",
}
```

## Related Entities
- **FireteamFinder.DestinyFireteamFinderLobbyResponse**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderGetPlayerLobbiesResponse":   {
      "type": "object",
      "properties": {
          "lobbies": {
              "description": "All available lobbies that this player has created or is a member of.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/FireteamFinder.DestinyFireteamFinderLobbyResponse"
              }
          },
          "pageSize": {
              "format": "int32",
              "description": "The number of results requested.",
              "type": "integer"
          },
          "nextPageToken": {
              "description": "A string token required to get the next page of results. This will be null or empty if there are no more results.",
              "type": "string"
          }
      }
  }
}
```
