# Destiny.Milestones.DestinyMilestoneQuest

## Entity Information
- **Entity Name**: Destiny.Milestones.DestinyMilestoneQuest
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
If a Milestone has one or more Quests, this will contain the live information for the character's status with one of those quests.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| questItemHash | integer (uint32) | Quests are defined as Items in content. As such, this is the hash identifier of the DestinyInventoryItemDefinition that represents this quest. It will have pointers to all of the steps in the quest, and display information for the quest (title, description, icon etc) Individual steps will be referred to in the Quest item's DestinyInventoryItemDefinition.setData property, and themselves are Items with their own renderable data. | No |
| status | object | The current status of the quest for the character making the request. | No |
| activity | object | *IF* the Milestone has an active Activity that can give you greater details about what you need to do, it will be returned here. Remember to associate this with the DestinyMilestoneDefinition's activities to get details about the activity, including what specific quest it is related to if you have multiple quests to choose from. | No |
| challenges | Array[Destiny.Challenges.DestinyChallengeStatus] | The activities referred to by this quest can have many associated challenges. They are all contained here, with activityHashes so that you can associate them with the specific activity variants in which they can be found. In retrospect, I probably should have put these under the specific Activity Variants, but it's too late to change it now. Theoretically, a quest without Activities can still have Challenges, which is why this is on a higher level than activity/variants, but it probably should have been in both places. That may come as a later revision. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Milestones.DestinyMilestoneQuest object
const example = {
  questItemHash: 123,
  status: null,
  activity: null,
  challenges: [],
};
```

### Python
```python
# Example Destiny.Milestones.DestinyMilestoneQuest object
example = {
    "questItemHash": 123,
    "status": None,
    "activity": None,
    "challenges": [],
}
```

## Related Entities
- **Destiny.Challenges.DestinyChallengeStatus**: Referenced in this entity
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Milestones.DestinyMilestoneActivity**: Referenced in this entity
- **Destiny.Quests.DestinyQuestStatus**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Milestones.DestinyMilestoneQuest":   {
      "description": "If a Milestone has one or more Quests, this will contain the live information for the character's status with one of those quests.",
      "type": "object",
      "properties": {
          "questItemHash": {
              "format": "uint32",
              "description": "Quests are defined as Items in content. As such, this is the hash identifier of the DestinyInventoryItemDefinition that represents this quest. It will have pointers to all of the steps in the quest, and display information for the quest (title, description, icon etc) Individual steps will be referred to in the Quest item's DestinyInventoryItemDefinition.setData property, and themselves are Items with their own renderable data.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "status": {
              "description": "The current status of the quest for the character making the request.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Quests.DestinyQuestStatus"
                  }
              ]
          },
          "activity": {
              "description": "*IF* the Milestone has an active Activity that can give you greater details about what you need to do, it will be returned here. Remember to associate this with the DestinyMilestoneDefinition's activities to get details about the activity, including what specific quest it is related to if you have multiple quests to choose from.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Milestones.DestinyMilestoneActivity"
                  }
              ]
          },
          "challenges": {
              "description": "The activities referred to by this quest can have many associated challenges. They are all contained here, with activityHashes so that you can associate them with the specific activity variants in which they can be found. In retrospect, I probably should have put these under the specific Activity Variants, but it's too late to change it now. Theoretically, a quest without Activities can still have Challenges, which is why this is on a higher level than activity/variants, but it probably should have been in both places. That may come as a later revision.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Challenges.DestinyChallengeStatus"
              }
          }
      }
  }
}
```
