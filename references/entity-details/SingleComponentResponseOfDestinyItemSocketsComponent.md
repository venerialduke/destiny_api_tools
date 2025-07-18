# SingleComponentResponseOfDestinyItemSocketsComponent

## Entity Information
- **Entity Name**: SingleComponentResponseOfDestinyItemSocketsComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing singlecomponentresponseofdestinyitemsocketscomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| data | Destiny.Entities.Items.DestinyItemSocketsComponent |  | No |
| privacy | integer (int32) |  | No |
| disabled | boolean | If true, this component is disabled. | No |

## Usage Examples

### JavaScript
```javascript
// Example SingleComponentResponseOfDestinyItemSocketsComponent object
const example = {
  data: null,
  privacy: 123,
  disabled: true,
};
```

### Python
```python
# Example SingleComponentResponseOfDestinyItemSocketsComponent object
example = {
    "data": None,
    "privacy": 123,
    "disabled": True,
}
```

## Related Entities
- **Components.ComponentPrivacySetting**: Referenced in this entity
- **Destiny.Entities.Items.DestinyItemSocketsComponent**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "SingleComponentResponseOfDestinyItemSocketsComponent":   {
      "type": "object",
      "properties": {
          "data": {
              "$ref": "#/definitions/Destiny.Entities.Items.DestinyItemSocketsComponent"
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
