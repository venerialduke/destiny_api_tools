# FireteamFinder.DestinyFireteamFinderBulkGetListingStatusResponse

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderBulkGetListingStatusResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderbulkgetlistingstatusresponse data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| listingStatus | Array[FireteamFinder.DestinyFireteamFinderListingStatus] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderBulkGetListingStatusResponse object
const example = {
  listingStatus: [],
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderBulkGetListingStatusResponse object
example = {
    "listingStatus": [],
}
```

## Related Entities
- **FireteamFinder.DestinyFireteamFinderListingStatus**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderBulkGetListingStatusResponse":   {
      "type": "object",
      "properties": {
          "listingStatus": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/FireteamFinder.DestinyFireteamFinderListingStatus"
              }
          }
      }
  }
}
```
