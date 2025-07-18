# Destiny.Activities.DestinyPublicActivityStatus

## Entity Information
- **Entity Name**: Destiny.Activities.DestinyPublicActivityStatus
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Represents the public-facing status of an activity: any data about what is currently active in the Activity, regardless of an individual character's progress in it.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| challengeObjectiveHashes | Array[integer] | Active Challenges for the activity, if any - represented as hashes for DestinyObjectiveDefinitions. | No |
| modifierHashes | Array[integer] | The active modifiers on this activity, if any - represented as hashes for DestinyActivityModifierDefinitions. | No |
| rewardTooltipItems | Array[Destiny.DestinyItemQuantity] | If the activity itself provides any specific "mock" rewards, this will be the items and their quantity.
Why "mock", you ask? Because these are the rewards as they are represented in the tooltip of the Activity.
These are often pointers to fake items that look good in a tooltip, but represent an abstract concept of what you will get for a reward rather than the specific items you may obtain. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Activities.DestinyPublicActivityStatus object
const example = {
  challengeObjectiveHashes: [],
  modifierHashes: [],
  rewardTooltipItems: [],
};
```

### Python
```python
# Example Destiny.Activities.DestinyPublicActivityStatus object
example = {
    "challengeObjectiveHashes": [],
    "modifierHashes": [],
    "rewardTooltipItems": [],
}
```

## Related Entities
- **Destiny.Definitions.ActivityModifiers.DestinyActivityModifierDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyObjectiveDefinition**: Referenced in this entity
- **Destiny.DestinyItemQuantity**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Activities.DestinyPublicActivityStatus":   {
      "description": "Represents the public-facing status of an activity: any data about what is currently active in the Activity, regardless of an individual character's progress in it.",
      "type": "object",
      "properties": {
          "challengeObjectiveHashes": {
              "description": "Active Challenges for the activity, if any - represented as hashes for DestinyObjectiveDefinitions.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyObjectiveDefinition"
              }
          },
          "modifierHashes": {
              "description": "The active modifiers on this activity, if any - represented as hashes for DestinyActivityModifierDefinitions.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.ActivityModifiers.DestinyActivityModifierDefinition"
              }
          },
          "rewardTooltipItems": {
              "description": "If the activity itself provides any specific \"mock\" rewards, this will be the items and their quantity.\r\nWhy \"mock\", you ask? Because these are the rewards as they are represented in the tooltip of the Activity.\r\nThese are often pointers to fake items that look good in a tooltip, but represent an abstract concept of what you will get for a reward rather than the specific items you may obtain.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.DestinyItemQuantity"
              }
          }
      }
  }
}
```
