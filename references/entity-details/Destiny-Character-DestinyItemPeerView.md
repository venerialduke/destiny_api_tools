# Destiny.Character.DestinyItemPeerView

## Entity Information
- **Entity Name**: Destiny.Character.DestinyItemPeerView
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Bare minimum summary information for an item, for the sake of 3D rendering the item.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| itemHash | integer (uint32) | The hash identifier of the item in question. Use it to look up the DestinyInventoryItemDefinition of the item for static rendering data. | No |
| dyes | Array[Destiny.DyeReference] | The list of dyes that have been applied to this item. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Character.DestinyItemPeerView object
const example = {
  itemHash: 123,
  dyes: [],
};
```

### Python
```python
# Example Destiny.Character.DestinyItemPeerView object
example = {
    "itemHash": 123,
    "dyes": [],
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.DyeReference**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Character.DestinyItemPeerView":   {
      "description": "Bare minimum summary information for an item, for the sake of 3D rendering the item.",
      "type": "object",
      "properties": {
          "itemHash": {
              "format": "uint32",
              "description": "The hash identifier of the item in question. Use it to look up the DestinyInventoryItemDefinition of the item for static rendering data.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "dyes": {
              "description": "The list of dyes that have been applied to this item.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.DyeReference"
              }
          }
      }
  }
}
```
