# FireteamFinder.DestinyFireteamFinderRespondToOfferResponse

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderRespondToOfferResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderrespondtoofferresponse data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| offerId | integer (int64) |  | No |
| revision | integer (int32) |  | No |
| state | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderRespondToOfferResponse object
const example = {
  offerId: 123,
  revision: 123,
  state: 123,
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderRespondToOfferResponse object
example = {
    "offerId": 123,
    "revision": 123,
    "state": 123,
}
```

## Related Entities
- **FireteamFinder.DestinyFireteamFinderOfferState**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderRespondToOfferResponse":   {
      "type": "object",
      "properties": {
          "offerId": {
              "format": "int64",
              "type": "integer"
          },
          "revision": {
              "format": "int32",
              "type": "integer"
          },
          "state": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/FireteamFinder.DestinyFireteamFinderOfferState"
              }
          }
      }
  }
}
```
