# Destiny.Definitions.Items.DestinyDerivedItemCategoryDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Items.DestinyDerivedItemCategoryDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
A shortcut for the fact that some items have a "Preview Vendor" - See DestinyInventoryItemDefinition.preview.previewVendorHash - that is intended to be used to show what items you can get as a result of acquiring or using this item.
A common example of this in Destiny 1 was Eververse "Boxes," which could have many possible items. This "Preview Vendor" is not a vendor you can actually see in the game, but it defines categories and sale items for all of the possible items you could get from the Box so that the game can show them to you. We summarize that info here so that you don't have to do that Vendor lookup and aggregation manually.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| categoryDescription | string | The localized string for the category title. This will be something describing the items you can get as a group, or your likelihood/the quantity you'll get. | No |
| items | Array[Destiny.Definitions.Items.DestinyDerivedItemDefinition] | This is the list of all of the items for this category and the basic properties we'll know about them. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Items.DestinyDerivedItemCategoryDefinition object
const example = {
  categoryDescription: "example value",
  items: [],
};
```

### Python
```python
# Example Destiny.Definitions.Items.DestinyDerivedItemCategoryDefinition object
example = {
    "categoryDescription": "example value",
    "items": [],
}
```

## Related Entities
- **Destiny.Definitions.Items.DestinyDerivedItemDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Items.DestinyDerivedItemCategoryDefinition":   {
      "description": "A shortcut for the fact that some items have a \"Preview Vendor\" - See DestinyInventoryItemDefinition.preview.previewVendorHash - that is intended to be used to show what items you can get as a result of acquiring or using this item.\r\nA common example of this in Destiny 1 was Eververse \"Boxes,\" which could have many possible items. This \"Preview Vendor\" is not a vendor you can actually see in the game, but it defines categories and sale items for all of the possible items you could get from the Box so that the game can show them to you. We summarize that info here so that you don't have to do that Vendor lookup and aggregation manually.",
      "type": "object",
      "properties": {
          "categoryDescription": {
              "description": "The localized string for the category title. This will be something describing the items you can get as a group, or your likelihood/the quantity you'll get.",
              "type": "string"
          },
          "items": {
              "description": "This is the list of all of the items for this category and the basic properties we'll know about them.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Items.DestinyDerivedItemDefinition"
              }
          }
      }
  }
}
```
