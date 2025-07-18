# FireteamFinder.DestinyFireteamFinderListingFilter

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderListingFilter
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderlistingfilter data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| listingValue | FireteamFinder.DestinyFireteamFinderListingValue |  | No |
| rangeType | integer |  | No |
| matchType | integer |  | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderListingFilter object
const example = {
  listingValue: null,
  rangeType: 123,
  matchType: 123,
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderListingFilter object
example = {
    "listingValue": None,
    "rangeType": 123,
    "matchType": 123,
}
```

## Related Entities
- **FireteamFinder.DestinyFireteamFinderListingFilterMatchType**: Referenced in this entity
- **FireteamFinder.DestinyFireteamFinderListingFilterRangeType**: Referenced in this entity
- **FireteamFinder.DestinyFireteamFinderListingValue**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderListingFilter":   {
      "type": "object",
      "properties": {
          "listingValue": {
              "$ref": "#/definitions/FireteamFinder.DestinyFireteamFinderListingValue"
          },
          "rangeType": {
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/FireteamFinder.DestinyFireteamFinderListingFilterRangeType"
              }
          },
          "matchType": {
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/FireteamFinder.DestinyFireteamFinderListingFilterMatchType"
              }
          }
      }
  }
}
```
