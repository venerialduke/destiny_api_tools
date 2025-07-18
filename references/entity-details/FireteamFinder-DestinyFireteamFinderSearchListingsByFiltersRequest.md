# FireteamFinder.DestinyFireteamFinderSearchListingsByFiltersRequest

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderSearchListingsByFiltersRequest
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfindersearchlistingsbyfiltersrequest data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| filters | Array[FireteamFinder.DestinyFireteamFinderListingFilter] |  | No |
| pageSize | integer (int32) |  | No |
| pageToken | string |  | No |
| lobbyState | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderSearchListingsByFiltersRequest object
const example = {
  filters: [],
  pageSize: 123,
  pageToken: "example value",
  lobbyState: 123,
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderSearchListingsByFiltersRequest object
example = {
    "filters": [],
    "pageSize": 123,
    "pageToken": "example value",
    "lobbyState": 123,
}
```

## Related Entities
- **FireteamFinder.DestinyFireteamFinderListingFilter**: Referenced in this entity
- **FireteamFinder.DestinyFireteamFinderLobbyState**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderSearchListingsByFiltersRequest":   {
      "type": "object",
      "properties": {
          "filters": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/FireteamFinder.DestinyFireteamFinderListingFilter"
              }
          },
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
