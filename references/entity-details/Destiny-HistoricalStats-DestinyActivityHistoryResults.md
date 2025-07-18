# Destiny.HistoricalStats.DestinyActivityHistoryResults

## Entity Information
- **Entity Name**: Destiny.HistoricalStats.DestinyActivityHistoryResults
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyactivityhistoryresults data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| activities | Array[Destiny.HistoricalStats.DestinyHistoricalStatsPeriodGroup] | List of activities, the most recent activity first. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.HistoricalStats.DestinyActivityHistoryResults object
const example = {
  activities: [],
};
```

### Python
```python
# Example Destiny.HistoricalStats.DestinyActivityHistoryResults object
example = {
    "activities": [],
}
```

## Related Entities
- **Destiny.HistoricalStats.DestinyHistoricalStatsPeriodGroup**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.HistoricalStats.DestinyActivityHistoryResults":   {
      "type": "object",
      "properties": {
          "activities": {
              "description": "List of activities, the most recent activity first.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.HistoricalStats.DestinyHistoricalStatsPeriodGroup"
              }
          }
      }
  }
}
```
