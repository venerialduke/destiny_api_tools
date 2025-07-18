# Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Many Destiny*Definition contracts - the "first order" entities of Destiny that have their own tables in the Manifest Database - also have displayable information. This is the base class for that display information.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
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
// Example Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition object
const example = {
  description: "example value",
  name: "example value",
  icon: "example value",
  iconSequences: [],
  highResIcon: "example value",
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition object
example = {
    "description": "example value",
    "name": "example value",
    "icon": "example value",
    "iconSequences": [],
    "highResIcon": "example value",
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyIconSequenceDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition":   {
      "description": "Many Destiny*Definition contracts - the \"first order\" entities of Destiny that have their own tables in the Manifest Database - also have displayable information. This is the base class for that display information.",
      "type": "object",
      "properties": {
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
