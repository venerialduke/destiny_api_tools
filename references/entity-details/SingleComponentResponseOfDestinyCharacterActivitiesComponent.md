# SingleComponentResponseOfDestinyCharacterActivitiesComponent

## Entity Information
- **Entity Name**: SingleComponentResponseOfDestinyCharacterActivitiesComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing singlecomponentresponseofdestinycharacteractivitiescomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| data | Destiny.Entities.Characters.DestinyCharacterActivitiesComponent |  | No |
| privacy | integer (int32) |  | No |
| disabled | boolean | If true, this component is disabled. | No |

## Usage Examples

### JavaScript
```javascript
// Example SingleComponentResponseOfDestinyCharacterActivitiesComponent object
const example = {
  data: null,
  privacy: 123,
  disabled: true,
};
```

### Python
```python
# Example SingleComponentResponseOfDestinyCharacterActivitiesComponent object
example = {
    "data": None,
    "privacy": 123,
    "disabled": True,
}
```

## Related Entities
- **Components.ComponentPrivacySetting**: Referenced in this entity
- **Destiny.Entities.Characters.DestinyCharacterActivitiesComponent**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "SingleComponentResponseOfDestinyCharacterActivitiesComponent":   {
      "type": "object",
      "properties": {
          "data": {
              "$ref": "#/definitions/Destiny.Entities.Characters.DestinyCharacterActivitiesComponent"
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
