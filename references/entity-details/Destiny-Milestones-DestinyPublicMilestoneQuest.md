# Destiny.Milestones.DestinyPublicMilestoneQuest

## Entity Information
- **Entity Name**: Destiny.Milestones.DestinyPublicMilestoneQuest
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinypublicmilestonequest data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| questItemHash | integer (uint32) | Quests are defined as Items in content. As such, this is the hash identifier of the DestinyInventoryItemDefinition that represents this quest. It will have pointers to all of the steps in the quest, and display information for the quest (title, description, icon etc) Individual steps will be referred to in the Quest item's DestinyInventoryItemDefinition.setData property, and themselves are Items with their own renderable data. | No |
| activity | object | A milestone need not have an active activity, but if there is one it will be returned here, along with any variant and additional information. | No |
| challenges | Array[Destiny.Milestones.DestinyPublicMilestoneChallenge] | For the given quest there could be 0-to-Many challenges: mini quests that you can perform in the course of doing this quest, that may grant you rewards and benefits. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Milestones.DestinyPublicMilestoneQuest object
const example = {
  questItemHash: 123,
  activity: null,
  challenges: [],
};
```

### Python
```python
# Example Destiny.Milestones.DestinyPublicMilestoneQuest object
example = {
    "questItemHash": 123,
    "activity": None,
    "challenges": [],
}
```

## Related Entities
- **Destiny.Definitions.Milestones.DestinyMilestoneDefinition**: Referenced in this entity
- **Destiny.Milestones.DestinyPublicMilestoneActivity**: Referenced in this entity
- **Destiny.Milestones.DestinyPublicMilestoneChallenge**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Milestones.DestinyPublicMilestoneQuest":   {
      "type": "object",
      "properties": {
          "questItemHash": {
              "format": "uint32",
              "description": "Quests are defined as Items in content. As such, this is the hash identifier of the DestinyInventoryItemDefinition that represents this quest. It will have pointers to all of the steps in the quest, and display information for the quest (title, description, icon etc) Individual steps will be referred to in the Quest item's DestinyInventoryItemDefinition.setData property, and themselves are Items with their own renderable data.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Milestones.DestinyMilestoneDefinition"
              }
          },
          "activity": {
              "description": "A milestone need not have an active activity, but if there is one it will be returned here, along with any variant and additional information.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Milestones.DestinyPublicMilestoneActivity"
                  }
              ]
          },
          "challenges": {
              "description": "For the given quest there could be 0-to-Many challenges: mini quests that you can perform in the course of doing this quest, that may grant you rewards and benefits.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Milestones.DestinyPublicMilestoneChallenge"
              }
          }
      }
  }
}
```
