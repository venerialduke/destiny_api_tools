# Destiny.Entities.Items.DestinyItemObjectivesComponent

## Entity Information
- **Entity Name**: Destiny.Entities.Items.DestinyItemObjectivesComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Items can have objectives and progression. When you request this block, you will obtain information about any Objectives and progression tied to this item.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| objectives | Array[Destiny.Quests.DestinyObjectiveProgress] | If the item has a hard association with objectives, your progress on them will be defined here. 
Objectives are our standard way to describe a series of tasks that have to be completed for a reward. | No |
| flavorObjective | object | I may regret naming it this way - but this represents when an item has an objective that doesn't serve a beneficial purpose, but rather is used for "flavor" or additional information. For instance, when Emblems track specific stats, those stats are represented as Objectives on the item. | No |
| dateCompleted | string (date-time) | If we have any information on when these objectives were completed, this will be the date of that completion. This won't be on many items, but could be interesting for some items that do store this information. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Entities.Items.DestinyItemObjectivesComponent object
const example = {
  objectives: [],
  flavorObjective: null,
  dateCompleted: "example value",
};
```

### Python
```python
# Example Destiny.Entities.Items.DestinyItemObjectivesComponent object
example = {
    "objectives": [],
    "flavorObjective": None,
    "dateCompleted": "example value",
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
  "Destiny.Entities.Items.DestinyItemObjectivesComponent":   {
      "description": "Items can have objectives and progression. When you request this block, you will obtain information about any Objectives and progression tied to this item.",
      "type": "object",
      "properties": {
          "objectives": {
              "description": "If the item has a hard association with objectives, your progress on them will be defined here. \r\nObjectives are our standard way to describe a series of tasks that have to be completed for a reward.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Quests.DestinyObjectiveProgress"
              }
          },
          "flavorObjective": {
              "description": "I may regret naming it this way - but this represents when an item has an objective that doesn't serve a beneficial purpose, but rather is used for \"flavor\" or additional information. For instance, when Emblems track specific stats, those stats are represented as Objectives on the item.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Quests.DestinyObjectiveProgress"
                  }
              ]
          },
          "dateCompleted": {
              "format": "date-time",
              "description": "If we have any information on when these objectives were completed, this will be the date of that completion. This won't be on many items, but could be interesting for some items that do store this information.",
              "type": "string"
          }
      },
      "x-destiny-component-type-dependency": "ItemObjectives"
  }
}
```
