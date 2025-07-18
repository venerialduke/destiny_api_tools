# Destiny.Responses.PublicDestinyVendorSaleItemSetComponent

## Entity Information
- **Entity Name**: Destiny.Responses.PublicDestinyVendorSaleItemSetComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing publicdestinyvendorsaleitemsetcomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| saleItems | object |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Responses.PublicDestinyVendorSaleItemSetComponent object
const example = {
  saleItems: null,
};
```

### Python
```python
# Example Destiny.Responses.PublicDestinyVendorSaleItemSetComponent object
example = {
    "saleItems": None,
}
```

## Related Entities
- **Destiny.Components.Vendors.DestinyPublicVendorSaleItemComponent**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Responses.PublicDestinyVendorSaleItemSetComponent":   {
      "type": "object",
      "properties": {
          "saleItems": {
              "type": "object",
              "additionalProperties": {
                  "x-destiny-component-type-dependency": "VendorSales",
                  "$ref": "#/definitions/Destiny.Components.Vendors.DestinyPublicVendorSaleItemComponent"
              }
          }
      },
      "x-destiny-component-type-dependency": "VendorSales"
  }
}
```
