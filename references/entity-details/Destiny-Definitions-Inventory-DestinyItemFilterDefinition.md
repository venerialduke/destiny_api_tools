# Destiny.Definitions.Inventory.DestinyItemFilterDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Inventory.DestinyItemFilterDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Lists of items that can be used for a variety of purposes, including featuring them as new gear

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| setItems | Array[integer] | The items in this set | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Inventory.DestinyItemFilterDefinition object
const example = {
  setItems: [],
  hash: 123,
  index: 123,
  redacted: true,
};
```

### Python
```python
# Example Destiny.Definitions.Inventory.DestinyItemFilterDefinition object
example = {
    "setItems": [],
    "hash": 123,
    "index": 123,
    "redacted": True,
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Inventory.DestinyItemFilterDefinition":   {
      "description": "Lists of items that can be used for a variety of purposes, including featuring them as new gear",
      "type": "object",
      "properties": {
          "setItems": {
              "description": "The items in this set",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
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
      "x-mobile-manifest-name": "itemFilters"
  }
}
```
