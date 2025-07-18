# FireteamFinder.DestinyFireteamFinderUpdateLobbySettingsRequest

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderUpdateLobbySettingsRequest
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderupdatelobbysettingsrequest data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| updatedSettings | FireteamFinder.DestinyFireteamFinderLobbySettings |  | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderUpdateLobbySettingsRequest object
const example = {
  updatedSettings: null,
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderUpdateLobbySettingsRequest object
example = {
    "updatedSettings": None,
}
```

## Related Entities
- **FireteamFinder.DestinyFireteamFinderLobbySettings**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderUpdateLobbySettingsRequest":   {
      "type": "object",
      "properties": {
          "updatedSettings": {
              "$ref": "#/definitions/FireteamFinder.DestinyFireteamFinderLobbySettings"
          }
      }
  }
}
```
