# Destiny.HistoricalStats.DestinyHistoricalStatsPeriodGroup

## Entity Information
- **Entity Name**: Destiny.HistoricalStats.DestinyHistoricalStatsPeriodGroup
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyhistoricalstatsperiodgroup data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| period | string (date-time) | Period for the group. If the stat periodType is day, then this will have a specific day. If the type is monthly, then this value will be the first day of the applicable month. This value is not set when the periodType is 'all time'. | No |
| activityDetails | object | If the period group is for a specific activity, this property will be set. | No |
| values | object | Collection of stats for the period. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.HistoricalStats.DestinyHistoricalStatsPeriodGroup object
const example = {
  period: "example value",
  activityDetails: null,
  values: null,
};
```

### Python
```python
# Example Destiny.HistoricalStats.DestinyHistoricalStatsPeriodGroup object
example = {
    "period": "example value",
    "activityDetails": None,
    "values": None,
}
```

## Related Entities
- **Destiny.HistoricalStats.DestinyHistoricalStatsActivity**: Referenced in this entity
- **Destiny.HistoricalStats.DestinyHistoricalStatsValue**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.HistoricalStats.DestinyHistoricalStatsPeriodGroup":   {
      "type": "object",
      "properties": {
          "period": {
              "format": "date-time",
              "description": "Period for the group. If the stat periodType is day, then this will have a specific day. If the type is monthly, then this value will be the first day of the applicable month. This value is not set when the periodType is 'all time'.",
              "type": "string"
          },
          "activityDetails": {
              "description": "If the period group is for a specific activity, this property will be set.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.HistoricalStats.DestinyHistoricalStatsActivity"
                  }
              ]
          },
          "values": {
              "description": "Collection of stats for the period.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.HistoricalStats.DestinyHistoricalStatsValue"
              }
          }
      }
  }
}
```
