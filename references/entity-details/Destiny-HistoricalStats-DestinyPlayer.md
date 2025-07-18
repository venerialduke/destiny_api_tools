# Destiny.HistoricalStats.DestinyPlayer

## Entity Information
- **Entity Name**: Destiny.HistoricalStats.DestinyPlayer
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyplayer data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| destinyUserInfo | object | Details about the player as they are known in game (platform display name, Destiny emblem) | No |
| characterClass | string | Class of the character if applicable and available. | No |
| classHash | integer (uint32) |  | No |
| raceHash | integer (uint32) |  | No |
| genderHash | integer (uint32) |  | No |
| characterLevel | integer (int32) | Level of the character if available. Zero if it is not available. | No |
| lightLevel | integer (int32) | Light Level of the character if available. Zero if it is not available. | No |
| bungieNetUserInfo | object | Details about the player as they are known on BungieNet. This will be undefined if the player has marked their credential private, or does not have a BungieNet account. | No |
| clanName | string | Current clan name for the player. This value may be null or an empty string if the user does not have a clan. | No |
| clanTag | string | Current clan tag for the player. This value may be null or an empty string if the user does not have a clan. | No |
| emblemHash | integer (uint32) | If we know the emblem's hash, this can be used to look up the player's emblem at the time of a match when receiving PGCR data, or otherwise their currently equipped emblem (if we are able to obtain it). | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.HistoricalStats.DestinyPlayer object
const example = {
  destinyUserInfo: null,
  characterClass: "example value",
  classHash: 123,
  raceHash: 123,
  genderHash: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.HistoricalStats.DestinyPlayer object
example = {
    "destinyUserInfo": None,
    "characterClass": "example value",
    "classHash": 123,
    "raceHash": 123,
    "genderHash": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyClassDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyGenderDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyRaceDefinition**: Referenced in this entity
- **User.UserInfoCard**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.HistoricalStats.DestinyPlayer":   {
      "type": "object",
      "properties": {
          "destinyUserInfo": {
              "description": "Details about the player as they are known in game (platform display name, Destiny emblem)",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/User.UserInfoCard"
                  }
              ]
          },
          "characterClass": {
              "description": "Class of the character if applicable and available.",
              "type": "string"
          },
          "classHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyClassDefinition"
              }
          },
          "raceHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyRaceDefinition"
              }
          },
          "genderHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyGenderDefinition"
              }
          },
          "characterLevel": {
              "format": "int32",
              "description": "Level of the character if available. Zero if it is not available.",
              "type": "integer"
          },
          "lightLevel": {
              "format": "int32",
              "description": "Light Level of the character if available. Zero if it is not available.",
              "type": "integer"
          },
          "bungieNetUserInfo": {
              "description": "Details about the player as they are known on BungieNet. This will be undefined if the player has marked their credential private, or does not have a BungieNet account.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/User.UserInfoCard"
                  }
              ]
          },
          "clanName": {
              "description": "Current clan name for the player. This value may be null or an empty string if the user does not have a clan.",
              "type": "string"
          },
          "clanTag": {
              "description": "Current clan tag for the player. This value may be null or an empty string if the user does not have a clan.",
              "type": "string"
          },
          "emblemHash": {
              "format": "uint32",
              "description": "If we know the emblem's hash, this can be used to look up the player's emblem at the time of a match when receiving PGCR data, or otherwise their currently equipped emblem (if we are able to obtain it).",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          }
      }
  }
}
```
