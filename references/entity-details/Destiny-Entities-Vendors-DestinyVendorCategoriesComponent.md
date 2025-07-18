# Destiny.Entities.Vendors.DestinyVendorCategoriesComponent

## Entity Information
- **Entity Name**: Destiny.Entities.Vendors.DestinyVendorCategoriesComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
A vendor can have many categories of items that they sell. This component will return the category information for available items, as well as the index into those items in the user's sale item list.
Note that, since both the category and items are indexes, this data is Content Version dependent. Be sure to check that your content is up to date before using this data. This is an unfortunate, but permanent, limitation of Vendor data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| categories | Array[Destiny.Entities.Vendors.DestinyVendorCategory] | The list of categories for items that the vendor sells, in rendering order.
These categories each point to a "display category" in the displayCategories property of the DestinyVendorDefinition, as opposed to the other categories. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Entities.Vendors.DestinyVendorCategoriesComponent object
const example = {
  categories: [],
};
```

### Python
```python
# Example Destiny.Entities.Vendors.DestinyVendorCategoriesComponent object
example = {
    "categories": [],
}
```

## Related Entities
- **Destiny.Entities.Vendors.DestinyVendorCategory**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Entities.Vendors.DestinyVendorCategoriesComponent":   {
      "description": "A vendor can have many categories of items that they sell. This component will return the category information for available items, as well as the index into those items in the user's sale item list.\r\nNote that, since both the category and items are indexes, this data is Content Version dependent. Be sure to check that your content is up to date before using this data. This is an unfortunate, but permanent, limitation of Vendor data.",
      "type": "object",
      "properties": {
          "categories": {
              "description": "The list of categories for items that the vendor sells, in rendering order.\r\nThese categories each point to a \"display category\" in the displayCategories property of the DestinyVendorDefinition, as opposed to the other categories.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Entities.Vendors.DestinyVendorCategory"
              }
          }
      },
      "x-destiny-component-type-dependency": "VendorCategories"
  }
}
```
