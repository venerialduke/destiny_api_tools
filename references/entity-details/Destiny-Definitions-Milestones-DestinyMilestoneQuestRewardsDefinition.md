# Destiny.Definitions.Milestones.DestinyMilestoneQuestRewardsDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Milestones.DestinyMilestoneQuestRewardsDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
If rewards are given in a quest - as opposed to overall in the entire Milestone - there's way less to track. We're going to simplify this contract as a result. However, this also gives us the opportunity to potentially put more than just item information into the reward data if we're able to mine it out in the future. Remember this if you come back and ask "why are quest reward items nested inside of their own class?"

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| items | Array[Destiny.Definitions.Milestones.DestinyMilestoneQuestRewardItem] | The items that represent your reward for completing the quest.
Be warned, these could be "dummy" items: items that are only used to render a good-looking in-game tooltip, but aren't the actual items themselves.
For instance, when experience is given there's often a dummy item representing "experience", with quantity being the amount of experience you got. We don't have a programmatic association between those and whatever Progression is actually getting that experience... yet. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Milestones.DestinyMilestoneQuestRewardsDefinition object
const example = {
  items: [],
};
```

### Python
```python
# Example Destiny.Definitions.Milestones.DestinyMilestoneQuestRewardsDefinition object
example = {
    "items": [],
}
```

## Related Entities
- **Destiny.Definitions.Milestones.DestinyMilestoneQuestRewardItem**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Milestones.DestinyMilestoneQuestRewardsDefinition":   {
      "description": "If rewards are given in a quest - as opposed to overall in the entire Milestone - there's way less to track. We're going to simplify this contract as a result. However, this also gives us the opportunity to potentially put more than just item information into the reward data if we're able to mine it out in the future. Remember this if you come back and ask \"why are quest reward items nested inside of their own class?\"",
      "type": "object",
      "properties": {
          "items": {
              "description": "The items that represent your reward for completing the quest.\r\nBe warned, these could be \"dummy\" items: items that are only used to render a good-looking in-game tooltip, but aren't the actual items themselves.\r\nFor instance, when experience is given there's often a dummy item representing \"experience\", with quantity being the amount of experience you got. We don't have a programmatic association between those and whatever Progression is actually getting that experience... yet.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Milestones.DestinyMilestoneQuestRewardItem"
              }
          }
      }
  }
}
```
