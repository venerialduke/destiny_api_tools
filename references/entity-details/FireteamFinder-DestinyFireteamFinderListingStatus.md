# FireteamFinder.DestinyFireteamFinderListingStatus

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderListingStatus
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderlistingstatus data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| listingId | integer (int64) |  | No |
| listingRevision | integer (int32) |  | No |
| availableSlots | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderListingStatus object
const example = {
  listingId: 123,
  listingRevision: 123,
  availableSlots: 123,
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderListingStatus object
example = {
    "listingId": 123,
    "listingRevision": 123,
    "availableSlots": 123,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderListingStatus":   {
      "type": "object",
      "properties": {
          "listingId": {
              "format": "int64",
              "type": "integer"
          },
          "listingRevision": {
              "format": "int32",
              "type": "integer"
          },
          "availableSlots": {
              "format": "int32",
              "type": "integer"
          }
      }
  }
}
```
