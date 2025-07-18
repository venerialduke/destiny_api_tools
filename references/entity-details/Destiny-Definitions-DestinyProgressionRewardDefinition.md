# Destiny.Definitions.DestinyProgressionRewardDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyProgressionRewardDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Inventory Items can reward progression when actions are performed on them. A common example of this in Destiny 1 was Bounties, which would reward Experience on your Character and the like when you completed the bounty.
Note that this maps to a DestinyProgressionMappingDefinition, and *not* a DestinyProgressionDefinition directly. This is apparently so that multiple progressions can be granted progression points/experience at the same time.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| progressionMappingHash | integer (uint32) | The hash identifier of the DestinyProgressionMappingDefinition that contains the progressions for which experience should be applied. | No |
| amount | integer (int32) | The amount of experience to give to each of the mapped progressions. | No |
| applyThrottles | boolean | If true, the game's internal mechanisms to throttle progression should be applied. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyProgressionRewardDefinition object
const example = {
  progressionMappingHash: 123,
  amount: 123,
  applyThrottles: true,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyProgressionRewardDefinition object
example = {
    "progressionMappingHash": 123,
    "amount": 123,
    "applyThrottles": True,
}
```

## Related Entities
- **Destiny.Definitions.DestinyProgressionMappingDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyProgressionRewardDefinition":   {
      "description": "Inventory Items can reward progression when actions are performed on them. A common example of this in Destiny 1 was Bounties, which would reward Experience on your Character and the like when you completed the bounty.\r\nNote that this maps to a DestinyProgressionMappingDefinition, and *not* a DestinyProgressionDefinition directly. This is apparently so that multiple progressions can be granted progression points/experience at the same time.",
      "type": "object",
      "properties": {
          "progressionMappingHash": {
              "format": "uint32",
              "description": "The hash identifier of the DestinyProgressionMappingDefinition that contains the progressions for which experience should be applied.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyProgressionMappingDefinition"
              }
          },
          "amount": {
              "format": "int32",
              "description": "The amount of experience to give to each of the mapped progressions.",
              "type": "integer"
          },
          "applyThrottles": {
              "description": "If true, the game's internal mechanisms to throttle progression should be applied.",
              "type": "boolean"
          }
      }
  }
}
```
