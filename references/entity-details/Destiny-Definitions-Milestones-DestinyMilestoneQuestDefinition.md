# Destiny.Definitions.Milestones.DestinyMilestoneQuestDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Milestones.DestinyMilestoneQuestDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Any data we need to figure out whether this Quest Item is the currently active one for the conceptual Milestone. Even just typing this description, I already regret it.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| questItemHash | integer (uint32) | The item representing this Milestone quest. Use this hash to look up the DestinyInventoryItemDefinition for the quest to find its steps and human readable data. | No |
| displayProperties | object | The individual quests may have different definitions from the overall milestone: if there's a specific active quest, use these displayProperties instead of that of the overall DestinyMilestoneDefinition. | No |
| overrideImage | string | If populated, this image can be shown instead of the generic milestone's image when this quest is live, or it can be used to show a background image for the quest itself that differs from that of the Activity or the Milestone. | No |
| questRewards | object | The rewards you will get for completing this quest, as best as we could extract them from our data. Sometimes, it'll be a decent amount of data. Sometimes, it's going to be sucky. Sorry. | No |
| activities | object | The full set of all possible "conceptual activities" that are related to this Milestone. Tiers or alternative modes of play within these conceptual activities will be defined as sub-entities. Keyed by the Conceptual Activity Hash. Use the key to look up DestinyActivityDefinition. | No |
| destinationHash | integer (uint32) | Sometimes, a Milestone's quest is related to an entire Destination rather than a specific activity. In that situation, this will be the hash of that Destination. Hotspots are currently the only Milestones that expose this data, but that does not preclude this data from being returned for other Milestones in the future. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Milestones.DestinyMilestoneQuestDefinition object
const example = {
  questItemHash: 123,
  displayProperties: null,
  overrideImage: "example value",
  questRewards: null,
  activities: null,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Milestones.DestinyMilestoneQuestDefinition object
example = {
    "questItemHash": 123,
    "displayProperties": None,
    "overrideImage": "example value",
    "questRewards": None,
    "activities": None,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyActivityDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyDestinationDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.Milestones.DestinyMilestoneActivityDefinition**: Referenced in this entity
- **Destiny.Definitions.Milestones.DestinyMilestoneQuestRewardsDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Milestones.DestinyMilestoneQuestDefinition":   {
      "description": "Any data we need to figure out whether this Quest Item is the currently active one for the conceptual Milestone. Even just typing this description, I already regret it.",
      "type": "object",
      "properties": {
          "questItemHash": {
              "format": "uint32",
              "description": "The item representing this Milestone quest. Use this hash to look up the DestinyInventoryItemDefinition for the quest to find its steps and human readable data.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "displayProperties": {
              "description": "The individual quests may have different definitions from the overall milestone: if there's a specific active quest, use these displayProperties instead of that of the overall DestinyMilestoneDefinition.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
                  }
              ]
          },
          "overrideImage": {
              "description": "If populated, this image can be shown instead of the generic milestone's image when this quest is live, or it can be used to show a background image for the quest itself that differs from that of the Activity or the Milestone.",
              "type": "string"
          },
          "questRewards": {
              "description": "The rewards you will get for completing this quest, as best as we could extract them from our data. Sometimes, it'll be a decent amount of data. Sometimes, it's going to be sucky. Sorry.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Milestones.DestinyMilestoneQuestRewardsDefinition"
                  }
              ]
          },
          "activities": {
              "description": "The full set of all possible \"conceptual activities\" that are related to this Milestone. Tiers or alternative modes of play within these conceptual activities will be defined as sub-entities. Keyed by the Conceptual Activity Hash. Use the key to look up DestinyActivityDefinition.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.Definitions.Milestones.DestinyMilestoneActivityDefinition"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityDefinition"
              }
          },
          "destinationHash": {
              "format": "uint32",
              "description": "Sometimes, a Milestone's quest is related to an entire Destination rather than a specific activity. In that situation, this will be the hash of that Destination. Hotspots are currently the only Milestones that expose this data, but that does not preclude this data from being returned for other Milestones in the future.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyDestinationDefinition"
              }
          }
      }
  }
}
```
