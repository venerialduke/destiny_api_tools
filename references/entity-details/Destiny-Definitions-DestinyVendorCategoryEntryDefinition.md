# Destiny.Definitions.DestinyVendorCategoryEntryDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyVendorCategoryEntryDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
This is the definition for a single Vendor Category, into which Sale Items are grouped.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| categoryIndex | integer (int32) | The index of the category in the original category definitions for the vendor. | No |
| sortValue | integer (int32) | Used in sorting items in vendors... but there's a lot more to it. Just go with the order provided in the itemIndexes property on the DestinyVendorCategoryComponent instead, it should be more reliable than trying to recalculate it yourself. | No |
| categoryHash | integer (uint32) | The hashed identifier for the category. | No |
| quantityAvailable | integer (int32) | The amount of items that will be available when this category is shown. | No |
| showUnavailableItems | boolean | If items aren't up for sale in this category, should we still show them (greyed out)? | No |
| hideIfNoCurrency | boolean | If you don't have the currency required to buy items from this category, should the items be hidden? | No |
| hideFromRegularPurchase | boolean | True if this category doesn't allow purchases. | No |
| buyStringOverride | string | The localized string for making purchases from this category, if it is different from the vendor's string for purchasing. | No |
| disabledDescription | string | If the category is disabled, this is the localized description to show. | No |
| displayTitle | string | The localized title of the category. | No |
| overlay | object | If this category has an overlay prompt that should appear, this contains the details of that prompt. | No |
| vendorItemIndexes | Array[integer] | A shortcut for the vendor item indexes sold under this category. Saves us from some expensive reorganization at runtime. | No |
| isPreview | boolean | Sometimes a category isn't actually used to sell items, but rather to preview them. This implies different UI (and manual placement of the category in the UI) in the game, and special treatment. | No |
| isDisplayOnly | boolean | If true, this category only displays items: you can't purchase anything in them. | No |
| resetIntervalMinutesOverride | integer (int32) |  | No |
| resetOffsetMinutesOverride | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyVendorCategoryEntryDefinition object
const example = {
  categoryIndex: 123,
  sortValue: 123,
  categoryHash: 123,
  quantityAvailable: 123,
  showUnavailableItems: true,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyVendorCategoryEntryDefinition object
example = {
    "categoryIndex": 123,
    "sortValue": 123,
    "categoryHash": 123,
    "quantityAvailable": 123,
    "showUnavailableItems": True,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyVendorCategoryOverlayDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyVendorCategoryEntryDefinition":   {
      "description": "This is the definition for a single Vendor Category, into which Sale Items are grouped.",
      "type": "object",
      "properties": {
          "categoryIndex": {
              "format": "int32",
              "description": "The index of the category in the original category definitions for the vendor.",
              "type": "integer"
          },
          "sortValue": {
              "format": "int32",
              "description": "Used in sorting items in vendors... but there's a lot more to it. Just go with the order provided in the itemIndexes property on the DestinyVendorCategoryComponent instead, it should be more reliable than trying to recalculate it yourself.",
              "type": "integer"
          },
          "categoryHash": {
              "format": "uint32",
              "description": "The hashed identifier for the category.",
              "type": "integer"
          },
          "quantityAvailable": {
              "format": "int32",
              "description": "The amount of items that will be available when this category is shown.",
              "type": "integer"
          },
          "showUnavailableItems": {
              "description": "If items aren't up for sale in this category, should we still show them (greyed out)?",
              "type": "boolean"
          },
          "hideIfNoCurrency": {
              "description": "If you don't have the currency required to buy items from this category, should the items be hidden?",
              "type": "boolean"
          },
          "hideFromRegularPurchase": {
              "description": "True if this category doesn't allow purchases.",
              "type": "boolean"
          },
          "buyStringOverride": {
              "description": "The localized string for making purchases from this category, if it is different from the vendor's string for purchasing.",
              "type": "string"
          },
          "disabledDescription": {
              "description": "If the category is disabled, this is the localized description to show.",
              "type": "string"
          },
          "displayTitle": {
              "description": "The localized title of the category.",
              "type": "string"
          },
          "overlay": {
              "description": "If this category has an overlay prompt that should appear, this contains the details of that prompt.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.DestinyVendorCategoryOverlayDefinition"
                  }
              ]
          },
          "vendorItemIndexes": {
              "description": "A shortcut for the vendor item indexes sold under this category. Saves us from some expensive reorganization at runtime.",
              "type": "array",
              "items": {
                  "format": "int32",
                  "type": "integer"
              }
          },
          "isPreview": {
              "description": "Sometimes a category isn't actually used to sell items, but rather to preview them. This implies different UI (and manual placement of the category in the UI) in the game, and special treatment.",
              "type": "boolean"
          },
          "isDisplayOnly": {
              "description": "If true, this category only displays items: you can't purchase anything in them.",
              "type": "boolean"
          },
          "resetIntervalMinutesOverride": {
              "format": "int32",
              "type": "integer"
          },
          "resetOffsetMinutesOverride": {
              "format": "int32",
              "type": "integer"
          }
      }
  }
}
```
