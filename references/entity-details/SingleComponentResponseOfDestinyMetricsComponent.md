# SingleComponentResponseOfDestinyMetricsComponent

## Entity Information
- **Entity Name**: SingleComponentResponseOfDestinyMetricsComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing singlecomponentresponseofdestinymetricscomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| data | Destiny.Components.Metrics.DestinyMetricsComponent |  | No |
| privacy | integer (int32) |  | No |
| disabled | boolean | If true, this component is disabled. | No |

## Usage Examples

### JavaScript
```javascript
// Example SingleComponentResponseOfDestinyMetricsComponent object
const example = {
  data: null,
  privacy: 123,
  disabled: true,
};
```

### Python
```python
# Example SingleComponentResponseOfDestinyMetricsComponent object
example = {
    "data": None,
    "privacy": 123,
    "disabled": True,
}
```

## Related Entities
- **Components.ComponentPrivacySetting**: Referenced in this entity
- **Destiny.Components.Metrics.DestinyMetricsComponent**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "SingleComponentResponseOfDestinyMetricsComponent":   {
      "type": "object",
      "properties": {
          "data": {
              "$ref": "#/definitions/Destiny.Components.Metrics.DestinyMetricsComponent"
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
