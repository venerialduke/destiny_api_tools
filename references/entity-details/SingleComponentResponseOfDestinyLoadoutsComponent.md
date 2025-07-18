# SingleComponentResponseOfDestinyLoadoutsComponent

## Entity Information
- **Entity Name**: SingleComponentResponseOfDestinyLoadoutsComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing singlecomponentresponseofdestinyloadoutscomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| data | Destiny.Components.Loadouts.DestinyLoadoutsComponent |  | No |
| privacy | integer (int32) |  | No |
| disabled | boolean | If true, this component is disabled. | No |

## Usage Examples

### JavaScript
```javascript
// Example SingleComponentResponseOfDestinyLoadoutsComponent object
const example = {
  data: null,
  privacy: 123,
  disabled: true,
};
```

### Python
```python
# Example SingleComponentResponseOfDestinyLoadoutsComponent object
example = {
    "data": None,
    "privacy": 123,
    "disabled": True,
}
```

## Related Entities
- **Components.ComponentPrivacySetting**: Referenced in this entity
- **Destiny.Components.Loadouts.DestinyLoadoutsComponent**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "SingleComponentResponseOfDestinyLoadoutsComponent":   {
      "type": "object",
      "properties": {
          "data": {
              "$ref": "#/definitions/Destiny.Components.Loadouts.DestinyLoadoutsComponent"
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
