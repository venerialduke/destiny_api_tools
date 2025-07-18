# Destiny.Definitions.DestinyInventoryBucketDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyInventoryBucketDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
An Inventory (be it Character or Profile level) is comprised of many Buckets. An example of a bucket is "Primary Weapons", where all of the primary weapons on a character are gathered together into a single visual element in the UI: a subset of the inventory that has a limited number of slots, and in this case also has an associated Equipment Slot for equipping an item in the bucket.
Item definitions declare what their "default" bucket is (DestinyInventoryItemDefinition.inventory.bucketTypeHash), and Item instances will tell you which bucket they are currently residing in (DestinyItemComponent.bucketHash). You can use this information along with the DestinyInventoryBucketDefinition to show these items grouped by bucket.
You cannot transfer an item to a bucket that is not its Default without going through a Vendor's "accepted items" (DestinyVendorDefinition.acceptedItems). This is how transfer functionality like the Vault is implemented, as a feature of a Vendor. See the vendor's acceptedItems property for more details.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| scope | integer (int32) | Where the bucket is found. 0 = Character, 1 = Account | No |
| category | integer (int32) | An enum value for what items can be found in the bucket. See the BucketCategory enum for more details. | No |
| bucketOrder | integer (int32) | Use this property to provide a quick-and-dirty recommended ordering for buckets in the UI. Most UIs will likely want to forsake this for something more custom and manual. | No |
| itemCount | integer (int32) | The maximum # of item "slots" in a bucket. A slot is a given combination of item + quantity.
For instance, a Weapon will always take up a single slot, and always have a quantity of 1. But a material could take up only a single slot with hundreds of quantity. | No |
| location | integer (int32) | Sometimes, inventory buckets represent conceptual "locations" in the game that might not be expected. This value indicates the conceptual location of the bucket, regardless of where it is actually contained on the character/account. 
See ItemLocation for details. 
Note that location includes the Vault and the Postmaster (both of whom being just inventory buckets with additional actions that can be performed on them through a Vendor) | No |
| hasTransferDestination | boolean | If TRUE, there is at least one Vendor that can transfer items to/from this bucket. See the DestinyVendorDefinition's acceptedItems property for more information on how transferring works. | No |
| enabled | boolean | If True, this bucket is enabled. Disabled buckets may include buckets that were included for test purposes, or that were going to be used but then were abandoned but never removed from content *cough*. | No |
| fifo | boolean | if a FIFO bucket fills up, it will delete the oldest item from said bucket when a new item tries to be added to it. If this is FALSE, the bucket will not allow new items to be placed in it until room is made by the user manually deleting items from it. You can see an example of this with the Postmaster's bucket. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyInventoryBucketDefinition object
const example = {
  displayProperties: null,
  scope: 123,
  category: 123,
  bucketOrder: 123,
  itemCount: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyInventoryBucketDefinition object
example = {
    "displayProperties": None,
    "scope": 123,
    "category": 123,
    "bucketOrder": 123,
    "itemCount": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.BucketCategory**: Referenced in this entity
- **Destiny.BucketScope**: Referenced in this entity
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.ItemLocation**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyInventoryBucketDefinition":   {
      "description": "An Inventory (be it Character or Profile level) is comprised of many Buckets. An example of a bucket is \"Primary Weapons\", where all of the primary weapons on a character are gathered together into a single visual element in the UI: a subset of the inventory that has a limited number of slots, and in this case also has an associated Equipment Slot for equipping an item in the bucket.\r\nItem definitions declare what their \"default\" bucket is (DestinyInventoryItemDefinition.inventory.bucketTypeHash), and Item instances will tell you which bucket they are currently residing in (DestinyItemComponent.bucketHash). You can use this information along with the DestinyInventoryBucketDefinition to show these items grouped by bucket.\r\nYou cannot transfer an item to a bucket that is not its Default without going through a Vendor's \"accepted items\" (DestinyVendorDefinition.acceptedItems). This is how transfer functionality like the Vault is implemented, as a feature of a Vendor. See the vendor's acceptedItems property for more details.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "scope": {
              "format": "int32",
              "description": "Where the bucket is found. 0 = Character, 1 = Account",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.BucketScope"
              }
          },
          "category": {
              "format": "int32",
              "description": "An enum value for what items can be found in the bucket. See the BucketCategory enum for more details.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.BucketCategory"
              }
          },
          "bucketOrder": {
              "format": "int32",
              "description": "Use this property to provide a quick-and-dirty recommended ordering for buckets in the UI. Most UIs will likely want to forsake this for something more custom and manual.",
              "type": "integer"
          },
          "itemCount": {
              "format": "int32",
              "description": "The maximum # of item \"slots\" in a bucket. A slot is a given combination of item + quantity.\r\nFor instance, a Weapon will always take up a single slot, and always have a quantity of 1. But a material could take up only a single slot with hundreds of quantity.",
              "type": "integer"
          },
          "location": {
              "format": "int32",
              "description": "Sometimes, inventory buckets represent conceptual \"locations\" in the game that might not be expected. This value indicates the conceptual location of the bucket, regardless of where it is actually contained on the character/account. \r\nSee ItemLocation for details. \r\nNote that location includes the Vault and the Postmaster (both of whom being just inventory buckets with additional actions that can be performed on them through a Vendor)",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.ItemLocation"
              }
          },
          "hasTransferDestination": {
              "description": "If TRUE, there is at least one Vendor that can transfer items to/from this bucket. See the DestinyVendorDefinition's acceptedItems property for more information on how transferring works.",
              "type": "boolean"
          },
          "enabled": {
              "description": "If True, this bucket is enabled. Disabled buckets may include buckets that were included for test purposes, or that were going to be used but then were abandoned but never removed from content *cough*.",
              "type": "boolean"
          },
          "fifo": {
              "description": "if a FIFO bucket fills up, it will delete the oldest item from said bucket when a new item tries to be added to it. If this is FALSE, the bucket will not allow new items to be placed in it until room is made by the user manually deleting items from it. You can see an example of this with the Postmaster's bucket.",
              "type": "boolean"
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
      "x-mobile-manifest-name": "InventoryBuckets"
  }
}
```
