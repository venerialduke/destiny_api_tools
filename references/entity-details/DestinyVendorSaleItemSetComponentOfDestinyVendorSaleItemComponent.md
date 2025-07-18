# DestinyVendorSaleItemSetComponentOfDestinyVendorSaleItemComponent

## Entity Information
- **Entity Name**: DestinyVendorSaleItemSetComponentOfDestinyVendorSaleItemComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyvendorsaleitemsetcomponentofdestinyvendorsaleitemcomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| saleItems | object |  | No |

## Usage Examples

### JavaScript
```javascript
// Example DestinyVendorSaleItemSetComponentOfDestinyVendorSaleItemComponent object
const example = {
  saleItems: null,
};
```

### Python
```python
# Example DestinyVendorSaleItemSetComponentOfDestinyVendorSaleItemComponent object
example = {
    "saleItems": None,
}
```

## Related Entities
- **Destiny.Entities.Vendors.DestinyVendorSaleItemComponent**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "DestinyVendorSaleItemSetComponentOfDestinyVendorSaleItemComponent":   {
      "type": "object",
      "properties": {
          "saleItems": {
              "type": "object",
              "additionalProperties": {
                  "x-destiny-component-type-dependency": "VendorSales",
                  "$ref": "#/definitions/Destiny.Entities.Vendors.DestinyVendorSaleItemComponent"
              }
          }
      },
      "x-destiny-component-type-dependency": "VendorSales"
  }
}
```
