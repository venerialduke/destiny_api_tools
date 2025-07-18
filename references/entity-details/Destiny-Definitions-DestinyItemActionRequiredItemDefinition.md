# Destiny.Definitions.DestinyItemActionRequiredItemDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemActionRequiredItemDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The definition of an item and quantity required in a character's inventory in order to perform an action.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| count | integer (int32) | The minimum quantity of the item you have to have. | No |
| itemHash | integer (uint32) | The hash identifier of the item you need to have. Use it to look up the DestinyInventoryItemDefinition for more info. | No |
| deleteOnAction | boolean | If true, the item/quantity will be deleted from your inventory when the action is performed. Otherwise, you'll retain these required items after the action is complete. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemActionRequiredItemDefinition object
const example = {
  count: 123,
  itemHash: 123,
  deleteOnAction: true,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemActionRequiredItemDefinition object
example = {
    "count": 123,
    "itemHash": 123,
    "deleteOnAction": True,
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyItemActionRequiredItemDefinition":   {
      "description": "The definition of an item and quantity required in a character's inventory in order to perform an action.",
      "type": "object",
      "properties": {
          "count": {
              "format": "int32",
              "description": "The minimum quantity of the item you have to have.",
              "type": "integer"
          },
          "itemHash": {
              "format": "uint32",
              "description": "The hash identifier of the item you need to have. Use it to look up the DestinyInventoryItemDefinition for more info.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "deleteOnAction": {
              "description": "If true, the item/quantity will be deleted from your inventory when the action is performed. Otherwise, you'll retain these required items after the action is complete.",
              "type": "boolean"
          }
      }
  }
}
```
