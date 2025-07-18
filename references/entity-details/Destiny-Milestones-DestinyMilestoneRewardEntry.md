# Destiny.Milestones.DestinyMilestoneRewardEntry

## Entity Information
- **Entity Name**: Destiny.Milestones.DestinyMilestoneRewardEntry
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The character-specific data for a milestone's reward entry. See DestinyMilestoneDefinition for more information about Reward Entries.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| rewardEntryHash | integer (uint32) | The identifier for the reward entry in question. It is important to look up the related DestinyMilestoneRewardEntryDefinition to get the static details about the reward, which you can do by looking up the milestone's DestinyMilestoneDefinition and examining the DestinyMilestoneDefinition.rewards[rewardCategoryHash].rewardEntries[rewardEntryHash] data. | No |
| earned | boolean | If TRUE, the player has earned this reward. | No |
| redeemed | boolean | If TRUE, the player has redeemed/picked up/obtained this reward. Feel free to alias this to "gotTheShinyBauble" in your own codebase. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Milestones.DestinyMilestoneRewardEntry object
const example = {
  rewardEntryHash: 123,
  earned: true,
  redeemed: true,
};
```

### Python
```python
# Example Destiny.Milestones.DestinyMilestoneRewardEntry object
example = {
    "rewardEntryHash": 123,
    "earned": True,
    "redeemed": True,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Milestones.DestinyMilestoneRewardEntry":   {
      "description": "The character-specific data for a milestone's reward entry. See DestinyMilestoneDefinition for more information about Reward Entries.",
      "type": "object",
      "properties": {
          "rewardEntryHash": {
              "format": "uint32",
              "description": "The identifier for the reward entry in question. It is important to look up the related DestinyMilestoneRewardEntryDefinition to get the static details about the reward, which you can do by looking up the milestone's DestinyMilestoneDefinition and examining the DestinyMilestoneDefinition.rewards[rewardCategoryHash].rewardEntries[rewardEntryHash] data.",
              "type": "integer"
          },
          "earned": {
              "description": "If TRUE, the player has earned this reward.",
              "type": "boolean"
          },
          "redeemed": {
              "description": "If TRUE, the player has redeemed/picked up/obtained this reward. Feel free to alias this to \"gotTheShinyBauble\" in your own codebase.",
              "type": "boolean"
          }
      }
  }
}
```
