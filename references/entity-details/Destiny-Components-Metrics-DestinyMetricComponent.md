# Destiny.Components.Metrics.DestinyMetricComponent

## Entity Information
- **Entity Name**: Destiny.Components.Metrics.DestinyMetricComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinymetriccomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| invisible | boolean |  | No |
| objectiveProgress | Destiny.Quests.DestinyObjectiveProgress |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Metrics.DestinyMetricComponent object
const example = {
  invisible: true,
  objectiveProgress: null,
};
```

### Python
```python
# Example Destiny.Components.Metrics.DestinyMetricComponent object
example = {
    "invisible": True,
    "objectiveProgress": None,
}
```

## Related Entities
- **Destiny.Quests.DestinyObjectiveProgress**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Metrics.DestinyMetricComponent":   {
      "type": "object",
      "properties": {
          "invisible": {
              "type": "boolean"
          },
          "objectiveProgress": {
              "$ref": "#/definitions/Destiny.Quests.DestinyObjectiveProgress"
          }
      }
  }
}
```
