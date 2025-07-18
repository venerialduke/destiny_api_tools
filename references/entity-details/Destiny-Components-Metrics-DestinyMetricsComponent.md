# Destiny.Components.Metrics.DestinyMetricsComponent

## Entity Information
- **Entity Name**: Destiny.Components.Metrics.DestinyMetricsComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinymetricscomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| metrics | object |  | No |
| metricsRootNodeHash | integer (uint32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Metrics.DestinyMetricsComponent object
const example = {
  metrics: null,
  metricsRootNodeHash: 123,
};
```

### Python
```python
# Example Destiny.Components.Metrics.DestinyMetricsComponent object
example = {
    "metrics": None,
    "metricsRootNodeHash": 123,
}
```

## Related Entities
- **Destiny.Components.Metrics.DestinyMetricComponent**: Referenced in this entity
- **Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Metrics.DestinyMetricsComponent":   {
      "type": "object",
      "properties": {
          "metrics": {
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.Components.Metrics.DestinyMetricComponent"
              }
          },
          "metricsRootNodeHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
              }
          }
      },
      "x-destiny-component-type-dependency": "Metrics"
  }
}
```
