# FireteamFinder.DestinyFireteamFinderGetPlayerOffersResponse

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderGetPlayerOffersResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfindergetplayeroffersresponse data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| offers | Array[FireteamFinder.DestinyFireteamFinderOffer] | All offers that this player has recieved. | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderGetPlayerOffersResponse object
const example = {
  offers: [],
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderGetPlayerOffersResponse object
example = {
    "offers": [],
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
  "FireteamFinder.DestinyFireteamFinderGetPlayerOffersResponse":   {
      "type": "object",
      "properties": {
          "offers": {
              "description": "All offers that this player has recieved.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/FireteamFinder.DestinyFireteamFinderOffer"
              }
          }
      }
  }
}
```
