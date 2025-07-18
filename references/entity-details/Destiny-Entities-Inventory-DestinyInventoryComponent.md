# Destiny.Entities.Inventory.DestinyInventoryComponent

## Entity Information
- **Entity Name**: Destiny.Entities.Inventory.DestinyInventoryComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
A list of minimal information for items in an inventory: be it a character's inventory, or a Profile's inventory. (Note that the Vault is a collection of inventory buckets in the Profile's inventory)
Inventory Items returned here are in a flat list, but importantly they have a bucketHash property that indicates the specific inventory bucket that is holding them. These buckets constitute things like the separate sections of the Vault, the user's inventory slots, etc. See DestinyInventoryBucketDefinition for more info.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| items | Array[Destiny.Entities.Items.DestinyItemComponent] | The items in this inventory. If you care to bucket them, use the item's bucketHash property to group them. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Entities.Inventory.DestinyInventoryComponent object
const example = {
  items: [],
};
```

### Python
```python
# Example Destiny.Entities.Inventory.DestinyInventoryComponent object
example = {
    "items": [],
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
  "Destiny.Entities.Inventory.DestinyInventoryComponent":   {
      "description": "A list of minimal information for items in an inventory: be it a character's inventory, or a Profile's inventory. (Note that the Vault is a collection of inventory buckets in the Profile's inventory)\r\nInventory Items returned here are in a flat list, but importantly they have a bucketHash property that indicates the specific inventory bucket that is holding them. These buckets constitute things like the separate sections of the Vault, the user's inventory slots, etc. See DestinyInventoryBucketDefinition for more info.",
      "type": "object",
      "properties": {
          "items": {
              "description": "The items in this inventory. If you care to bucket them, use the item's bucketHash property to group them.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Entities.Items.DestinyItemComponent"
              }
          }
      }
  }
}
```
