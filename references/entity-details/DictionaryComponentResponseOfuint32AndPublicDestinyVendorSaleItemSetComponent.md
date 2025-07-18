# DictionaryComponentResponseOfuint32AndPublicDestinyVendorSaleItemSetComponent

## Entity Information
- **Entity Name**: DictionaryComponentResponseOfuint32AndPublicDestinyVendorSaleItemSetComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing dictionarycomponentresponseofuint32andpublicdestinyvendorsaleitemsetcomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| data | object |  | No |
| privacy | integer (int32) |  | No |
| disabled | boolean | If true, this component is disabled. | No |

## Usage Examples

### JavaScript
```javascript
// Example DictionaryComponentResponseOfuint32AndPublicDestinyVendorSaleItemSetComponent object
const example = {
  data: null,
  privacy: 123,
  disabled: true,
};
```

### Python
```python
# Example DictionaryComponentResponseOfuint32AndPublicDestinyVendorSaleItemSetComponent object
example = {
    "data": None,
    "privacy": 123,
    "disabled": True,
}
```

## Related Entities
- **Components.ComponentPrivacySetting**: Referenced in this entity
- **Destiny.Responses.PublicDestinyVendorSaleItemSetComponent**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "DictionaryComponentResponseOfuint32AndPublicDestinyVendorSaleItemSetComponent":   {
      "type": "object",
      "properties": {
          "data": {
              "type": "object",
              "additionalProperties": {
                  "x-destiny-component-type-dependency": "VendorSales",
                  "$ref": "#/definitions/Destiny.Responses.PublicDestinyVendorSaleItemSetComponent"
              }
          },
          "privacy": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Components.ComponentPrivacySetting"
              }
          },
          "disabled": {
              "description": "If true, this component is disabled.",
              "type": "boolean"
          }
      }
  }
}
```
