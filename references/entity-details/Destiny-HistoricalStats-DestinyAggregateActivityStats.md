# Destiny.HistoricalStats.DestinyAggregateActivityStats

## Entity Information
- **Entity Name**: Destiny.HistoricalStats.DestinyAggregateActivityStats
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyaggregateactivitystats data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| activityHash | integer (uint32) | Hash ID that can be looked up in the DestinyActivityTable. | No |
| values | object | Collection of stats for the player in this activity. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.HistoricalStats.DestinyAggregateActivityStats object
const example = {
  activityHash: 123,
  values: null,
};
```

### Python
```python
# Example Destiny.HistoricalStats.DestinyAggregateActivityStats object
example = {
    "activityHash": 123,
    "values": None,
}
```

## Related Entities
- **Destiny.Definitions.DestinyActivityDefinition**: Referenced in this entity
- **Destiny.HistoricalStats.DestinyHistoricalStatsValue**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.HistoricalStats.DestinyAggregateActivityStats":   {
      "type": "object",
      "properties": {
          "activityHash": {
              "format": "uint32",
              "description": "Hash ID that can be looked up in the DestinyActivityTable.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityDefinition"
              }
          },
          "values": {
              "description": "Collection of stats for the player in this activity.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.HistoricalStats.DestinyHistoricalStatsValue"
              }
          }
      }
  }
}
```
