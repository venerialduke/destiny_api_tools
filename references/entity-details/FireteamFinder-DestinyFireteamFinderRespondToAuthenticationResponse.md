# FireteamFinder.DestinyFireteamFinderRespondToAuthenticationResponse

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderRespondToAuthenticationResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderrespondtoauthenticationresponse data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| applicationId | integer (int64) |  | No |
| applicationRevision | integer (int32) |  | No |
| offer | FireteamFinder.DestinyFireteamFinderOffer |  | No |
| listing | FireteamFinder.DestinyFireteamFinderListing |  | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderRespondToAuthenticationResponse object
const example = {
  applicationId: 123,
  applicationRevision: 123,
  offer: null,
  listing: null,
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderRespondToAuthenticationResponse object
example = {
    "applicationId": 123,
    "applicationRevision": 123,
    "offer": None,
    "listing": None,
}
```

## Related Entities
- **FireteamFinder.DestinyFireteamFinderListing**: Referenced in this entity
- **FireteamFinder.DestinyFireteamFinderOffer**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderRespondToAuthenticationResponse":   {
      "type": "object",
      "properties": {
          "applicationId": {
              "format": "int64",
              "type": "integer"
          },
          "applicationRevision": {
              "format": "int32",
              "type": "integer"
          },
          "offer": {
              "$ref": "#/definitions/FireteamFinder.DestinyFireteamFinderOffer"
          },
          "listing": {
              "$ref": "#/definitions/FireteamFinder.DestinyFireteamFinderListing"
          }
      }
  }
}
```
