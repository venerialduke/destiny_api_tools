# Destiny.DestinyProgression

## Entity Information
- **Entity Name**: Destiny.DestinyProgression
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Information about a current character's status with a Progression. A progression is a value that can increase with activity and has levels. Think Character Level and Reputation Levels. Combine this "live" data with the related DestinyProgressionDefinition for a full picture of the Progression.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| progressionHash | integer (uint32) | The hash identifier of the Progression in question. Use it to look up the DestinyProgressionDefinition in static data. | No |
| dailyProgress | integer (int32) | The amount of progress earned today for this progression. | No |
| dailyLimit | integer (int32) | If this progression has a daily limit, this is that limit. | No |
| weeklyProgress | integer (int32) | The amount of progress earned toward this progression in the current week. | No |
| weeklyLimit | integer (int32) | If this progression has a weekly limit, this is that limit. | No |
| currentProgress | integer (int32) | This is the total amount of progress obtained overall for this progression (for instance, the total amount of Character Level experience earned) | No |
| level | integer (int32) | This is the level of the progression (for instance, the Character Level). | No |
| levelCap | integer (int32) | This is the maximum possible level you can achieve for this progression (for example, the maximum character level obtainable) | No |
| stepIndex | integer (int32) | Progressions define their levels in "steps". Since the last step may be repeatable, the user may be at a higher level than the actual Step achieved in the progression. Not necessarily useful, but potentially interesting for those cruising the API. Relate this to the "steps" property of the DestinyProgression to see which step the user is on, if you care about that. (Note that this is Content Version dependent since it refers to indexes.) | No |
| progressToNextLevel | integer (int32) | The amount of progression (i.e. "Experience") needed to reach the next level of this Progression. Jeez, progression is such an overloaded word. | No |
| nextLevelAt | integer (int32) | The total amount of progression (i.e. "Experience") needed in order to reach the next level. | No |
| currentResetCount | integer (int32) | The number of resets of this progression you've executed this season, if applicable to this progression. | No |
| seasonResets | Array[Destiny.DestinyProgressionResetEntry] | Information about historical resets of this progression, if there is any data for it. | No |
| rewardItemStates | Array[integer] | Information about historical rewards for this progression, if there is any data for it. | No |
| rewardItemSocketOverrideStates | object | Information about items stats and states that have socket overrides, if there is any data for it. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.DestinyProgression object
const example = {
  progressionHash: 123,
  dailyProgress: 123,
  dailyLimit: 123,
  weeklyProgress: 123,
  weeklyLimit: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.DestinyProgression object
example = {
    "progressionHash": 123,
    "dailyProgress": 123,
    "dailyLimit": 123,
    "weeklyProgress": 123,
    "weeklyLimit": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyProgressionDefinition**: Referenced in this entity
- **Destiny.DestinyProgressionResetEntry**: Referenced in this entity
- **Destiny.DestinyProgressionRewardItemSocketOverrideState**: Referenced in this entity
- **Destiny.DestinyProgressionRewardItemState**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyProgression":   {
      "description": "Information about a current character's status with a Progression. A progression is a value that can increase with activity and has levels. Think Character Level and Reputation Levels. Combine this \"live\" data with the related DestinyProgressionDefinition for a full picture of the Progression.",
      "type": "object",
      "properties": {
          "progressionHash": {
              "format": "uint32",
              "description": "The hash identifier of the Progression in question. Use it to look up the DestinyProgressionDefinition in static data.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyProgressionDefinition"
              }
          },
          "dailyProgress": {
              "format": "int32",
              "description": "The amount of progress earned today for this progression.",
              "type": "integer"
          },
          "dailyLimit": {
              "format": "int32",
              "description": "If this progression has a daily limit, this is that limit.",
              "type": "integer"
          },
          "weeklyProgress": {
              "format": "int32",
              "description": "The amount of progress earned toward this progression in the current week.",
              "type": "integer"
          },
          "weeklyLimit": {
              "format": "int32",
              "description": "If this progression has a weekly limit, this is that limit.",
              "type": "integer"
          },
          "currentProgress": {
              "format": "int32",
              "description": "This is the total amount of progress obtained overall for this progression (for instance, the total amount of Character Level experience earned)",
              "type": "integer"
          },
          "level": {
              "format": "int32",
              "description": "This is the level of the progression (for instance, the Character Level).",
              "type": "integer"
          },
          "levelCap": {
              "format": "int32",
              "description": "This is the maximum possible level you can achieve for this progression (for example, the maximum character level obtainable)",
              "type": "integer"
          },
          "stepIndex": {
              "format": "int32",
              "description": "Progressions define their levels in \"steps\". Since the last step may be repeatable, the user may be at a higher level than the actual Step achieved in the progression. Not necessarily useful, but potentially interesting for those cruising the API. Relate this to the \"steps\" property of the DestinyProgression to see which step the user is on, if you care about that. (Note that this is Content Version dependent since it refers to indexes.)",
              "type": "integer"
          },
          "progressToNextLevel": {
              "format": "int32",
              "description": "The amount of progression (i.e. \"Experience\") needed to reach the next level of this Progression. Jeez, progression is such an overloaded word.",
              "type": "integer"
          },
          "nextLevelAt": {
              "format": "int32",
              "description": "The total amount of progression (i.e. \"Experience\") needed in order to reach the next level.",
              "type": "integer"
          },
          "currentResetCount": {
              "format": "int32",
              "description": "The number of resets of this progression you've executed this season, if applicable to this progression.",
              "type": "integer"
          },
          "seasonResets": {
              "description": "Information about historical resets of this progression, if there is any data for it.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.DestinyProgressionResetEntry"
              }
          },
          "rewardItemStates": {
              "description": "Information about historical rewards for this progression, if there is any data for it.",
              "type": "array",
              "items": {
                  "format": "int32",
                  "description": "Represents the different states a progression reward item can be in.",
                  "type": "integer",
                  "x-enum-reference": {
                      "$ref": "#/components/schemas/Destiny.DestinyProgressionRewardItemState"
                  }
              }
          },
          "rewardItemSocketOverrideStates": {
              "description": "Information about items stats and states that have socket overrides, if there is any data for it.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.DestinyProgressionRewardItemSocketOverrideState"
              }
          }
      }
  }
}
```
