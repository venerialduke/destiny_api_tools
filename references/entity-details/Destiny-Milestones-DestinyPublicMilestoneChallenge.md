# Destiny.Milestones.DestinyPublicMilestoneChallenge

## Entity Information
- **Entity Name**: Destiny.Milestones.DestinyPublicMilestoneChallenge
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
A Milestone can have many Challenges. Challenges are just extra Objectives that provide a fun way to mix-up play and provide extra rewards.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| objectiveHash | integer (uint32) | The objective for the Challenge, which should have human-readable data about what needs to be done to accomplish the objective. Use this hash to look up the DestinyObjectiveDefinition. | No |
| activityHash | integer (uint32) | IF the Objective is related to a specific Activity, this will be that activity's hash. Use it to look up the DestinyActivityDefinition for additional data to show. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Milestones.DestinyPublicMilestoneChallenge object
const example = {
  objectiveHash: 123,
  activityHash: 123,
};
```

### Python
```python
# Example Destiny.Milestones.DestinyPublicMilestoneChallenge object
example = {
    "objectiveHash": 123,
    "activityHash": 123,
}
```

## Related Entities
- **Destiny.Definitions.DestinyActivityDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyObjectiveDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Milestones.DestinyPublicMilestoneChallenge":   {
      "description": "A Milestone can have many Challenges. Challenges are just extra Objectives that provide a fun way to mix-up play and provide extra rewards.",
      "type": "object",
      "properties": {
          "objectiveHash": {
              "format": "uint32",
              "description": "The objective for the Challenge, which should have human-readable data about what needs to be done to accomplish the objective. Use this hash to look up the DestinyObjectiveDefinition.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyObjectiveDefinition"
              }
          },
          "activityHash": {
              "format": "uint32",
              "description": "IF the Objective is related to a specific Activity, this will be that activity's hash. Use it to look up the DestinyActivityDefinition for additional data to show.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityDefinition"
              }
          }
      }
  }
}
```
