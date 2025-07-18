# FireteamFinder.DestinyFireteamFinderApplyToListingResponse

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderApplyToListingResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderapplytolistingresponse data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| isApplied | boolean |  | No |
| application | FireteamFinder.DestinyFireteamFinderApplication |  | No |
| listing | FireteamFinder.DestinyFireteamFinderListing |  | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderApplyToListingResponse object
const example = {
  isApplied: true,
  application: null,
  listing: null,
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderApplyToListingResponse object
example = {
    "isApplied": True,
    "application": None,
    "listing": None,
}
```

## Related Entities
- **FireteamFinder.DestinyFireteamFinderApplication**: Referenced in this entity
- **FireteamFinder.DestinyFireteamFinderListing**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderApplyToListingResponse":   {
      "type": "object",
      "properties": {
          "isApplied": {
              "type": "boolean"
          },
          "application": {
              "$ref": "#/definitions/FireteamFinder.DestinyFireteamFinderApplication"
          },
          "listing": {
              "$ref": "#/definitions/FireteamFinder.DestinyFireteamFinderListing"
          }
      }
  }
}
```
