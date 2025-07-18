# FireteamFinder.DestinyFireteamFinderSearchListingsByClanRequest

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderSearchListingsByClanRequest
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfindersearchlistingsbyclanrequest data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| pageSize | integer (int32) |  | No |
| pageToken | string |  | No |
| lobbyState | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderSearchListingsByClanRequest object
const example = {
  pageSize: 123,
  pageToken: "example value",
  lobbyState: 123,
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderSearchListingsByClanRequest object
example = {
    "pageSize": 123,
    "pageToken": "example value",
    "lobbyState": 123,
}
```

## Related Entities
- **FireteamFinder.DestinyFireteamFinderLobbyState**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderSearchListingsByClanRequest":   {
      "type": "object",
      "properties": {
          "pageSize": {
              "format": "int32",
              "type": "integer"
          },
          "pageToken": {
              "type": "string"
          },
          "lobbyState": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/FireteamFinder.DestinyFireteamFinderLobbyState"
              }
          }
      }
  }
}
```
