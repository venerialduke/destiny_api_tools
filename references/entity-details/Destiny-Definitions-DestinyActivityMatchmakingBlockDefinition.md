# Destiny.Definitions.DestinyActivityMatchmakingBlockDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyActivityMatchmakingBlockDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Information about matchmaking and party size for the activity.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| isMatchmade | boolean | If TRUE, the activity is matchmade. Otherwise, it requires explicit forming of a party. | No |
| minParty | integer (int32) | The minimum # of people in the fireteam for the activity to launch. | No |
| maxParty | integer (int32) | The maximum # of people allowed in a Fireteam. | No |
| maxPlayers | integer (int32) | The maximum # of people allowed across all teams in the activity. | No |
| requiresGuardianOath | boolean | If true, you have to Solemnly Swear to be up to Nothing But Good(tm) to play. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyActivityMatchmakingBlockDefinition object
const example = {
  isMatchmade: true,
  minParty: 123,
  maxParty: 123,
  maxPlayers: 123,
  requiresGuardianOath: true,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyActivityMatchmakingBlockDefinition object
example = {
    "isMatchmade": True,
    "minParty": 123,
    "maxParty": 123,
    "maxPlayers": 123,
    "requiresGuardianOath": True,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyActivityMatchmakingBlockDefinition":   {
      "description": "Information about matchmaking and party size for the activity.",
      "type": "object",
      "properties": {
          "isMatchmade": {
              "description": "If TRUE, the activity is matchmade. Otherwise, it requires explicit forming of a party.",
              "type": "boolean"
          },
          "minParty": {
              "format": "int32",
              "description": "The minimum # of people in the fireteam for the activity to launch.",
              "type": "integer"
          },
          "maxParty": {
              "format": "int32",
              "description": "The maximum # of people allowed in a Fireteam.",
              "type": "integer"
          },
          "maxPlayers": {
              "format": "int32",
              "description": "The maximum # of people allowed across all teams in the activity.",
              "type": "integer"
          },
          "requiresGuardianOath": {
              "description": "If true, you have to Solemnly Swear to be up to Nothing But Good(tm) to play.",
              "type": "boolean"
          }
      }
  }
}
```
