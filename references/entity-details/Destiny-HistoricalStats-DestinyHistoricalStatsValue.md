# Destiny.HistoricalStats.DestinyHistoricalStatsValue

## Entity Information
- **Entity Name**: Destiny.HistoricalStats.DestinyHistoricalStatsValue
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyhistoricalstatsvalue data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| statId | string | Unique ID for this stat | No |
| basic | object | Basic stat value. | No |
| pga | object | Per game average for the statistic, if applicable | No |
| weighted | object | Weighted value of the stat if a weight greater than 1 has been assigned. | No |
| activityId | integer (int64) | When a stat represents the best, most, longest, fastest or some other personal best, the actual activity ID where that personal best was established is available on this property. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.HistoricalStats.DestinyHistoricalStatsValue object
const example = {
  statId: "example value",
  basic: null,
  pga: null,
  weighted: null,
  activityId: 123,
};
```

### Python
```python
# Example Destiny.HistoricalStats.DestinyHistoricalStatsValue object
example = {
    "statId": "example value",
    "basic": None,
    "pga": None,
    "weighted": None,
    "activityId": 123,
}
```

## Related Entities
- **Destiny.HistoricalStats.DestinyHistoricalStatsValuePair**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.HistoricalStats.DestinyHistoricalStatsValue":   {
      "type": "object",
      "properties": {
          "statId": {
              "description": "Unique ID for this stat",
              "type": "string"
          },
          "basic": {
              "description": "Basic stat value.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.HistoricalStats.DestinyHistoricalStatsValuePair"
                  }
              ]
          },
          "pga": {
              "description": "Per game average for the statistic, if applicable",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.HistoricalStats.DestinyHistoricalStatsValuePair"
                  }
              ]
          },
          "weighted": {
              "description": "Weighted value of the stat if a weight greater than 1 has been assigned.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.HistoricalStats.DestinyHistoricalStatsValuePair"
                  }
              ]
          },
          "activityId": {
              "format": "int64",
              "description": "When a stat represents the best, most, longest, fastest or some other personal best, the actual activity ID where that personal best was established is available on this property.",
              "type": "integer"
          }
      }
  }
}
```
