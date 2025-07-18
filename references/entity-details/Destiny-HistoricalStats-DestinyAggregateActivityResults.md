# Destiny.HistoricalStats.DestinyAggregateActivityResults

## Entity Information
- **Entity Name**: Destiny.HistoricalStats.DestinyAggregateActivityResults
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyaggregateactivityresults data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| activities | Array[Destiny.HistoricalStats.DestinyAggregateActivityStats] | List of all activities the player has participated in. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.HistoricalStats.DestinyAggregateActivityResults object
const example = {
  activities: [],
};
```

### Python
```python
# Example Destiny.HistoricalStats.DestinyAggregateActivityResults object
example = {
    "activities": [],
}
```

## Related Entities
- **Destiny.HistoricalStats.DestinyAggregateActivityStats**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.HistoricalStats.DestinyAggregateActivityResults":   {
      "type": "object",
      "properties": {
          "activities": {
              "description": "List of all activities the player has participated in.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.HistoricalStats.DestinyAggregateActivityStats"
              }
          }
      }
  }
}
```
