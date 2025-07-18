# Destiny.HistoricalStats.DestinyClanAggregateStat

## Entity Information
- **Entity Name**: Destiny.HistoricalStats.DestinyClanAggregateStat
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyclanaggregatestat data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| mode | integer (int32) | The id of the mode of stats (allPvp, allPvE, etc) | No |
| statId | string | The id of the stat | No |
| value | object | Value of the stat for this player | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.HistoricalStats.DestinyClanAggregateStat object
const example = {
  mode: 123,
  statId: "example value",
  value: null,
};
```

### Python
```python
# Example Destiny.HistoricalStats.DestinyClanAggregateStat object
example = {
    "mode": 123,
    "statId": "example value",
    "value": None,
}
```

## Related Entities
- **Destiny.HistoricalStats.Definitions.DestinyActivityModeType**: Referenced in this entity
- **Destiny.HistoricalStats.DestinyHistoricalStatsValue**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.HistoricalStats.DestinyClanAggregateStat":   {
      "type": "object",
      "properties": {
          "mode": {
              "format": "int32",
              "description": "The id of the mode of stats (allPvp, allPvE, etc)",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.HistoricalStats.Definitions.DestinyActivityModeType"
              }
          },
          "statId": {
              "description": "The id of the stat",
              "type": "string"
          },
          "value": {
              "description": "Value of the stat for this player",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.HistoricalStats.DestinyHistoricalStatsValue"
                  }
              ]
          }
      }
  }
}
```
