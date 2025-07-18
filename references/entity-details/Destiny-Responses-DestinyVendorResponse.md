# Destiny.Responses.DestinyVendorResponse

## Entity Information
- **Entity Name**: Destiny.Responses.DestinyVendorResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
A response containing all of the components for a vendor.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| vendor | object | The base properties of the vendor.
COMPONENT TYPE: Vendors | No |
| categories | object | Categories that the vendor has available, and references to the sales therein.
COMPONENT TYPE: VendorCategories | No |
| sales | object | Sales, keyed by the vendorItemIndex of the item being sold.
COMPONENT TYPE: VendorSales | No |
| itemComponents | object | Item components, keyed by the vendorItemIndex of the active sale items.
COMPONENT TYPE: [See inside the DestinyVendorItemComponentSet contract for component types.] | No |
| currencyLookups | object | A "lookup" convenience component that can be used to quickly check if the character has access to items that can be used for purchasing.
COMPONENT TYPE: CurrencyLookups | No |
| stringVariables | object | A map of string variable values by hash for this character context.
COMPONENT TYPE: StringVariables | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Responses.DestinyVendorResponse object
const example = {
  vendor: null,
  categories: null,
  sales: null,
  itemComponents: null,
  currencyLookups: null,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Responses.DestinyVendorResponse object
example = {
    "vendor": None,
    "categories": None,
    "sales": None,
    "itemComponents": None,
    "currencyLookups": None,
    # ... more properties
}
```

## Related Entities
- **DestinyVendorItemComponentSetOfint32**: Referenced in this entity
- **DictionaryComponentResponseOfint32AndDestinyVendorSaleItemComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyCurrenciesComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyStringVariablesComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyVendorCategoriesComponent**: Referenced in this entity
- **SingleComponentResponseOfDestinyVendorComponent**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Responses.DestinyVendorResponse":   {
      "description": "A response containing all of the components for a vendor.",
      "type": "object",
      "properties": {
          "vendor": {
              "description": "The base properties of the vendor.\r\nCOMPONENT TYPE: Vendors",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyVendorComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "Vendors"
          },
          "categories": {
              "description": "Categories that the vendor has available, and references to the sales therein.\r\nCOMPONENT TYPE: VendorCategories",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/SingleComponentResponseOfDestinyVendorCategoriesComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "VendorCategories"
          },
          "sales": {
              "description": "Sales, keyed by the vendorItemIndex of the item being sold.\r\nCOMPONENT TYPE: VendorSales",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/DictionaryComponentResponseOfint32AndDestinyVendorSaleItemComponent"
                  }
              ],
              "x-destiny-component-type-dependency": "VendorSales"
          },
          "itemComponents": {
              "description": "Item components, keyed by the vendorItemIndex of the active sale items.\r\nCOMPONENT TYPE: [See inside the DestinyVendorItemComponentSet contract for component types.]",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/DestinyVendorItemComponentSetOfint32"
                  }
              ]
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
