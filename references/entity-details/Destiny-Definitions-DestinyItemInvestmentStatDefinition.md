# Destiny.Definitions.DestinyItemInvestmentStatDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemInvestmentStatDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Represents a "raw" investment stat, before calculated stats are calculated and before any DestinyStatGroupDefinition is applied to transform the stat into something closer to what you see in-game.
Because these won't match what you see in-game, consider carefully whether you really want to use these stats. I have left them in case someone can do something useful or interesting with the pre-processed statistics.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| statTypeHash | integer (uint32) | The hash identifier for the DestinyStatDefinition defining this stat. | No |
| value | integer (int32) | The raw "Investment" value for the stat, before transformations are performed to turn this raw stat into stats that are displayed in the game UI. | No |
| isConditionallyActive | boolean | If this is true, the stat will only be applied on the item in certain game state conditions, and we can't know statically whether or not this stat will be applied. Check the "live" API data instead for whether this value is being applied on a specific instance of the item in question, and you can use this to decide whether you want to show the stat on the generic view of the item, or whether you want to show some kind of caveat or warning about the stat value being conditional on game state. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemInvestmentStatDefinition object
const example = {
  statTypeHash: 123,
  value: 123,
  isConditionallyActive: true,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemInvestmentStatDefinition object
example = {
    "statTypeHash": 123,
    "value": 123,
    "isConditionallyActive": True,
}
```

## Related Entities
- **Destiny.Definitions.DestinyStatDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyItemInvestmentStatDefinition":   {
      "description": "Represents a \"raw\" investment stat, before calculated stats are calculated and before any DestinyStatGroupDefinition is applied to transform the stat into something closer to what you see in-game.\r\nBecause these won't match what you see in-game, consider carefully whether you really want to use these stats. I have left them in case someone can do something useful or interesting with the pre-processed statistics.",
      "type": "object",
      "properties": {
          "statTypeHash": {
              "format": "uint32",
              "description": "The hash identifier for the DestinyStatDefinition defining this stat.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyStatDefinition"
              }
          },
          "value": {
              "format": "int32",
              "description": "The raw \"Investment\" value for the stat, before transformations are performed to turn this raw stat into stats that are displayed in the game UI.",
              "type": "integer"
          },
          "isConditionallyActive": {
              "description": "If this is true, the stat will only be applied on the item in certain game state conditions, and we can't know statically whether or not this stat will be applied. Check the \"live\" API data instead for whether this value is being applied on a specific instance of the item in question, and you can use this to decide whether you want to show the stat on the generic view of the item, or whether you want to show some kind of caveat or warning about the stat value being conditional on game state.",
              "type": "boolean"
          }
      }
  }
}
```
