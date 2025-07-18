# Destiny.Responses.DestinyVendorsResponse

## Entity Information
- **Entity Name**: Destiny.Responses.DestinyVendorsResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
A response containing all of the components for all requested vendors.

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
Note that within the Sale Item Set component, the sales are themselves keyed by the vendorSaleIndex, so you can relate it to the current sale item definition within the Vendor's definition.
COMPONENT TYPE: VendorSales | No |
| itemComponents | object | The set of item detail components, one set of item components per Vendor. These are keyed by the Vendor Hash, so you will get one Item Component Set per vendor returned.
The components contained inside are themselves keyed by the vendorSaleIndex, and will have whatever item-level components you requested (Sockets, Stats, Instance data etc...) per item being sold by the vendor. | No |
| currencyLookups | object | A "lookup" convenience component that can be used to quickly check if the character has access to items that can be used for purchasing.
COMPONENT TYPE: CurrencyLookups | No |
| stringVariables | object | A map of string variable values by hash for this character context.
COMPONENT TYPE: StringVariables | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Responses.DestinyVendorsResponse object
const example = {
  vendorGroups: null,
  vendors: null,
  categories: null,
  sales: null,
  itemComponents: null,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Responses.DestinyVendorsResponse object
example = {
    "vendorGroups": None,
    "vendors": None,
    "categories": None,
    "sales": None,
    "itemComponents": None,
    # ... more properties
}
```

## Related Entities
- **DestinyVendorItemComponentSetOfint32**: Referenced in this entity
- **DictionaryComponentResponseOfuint32AndDestinyVendorCategoriesComponent**: Referenced in this entity
- **DictionaryComponentResponseOfuint32AndDestinyVendorComponent**: Referenced in this entity
- **DictionaryComponentResponseOfuint32AndPersonalDestinyVendorSaleItemSetComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyCurrenciesComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyStringVariablesComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyVendorGroupComponent**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Responses.DestinyVendorsResponse":   {
      "description": "A response containing all of the components for all requested vendors.",
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
                      "$ref": "#/definitions/DictionaryComponentResponseOfuint32AndDestinyVendorComponent"
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
              "description": "Sales, keyed by the vendorItemIndex of the item being sold. These are keyed by the Vendor Hash, so you will get one Sale Item Set Component per vendor returned.\r\nNote that within the Sale Item Set component, the sales are themselves keyed by the vendorSaleIndex, so you can relate it to the current sale item definition within the Vendor's definition.\r\nCOMPONENT TYPE: VendorSales",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/DictionaryComponentResponseOfuint32AndPersonalDestinyVendorSaleItemSetComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "VendorSales"
          },
          "itemComponents": {
              "description": "The set of item detail components, one set of item components per Vendor. These are keyed by the Vendor Hash, so you will get one Item Component Set per vendor returned.\r\nThe components contained inside are themselves keyed by the vendorSaleIndex, and will have whatever item-level components you requested (Sockets, Stats, Instance data etc...) per item being sold by the vendor.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/DestinyVendorItemComponentSetOfint32"
              }
          },
          "currencyLookups": {
              "description": "A \"lookup\" convenience component that can be used to quickly check if the character has access to items that can be used for purchasing.\r\nCOMPONENT TYPE: CurrencyLookups",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyCurrenciesComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "CurrencyLookups"
          },
          "stringVariables": {
              "description": "A map of string variable values by hash for this character context.\r\nCOMPONENT TYPE: StringVariables",
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
