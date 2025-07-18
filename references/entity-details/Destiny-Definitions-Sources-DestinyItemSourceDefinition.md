# Destiny.Definitions.Sources.DestinyItemSourceDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Sources.DestinyItemSourceDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Properties of a DestinyInventoryItemDefinition that store all of the information we were able to discern about how the item spawns, and where you can find the item.
Items will have many of these sources, one per level at which it spawns, to try and give more granular data about where items spawn for specific level ranges.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| level | integer (int32) | The level at which the item spawns. Essentially the Primary Key for this source data: there will be multiple of these source entries per item that has source data, grouped by the level at which the item spawns. | No |
| minQuality | integer (int32) | The minimum Quality at which the item spawns for this level. Examine DestinyInventoryItemDefinition for more information about what Quality means. Just don't ask Phaedrus about it, he'll never stop talking and you'll have to write a book about it. | No |
| maxQuality | integer (int32) | The maximum quality at which the item spawns for this level. | No |
| minLevelRequired | integer (int32) | The minimum Character Level required for equipping the item when the item spawns at the item level defined on this DestinyItemSourceDefinition, as far as we saw in our processing. | No |
| maxLevelRequired | integer (int32) | The maximum Character Level required for equipping the item when the item spawns at the item level defined on this DestinyItemSourceDefinition, as far as we saw in our processing. | No |
| computedStats | object | The stats computed for this level/quality range. | No |
| sourceHashes | Array[integer] | The DestinyRewardSourceDefinitions found that can spawn the item at this level. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Sources.DestinyItemSourceDefinition object
const example = {
  level: 123,
  minQuality: 123,
  maxQuality: 123,
  minLevelRequired: 123,
  maxLevelRequired: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Sources.DestinyItemSourceDefinition object
example = {
    "level": 123,
    "minQuality": 123,
    "maxQuality": 123,
    "minLevelRequired": 123,
    "maxLevelRequired": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryItemStatDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyRewardSourceDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Sources.DestinyItemSourceDefinition":   {
      "description": "Properties of a DestinyInventoryItemDefinition that store all of the information we were able to discern about how the item spawns, and where you can find the item.\r\nItems will have many of these sources, one per level at which it spawns, to try and give more granular data about where items spawn for specific level ranges.",
      "type": "object",
      "properties": {
          "level": {
              "format": "int32",
              "description": "The level at which the item spawns. Essentially the Primary Key for this source data: there will be multiple of these source entries per item that has source data, grouped by the level at which the item spawns.",
              "type": "integer"
          },
          "minQuality": {
              "format": "int32",
              "description": "The minimum Quality at which the item spawns for this level. Examine DestinyInventoryItemDefinition for more information about what Quality means. Just don't ask Phaedrus about it, he'll never stop talking and you'll have to write a book about it.",
              "type": "integer"
          },
          "maxQuality": {
              "format": "int32",
              "description": "The maximum quality at which the item spawns for this level.",
              "type": "integer"
          },
          "minLevelRequired": {
              "format": "int32",
              "description": "The minimum Character Level required for equipping the item when the item spawns at the item level defined on this DestinyItemSourceDefinition, as far as we saw in our processing.",
              "type": "integer"
          },
          "maxLevelRequired": {
              "format": "int32",
              "description": "The maximum Character Level required for equipping the item when the item spawns at the item level defined on this DestinyItemSourceDefinition, as far as we saw in our processing.",
              "type": "integer"
          },
          "computedStats": {
              "description": "The stats computed for this level/quality range.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemStatDefinition"
              }
          },
          "sourceHashes": {
              "description": "The DestinyRewardSourceDefinitions found that can spawn the item at this level.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyRewardSourceDefinition"
              }
          }
      }
  }
}
```
