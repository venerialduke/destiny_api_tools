# Destiny.Definitions.DestinyActivityRewardDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyActivityRewardDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Activities can refer to one or more sets of tooltip-friendly reward data. These are the definitions for those tooltip friendly rewards.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| rewardText | string | The header for the reward set, if any. | No |
| rewardItems | Array[Destiny.DestinyItemQuantity] | The "Items provided" in the reward. This is almost always a pointer to a DestinyInventoryItemDefintion for an item that you can't actually earn in-game, but that has name/description/icon information for the vague concept of the rewards you will receive. This is because the actual reward generation is non-deterministic and extremely complicated, so the best the game can do is tell you what you'll get in vague terms. And so too shall we.
Interesting trivia: you actually *do* earn these items when you complete the activity. They go into a single-slot bucket on your profile, which is how you see the pop-ups of these rewards when you complete an activity that match these "dummy" items. You can even see them if you look at the last one you earned in your profile-level inventory through the BNet API! Who said reading documentation is a waste of time? | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyActivityRewardDefinition object
const example = {
  rewardText: "example value",
  rewardItems: [],
};
```

### Python
```python
# Example Destiny.Definitions.DestinyActivityRewardDefinition object
example = {
    "rewardText": "example value",
    "rewardItems": [],
}
```

## Related Entities
- **Destiny.DestinyItemQuantity**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyActivityRewardDefinition":   {
      "description": "Activities can refer to one or more sets of tooltip-friendly reward data. These are the definitions for those tooltip friendly rewards.",
      "type": "object",
      "properties": {
          "rewardText": {
              "description": "The header for the reward set, if any.",
              "type": "string"
          },
          "rewardItems": {
              "description": "The \"Items provided\" in the reward. This is almost always a pointer to a DestinyInventoryItemDefintion for an item that you can't actually earn in-game, but that has name/description/icon information for the vague concept of the rewards you will receive. This is because the actual reward generation is non-deterministic and extremely complicated, so the best the game can do is tell you what you'll get in vague terms. And so too shall we.\r\nInteresting trivia: you actually *do* earn these items when you complete the activity. They go into a single-slot bucket on your profile, which is how you see the pop-ups of these rewards when you complete an activity that match these \"dummy\" items. You can even see them if you look at the last one you earned in your profile-level inventory through the BNet API! Who said reading documentation is a waste of time?",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.DestinyItemQuantity"
              }
          }
      }
  }
}
```
