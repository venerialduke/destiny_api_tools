# DictionaryComponentResponseOfint64AndDestinyCharacterComponent

## Entity Information
- **Entity Name**: DictionaryComponentResponseOfint64AndDestinyCharacterComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing dictionarycomponentresponseofint64anddestinycharactercomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| data | object |  | No |
| privacy | integer (int32) |  | No |
| disabled | boolean | If true, this component is disabled. | No |

## Usage Examples

### JavaScript
```javascript
// Example DictionaryComponentResponseOfint64AndDestinyCharacterComponent object
const example = {
  data: null,
  privacy: 123,
  disabled: true,
};
```

### Python
```python
# Example DictionaryComponentResponseOfint64AndDestinyCharacterComponent object
example = {
    "data": None,
    "privacy": 123,
    "disabled": True,
}
```

## Related Entities
- **Components.ComponentPrivacySetting**: Referenced in this entity
- **Destiny.Entities.Characters.DestinyCharacterComponent**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "DictionaryComponentResponseOfint64AndDestinyCharacterComponent":   {
      "type": "object",
      "properties": {
          "data": {
              "type": "object",
              "additionalProperties": {
                  "x-destiny-component-type-dependency": "Characters",
                  "$ref": "#/definitions/Destiny.Entities.Characters.DestinyCharacterComponent"
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
