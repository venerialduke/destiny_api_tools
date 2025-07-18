# FireteamFinder.DestinyFireteamFinderSearchListingsByFiltersResponse

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderSearchListingsByFiltersResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfindersearchlistingsbyfiltersresponse data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| listings | Array[FireteamFinder.DestinyFireteamFinderListing] |  | No |
| pageToken | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderSearchListingsByFiltersResponse object
const example = {
  listings: [],
  pageToken: "example value",
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderSearchListingsByFiltersResponse object
example = {
    "listings": [],
    "pageToken": "example value",
}
```

## Related Entities
- **FireteamFinder.DestinyFireteamFinderListing**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderSearchListingsByFiltersResponse":   {
      "type": "object",
      "properties": {
          "listings": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/FireteamFinder.DestinyFireteamFinderListing"
              }
          },
          "pageToken": {
              "type": "string"
          }
      }
  }
}
```
