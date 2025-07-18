# Destiny.HistoricalStats.DestinyHistoricalStatsWithMerged

## Entity Information
- **Entity Name**: Destiny.HistoricalStats.DestinyHistoricalStatsWithMerged
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyhistoricalstatswithmerged data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| results | object |  | No |
| merged | Destiny.HistoricalStats.DestinyHistoricalStatsByPeriod |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.HistoricalStats.DestinyHistoricalStatsWithMerged object
const example = {
  results: null,
  merged: null,
};
```

### Python
```python
# Example Destiny.HistoricalStats.DestinyHistoricalStatsWithMerged object
example = {
    "results": None,
    "merged": None,
}
```

## Related Entities
- **Destiny.HistoricalStats.DestinyHistoricalStatsByPeriod**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.HistoricalStats.DestinyHistoricalStatsWithMerged":   {
      "type": "object",
      "properties": {
          "results": {
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.HistoricalStats.DestinyHistoricalStatsByPeriod"
              }
          },
          "merged": {
              "$ref": "#/definitions/Destiny.HistoricalStats.DestinyHistoricalStatsByPeriod"
          }
      }
  }
}
```
