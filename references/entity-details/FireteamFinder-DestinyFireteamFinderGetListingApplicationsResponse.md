# FireteamFinder.DestinyFireteamFinderGetListingApplicationsResponse

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderGetListingApplicationsResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfindergetlistingapplicationsresponse data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| applications | Array[FireteamFinder.DestinyFireteamFinderApplication] |  | No |
| pageSize | integer (int32) |  | No |
| nextPageToken | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderGetListingApplicationsResponse object
const example = {
  applications: [],
  pageSize: 123,
  nextPageToken: "example value",
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderGetListingApplicationsResponse object
example = {
    "applications": [],
    "pageSize": 123,
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
  "FireteamFinder.DestinyFireteamFinderGetListingApplicationsResponse":   {
      "type": "object",
      "properties": {
          "applications": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/FireteamFinder.DestinyFireteamFinderApplication"
              }
          },
          "pageSize": {
              "format": "int32",
              "type": "integer"
          },
          "nextPageToken": {
              "type": "string"
          }
      }
  }
}
```
