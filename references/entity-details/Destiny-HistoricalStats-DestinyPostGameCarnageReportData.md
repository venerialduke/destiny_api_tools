# Destiny.HistoricalStats.DestinyPostGameCarnageReportData

## Entity Information
- **Entity Name**: Destiny.HistoricalStats.DestinyPostGameCarnageReportData
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinypostgamecarnagereportdata data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| period | string (date-time) | Date and time for the activity. | No |
| startingPhaseIndex | integer (int32) | If this activity has "phases", this is the phase at which the activity was started. This value is only valid for activities before the Beyond Light expansion shipped. Subsequent activities will not have a valid value here. | No |
| activityWasStartedFromBeginning | boolean | True if the activity was started from the beginning, if that information is available and the activity was played post Witch Queen release. | No |
| activityDifficultyTier | integer (int32) | Difficulty tier index value for the activity. | No |
| selectedSkullHashes | Array[integer] | Collection of player-selected skull hashes active for the activity. | No |
| activityDetails | object | Details about the activity. | No |
| entries | Array[Destiny.HistoricalStats.DestinyPostGameCarnageReportEntry] | Collection of players and their data for this activity. | No |
| teams | Array[Destiny.HistoricalStats.DestinyPostGameCarnageReportTeamEntry] | Collection of stats for the player in this activity. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.HistoricalStats.DestinyPostGameCarnageReportData object
const example = {
  period: "example value",
  startingPhaseIndex: 123,
  activityWasStartedFromBeginning: true,
  activityDifficultyTier: 123,
  selectedSkullHashes: [],
  // ... more properties
};
```

### Python
```python
# Example Destiny.HistoricalStats.DestinyPostGameCarnageReportData object
example = {
    "period": "example value",
    "startingPhaseIndex": 123,
    "activityWasStartedFromBeginning": True,
    "activityDifficultyTier": 123,
    "selectedSkullHashes": [],
    # ... more properties
}
```

## Related Entities
- **Destiny.HistoricalStats.DestinyHistoricalStatsActivity**: Referenced in this entity
- **Destiny.HistoricalStats.DestinyPostGameCarnageReportEntry**: Referenced in this entity
- **Destiny.HistoricalStats.DestinyPostGameCarnageReportTeamEntry**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.HistoricalStats.DestinyPostGameCarnageReportData":   {
      "type": "object",
      "properties": {
          "period": {
              "format": "date-time",
              "description": "Date and time for the activity.",
              "type": "string"
          },
          "startingPhaseIndex": {
              "format": "int32",
              "description": "If this activity has \"phases\", this is the phase at which the activity was started. This value is only valid for activities before the Beyond Light expansion shipped. Subsequent activities will not have a valid value here.",
              "type": "integer"
          },
          "activityWasStartedFromBeginning": {
              "description": "True if the activity was started from the beginning, if that information is available and the activity was played post Witch Queen release.",
              "type": "boolean"
          },
          "activityDifficultyTier": {
              "format": "int32",
              "description": "Difficulty tier index value for the activity.",
              "type": "integer"
          },
          "selectedSkullHashes": {
              "description": "Collection of player-selected skull hashes active for the activity.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              }
          },
          "activityDetails": {
              "description": "Details about the activity.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.HistoricalStats.DestinyHistoricalStatsActivity"
                  }
              ]
          },
          "entries": {
              "description": "Collection of players and their data for this activity.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.HistoricalStats.DestinyPostGameCarnageReportEntry"
              }
          },
          "teams": {
              "description": "Collection of stats for the player in this activity.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.HistoricalStats.DestinyPostGameCarnageReportTeamEntry"
              }
          }
      }
  }
}
```
