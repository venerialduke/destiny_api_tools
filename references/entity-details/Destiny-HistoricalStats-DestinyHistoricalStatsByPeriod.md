# Destiny.HistoricalStats.DestinyHistoricalStatsByPeriod

## Entity Information
- **Entity Name**: Destiny.HistoricalStats.DestinyHistoricalStatsByPeriod
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyhistoricalstatsbyperiod data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| allTime | object |  | No |
| allTimeTier1 | object |  | No |
| allTimeTier2 | object |  | No |
| allTimeTier3 | object |  | No |
| daily | Array[Destiny.HistoricalStats.DestinyHistoricalStatsPeriodGroup] |  | No |
| monthly | Array[Destiny.HistoricalStats.DestinyHistoricalStatsPeriodGroup] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.HistoricalStats.DestinyHistoricalStatsByPeriod object
const example = {
  allTime: null,
  allTimeTier1: null,
  allTimeTier2: null,
  allTimeTier3: null,
  daily: [],
  // ... more properties
};
```

### Python
```python
# Example Destiny.HistoricalStats.DestinyHistoricalStatsByPeriod object
example = {
    "allTime": None,
    "allTimeTier1": None,
    "allTimeTier2": None,
    "allTimeTier3": None,
    "daily": [],
    # ... more properties
}
```

## Related Entities
- **Destiny.HistoricalStats.DestinyHistoricalStatsPeriodGroup**: Referenced in this entity
- **Destiny.HistoricalStats.DestinyHistoricalStatsValue**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.HistoricalStats.DestinyHistoricalStatsByPeriod":   {
      "type": "object",
      "properties": {
          "allTime": {
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.HistoricalStats.DestinyHistoricalStatsValue"
              }
          },
          "allTimeTier1": {
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.HistoricalStats.DestinyHistoricalStatsValue"
              }
          },
          "allTimeTier2": {
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.HistoricalStats.DestinyHistoricalStatsValue"
              }
          },
          "allTimeTier3": {
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.HistoricalStats.DestinyHistoricalStatsValue"
              }
          },
          "daily": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.HistoricalStats.DestinyHistoricalStatsPeriodGroup"
              }
          },
          "monthly": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.HistoricalStats.DestinyHistoricalStatsPeriodGroup"
              }
          }
      }
  }
}
```
