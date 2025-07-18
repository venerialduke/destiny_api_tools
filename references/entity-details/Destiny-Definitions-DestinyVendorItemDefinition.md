# Destiny.Definitions.DestinyVendorItemDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyVendorItemDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
This represents an item being sold by the vendor.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| vendorItemIndex | integer (int32) | The index into the DestinyVendorDefinition.saleList. This is what we use to refer to items being sold throughout live and definition data. | No |
| itemHash | integer (uint32) | The hash identifier of the item being sold (DestinyInventoryItemDefinition).
Note that a vendor can sell the same item in multiple ways, so don't assume that itemHash is a unique identifier for this entity. | No |
| quantity | integer (int32) | The amount you will recieve of the item described in itemHash if you make the purchase. | No |
| failureIndexes | Array[integer] | An list of indexes into the DestinyVendorDefinition.failureStrings array, indicating the possible failure strings that can be relevant for this item. | No |
| currencies | Array[Destiny.Definitions.DestinyVendorItemQuantity] | This is a pre-compiled aggregation of item value and priceOverrideList, so that we have one place to check for what the purchaser must pay for the item. Use this instead of trying to piece together the price separately.
The somewhat crappy part about this is that, now that item quantity overrides have dynamic modifiers, this will not necessarily be statically true. If you were using this instead of live data, switch to using live data. | No |
| refundPolicy | integer (int32) | If this item can be refunded, this is the policy for what will be refundd, how, and in what time period. | No |
| refundTimeLimit | integer (int32) | The amount of time before refundability of the newly purchased item will expire. | No |
| creationLevels | Array[Destiny.Definitions.DestinyItemCreationEntryLevelDefinition] | The Default level at which the item will spawn. Almost always driven by an adjusto these days. Ideally should be singular. It's a long story how this ended up as a list, but there is always either going to be 0:1 of these entities. | No |
| displayCategoryIndex | integer (int32) | This is an index specifically into the display category, as opposed to the server-side Categories (which do not need to match or pair with each other in any way: server side categories are really just structures for common validation. Display Category will let us more easily categorize items visually) | No |
| categoryIndex | integer (int32) | The index into the DestinyVendorDefinition.categories array, so you can find the category associated with this item. | No |
| originalCategoryIndex | integer (int32) | Same as above, but for the original category indexes. | No |
| minimumLevel | integer (int32) | The minimum character level at which this item is available for sale. | No |
| maximumLevel | integer (int32) | The maximum character level at which this item is available for sale. | No |
| action | object | The action to be performed when purchasing the item, if it's not just "buy". | No |
| displayCategory | string | The string identifier for the category selling this item. | No |
| inventoryBucketHash | integer (uint32) | The inventory bucket into which this item will be placed upon purchase. | No |
| visibilityScope | integer (int32) | The most restrictive scope that determines whether the item is available in the Vendor's inventory. See DestinyGatingScope's documentation for more information.
This can be determined by Unlock gating, or by whether or not the item has purchase level requirements (minimumLevel and maximumLevel properties). | No |
| purchasableScope | integer (int32) | Similar to visibilityScope, it represents the most restrictive scope that determines whether the item can be purchased. It will at least be as restrictive as visibilityScope, but could be more restrictive if the item has additional purchase requirements beyond whether it is merely visible or not.
See DestinyGatingScope's documentation for more information. | No |
| exclusivity | integer (int32) | If this item can only be purchased by a given platform, this indicates the platform to which it is restricted. | No |
| isOffer | boolean | If this sale can only be performed as the result of an offer check, this is true. | No |
| isCrm | boolean | If this sale can only be performed as the result of receiving a CRM offer, this is true. | No |
| sortValue | integer (int32) | *if* the category this item is in supports non-default sorting, this value should represent the sorting value to use, pre-processed and ready to go. | No |
| expirationTooltip | string | If this item can expire, this is the tooltip message to show with its expiration info. | No |
| redirectToSaleIndexes | Array[integer] | If this is populated, the purchase of this item should redirect to purchasing these other items instead. | No |
| socketOverrides | Array[Destiny.Definitions.DestinyVendorItemSocketOverride] |  | No |
| unpurchasable | boolean | If true, this item is some sort of dummy sale item that cannot actually be purchased. It may be a display only item, or some fluff left by a content designer for testing purposes, or something that got disabled because it was a terrible idea. You get the picture. We won't know *why* it can't be purchased, only that it can't be. Sorry.
This is also only whether it's unpurchasable as a static property according to game content. There are other reasons why an item may or may not be purchasable at runtime, so even if this isn't set to True you should trust the runtime value for this sale item over the static definition if this is unset. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyVendorItemDefinition object
const example = {
  vendorItemIndex: 123,
  itemHash: 123,
  quantity: 123,
  failureIndexes: [],
  currencies: [],
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyVendorItemDefinition object
example = {
    "vendorItemIndex": 123,
    "itemHash": 123,
    "quantity": 123,
    "failureIndexes": [],
    "currencies": [],
    # ... more properties
}
```

## Related Entities
- **BungieMembershipType**: Referenced in this entity
- **Destiny.Definitions.DestinyInventoryBucketDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyItemCreationEntryLevelDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyVendorItemQuantity**: Referenced in this entity
- **Destiny.Definitions.DestinyVendorItemSocketOverride**: Referenced in this entity
- **Destiny.Definitions.DestinyVendorSaleItemActionBlockDefinition**: Referenced in this entity
- **Destiny.DestinyGatingScope**: Referenced in this entity
- **Destiny.DestinyVendorItemRefundPolicy**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyVendorItemDefinition":   {
      "description": "This represents an item being sold by the vendor.",
      "type": "object",
      "properties": {
          "vendorItemIndex": {
              "format": "int32",
              "description": "The index into the DestinyVendorDefinition.saleList. This is what we use to refer to items being sold throughout live and definition data.",
              "type": "integer"
          },
          "itemHash": {
              "format": "uint32",
              "description": "The hash identifier of the item being sold (DestinyInventoryItemDefinition).\r\nNote that a vendor can sell the same item in multiple ways, so don't assume that itemHash is a unique identifier for this entity.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "quantity": {
              "format": "int32",
              "description": "The amount you will recieve of the item described in itemHash if you make the purchase.",
              "type": "integer"
          },
          "failureIndexes": {
              "description": "An list of indexes into the DestinyVendorDefinition.failureStrings array, indicating the possible failure strings that can be relevant for this item.",
              "type": "array",
              "items": {
                  "format": "int32",
                  "type": "integer"
              }
          },
          "currencies": {
              "description": "This is a pre-compiled aggregation of item value and priceOverrideList, so that we have one place to check for what the purchaser must pay for the item. Use this instead of trying to piece together the price separately.\r\nThe somewhat crappy part about this is that, now that item quantity overrides have dynamic modifiers, this will not necessarily be statically true. If you were using this instead of live data, switch to using live data.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorItemQuantity"
              }
          },
          "refundPolicy": {
              "format": "int32",
              "description": "If this item can be refunded, this is the policy for what will be refundd, how, and in what time period.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyVendorItemRefundPolicy"
              }
          },
          "refundTimeLimit": {
              "format": "int32",
              "description": "The amount of time before refundability of the newly purchased item will expire.",
              "type": "integer"
          },
          "creationLevels": {
              "description": "The Default level at which the item will spawn. Almost always driven by an adjusto these days. Ideally should be singular. It's a long story how this ended up as a list, but there is always either going to be 0:1 of these entities.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyItemCreationEntryLevelDefinition"
              }
          },
          "displayCategoryIndex": {
              "format": "int32",
              "description": "This is an index specifically into the display category, as opposed to the server-side Categories (which do not need to match or pair with each other in any way: server side categories are really just structures for common validation. Display Category will let us more easily categorize items visually)",
              "type": "integer"
          },
          "categoryIndex": {
              "format": "int32",
              "description": "The index into the DestinyVendorDefinition.categories array, so you can find the category associated with this item.",
              "type": "integer"
          },
          "originalCategoryIndex": {
              "format": "int32",
              "description": "Same as above, but for the original category indexes.",
              "type": "integer"
          },
          "minimumLevel": {
              "format": "int32",
              "description": "The minimum character level at which this item is available for sale.",
              "type": "integer"
          },
          "maximumLevel": {
              "format": "int32",
              "description": "The maximum character level at which this item is available for sale.",
              "type": "integer"
          },
          "action": {
              "description": "The action to be performed when purchasing the item, if it's not just \"buy\".",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.DestinyVendorSaleItemActionBlockDefinition"
                  }
              ]
          },
          "displayCategory": {
              "description": "The string identifier for the category selling this item.",
              "type": "string"
          },
          "inventoryBucketHash": {
              "format": "uint32",
              "description": "The inventory bucket into which this item will be placed upon purchase.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryBucketDefinition"
              }
          },
          "visibilityScope": {
              "format": "int32",
              "description": "The most restrictive scope that determines whether the item is available in the Vendor's inventory. See DestinyGatingScope's documentation for more information.\r\nThis can be determined by Unlock gating, or by whether or not the item has purchase level requirements (minimumLevel and maximumLevel properties).",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyGatingScope"
              }
          },
          "purchasableScope": {
              "format": "int32",
              "description": "Similar to visibilityScope, it represents the most restrictive scope that determines whether the item can be purchased. It will at least be as restrictive as visibilityScope, but could be more restrictive if the item has additional purchase requirements beyond whether it is merely visible or not.\r\nSee DestinyGatingScope's documentation for more information.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyGatingScope"
              }
          },
          "exclusivity": {
              "format": "int32",
              "description": "If this item can only be purchased by a given platform, this indicates the platform to which it is restricted.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/BungieMembershipType"
              }
          },
          "isOffer": {
              "description": "If this sale can only be performed as the result of an offer check, this is true.",
              "type": "boolean"
          },
          "isCrm": {
              "description": "If this sale can only be performed as the result of receiving a CRM offer, this is true.",
              "type": "boolean"
          },
          "sortValue": {
              "format": "int32",
              "description": "*if* the category this item is in supports non-default sorting, this value should represent the sorting value to use, pre-processed and ready to go.",
              "type": "integer"
          },
          "expirationTooltip": {
              "description": "If this item can expire, this is the tooltip message to show with its expiration info.",
              "type": "string"
          },
          "redirectToSaleIndexes": {
              "description": "If this is populated, the purchase of this item should redirect to purchasing these other items instead.",
              "type": "array",
              "items": {
                  "format": "int32",
                  "type": "integer"
              }
          },
          "socketOverrides": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorItemSocketOverride"
              }
          },
          "unpurchasable": {
              "description": "If true, this item is some sort of dummy sale item that cannot actually be purchased. It may be a display only item, or some fluff left by a content designer for testing purposes, or something that got disabled because it was a terrible idea. You get the picture. We won't know *why* it can't be purchased, only that it can't be. Sorry.\r\nThis is also only whether it's unpurchasable as a static property according to game content. There are other reasons why an item may or may not be purchasable at runtime, so even if this isn't set to True you should trust the runtime value for this sale item over the static definition if this is unset.",
              "type": "boolean"
          }
      }
  }
}
```
