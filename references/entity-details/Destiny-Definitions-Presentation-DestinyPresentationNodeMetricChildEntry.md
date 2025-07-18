# Destiny.Definitions.Presentation.DestinyPresentationNodeMetricChildEntry

## Entity Information
- **Entity Name**: Destiny.Definitions.Presentation.DestinyPresentationNodeMetricChildEntry
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinypresentationnodemetricchildentry data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| metricHash | integer (uint32) |  | No |
| nodeDisplayPriority | integer (uint32) | Use this value to sort the presentation node children in ascending order. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Presentation.DestinyPresentationNodeMetricChildEntry object
const example = {
  metricHash: 123,
  nodeDisplayPriority: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Presentation.DestinyPresentationNodeMetricChildEntry object
example = {
    "metricHash": 123,
    "nodeDisplayPriority": 123,
}
```

## Related Entities
- **Destiny.Definitions.Metrics.DestinyMetricDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Presentation.DestinyPresentationNodeMetricChildEntry":   {
      "type": "object",
      "properties": {
          "metricHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Metrics.DestinyMetricDefinition"
              }
          },
          "nodeDisplayPriority": {
              "format": "uint32",
              "description": "Use this value to sort the presentation node children in ascending order.",
              "type": "integer"
          }
      }
  }
}
```
