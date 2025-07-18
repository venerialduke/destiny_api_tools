# FireteamFinder.DestinyFireteamFinderUpdateLobbySettingsResponse

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderUpdateLobbySettingsResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderupdatelobbysettingsresponse data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| updatedLobby | FireteamFinder.DestinyFireteamFinderLobbyResponse |  | No |
| updatedListing | FireteamFinder.DestinyFireteamFinderListing |  | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderUpdateLobbySettingsResponse object
const example = {
  updatedLobby: null,
  updatedListing: null,
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderUpdateLobbySettingsResponse object
example = {
    "updatedLobby": None,
    "updatedListing": None,
}
```

## Related Entities
- **FireteamFinder.DestinyFireteamFinderListing**: Referenced in this entity
- **FireteamFinder.DestinyFireteamFinderLobbyResponse**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderUpdateLobbySettingsResponse":   {
      "type": "object",
      "properties": {
          "updatedLobby": {
              "$ref": "#/definitions/FireteamFinder.DestinyFireteamFinderLobbyResponse"
          },
          "updatedListing": {
              "$ref": "#/definitions/FireteamFinder.DestinyFireteamFinderListing"
          }
      }
  }
}
```
