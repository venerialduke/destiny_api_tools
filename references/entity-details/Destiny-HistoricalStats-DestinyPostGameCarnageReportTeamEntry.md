# Destiny.HistoricalStats.DestinyPostGameCarnageReportTeamEntry

## Entity Information
- **Entity Name**: Destiny.HistoricalStats.DestinyPostGameCarnageReportTeamEntry
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinypostgamecarnagereportteamentry data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| teamId | integer (int32) | Integer ID for the team. | No |
| standing | object | Team's standing relative to other teams. | No |
| score | object | Score earned by the team | No |
| teamName | string | Alpha or Bravo | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.HistoricalStats.DestinyPostGameCarnageReportTeamEntry object
const example = {
  teamId: 123,
  standing: null,
  score: null,
  teamName: "example value",
};
```

### Python
```python
# Example Destiny.HistoricalStats.DestinyPostGameCarnageReportTeamEntry object
example = {
    "teamId": 123,
    "standing": None,
    "score": None,
    "teamName": "example value",
}
```

## Related Entities
- **Destiny.HistoricalStats.DestinyHistoricalStatsValue**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.HistoricalStats.DestinyPostGameCarnageReportTeamEntry":   {
      "type": "object",
      "properties": {
          "teamId": {
              "format": "int32",
              "description": "Integer ID for the team.",
              "type": "integer"
          },
          "standing": {
              "description": "Team's standing relative to other teams.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.HistoricalStats.DestinyHistoricalStatsValue"
                  }
              ]
          },
          "score": {
              "description": "Score earned by the team",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.HistoricalStats.DestinyHistoricalStatsValue"
                  }
              ]
          },
          "teamName": {
              "description": "Alpha or Bravo",
              "type": "string"
          }
      }
  }
}
```
