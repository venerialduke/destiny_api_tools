# Destiny.HistoricalStats.DestinyHistoricalStatsAccountResult

## Entity Information
- **Entity Name**: Destiny.HistoricalStats.DestinyHistoricalStatsAccountResult
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyhistoricalstatsaccountresult data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| mergedDeletedCharacters | Destiny.HistoricalStats.DestinyHistoricalStatsWithMerged |  | No |
| mergedAllCharacters | Destiny.HistoricalStats.DestinyHistoricalStatsWithMerged |  | No |
| characters | Array[Destiny.HistoricalStats.DestinyHistoricalStatsPerCharacter] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.HistoricalStats.DestinyHistoricalStatsAccountResult object
const example = {
  mergedDeletedCharacters: null,
  mergedAllCharacters: null,
  characters: [],
};
```

### Python
```python
# Example Destiny.HistoricalStats.DestinyHistoricalStatsAccountResult object
example = {
    "mergedDeletedCharacters": None,
    "mergedAllCharacters": None,
    "characters": [],
}
```

## Related Entities
- **Destiny.HistoricalStats.DestinyHistoricalStatsPerCharacter**: Referenced in this entity
- **Destiny.HistoricalStats.DestinyHistoricalStatsWithMerged**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.HistoricalStats.DestinyHistoricalStatsAccountResult":   {
      "type": "object",
      "properties": {
          "mergedDeletedCharacters": {
              "$ref": "#/definitions/Destiny.HistoricalStats.DestinyHistoricalStatsWithMerged"
          },
          "mergedAllCharacters": {
              "$ref": "#/definitions/Destiny.HistoricalStats.DestinyHistoricalStatsWithMerged"
          },
          "characters": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.HistoricalStats.DestinyHistoricalStatsPerCharacter"
              }
          }
      }
  }
}
```
