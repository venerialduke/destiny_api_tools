# Destiny.HistoricalStats.DestinyHistoricalStatsValuePair

## Entity Information
- **Entity Name**: Destiny.HistoricalStats.DestinyHistoricalStatsValuePair
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyhistoricalstatsvaluepair data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| value | number (double) | Raw value of the statistic | No |
| displayValue | string | Localized formated version of the value. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.HistoricalStats.DestinyHistoricalStatsValuePair object
const example = {
  value: 123.45,
  displayValue: "example value",
};
```

### Python
```python
# Example Destiny.HistoricalStats.DestinyHistoricalStatsValuePair object
example = {
    "value": 123.45,
    "displayValue": "example value",
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.HistoricalStats.DestinyHistoricalStatsValuePair":   {
      "type": "object",
      "properties": {
          "value": {
              "format": "double",
              "description": "Raw value of the statistic",
              "type": "number"
          },
          "displayValue": {
              "description": "Localized formated version of the value.",
              "type": "string"
          }
      }
  }
}
```
