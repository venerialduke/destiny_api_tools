# Destiny.Entities.Vendors.DestinyVendorCategory

## Entity Information
- **Entity Name**: Destiny.Entities.Vendors.DestinyVendorCategory
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Information about the category and items currently sold in that category.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayCategoryIndex | integer (int32) | An index into the DestinyVendorDefinition.displayCategories property, so you can grab the display data for this category. | No |
| itemIndexes | Array[integer] | An ordered list of indexes into items being sold in this category (DestinyVendorDefinition.itemList) which will contain more information about the items being sold themselves. Can also be used to index into DestinyVendorSaleItemComponent data, if you asked for that data to be returned. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Entities.Vendors.DestinyVendorCategory object
const example = {
  displayCategoryIndex: 123,
  itemIndexes: [],
};
```

### Python
```python
# Example Destiny.Entities.Vendors.DestinyVendorCategory object
example = {
    "displayCategoryIndex": 123,
    "itemIndexes": [],
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Entities.Vendors.DestinyVendorCategory":   {
      "description": "Information about the category and items currently sold in that category.",
      "type": "object",
      "properties": {
          "displayCategoryIndex": {
              "format": "int32",
              "description": "An index into the DestinyVendorDefinition.displayCategories property, so you can grab the display data for this category.",
              "type": "integer"
          },
          "itemIndexes": {
              "description": "An ordered list of indexes into items being sold in this category (DestinyVendorDefinition.itemList) which will contain more information about the items being sold themselves. Can also be used to index into DestinyVendorSaleItemComponent data, if you asked for that data to be returned.",
              "type": "array",
              "items": {
                  "format": "int32",
                  "type": "integer"
              }
          }
      }
  }
}
```
