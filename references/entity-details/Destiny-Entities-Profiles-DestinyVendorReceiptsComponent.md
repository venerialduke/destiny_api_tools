# Destiny.Entities.Profiles.DestinyVendorReceiptsComponent

## Entity Information
- **Entity Name**: Destiny.Entities.Profiles.DestinyVendorReceiptsComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
For now, this isn't used for much: it's a record of the recent refundable purchases that the user has made. In the future, it could be used for providing refunds/buyback via the API. Wouldn't that be fun?

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| receipts | Array[Destiny.Vendors.DestinyVendorReceipt] | The receipts for refundable purchases made at a vendor. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Entities.Profiles.DestinyVendorReceiptsComponent object
const example = {
  receipts: [],
};
```

### Python
```python
# Example Destiny.Entities.Profiles.DestinyVendorReceiptsComponent object
example = {
    "receipts": [],
}
```

## Related Entities
- **Destiny.Vendors.DestinyVendorReceipt**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Entities.Profiles.DestinyVendorReceiptsComponent":   {
      "description": "For now, this isn't used for much: it's a record of the recent refundable purchases that the user has made. In the future, it could be used for providing refunds/buyback via the API. Wouldn't that be fun?",
      "type": "object",
      "properties": {
          "receipts": {
              "description": "The receipts for refundable purchases made at a vendor.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Vendors.DestinyVendorReceipt"
              }
          }
      },
      "x-destiny-component-type-dependency": "VendorReceipts"
  }
}
```
