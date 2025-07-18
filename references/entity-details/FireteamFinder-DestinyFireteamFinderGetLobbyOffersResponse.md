# FireteamFinder.DestinyFireteamFinderGetLobbyOffersResponse

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderGetLobbyOffersResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfindergetlobbyoffersresponse data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| offers | Array[FireteamFinder.DestinyFireteamFinderOffer] |  | No |
| pageToken | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderGetLobbyOffersResponse object
const example = {
  offers: [],
  pageToken: "example value",
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderGetLobbyOffersResponse object
example = {
    "offers": [],
    "pageToken": "example value",
}
```

## Related Entities
- **FireteamFinder.DestinyFireteamFinderOffer**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderGetLobbyOffersResponse":   {
      "type": "object",
      "properties": {
          "offers": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/FireteamFinder.DestinyFireteamFinderOffer"
              }
          },
          "pageToken": {
              "type": "string"
          }
      }
  }
}
```
