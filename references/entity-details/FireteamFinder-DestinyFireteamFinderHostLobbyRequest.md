# FireteamFinder.DestinyFireteamFinderHostLobbyRequest

## Entity Information
- **Entity Name**: FireteamFinder.DestinyFireteamFinderHostLobbyRequest
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderhostlobbyrequest data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| maxPlayerCount | integer (int32) |  | No |
| onlinePlayersOnly | boolean |  | No |
| privacyScope | integer (int32) |  | No |
| scheduledDateTime | string (date-time) |  | No |
| clanId | integer (int64) |  | No |
| listingValues | Array[FireteamFinder.DestinyFireteamFinderListingValue] |  | No |
| activityGraphHash | integer (uint32) |  | No |
| activityHash | integer (uint32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example FireteamFinder.DestinyFireteamFinderHostLobbyRequest object
const example = {
  maxPlayerCount: 123,
  onlinePlayersOnly: true,
  privacyScope: 123,
  scheduledDateTime: "example value",
  clanId: 123,
  // ... more properties
};
```

### Python
```python
# Example FireteamFinder.DestinyFireteamFinderHostLobbyRequest object
example = {
    "maxPlayerCount": 123,
    "onlinePlayersOnly": True,
    "privacyScope": 123,
    "scheduledDateTime": "example value",
    "clanId": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyActivityDefinition**: Referenced in this entity
- **Destiny.Definitions.FireteamFinder.DestinyFireteamFinderActivityGraphDefinition**: Referenced in this entity
- **FireteamFinder.DestinyFireteamFinderListingValue**: Referenced in this entity
- **FireteamFinder.DestinyFireteamFinderLobbyPrivacyScope**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "FireteamFinder.DestinyFireteamFinderHostLobbyRequest":   {
      "type": "object",
      "properties": {
          "maxPlayerCount": {
              "format": "int32",
              "type": "integer"
          },
          "onlinePlayersOnly": {
              "type": "boolean"
          },
          "privacyScope": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/FireteamFinder.DestinyFireteamFinderLobbyPrivacyScope"
              }
          },
          "scheduledDateTime": {
              "format": "date-time",
              "type": "string"
          },
          "clanId": {
              "format": "int64",
              "type": "integer"
          },
          "listingValues": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/FireteamFinder.DestinyFireteamFinderListingValue"
              }
          },
          "activityGraphHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.FireteamFinder.DestinyFireteamFinderActivityGraphDefinition"
              }
          },
          "activityHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityDefinition"
              }
          }
      }
  }
}
```
