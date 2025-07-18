# Destiny.Responses.DestinyPublicVendorsResponse

## Entity Information
- **Entity Name**: Destiny.Responses.DestinyPublicVendorsResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
A response containing all valid components for the public Vendors endpoint.
 It is a decisively smaller subset of data compared to what we can get when we know the specific user making the request.
 If you want any of the other data - item details, whether or not you can buy it, etc... you'll have to call in the context of a character. I know, sad but true.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| vendorGroups | object | For Vendors being returned, this will give you the information you need to group them and order them in the same way that the Bungie Companion app performs grouping. It will automatically be returned if you request the Vendors component.
COMPONENT TYPE: Vendors | No |
| vendors | object | The base properties of the vendor. These are keyed by the Vendor Hash, so you will get one Vendor Component per vendor returned.
COMPONENT TYPE: Vendors | No |
| categories | object | Categories that the vendor has available, and references to the sales therein. These are keyed by the Vendor Hash, so you will get one Categories Component per vendor returned.
COMPONENT TYPE: VendorCategories | No |
| sales | object | Sales, keyed by the vendorItemIndex of the item being sold. These are keyed by the Vendor Hash, so you will get one Sale Item Set Component per vendor returned.
Note that within the Sale Item Set component, the sales are themselves keyed by the vendorSaleIndex, so you can relate it to the corrent sale item definition within the Vendor's definition.
COMPONENT TYPE: VendorSales | No |
| stringVariables | object | A set of string variable values by hash for a public vendors context.
COMPONENT TYPE: StringVariables | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Responses.DestinyPublicVendorsResponse object
const example = {
  vendorGroups: null,
  vendors: null,
  categories: null,
  sales: null,
  stringVariables: null,
};
```

### Python
```python
# Example Destiny.Responses.DestinyPublicVendorsResponse object
example = {
    "vendorGroups": None,
    "vendors": None,
    "categories": None,
    "sales": None,
    "stringVariables": None,
}
```

## Related Entities
- **DictionaryComponentResponseOfuint32AndDestinyPublicVendorComponent**: Referenced in this entity
- **DictionaryComponentResponseOfuint32AndDestinyVendorCategoriesComponent**: Referenced in this entity
- **DictionaryComponentResponseOfuint32AndPublicDestinyVendorSaleItemSetComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyStringVariablesComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyVendorGroupComponent**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Responses.DestinyPublicVendorsResponse":   {
      "description": "A response containing all valid components for the public Vendors endpoint.\r\n It is a decisively smaller subset of data compared to what we can get when we know the specific user making the request.\r\n If you want any of the other data - item details, whether or not you can buy it, etc... you'll have to call in the context of a character. I know, sad but true.",
      "type": "object",
      "properties": {
          "vendorGroups": {
              "description": "For Vendors being returned, this will give you the information you need to group them and order them in the same way that the Bungie Companion app performs grouping. It will automatically be returned if you request the Vendors component.\r\nCOMPONENT TYPE: Vendors",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyVendorGroupComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "Vendors"
          },
          "vendors": {
              "description": "The base properties of the vendor. These are keyed by the Vendor Hash, so you will get one Vendor Component per vendor returned.\r\nCOMPONENT TYPE: Vendors",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/DictionaryComponentResponseOfuint32AndDestinyPublicVendorComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "Vendors"
          },
          "categories": {
              "description": "Categories that the vendor has available, and references to the sales therein. These are keyed by the Vendor Hash, so you will get one Categories Component per vendor returned.\r\nCOMPONENT TYPE: VendorCategories",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/DictionaryComponentResponseOfuint32AndDestinyVendorCategoriesComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "VendorCategories"
          },
          "sales": {
              "description": "Sales, keyed by the vendorItemIndex of the item being sold. These are keyed by the Vendor Hash, so you will get one Sale Item Set Component per vendor returned.\r\nNote that within the Sale Item Set component, the sales are themselves keyed by the vendorSaleIndex, so you can relate it to the corrent sale item definition within the Vendor's definition.\r\nCOMPONENT TYPE: VendorSales",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/DictionaryComponentResponseOfuint32AndPublicDestinyVendorSaleItemSetComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "VendorSales"
          },
          "stringVariables": {
              "description": "A set of string variable values by hash for a public vendors context.\r\nCOMPONENT TYPE: StringVariables",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyStringVariablesComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "StringVariables"
          }
      }
  }
}
```
