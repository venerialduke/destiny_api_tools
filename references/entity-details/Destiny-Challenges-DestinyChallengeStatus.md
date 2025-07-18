# Destiny.Challenges.DestinyChallengeStatus

## Entity Information
- **Entity Name**: Destiny.Challenges.DestinyChallengeStatus
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Represents the status and other related information for a challenge that is - or was - available to a player. 
A challenge is a bonus objective, generally tacked onto Quests or Activities, that provide additional variations on play.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| objective | object | The progress - including completion status - of the active challenge. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Challenges.DestinyChallengeStatus object
const example = {
  objective: null,
};
```

### Python
```python
# Example Destiny.Challenges.DestinyChallengeStatus object
example = {
    "objective": None,
}
```

## Related Entities
- **Destiny.Quests.DestinyObjectiveProgress**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Challenges.DestinyChallengeStatus":   {
      "description": "Represents the status and other related information for a challenge that is - or was - available to a player. \r\nA challenge is a bonus objective, generally tacked onto Quests or Activities, that provide additional variations on play.",
      "type": "object",
      "properties": {
          "objective": {
              "description": "The progress - including completion status - of the active challenge.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Quests.DestinyObjectiveProgress"
                  }
              ]
          }
      }
  }
}
```
