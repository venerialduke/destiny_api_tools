# Destiny.Definitions.Milestones.DestinyMilestoneChallengeActivityDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Milestones.DestinyMilestoneChallengeActivityDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinymilestonechallengeactivitydefinition data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| activityHash | integer (uint32) | The activity for which this challenge is active. | No |
| challenges | Array[Destiny.Definitions.Milestones.DestinyMilestoneChallengeDefinition] |  | No |
| activityGraphNodes | Array[Destiny.Definitions.Milestones.DestinyMilestoneChallengeActivityGraphNodeEntry] | If the activity and its challenge is visible on any of these nodes, it will be returned. | No |
| phases | Array[Destiny.Definitions.Milestones.DestinyMilestoneChallengeActivityPhase] | Phases related to this activity, if there are any.
These will be listed in the order in which they will appear in the actual activity. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Milestones.DestinyMilestoneChallengeActivityDefinition object
const example = {
  activityHash: 123,
  challenges: [],
  activityGraphNodes: [],
  phases: [],
};
```

### Python
```python
# Example Destiny.Definitions.Milestones.DestinyMilestoneChallengeActivityDefinition object
example = {
    "activityHash": 123,
    "challenges": [],
    "activityGraphNodes": [],
    "phases": [],
}
```

## Related Entities
- **Destiny.Definitions.DestinyActivityDefinition**: Referenced in this entity
- **Destiny.Definitions.Milestones.DestinyMilestoneChallengeActivityGraphNodeEntry**: Referenced in this entity
- **Destiny.Definitions.Milestones.DestinyMilestoneChallengeActivityPhase**: Referenced in this entity
- **Destiny.Definitions.Milestones.DestinyMilestoneChallengeDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Milestones.DestinyMilestoneChallengeActivityDefinition":   {
      "type": "object",
      "properties": {
          "activityHash": {
              "format": "uint32",
              "description": "The activity for which this challenge is active.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityDefinition"
              }
          },
          "challenges": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Milestones.DestinyMilestoneChallengeDefinition"
              }
          },
          "activityGraphNodes": {
              "description": "If the activity and its challenge is visible on any of these nodes, it will be returned.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Milestones.DestinyMilestoneChallengeActivityGraphNodeEntry"
              }
          },
          "phases": {
              "description": "Phases related to this activity, if there are any.\r\nThese will be listed in the order in which they will appear in the actual activity.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Milestones.DestinyMilestoneChallengeActivityPhase"
              }
          }
      }
  }
}
```
