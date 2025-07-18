# DictionaryComponentResponseOfint64AndDestinyKiosksComponent

## Entity Information
- **Entity Name**: DictionaryComponentResponseOfint64AndDestinyKiosksComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing dictionarycomponentresponseofint64anddestinykioskscomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| data | object |  | No |
| privacy | integer (int32) |  | No |
| disabled | boolean | If true, this component is disabled. | No |

## Usage Examples

### JavaScript
```javascript
// Example DictionaryComponentResponseOfint64AndDestinyKiosksComponent object
const example = {
  data: null,
  privacy: 123,
  disabled: true,
};
```

### Python
```python
# Example DictionaryComponentResponseOfint64AndDestinyKiosksComponent object
example = {
    "data": None,
    "privacy": 123,
    "disabled": True,
}
```

## Related Entities
- **Components.ComponentPrivacySetting**: Referenced in this entity
- **Destiny.Components.Kiosks.DestinyKiosksComponent**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "DictionaryComponentResponseOfint64AndDestinyKiosksComponent":   {
      "type": "object",
      "properties": {
          "data": {
              "type": "object",
              "additionalProperties": {
                  "x-destiny-component-type-dependency": "Kiosks",
                  "$ref": "#/definitions/Destiny.Components.Kiosks.DestinyKiosksComponent"
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
