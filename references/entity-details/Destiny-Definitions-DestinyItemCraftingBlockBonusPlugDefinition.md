# Destiny.Definitions.DestinyItemCraftingBlockBonusPlugDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemCraftingBlockBonusPlugDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyitemcraftingblockbonusplugdefinition data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| socketTypeHash | integer (uint32) |  | No |
| plugItemHash | integer (uint32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemCraftingBlockBonusPlugDefinition object
const example = {
  socketTypeHash: 123,
  plugItemHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemCraftingBlockBonusPlugDefinition object
example = {
    "socketTypeHash": 123,
    "plugItemHash": 123,
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.Sockets.DestinySocketTypeDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyItemCraftingBlockBonusPlugDefinition":   {
      "type": "object",
      "properties": {
          "socketTypeHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Sockets.DestinySocketTypeDefinition"
              }
          },
          "plugItemHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          }
      }
  }
}
```
