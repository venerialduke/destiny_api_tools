# Destiny.Milestones.DestinyMilestoneRewardCategory

## Entity Information
- **Entity Name**: Destiny.Milestones.DestinyMilestoneRewardCategory
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Represents a category of "summary" rewards that can be earned for the Milestone regardless of specific quest rewards that can be earned.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| rewardCategoryHash | integer (uint32) | Look up the relevant DestinyMilestoneDefinition, and then use rewardCategoryHash to look up the category info in DestinyMilestoneDefinition.rewards. | No |
| entries | Array[Destiny.Milestones.DestinyMilestoneRewardEntry] | The individual reward entries for this category, and their status. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Milestones.DestinyMilestoneRewardCategory object
const example = {
  rewardCategoryHash: 123,
  entries: [],
};
```

### Python
```python
# Example Destiny.Milestones.DestinyMilestoneRewardCategory object
example = {
    "rewardCategoryHash": 123,
    "entries": [],
}
```

## Related Entities
- **Destiny.Milestones.DestinyMilestoneRewardEntry**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Milestones.DestinyMilestoneRewardCategory":   {
      "description": "Represents a category of \"summary\" rewards that can be earned for the Milestone regardless of specific quest rewards that can be earned.",
      "type": "object",
      "properties": {
          "rewardCategoryHash": {
              "format": "uint32",
              "description": "Look up the relevant DestinyMilestoneDefinition, and then use rewardCategoryHash to look up the category info in DestinyMilestoneDefinition.rewards.",
              "type": "integer"
          },
          "entries": {
              "description": "The individual reward entries for this category, and their status.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Milestones.DestinyMilestoneRewardEntry"
              }
          }
      }
  }
}
```
