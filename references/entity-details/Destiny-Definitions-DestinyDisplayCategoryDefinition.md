# Destiny.Definitions.DestinyDisplayCategoryDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyDisplayCategoryDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Display Categories are different from "categories" in that these are specifically for visual grouping and display of categories in Vendor UI. The "categories" structure is for validation of the contained items, and can be categorized entirely separately from "Display Categories", there need be and often will be no meaningful relationship between the two.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| index | integer (int32) |  | No |
| identifier | string | A string identifier for the display category. | No |
| displayCategoryHash | integer (uint32) |  | No |
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| displayInBanner | boolean | If true, this category should be displayed in the "Banner" section of the vendor's UI. | No |
| progressionHash | integer (uint32) | If it exists, this is the hash identifier of a DestinyProgressionDefinition that represents the progression to show on this display category.
Specific categories can now have thier own distinct progression, apparently. So that's cool. | No |
| sortOrder | integer (int32) | If this category sorts items in a nonstandard way, this will be the way we sort. | No |
| displayStyleHash | integer (uint32) | An indicator of how the category will be displayed in the UI. It's up to you to do something cool or interesting in response to this, or just to treat it as a normal category. | No |
| displayStyleIdentifier | string | An indicator of how the category will be displayed in the UI. It's up to you to do something cool or interesting in response to this, or just to treat it as a normal category. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyDisplayCategoryDefinition object
const example = {
  index: 123,
  identifier: "example value",
  displayCategoryHash: 123,
  displayProperties: null,
  displayInBanner: true,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyDisplayCategoryDefinition object
example = {
    "index": 123,
    "identifier": "example value",
    "displayCategoryHash": 123,
    "displayProperties": None,
    "displayInBanner": True,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyProgressionDefinition**: Referenced in this entity
- **Destiny.VendorDisplayCategorySortOrder**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyDisplayCategoryDefinition":   {
      "description": "Display Categories are different from \"categories\" in that these are specifically for visual grouping and display of categories in Vendor UI. The \"categories\" structure is for validation of the contained items, and can be categorized entirely separately from \"Display Categories\", there need be and often will be no meaningful relationship between the two.",
      "type": "object",
      "properties": {
          "index": {
              "format": "int32",
              "type": "integer"
          },
          "identifier": {
              "description": "A string identifier for the display category.",
              "type": "string"
          },
          "displayCategoryHash": {
              "format": "uint32",
              "type": "integer"
          },
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "displayInBanner": {
              "description": "If true, this category should be displayed in the \"Banner\" section of the vendor's UI.",
              "type": "boolean"
          },
          "progressionHash": {
              "format": "uint32",
              "description": "If it exists, this is the hash identifier of a DestinyProgressionDefinition that represents the progression to show on this display category.\r\nSpecific categories can now have thier own distinct progression, apparently. So that's cool.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyProgressionDefinition"
              }
          },
          "sortOrder": {
              "format": "int32",
              "description": "If this category sorts items in a nonstandard way, this will be the way we sort.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.VendorDisplayCategorySortOrder"
              }
          },
          "displayStyleHash": {
              "format": "uint32",
              "description": "An indicator of how the category will be displayed in the UI. It's up to you to do something cool or interesting in response to this, or just to treat it as a normal category.",
              "type": "integer"
          },
          "displayStyleIdentifier": {
              "description": "An indicator of how the category will be displayed in the UI. It's up to you to do something cool or interesting in response to this, or just to treat it as a normal category.",
              "type": "string"
          }
      }
  }
}
```
