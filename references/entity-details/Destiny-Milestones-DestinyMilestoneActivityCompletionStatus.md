# Destiny.Milestones.DestinyMilestoneActivityCompletionStatus

## Entity Information
- **Entity Name**: Destiny.Milestones.DestinyMilestoneActivityCompletionStatus
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Represents this player's personal completion status for the Activity under a Milestone, if the activity has trackable completion and progress information. (most activities won't, or the concept won't apply. For instance, it makes sense to talk about a tier of a raid as being Completed or having progress, but it doesn't make sense to talk about a Crucible Playlist in those terms.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| completed | boolean | If the activity has been "completed", that information will be returned here. | No |
| phases | Array[Destiny.Milestones.DestinyMilestoneActivityPhase] | If the Activity has discrete "phases" that we can track, that info will be here. Otherwise, this value will be NULL. Note that this is a list and not a dictionary: the order implies the ascending order of phases or progression in this activity. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Milestones.DestinyMilestoneActivityCompletionStatus object
const example = {
  completed: true,
  phases: [],
};
```

### Python
```python
# Example Destiny.Milestones.DestinyMilestoneActivityCompletionStatus object
example = {
    "completed": True,
    "phases": [],
}
```

## Related Entities
- **Destiny.Milestones.DestinyMilestoneActivityPhase**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Milestones.DestinyMilestoneActivityCompletionStatus":   {
      "description": "Represents this player's personal completion status for the Activity under a Milestone, if the activity has trackable completion and progress information. (most activities won't, or the concept won't apply. For instance, it makes sense to talk about a tier of a raid as being Completed or having progress, but it doesn't make sense to talk about a Crucible Playlist in those terms.",
      "type": "object",
      "properties": {
          "completed": {
              "description": "If the activity has been \"completed\", that information will be returned here.",
              "type": "boolean"
          },
          "phases": {
              "description": "If the Activity has discrete \"phases\" that we can track, that info will be here. Otherwise, this value will be NULL. Note that this is a list and not a dictionary: the order implies the ascending order of phases or progression in this activity.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Milestones.DestinyMilestoneActivityPhase"
              }
          }
      }
  }
}
```
