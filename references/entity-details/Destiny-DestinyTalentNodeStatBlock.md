# Destiny.DestinyTalentNodeStatBlock

## Entity Information
- **Entity Name**: Destiny.DestinyTalentNodeStatBlock
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
This property has some history. A talent grid can provide stats on both the item it's related to and the character equipping the item. This returns data about those stat bonuses.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| currentStepStats | Array[Destiny.DestinyStat] | The stat benefits conferred when this talent node is activated for the current Step that is active on the node. | No |
| nextStepStats | Array[Destiny.DestinyStat] | This is a holdover from the old days of Destiny 1, when a node could be activated multiple times, conferring multiple steps worth of benefits: you would use this property to show what activating the "next" step on the node would provide vs. what the current step is providing. While Nodes are currently not being used this way, the underlying system for this functionality still exists. I hesitate to remove this property while the ability for designers to make such a talent grid still exists. Whether you want to show it is up to you. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.DestinyTalentNodeStatBlock object
const example = {
  currentStepStats: [],
  nextStepStats: [],
};
```

### Python
```python
# Example Destiny.DestinyTalentNodeStatBlock object
example = {
    "currentStepStats": [],
    "nextStepStats": [],
}
```

## Related Entities
- **Destiny.DestinyStat**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyTalentNodeStatBlock":   {
      "description": "This property has some history. A talent grid can provide stats on both the item it's related to and the character equipping the item. This returns data about those stat bonuses.",
      "type": "object",
      "properties": {
          "currentStepStats": {
              "description": "The stat benefits conferred when this talent node is activated for the current Step that is active on the node.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.DestinyStat"
              }
          },
          "nextStepStats": {
              "description": "This is a holdover from the old days of Destiny 1, when a node could be activated multiple times, conferring multiple steps worth of benefits: you would use this property to show what activating the \"next\" step on the node would provide vs. what the current step is providing. While Nodes are currently not being used this way, the underlying system for this functionality still exists. I hesitate to remove this property while the ability for designers to make such a talent grid still exists. Whether you want to show it is up to you.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.DestinyStat"
              }
          }
      }
  }
}
```
