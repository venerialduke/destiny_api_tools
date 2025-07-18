# Destiny.HistoricalStats.DestinyHistoricalStatsPerCharacter

## Entity Information
- **Entity Name**: Destiny.HistoricalStats.DestinyHistoricalStatsPerCharacter
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyhistoricalstatspercharacter data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| characterId | integer (int64) |  | No |
| deleted | boolean |  | No |
| results | object |  | No |
| merged | Destiny.HistoricalStats.DestinyHistoricalStatsByPeriod |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.HistoricalStats.DestinyHistoricalStatsPerCharacter object
const example = {
  characterId: 123,
  deleted: true,
  results: null,
  merged: null,
};
```

### Python
```python
# Example Destiny.HistoricalStats.DestinyHistoricalStatsPerCharacter object
example = {
    "characterId": 123,
    "deleted": True,
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
  "Destiny.HistoricalStats.DestinyHistoricalStatsPerCharacter":   {
      "type": "object",
      "properties": {
          "characterId": {
              "format": "int64",
              "type": "integer"
          },
          "deleted": {
              "type": "boolean"
          },
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
