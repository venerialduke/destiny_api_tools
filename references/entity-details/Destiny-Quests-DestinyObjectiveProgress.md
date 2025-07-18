# Destiny.Quests.DestinyObjectiveProgress

## Entity Information
- **Entity Name**: Destiny.Quests.DestinyObjectiveProgress
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Returns data about a character's status with a given Objective. Combine with DestinyObjectiveDefinition static data for display purposes.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| objectiveHash | integer (uint32) | The unique identifier of the Objective being referred to. Use to look up the DestinyObjectiveDefinition in static data. | No |
| destinationHash | integer (uint32) | If the Objective has a Destination associated with it, this is the unique identifier of the Destination being referred to. Use to look up the DestinyDestinationDefinition in static data. This will give localized data about *where* in the universe the objective should be achieved. | No |
| activityHash | integer (uint32) | If the Objective has an Activity associated with it, this is the unique identifier of the Activity being referred to. Use to look up the DestinyActivityDefinition in static data. This will give localized data about *what* you should be playing for the objective to be achieved. | No |
| progress | integer (int32) | If progress has been made, and the progress can be measured numerically, this will be the value of that progress. You can compare it to the DestinyObjectiveDefinition.completionValue property for current vs. upper bounds, and use DestinyObjectiveDefinition.inProgressValueStyle or completedValueStyle to determine how this should be rendered. Note that progress, in Destiny 2, need not be a literal numeric progression. It could be one of a number of possible values, even a Timestamp. Always examine DestinyObjectiveDefinition.inProgressValueStyle or completedValueStyle before rendering progress. | No |
| completionValue | integer (int32) | As of Forsaken, objectives' completion value is determined dynamically at runtime.
This value represents the threshold of progress you need to surpass in order for this objective to be considered "complete".
If you were using objective data, switch from using the DestinyObjectiveDefinition's "completionValue" to this value. | No |
| complete | boolean | Whether or not the Objective is completed. | No |
| visible | boolean | If this is true, the objective is visible in-game. Otherwise, it's not yet visible to the player. Up to you if you want to honor this property. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Quests.DestinyObjectiveProgress object
const example = {
  objectiveHash: 123,
  destinationHash: 123,
  activityHash: 123,
  progress: 123,
  completionValue: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Quests.DestinyObjectiveProgress object
example = {
    "objectiveHash": 123,
    "destinationHash": 123,
    "activityHash": 123,
    "progress": 123,
    "completionValue": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyActivityDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyDestinationDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyObjectiveDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Quests.DestinyObjectiveProgress":   {
      "description": "Returns data about a character's status with a given Objective. Combine with DestinyObjectiveDefinition static data for display purposes.",
      "type": "object",
      "properties": {
          "objectiveHash": {
              "format": "uint32",
              "description": "The unique identifier of the Objective being referred to. Use to look up the DestinyObjectiveDefinition in static data.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyObjectiveDefinition"
              }
          },
          "destinationHash": {
              "format": "uint32",
              "description": "If the Objective has a Destination associated with it, this is the unique identifier of the Destination being referred to. Use to look up the DestinyDestinationDefinition in static data. This will give localized data about *where* in the universe the objective should be achieved.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyDestinationDefinition"
              }
          },
          "activityHash": {
              "format": "uint32",
              "description": "If the Objective has an Activity associated with it, this is the unique identifier of the Activity being referred to. Use to look up the DestinyActivityDefinition in static data. This will give localized data about *what* you should be playing for the objective to be achieved.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityDefinition"
              }
          },
          "progress": {
              "format": "int32",
              "description": "If progress has been made, and the progress can be measured numerically, this will be the value of that progress. You can compare it to the DestinyObjectiveDefinition.completionValue property for current vs. upper bounds, and use DestinyObjectiveDefinition.inProgressValueStyle or completedValueStyle to determine how this should be rendered. Note that progress, in Destiny 2, need not be a literal numeric progression. It could be one of a number of possible values, even a Timestamp. Always examine DestinyObjectiveDefinition.inProgressValueStyle or completedValueStyle before rendering progress.",
              "type": "integer"
          },
          "completionValue": {
              "format": "int32",
              "description": "As of Forsaken, objectives' completion value is determined dynamically at runtime.\r\nThis value represents the threshold of progress you need to surpass in order for this objective to be considered \"complete\".\r\nIf you were using objective data, switch from using the DestinyObjectiveDefinition's \"completionValue\" to this value.",
              "type": "integer"
          },
          "complete": {
              "description": "Whether or not the Objective is completed.",
              "type": "boolean"
          },
          "visible": {
              "description": "If this is true, the objective is visible in-game. Otherwise, it's not yet visible to the player. Up to you if you want to honor this property.",
              "type": "boolean"
          }
      }
  }
}
```
