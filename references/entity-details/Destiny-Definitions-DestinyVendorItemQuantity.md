# Destiny.Definitions.DestinyVendorItemQuantity

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyVendorItemQuantity
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
In addition to item quantity information for vendor prices, this also has any optional information that may exist about how the item's quantity can be modified. (unfortunately not information that is able to be read outside of the BNet servers, but it's there)

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| itemHash | integer (uint32) | The hash identifier for the item in question. Use it to look up the item's DestinyInventoryItemDefinition. | No |
| itemInstanceId | integer (int64) | If this quantity is referring to a specific instance of an item, this will have the item's instance ID. Normally, this will be null. | No |
| quantity | integer (int32) | The amount of the item needed/available depending on the context of where DestinyItemQuantity is being used. | No |
| hasConditionalVisibility | boolean | Indicates that this item quantity may be conditionally shown or hidden, based on various sources of state. For example: server flags, account state, or character progress. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyVendorItemQuantity object
const example = {
  itemHash: 123,
  itemInstanceId: 123,
  quantity: 123,
  hasConditionalVisibility: true,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyVendorItemQuantity object
example = {
    "itemHash": 123,
    "itemInstanceId": 123,
    "quantity": 123,
    "hasConditionalVisibility": True,
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
  "Destiny.Definitions.DestinyVendorItemQuantity":   {
      "description": "In addition to item quantity information for vendor prices, this also has any optional information that may exist about how the item's quantity can be modified. (unfortunately not information that is able to be read outside of the BNet servers, but it's there)",
      "type": "object",
      "properties": {
          "itemHash": {
              "format": "uint32",
              "description": "The hash identifier for the item in question. Use it to look up the item's DestinyInventoryItemDefinition.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "itemInstanceId": {
              "format": "int64",
              "description": "If this quantity is referring to a specific instance of an item, this will have the item's instance ID. Normally, this will be null.",
              "type": "integer"
          },
          "quantity": {
              "format": "int32",
              "description": "The amount of the item needed/available depending on the context of where DestinyItemQuantity is being used.",
              "type": "integer"
          },
          "hasConditionalVisibility": {
              "description": "Indicates that this item quantity may be conditionally shown or hidden, based on various sources of state. For example: server flags, account state, or character progress.",
              "type": "boolean"
          }
      }
  }
}
```
