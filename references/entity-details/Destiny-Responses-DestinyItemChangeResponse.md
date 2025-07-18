# Destiny.Responses.DestinyItemChangeResponse

## Entity Information
- **Entity Name**: Destiny.Responses.DestinyItemChangeResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyitemchangeresponse data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| item | Destiny.Responses.DestinyItemResponse |  | No |
| addedInventoryItems | Array[Destiny.Entities.Items.DestinyItemComponent] | Items that appeared in the inventory possibly as a result of an action. | No |
| removedInventoryItems | Array[Destiny.Entities.Items.DestinyItemComponent] | Items that disappeared from the inventory possibly as a result of an action. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Responses.DestinyItemChangeResponse object
const example = {
  item: null,
  addedInventoryItems: [],
  removedInventoryItems: [],
};
```

### Python
```python
# Example Destiny.Responses.DestinyItemChangeResponse object
example = {
    "item": None,
    "addedInventoryItems": [],
    "removedInventoryItems": [],
}
```

## Related Entities
- **Destiny.Entities.Items.DestinyItemComponent**: Referenced in this entity
- **Destiny.Responses.DestinyItemResponse**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Responses.DestinyItemChangeResponse":   {
      "type": "object",
      "properties": {
          "item": {
              "$ref": "#/definitions/Destiny.Responses.DestinyItemResponse"
          },
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
