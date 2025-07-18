# Destiny.Definitions.Items.DestinyEquipableItemSetDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Items.DestinyEquipableItemSetDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Perks that are active only when you have a certain number of set items equipped.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | object | Display Properties, including name and icon, for this item set | No |
| setItems | Array[integer] | The items that confer these perks. | No |
| setPerks | Array[Destiny.Definitions.Items.DestinyItemSetPerkDefinition] | The perks conferred by this set of armor pieces. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Items.DestinyEquipableItemSetDefinition object
const example = {
  displayProperties: null,
  setItems: [],
  setPerks: [],
  hash: 123,
  index: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Items.DestinyEquipableItemSetDefinition object
example = {
    "displayProperties": None,
    "setItems": [],
    "setPerks": [],
    "hash": 123,
    "index": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.Items.DestinyItemSetPerkDefinition**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Items.DestinyEquipableItemSetDefinition":   {
      "description": "Perks that are active only when you have a certain number of set items equipped.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "description": "Display Properties, including name and icon, for this item set",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
                  }
              ]
          },
          "setItems": {
              "description": "The items that confer these perks.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "setPerks": {
              "description": "The perks conferred by this set of armor pieces.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Items.DestinyItemSetPerkDefinition"
              }
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
      "x-mobile-manifest-name": "EquipableItemSets"
  }
}
```
