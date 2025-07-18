# Destiny.Definitions.DestinyVendorDisplayPropertiesDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyVendorDisplayPropertiesDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyvendordisplaypropertiesdefinition data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| largeIcon | string | I regret calling this a "large icon". It's more like a medium-sized image with a picture of the vendor's mug on it, trying their best to look cool. Not what one would call an icon. | No |
| subtitle | string |  | No |
| originalIcon | string | If we replaced the icon with something more glitzy, this is the original icon that the vendor had according to the game's content. It may be more lame and/or have less razzle-dazzle. But who am I to tell you which icon to use. | No |
| requirementsDisplay | Array[Destiny.Definitions.DestinyVendorRequirementDisplayEntryDefinition] | Vendors, in addition to expected display property data, may also show some "common requirements" as statically defined definition data. This might be when a vendor accepts a single type of currency, or when the currency is unique to the vendor and the designers wanted to show that currency when you interact with the vendor. | No |
| smallTransparentIcon | string | This is the icon used in parts of the game UI such as the vendor's waypoint. | No |
| mapIcon | string | This is the icon used in the map overview, when the vendor is located on the map. | No |
| largeTransparentIcon | string | This is apparently the "Watermark". I am not certain offhand where this is actually used in the Game UI, but some people may find it useful. | No |
| description | string |  | No |
| name | string |  | No |
| icon | string | Note that "icon" is sometimes misleading, and should be interpreted in the context of the entity. For instance, in Destiny 1 the DestinyRecordBookDefinition's icon was a big picture of a book.
But usually, it will be a small square image that you can use as... well, an icon.
They are currently represented as 96px x 96px images. | No |
| iconSequences | Array[Destiny.Definitions.Common.DestinyIconSequenceDefinition] |  | No |
| highResIcon | string | If this item has a high-res icon (at least for now, many things won't), then the path to that icon will be here. | No |
| hasIcon | boolean |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyVendorDisplayPropertiesDefinition object
const example = {
  largeIcon: "example value",
  subtitle: "example value",
  originalIcon: "example value",
  requirementsDisplay: [],
  smallTransparentIcon: "example value",
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyVendorDisplayPropertiesDefinition object
example = {
    "largeIcon": "example value",
    "subtitle": "example value",
    "originalIcon": "example value",
    "requirementsDisplay": [],
    "smallTransparentIcon": "example value",
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyIconSequenceDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyVendorRequirementDisplayEntryDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyVendorDisplayPropertiesDefinition":   {
      "type": "object",
      "properties": {
          "largeIcon": {
              "description": "I regret calling this a \"large icon\". It's more like a medium-sized image with a picture of the vendor's mug on it, trying their best to look cool. Not what one would call an icon.",
              "type": "string"
          },
          "subtitle": {
              "type": "string"
          },
          "originalIcon": {
              "description": "If we replaced the icon with something more glitzy, this is the original icon that the vendor had according to the game's content. It may be more lame and/or have less razzle-dazzle. But who am I to tell you which icon to use.",
              "type": "string"
          },
          "requirementsDisplay": {
              "description": "Vendors, in addition to expected display property data, may also show some \"common requirements\" as statically defined definition data. This might be when a vendor accepts a single type of currency, or when the currency is unique to the vendor and the designers wanted to show that currency when you interact with the vendor.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorRequirementDisplayEntryDefinition"
              }
          },
          "smallTransparentIcon": {
              "description": "This is the icon used in parts of the game UI such as the vendor's waypoint.",
              "type": "string"
          },
          "mapIcon": {
              "description": "This is the icon used in the map overview, when the vendor is located on the map.",
              "type": "string"
          },
          "largeTransparentIcon": {
              "description": "This is apparently the \"Watermark\". I am not certain offhand where this is actually used in the Game UI, but some people may find it useful.",
              "type": "string"
          },
          "description": {
              "type": "string"
          },
          "name": {
              "type": "string"
          },
          "icon": {
              "description": "Note that \"icon\" is sometimes misleading, and should be interpreted in the context of the entity. For instance, in Destiny 1 the DestinyRecordBookDefinition's icon was a big picture of a book.\r\nBut usually, it will be a small square image that you can use as... well, an icon.\r\nThey are currently represented as 96px x 96px images.",
              "type": "string"
          },
          "iconSequences": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Common.DestinyIconSequenceDefinition"
              }
          },
          "highResIcon": {
              "description": "If this item has a high-res icon (at least for now, many things won't), then the path to that icon will be here.",
              "type": "string"
          },
          "hasIcon": {
              "type": "boolean"
          }
      }
  }
}
```
