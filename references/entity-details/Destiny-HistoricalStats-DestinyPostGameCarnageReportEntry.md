# Destiny.HistoricalStats.DestinyPostGameCarnageReportEntry

## Entity Information
- **Entity Name**: Destiny.HistoricalStats.DestinyPostGameCarnageReportEntry
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinypostgamecarnagereportentry data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| standing | integer (int32) | Standing of the player | No |
| score | object | Score of the player if available | No |
| player | object | Identity details of the player | No |
| characterId | integer (int64) | ID of the player's character used in the activity. | No |
| values | object | Collection of stats for the player in this activity. | No |
| extended | object | Extended data extracted from the activity blob. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.HistoricalStats.DestinyPostGameCarnageReportEntry object
const example = {
  standing: 123,
  score: null,
  player: null,
  characterId: 123,
  values: null,
  // ... more properties
};
```

### Python
```python
# Example Destiny.HistoricalStats.DestinyPostGameCarnageReportEntry object
example = {
    "standing": 123,
    "score": None,
    "player": None,
    "characterId": 123,
    "values": None,
    # ... more properties
}
```

## Related Entities
- **Destiny.HistoricalStats.DestinyHistoricalStatsValue**: Referenced in this entity
- **Destiny.HistoricalStats.DestinyPlayer**: Referenced in this entity
- **Destiny.HistoricalStats.DestinyPostGameCarnageReportExtendedData**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.HistoricalStats.DestinyPostGameCarnageReportEntry":   {
      "type": "object",
      "properties": {
          "standing": {
              "format": "int32",
              "description": "Standing of the player",
              "type": "integer"
          },
          "score": {
              "description": "Score of the player if available",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.HistoricalStats.DestinyHistoricalStatsValue"
                  }
              ]
          },
          "player": {
              "description": "Identity details of the player",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.HistoricalStats.DestinyPlayer"
                  }
              ]
          },
          "characterId": {
              "format": "int64",
              "description": "ID of the player's character used in the activity.",
              "type": "integer"
          },
          "values": {
              "description": "Collection of stats for the player in this activity.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.HistoricalStats.DestinyHistoricalStatsValue"
              }
          },
          "extended": {
              "description": "Extended data extracted from the activity blob.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.HistoricalStats.DestinyPostGameCarnageReportExtendedData"
                  }
              ]
          }
      }
  }
}
```
