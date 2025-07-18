# Destiny.Quests.DestinyQuestStatus

## Entity Information
- **Entity Name**: Destiny.Quests.DestinyQuestStatus
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Data regarding the progress of a Quest for a specific character. Quests are composed of multiple steps, each with potentially multiple objectives: this QuestStatus will return Objective data for the *currently active* step in this quest.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| questHash | integer (uint32) | The hash identifier for the Quest Item. (Note: Quests are defined as Items, and thus you would use this to look up the quest's DestinyInventoryItemDefinition). For information on all steps in the quest, you can then examine its DestinyInventoryItemDefinition.setData property for Quest Steps (which are *also* items). You can use the Item Definition to display human readable data about the overall quest. | No |
| stepHash | integer (uint32) | The hash identifier of the current Quest Step, which is also a DestinyInventoryItemDefinition. You can use this to get human readable data about the current step and what to do in that step. | No |
| stepObjectives | Array[Destiny.Quests.DestinyObjectiveProgress] | A step can have multiple objectives. This will give you the progress for each objective in the current step, in the order in which they are rendered in-game. | No |
| tracked | boolean | Whether or not the quest is tracked | No |
| itemInstanceId | integer (int64) | The current Quest Step will be an instanced item in the player's inventory. If you care about that, this is the instance ID of that item. | No |
| completed | boolean | Whether or not the whole quest has been completed, regardless of whether or not you have redeemed the rewards for the quest. | No |
| redeemed | boolean | Whether or not you have redeemed rewards for this quest. | No |
| started | boolean | Whether or not you have started this quest. | No |
| vendorHash | integer (uint32) | If the quest has a related Vendor that you should talk to in order to initiate the quest/earn rewards/continue the quest, this will be the hash identifier of that Vendor. Look it up its DestinyVendorDefinition. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Quests.DestinyQuestStatus object
const example = {
  questHash: 123,
  stepHash: 123,
  stepObjectives: [],
  tracked: true,
  itemInstanceId: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Quests.DestinyQuestStatus object
example = {
    "questHash": 123,
    "stepHash": 123,
    "stepObjectives": [],
    "tracked": True,
    "itemInstanceId": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Quests.DestinyObjectiveProgress**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Quests.DestinyQuestStatus":   {
      "description": "Data regarding the progress of a Quest for a specific character. Quests are composed of multiple steps, each with potentially multiple objectives: this QuestStatus will return Objective data for the *currently active* step in this quest.",
      "type": "object",
      "properties": {
          "questHash": {
              "format": "uint32",
              "description": "The hash identifier for the Quest Item. (Note: Quests are defined as Items, and thus you would use this to look up the quest's DestinyInventoryItemDefinition). For information on all steps in the quest, you can then examine its DestinyInventoryItemDefinition.setData property for Quest Steps (which are *also* items). You can use the Item Definition to display human readable data about the overall quest.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "stepHash": {
              "format": "uint32",
              "description": "The hash identifier of the current Quest Step, which is also a DestinyInventoryItemDefinition. You can use this to get human readable data about the current step and what to do in that step.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "stepObjectives": {
              "description": "A step can have multiple objectives. This will give you the progress for each objective in the current step, in the order in which they are rendered in-game.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Quests.DestinyObjectiveProgress"
              }
          },
          "tracked": {
              "description": "Whether or not the quest is tracked",
              "type": "boolean"
          },
          "itemInstanceId": {
              "format": "int64",
              "description": "The current Quest Step will be an instanced item in the player's inventory. If you care about that, this is the instance ID of that item.",
              "type": "integer"
          },
          "completed": {
              "description": "Whether or not the whole quest has been completed, regardless of whether or not you have redeemed the rewards for the quest.",
              "type": "boolean"
          },
          "redeemed": {
              "description": "Whether or not you have redeemed rewards for this quest.",
              "type": "boolean"
          },
          "started": {
              "description": "Whether or not you have started this quest.",
              "type": "boolean"
          },
          "vendorHash": {
              "format": "uint32",
              "description": "If the quest has a related Vendor that you should talk to in order to initiate the quest/earn rewards/continue the quest, this will be the hash identifier of that Vendor. Look it up its DestinyVendorDefinition.",
              "type": "integer"
          }
      }
  }
}
```
