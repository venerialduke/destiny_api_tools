# FireteamFinder.DestinyFireteamFinderGetPlayerApplicationsResponse

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderGetPlayerApplicationsResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfindergetplayerapplicationsresponse data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| applications | Array[FireteamFinder.DestinyFireteamFinderApplication] | All applications that this player has sent. | No |
| nextPageToken | string | String token to request next page of results. | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderGetPlayerApplicationsResponse object
const example = {
  applications: [],
  nextPageToken: "example value",
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderGetPlayerApplicationsResponse object
example = {
    "applications": [],
    "nextPageToken": "example value",
}
```

## Related Entities
- **FireteamFinder.DestinyFireteamFinderApplication**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderGetPlayerApplicationsResponse":   {
      "type": "object",
      "properties": {
          "applications": {
              "description": "All applications that this player has sent.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/FireteamFinder.DestinyFireteamFinderApplication"
              }
          },
          "nextPageToken": {
              "description": "String token to request next page of results.",
              "type": "string"
          }
      }
  }
}
```
