# Destiny.Definitions.Milestones.DestinyMilestoneRewardCategoryDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Milestones.DestinyMilestoneRewardCategoryDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The definition of a category of rewards, that contains many individual rewards.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| categoryHash | integer (uint32) | Identifies the reward category. Only guaranteed unique within this specific component! | No |
| categoryIdentifier | string | The string identifier for the category, if you want to use it for some end. Guaranteed unique within the specific component. | No |
| displayProperties | object | Hopefully this is obvious by now. | No |
| rewardEntries | object | If this milestone can provide rewards, this will define the sets of rewards that can be earned, the conditions under which they can be acquired, internal data that we'll use at runtime to determine whether you've already earned or redeemed this set of rewards, and the category that this reward should be placed under. | No |
| order | integer (int32) | If you want to use BNet's recommended order for rendering categories programmatically, use this value and compare it to other categories to determine the order in which they should be rendered. I don't feel great about putting this here, I won't lie. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Milestones.DestinyMilestoneRewardCategoryDefinition object
const example = {
  categoryHash: 123,
  categoryIdentifier: "example value",
  displayProperties: null,
  rewardEntries: null,
  order: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Milestones.DestinyMilestoneRewardCategoryDefinition object
example = {
    "categoryHash": 123,
    "categoryIdentifier": "example value",
    "displayProperties": None,
    "rewardEntries": None,
    "order": 123,
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.Milestones.DestinyMilestoneRewardEntryDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Milestones.DestinyMilestoneRewardCategoryDefinition":   {
      "description": "The definition of a category of rewards, that contains many individual rewards.",
      "type": "object",
      "properties": {
          "categoryHash": {
              "format": "uint32",
              "description": "Identifies the reward category. Only guaranteed unique within this specific component!",
              "type": "integer"
          },
          "categoryIdentifier": {
              "description": "The string identifier for the category, if you want to use it for some end. Guaranteed unique within the specific component.",
              "type": "string"
          },
          "displayProperties": {
              "description": "Hopefully this is obvious by now.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
                  }
              ]
          },
          "rewardEntries": {
              "description": "If this milestone can provide rewards, this will define the sets of rewards that can be earned, the conditions under which they can be acquired, internal data that we'll use at runtime to determine whether you've already earned or redeemed this set of rewards, and the category that this reward should be placed under.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.Definitions.Milestones.DestinyMilestoneRewardEntryDefinition"
              }
          },
          "order": {
              "format": "int32",
              "description": "If you want to use BNet's recommended order for rendering categories programmatically, use this value and compare it to other categories to determine the order in which they should be rendered. I don't feel great about putting this here, I won't lie.",
              "type": "integer"
          }
      }
  }
}
```
