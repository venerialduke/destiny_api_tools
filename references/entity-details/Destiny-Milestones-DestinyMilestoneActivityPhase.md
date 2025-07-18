# Destiny.Milestones.DestinyMilestoneActivityPhase

## Entity Information
- **Entity Name**: Destiny.Milestones.DestinyMilestoneActivityPhase
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Represents whatever information we can return about an explicit phase in an activity. In the future, I hope we'll have more than just "guh, you done gone and did something," but for the forseeable future that's all we've got. I'm making it more than just a list of booleans out of that overly-optimistic hope.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| complete | boolean | Indicates if the phase has been completed. | No |
| phaseHash | integer (uint32) | In DestinyActivityDefinition, if the activity has phases, there will be a set of phases defined in the "insertionPoints" property. This is the hash that maps to that phase. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Milestones.DestinyMilestoneActivityPhase object
const example = {
  complete: true,
  phaseHash: 123,
};
```

### Python
```python
# Example Destiny.Milestones.DestinyMilestoneActivityPhase object
example = {
    "complete": True,
    "phaseHash": 123,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Milestones.DestinyMilestoneActivityPhase":   {
      "description": "Represents whatever information we can return about an explicit phase in an activity. In the future, I hope we'll have more than just \"guh, you done gone and did something,\" but for the forseeable future that's all we've got. I'm making it more than just a list of booleans out of that overly-optimistic hope.",
      "type": "object",
      "properties": {
          "complete": {
              "description": "Indicates if the phase has been completed.",
              "type": "boolean"
          },
          "phaseHash": {
              "format": "uint32",
              "description": "In DestinyActivityDefinition, if the activity has phases, there will be a set of phases defined in the \"insertionPoints\" property. This is the hash that maps to that phase.",
              "type": "integer"
          }
      }
  }
}
```
