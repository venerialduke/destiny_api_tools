# Destiny.Definitions.DestinyClassDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyClassDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Defines a Character Class in Destiny 2. These are types of characters you can play, like Titan, Warlock, and Hunter.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| classType | integer (int32) | In Destiny 1, we added a convenience Enumeration for referring to classes. We've kept it, though mostly for posterity. This is the enum value for this definition's class. | No |
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| genderedClassNames | object | A localized string referring to the singular form of the Class's name when referred to in gendered form. Keyed by the DestinyGender. | No |
| genderedClassNamesByGenderHash | object |  | No |
| mentorVendorHash | integer (uint32) | Mentors don't really mean anything anymore. Don't expect this to be populated. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyClassDefinition object
const example = {
  classType: 123,
  displayProperties: null,
  genderedClassNames: null,
  genderedClassNamesByGenderHash: null,
  mentorVendorHash: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyClassDefinition object
example = {
    "classType": 123,
    "displayProperties": None,
    "genderedClassNames": None,
    "genderedClassNamesByGenderHash": None,
    "mentorVendorHash": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyGenderDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyVendorDefinition**: Referenced in this entity
- **Destiny.DestinyClass**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyClassDefinition":   {
      "description": "Defines a Character Class in Destiny 2. These are types of characters you can play, like Titan, Warlock, and Hunter.",
      "type": "object",
      "properties": {
          "classType": {
              "format": "int32",
              "description": "In Destiny 1, we added a convenience Enumeration for referring to classes. We've kept it, though mostly for posterity. This is the enum value for this definition's class.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyClass"
              }
          },
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "genderedClassNames": {
              "description": "A localized string referring to the singular form of the Class's name when referred to in gendered form. Keyed by the DestinyGender.",
              "type": "object",
              "additionalProperties": {
                  "type": "string"
              }
          },
          "genderedClassNamesByGenderHash": {
              "type": "object",
              "additionalProperties": {
                  "type": "string"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyGenderDefinition"
              }
          },
          "mentorVendorHash": {
              "format": "uint32",
              "description": "Mentors don't really mean anything anymore. Don't expect this to be populated.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorDefinition"
              }
          },
          "hash": {
              "format": "uint32",
              "description": "The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.\r\nWhen entities refer to each other in Destiny content, it is this hash that they are referring to.",
              "type": "integer"
          },
          "index": {
              "format": "int32",
              "description": "The index of the entity as it was found in the investment tables.",
              "type": "integer"
          },
          "redacted": {
              "description": "If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!",
              "type": "boolean"
          }
      },
      "x-mobile-manifest-name": "Classes"
  }
}
```
