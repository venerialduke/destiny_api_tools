# Destiny.Entities.Vendors.DestinyVendorSaleItemComponent

## Entity Information
- **Entity Name**: Destiny.Entities.Vendors.DestinyVendorSaleItemComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Request this component if you want the details about an item being sold in relation to the character making the request: whether the character can buy it, whether they can afford it, and other data related to purchasing the item.
Note that if you want instance, stats, etc... data for the item, you'll have to request additional components such as ItemInstances, ItemPerks etc... and acquire them from the DestinyVendorResponse's "items" property.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| saleStatus | integer (int32) | A flag indicating whether the requesting character can buy the item, and if not the reasons why the character can't buy it. | No |
| requiredUnlocks | Array[integer] | If you can't buy the item due to a complex character state, these will be hashes for DestinyUnlockDefinitions that you can check to see messages regarding the failure (if the unlocks have human readable information: it is not guaranteed that Unlocks will have human readable strings, and your application will have to handle that)
Prefer using failureIndexes instead. These are provided for informational purposes, but have largely been supplanted by failureIndexes. | No |
| unlockStatuses | Array[Destiny.DestinyUnlockStatus] | If any complex unlock states are checked in determining purchasability, these will be returned here along with the status of the unlock check.
Prefer using failureIndexes instead. These are provided for informational purposes, but have largely been supplanted by failureIndexes. | No |
| failureIndexes | Array[integer] | Indexes in to the "failureStrings" lookup table in DestinyVendorDefinition for the given Vendor. Gives some more reliable failure information for why you can't purchase an item.
It is preferred to use these over requiredUnlocks and unlockStatuses: the latter are provided mostly in case someone can do something interesting with it that I didn't anticipate. | No |
| augments | integer (int32) | A flags enumeration value representing the current state of any "state modifiers" on the item being sold. These are meant to correspond with some sort of visual indicator as to the augmentation: for instance, if an item is on sale or if you already own the item in question.
Determining how you want to represent these in your own app (or if you even want to) is an exercise left for the reader. | No |
| itemValueVisibility | Array[boolean] | If available, a list that describes which item values (rewards) should be shown (true) or hidden (false). | No |
| vendorItemIndex | integer (int32) | The index into the DestinyVendorDefinition.itemList property. Note that this means Vendor data *is* Content Version dependent: make sure you have the latest content before you use Vendor data, or these indexes may mismatch. 
Most systems avoid this problem, but Vendors is one area where we are unable to reasonably avoid content dependency at the moment. | No |
| itemHash | integer (uint32) | The hash of the item being sold, as a quick shortcut for looking up the DestinyInventoryItemDefinition of the sale item. | No |
| overrideStyleItemHash | integer (uint32) | If populated, this is the hash of the item whose icon (and other secondary styles, but *not* the human readable strings) should override whatever icons/styles are on the item being sold.
If you don't do this, certain items whose styles are being overridden by socketed items - such as the "Recycle Shader" item - would show whatever their default icon/style is, and it wouldn't be pretty or look accurate. | No |
| quantity | integer (int32) | How much of the item you'll be getting. | No |
| costs | Array[Destiny.DestinyItemQuantity] | A summary of the current costs of the item. | No |
| overrideNextRefreshDate | string (date-time) | If this item has its own custom date where it may be removed from the Vendor's rotation, this is that date.
Note that there's not actually any guarantee that it will go away: it could be chosen again and end up still being in the Vendor's sale items! But this is the next date where that test will occur, and is also the date that the game shows for availability on things like Bounties being sold. So it's the best we can give. | No |
| apiPurchasable | boolean | If true, this item can be purchased through the Bungie.net API. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Entities.Vendors.DestinyVendorSaleItemComponent object
const example = {
  saleStatus: 123,
  requiredUnlocks: [],
  unlockStatuses: [],
  failureIndexes: [],
  augments: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Entities.Vendors.DestinyVendorSaleItemComponent object
example = {
    "saleStatus": 123,
    "requiredUnlocks": [],
    "unlockStatuses": [],
    "failureIndexes": [],
    "augments": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyUnlockDefinition**: Referenced in this entity
- **Destiny.DestinyItemQuantity**: Referenced in this entity
- **Destiny.DestinyUnlockStatus**: Referenced in this entity
- **Destiny.DestinyVendorItemState**: Referenced in this entity
- **Destiny.VendorItemStatus**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Entities.Vendors.DestinyVendorSaleItemComponent":   {
      "description": "Request this component if you want the details about an item being sold in relation to the character making the request: whether the character can buy it, whether they can afford it, and other data related to purchasing the item.\r\nNote that if you want instance, stats, etc... data for the item, you'll have to request additional components such as ItemInstances, ItemPerks etc... and acquire them from the DestinyVendorResponse's \"items\" property.",
      "type": "object",
      "properties": {
          "saleStatus": {
              "format": "int32",
              "description": "A flag indicating whether the requesting character can buy the item, and if not the reasons why the character can't buy it.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.VendorItemStatus"
              }
          },
          "requiredUnlocks": {
              "description": "If you can't buy the item due to a complex character state, these will be hashes for DestinyUnlockDefinitions that you can check to see messages regarding the failure (if the unlocks have human readable information: it is not guaranteed that Unlocks will have human readable strings, and your application will have to handle that)\r\nPrefer using failureIndexes instead. These are provided for informational purposes, but have largely been supplanted by failureIndexes.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyUnlockDefinition"
              }
          },
          "unlockStatuses": {
              "description": "If any complex unlock states are checked in determining purchasability, these will be returned here along with the status of the unlock check.\r\nPrefer using failureIndexes instead. These are provided for informational purposes, but have largely been supplanted by failureIndexes.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.DestinyUnlockStatus"
              }
          },
          "failureIndexes": {
              "description": "Indexes in to the \"failureStrings\" lookup table in DestinyVendorDefinition for the given Vendor. Gives some more reliable failure information for why you can't purchase an item.\r\nIt is preferred to use these over requiredUnlocks and unlockStatuses: the latter are provided mostly in case someone can do something interesting with it that I didn't anticipate.",
              "type": "array",
              "items": {
                  "format": "int32",
                  "type": "integer"
              }
          },
          "augments": {
              "format": "int32",
              "description": "A flags enumeration value representing the current state of any \"state modifiers\" on the item being sold. These are meant to correspond with some sort of visual indicator as to the augmentation: for instance, if an item is on sale or if you already own the item in question.\r\nDetermining how you want to represent these in your own app (or if you even want to) is an exercise left for the reader.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyVendorItemState"
              }
          },
          "itemValueVisibility": {
              "description": "If available, a list that describes which item values (rewards) should be shown (true) or hidden (false).",
              "type": "array",
              "items": {
                  "type": "boolean"
              }
          },
          "vendorItemIndex": {
              "format": "int32",
              "description": "The index into the DestinyVendorDefinition.itemList property. Note that this means Vendor data *is* Content Version dependent: make sure you have the latest content before you use Vendor data, or these indexes may mismatch. \r\nMost systems avoid this problem, but Vendors is one area where we are unable to reasonably avoid content dependency at the moment.",
              "type": "integer"
          },
          "itemHash": {
              "format": "uint32",
              "description": "The hash of the item being sold, as a quick shortcut for looking up the DestinyInventoryItemDefinition of the sale item.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "overrideStyleItemHash": {
              "format": "uint32",
              "description": "If populated, this is the hash of the item whose icon (and other secondary styles, but *not* the human readable strings) should override whatever icons/styles are on the item being sold.\r\nIf you don't do this, certain items whose styles are being overridden by socketed items - such as the \"Recycle Shader\" item - would show whatever their default icon/style is, and it wouldn't be pretty or look accurate.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "quantity": {
              "format": "int32",
              "description": "How much of the item you'll be getting.",
              "type": "integer"
          },
          "costs": {
              "description": "A summary of the current costs of the item.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.DestinyItemQuantity"
              }
          },
          "overrideNextRefreshDate": {
              "format": "date-time",
              "description": "If this item has its own custom date where it may be removed from the Vendor's rotation, this is that date.\r\nNote that there's not actually any guarantee that it will go away: it could be chosen again and end up still being in the Vendor's sale items! But this is the next date where that test will occur, and is also the date that the game shows for availability on things like Bounties being sold. So it's the best we can give.",
              "type": "string"
          },
          "apiPurchasable": {
              "description": "If true, this item can be purchased through the Bungie.net API.",
              "type": "boolean"
          }
      },
      "x-destiny-component-type-dependency": "VendorSales"
  }
}
```
