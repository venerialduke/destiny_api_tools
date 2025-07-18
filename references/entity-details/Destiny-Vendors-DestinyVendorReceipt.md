# Destiny.Vendors.DestinyVendorReceipt

## Entity Information
- **Entity Name**: Destiny.Vendors.DestinyVendorReceipt
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
If a character purchased an item that is refundable, a Vendor Receipt will be created on the user's Destiny Profile. These expire after a configurable period of time, but until then can be used to get refunds on items. BNet does not provide the ability to refund a purchase *yet*, but you know.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| currencyPaid | Array[Destiny.DestinyItemQuantity] | The amount paid for the item, in terms of items that were consumed in the purchase and their quantity. | No |
| itemReceived | object | The item that was received, and its quantity. | No |
| licenseUnlockHash | integer (uint32) | The unlock flag used to determine whether you still have the purchased item. | No |
| purchasedByCharacterId | integer (int64) | The ID of the character who made the purchase. | No |
| refundPolicy | integer (int32) | Whether you can get a refund, and what happens in order for the refund to be received. See the DestinyVendorItemRefundPolicy enum for details. | No |
| sequenceNumber | integer (int32) | The identifier of this receipt. | No |
| timeToExpiration | integer (int64) | The seconds since epoch at which this receipt is rendered invalid. | No |
| expiresOn | string (date-time) | The date at which this receipt is rendered invalid. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Vendors.DestinyVendorReceipt object
const example = {
  currencyPaid: [],
  itemReceived: null,
  licenseUnlockHash: 123,
  purchasedByCharacterId: 123,
  refundPolicy: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Vendors.DestinyVendorReceipt object
example = {
    "currencyPaid": [],
    "itemReceived": None,
    "licenseUnlockHash": 123,
    "purchasedByCharacterId": 123,
    "refundPolicy": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.DestinyItemQuantity**: Referenced in this entity
- **Destiny.DestinyVendorItemRefundPolicy**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Vendors.DestinyVendorReceipt":   {
      "description": "If a character purchased an item that is refundable, a Vendor Receipt will be created on the user's Destiny Profile. These expire after a configurable period of time, but until then can be used to get refunds on items. BNet does not provide the ability to refund a purchase *yet*, but you know.",
      "type": "object",
      "properties": {
          "currencyPaid": {
              "description": "The amount paid for the item, in terms of items that were consumed in the purchase and their quantity.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.DestinyItemQuantity"
              }
          },
          "itemReceived": {
              "description": "The item that was received, and its quantity.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.DestinyItemQuantity"
                  }
              ]
          },
          "licenseUnlockHash": {
              "format": "uint32",
              "description": "The unlock flag used to determine whether you still have the purchased item.",
              "type": "integer"
          },
          "purchasedByCharacterId": {
              "format": "int64",
              "description": "The ID of the character who made the purchase.",
              "type": "integer"
          },
          "refundPolicy": {
              "format": "int32",
              "description": "Whether you can get a refund, and what happens in order for the refund to be received. See the DestinyVendorItemRefundPolicy enum for details.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyVendorItemRefundPolicy"
              }
          },
          "sequenceNumber": {
              "format": "int32",
              "description": "The identifier of this receipt.",
              "type": "integer"
          },
          "timeToExpiration": {
              "format": "int64",
              "description": "The seconds since epoch at which this receipt is rendered invalid.",
              "type": "integer"
          },
          "expiresOn": {
              "format": "date-time",
              "description": "The date at which this receipt is rendered invalid.",
              "type": "string"
          }
      }
  }
}
```
