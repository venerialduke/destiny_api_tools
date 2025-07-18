# Destiny.Components.Presentation.DestinyPresentationNodeComponent

## Entity Information
- **Entity Name**: Destiny.Components.Presentation.DestinyPresentationNodeComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinypresentationnodecomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| state | integer (int32) |  | No |
| objective | object | An optional property: presentation nodes MAY have objectives, which can be used to infer more human readable data about the progress. However, progressValue and completionValue ought to be considered the canonical values for progress on Progression Nodes. | No |
| progressValue | integer (int32) | How much of the presentation node is considered to be completed so far by the given character/profile. | No |
| completionValue | integer (int32) | The value at which the presentation node is considered to be completed. | No |
| recordCategoryScore | integer (int32) | If available, this is the current score for the record category that this node represents. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Presentation.DestinyPresentationNodeComponent object
const example = {
  state: 123,
  objective: null,
  progressValue: 123,
  completionValue: 123,
  recordCategoryScore: 123,
};
```

### Python
```python
# Example Destiny.Components.Presentation.DestinyPresentationNodeComponent object
example = {
    "state": 123,
    "objective": None,
    "progressValue": 123,
    "completionValue": 123,
    "recordCategoryScore": 123,
}
```

## Related Entities
- **Destiny.DestinyPresentationNodeState**: Referenced in this entity
- **Destiny.Quests.DestinyObjectiveProgress**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Presentation.DestinyPresentationNodeComponent":   {
      "type": "object",
      "properties": {
          "state": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyPresentationNodeState"
              }
          },
          "objective": {
              "description": "An optional property: presentation nodes MAY have objectives, which can be used to infer more human readable data about the progress. However, progressValue and completionValue ought to be considered the canonical values for progress on Progression Nodes.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Quests.DestinyObjectiveProgress"
                  }
              ]
          },
          "progressValue": {
              "format": "int32",
              "description": "How much of the presentation node is considered to be completed so far by the given character/profile.",
              "type": "integer"
          },
          "completionValue": {
              "format": "int32",
              "description": "The value at which the presentation node is considered to be completed.",
              "type": "integer"
          },
          "recordCategoryScore": {
              "format": "int32",
              "description": "If available, this is the current score for the record category that this node represents.",
              "type": "integer"
          }
      }
  }
}
```
