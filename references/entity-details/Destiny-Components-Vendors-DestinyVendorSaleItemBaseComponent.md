# Destiny.Components.Vendors.DestinyVendorSaleItemBaseComponent

## Entity Information
- **Entity Name**: Destiny.Components.Vendors.DestinyVendorSaleItemBaseComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The base class for Vendor Sale Item data. Has a bunch of character-agnostic state about the item being sold.
Note that if you want instance, stats, etc... data for the item, you'll have to request additional components such as ItemInstances, ItemPerks etc... and acquire them from the DestinyVendorResponse's "items" property.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
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
// Example Destiny.Components.Vendors.DestinyVendorSaleItemBaseComponent object
const example = {
  vendorItemIndex: 123,
  itemHash: 123,
  overrideStyleItemHash: 123,
  quantity: 123,
  costs: [],
  // ... more properties
};
```

### Python
```python
# Example Destiny.Components.Vendors.DestinyVendorSaleItemBaseComponent object
example = {
    "vendorItemIndex": 123,
    "itemHash": 123,
    "overrideStyleItemHash": 123,
    "quantity": 123,
    "costs": [],
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.DestinyItemQuantity**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Vendors.DestinyVendorSaleItemBaseComponent":   {
      "description": "The base class for Vendor Sale Item data. Has a bunch of character-agnostic state about the item being sold.\r\nNote that if you want instance, stats, etc... data for the item, you'll have to request additional components such as ItemInstances, ItemPerks etc... and acquire them from the DestinyVendorResponse's \"items\" property.",
      "type": "object",
      "properties": {
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
