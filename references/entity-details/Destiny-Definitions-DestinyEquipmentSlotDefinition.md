# Destiny.Definitions.DestinyEquipmentSlotDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyEquipmentSlotDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Characters can not only have Inventory buckets (containers of items that are generally matched by their type or functionality), they can also have Equipment Slots.
The Equipment Slot is an indicator that the related bucket can have instanced items equipped on the character. For instance, the Primary Weapon bucket has an Equipment Slot that determines whether you can equip primary weapons, and holds the association between its slot and the inventory bucket from which it can have items equipped.
An Equipment Slot must have a related Inventory Bucket, but not all inventory buckets must have Equipment Slots.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| equipmentCategoryHash | integer (uint32) | These technically point to "Equipment Category Definitions". But don't get excited. There's nothing of significant value in those definitions, so I didn't bother to expose them. You can use the hash here to group equipment slots by common functionality, which serves the same purpose as if we had the Equipment Category definitions exposed. | No |
| bucketTypeHash | integer (uint32) | The inventory bucket that owns this equipment slot. | No |
| applyCustomArtDyes | boolean | If True, equipped items should have their custom art dyes applied when rendering the item. Otherwise, custom art dyes on an item should be ignored if the item is equipped in this slot. | No |
| artDyeChannels | Array[Destiny.Definitions.DestinyArtDyeReference] | The Art Dye Channels that apply to this equipment slot. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyEquipmentSlotDefinition object
const example = {
  displayProperties: null,
  equipmentCategoryHash: 123,
  bucketTypeHash: 123,
  applyCustomArtDyes: true,
  artDyeChannels: [],
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyEquipmentSlotDefinition object
example = {
    "displayProperties": None,
    "equipmentCategoryHash": 123,
    "bucketTypeHash": 123,
    "applyCustomArtDyes": True,
    "artDyeChannels": [],
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyArtDyeReference**: Referenced in this entity
- **Destiny.Definitions.DestinyInventoryBucketDefinition**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyEquipmentSlotDefinition":   {
      "description": "Characters can not only have Inventory buckets (containers of items that are generally matched by their type or functionality), they can also have Equipment Slots.\r\nThe Equipment Slot is an indicator that the related bucket can have instanced items equipped on the character. For instance, the Primary Weapon bucket has an Equipment Slot that determines whether you can equip primary weapons, and holds the association between its slot and the inventory bucket from which it can have items equipped.\r\nAn Equipment Slot must have a related Inventory Bucket, but not all inventory buckets must have Equipment Slots.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "equipmentCategoryHash": {
              "format": "uint32",
              "description": "These technically point to \"Equipment Category Definitions\". But don't get excited. There's nothing of significant value in those definitions, so I didn't bother to expose them. You can use the hash here to group equipment slots by common functionality, which serves the same purpose as if we had the Equipment Category definitions exposed.",
              "type": "integer"
          },
          "bucketTypeHash": {
              "format": "uint32",
              "description": "The inventory bucket that owns this equipment slot.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryBucketDefinition"
              }
          },
          "applyCustomArtDyes": {
              "description": "If True, equipped items should have their custom art dyes applied when rendering the item. Otherwise, custom art dyes on an item should be ignored if the item is equipped in this slot.",
              "type": "boolean"
          },
          "artDyeChannels": {
              "description": "The Art Dye Channels that apply to this equipment slot.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyArtDyeReference"
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
      "x-mobile-manifest-name": "EquipmentSlots"
  }
}
```
