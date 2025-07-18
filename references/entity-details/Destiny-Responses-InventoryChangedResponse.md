# Destiny.Responses.InventoryChangedResponse

## Entity Information
- **Entity Name**: Destiny.Responses.InventoryChangedResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
A response containing all of the components for all requested vendors.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| addedInventoryItems | Array[Destiny.Entities.Items.DestinyItemComponent] | Items that appeared in the inventory possibly as a result of an action. | No |
| removedInventoryItems | Array[Destiny.Entities.Items.DestinyItemComponent] | Items that disappeared from the inventory possibly as a result of an action. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Responses.InventoryChangedResponse object
const example = {
  addedInventoryItems: [],
  removedInventoryItems: [],
};
```

### Python
```python
# Example Destiny.Responses.InventoryChangedResponse object
example = {
    "addedInventoryItems": [],
    "removedInventoryItems": [],
}
```

## Related Entities
- **Destiny.Entities.Items.DestinyItemComponent**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Responses.InventoryChangedResponse":   {
      "description": "A response containing all of the components for all requested vendors.",
      "type": "object",
      "properties": {
          "addedInventoryItems": {
              "description": "Items that appeared in the inventory possibly as a result of an action.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Entities.Items.DestinyItemComponent"
              }
          },
          "removedInventoryItems": {
              "description": "Items that disappeared from the inventory possibly as a result of an action.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Entities.Items.DestinyItemComponent"
              }
          }
      }
  }
}
```
