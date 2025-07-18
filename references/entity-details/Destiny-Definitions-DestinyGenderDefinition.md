# Destiny.Definitions.DestinyGenderDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyGenderDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Gender is a social construct, and as such we have definitions for Genders. Right now there happens to only be two, but we'll see what the future holds.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| genderType | integer (int32) | This is a quick reference enumeration for all of the currently defined Genders. We use the enumeration for quicker lookups in related data, like DestinyClassDefinition.genderedClassNames. | No |
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyGenderDefinition object
const example = {
  genderType: 123,
  displayProperties: null,
  hash: 123,
  index: 123,
  redacted: true,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyGenderDefinition object
example = {
    "genderType": 123,
    "displayProperties": None,
    "hash": 123,
    "index": 123,
    "redacted": True,
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.DestinyGender**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyGenderDefinition":   {
      "description": "Gender is a social construct, and as such we have definitions for Genders. Right now there happens to only be two, but we'll see what the future holds.",
      "type": "object",
      "properties": {
          "genderType": {
              "format": "int32",
              "description": "This is a quick reference enumeration for all of the currently defined Genders. We use the enumeration for quicker lookups in related data, like DestinyClassDefinition.genderedClassNames.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyGender"
              }
          },
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
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
      "x-mobile-manifest-name": "Genders"
  }
}
```
