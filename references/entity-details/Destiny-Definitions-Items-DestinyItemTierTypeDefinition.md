# Destiny.Definitions.Items.DestinyItemTierTypeDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Items.DestinyItemTierTypeDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Defines the tier type of an item. Mostly this provides human readable properties for types like Common, Rare, etc...
It also provides some base data for infusion that could be useful.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| infusionProcess | object | If this tier defines infusion properties, they will be contained here. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Items.DestinyItemTierTypeDefinition object
const example = {
  displayProperties: null,
  infusionProcess: null,
  hash: 123,
  index: 123,
  redacted: true,
};
```

### Python
```python
# Example Destiny.Definitions.Items.DestinyItemTierTypeDefinition object
example = {
    "displayProperties": None,
    "infusionProcess": None,
    "hash": 123,
    "index": 123,
    "redacted": True,
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.Items.DestinyItemTierTypeInfusionBlock**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Items.DestinyItemTierTypeDefinition":   {
      "description": "Defines the tier type of an item. Mostly this provides human readable properties for types like Common, Rare, etc...\r\nIt also provides some base data for infusion that could be useful.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "infusionProcess": {
              "description": "If this tier defines infusion properties, they will be contained here.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Items.DestinyItemTierTypeInfusionBlock"
                  }
              ]
          },
          "hash": {
              "format": "uint32",
              "description": "The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.\r\nWhen entities refer to each other in Destiny content, it is this hash that they are referring to.",
              "type": "integer"
          },
          "index": {
              "format": "int32",
              "description": "The index of the entity as it was found in the investment tables.",
              "type": "integer"
          },
          "redacted": {
              "description": "If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!",
              "type": "boolean"
          }
      },
      "x-mobile-manifest-name": "ItemTierTypes"
  }
}
```
