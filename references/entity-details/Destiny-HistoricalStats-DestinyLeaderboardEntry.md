# Destiny.HistoricalStats.DestinyLeaderboardEntry

## Entity Information
- **Entity Name**: Destiny.HistoricalStats.DestinyLeaderboardEntry
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyleaderboardentry data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| rank | integer (int32) | Where this player ranks on the leaderboard. A value of 1 is the top rank. | No |
| player | object | Identity details of the player | No |
| characterId | integer (int64) | ID of the player's best character for the reported stat. | No |
| value | object | Value of the stat for this player | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.HistoricalStats.DestinyLeaderboardEntry object
const example = {
  rank: 123,
  player: null,
  characterId: 123,
  value: null,
};
```

### Python
```python
# Example Destiny.HistoricalStats.DestinyLeaderboardEntry object
example = {
    "rank": 123,
    "player": None,
    "characterId": 123,
    "value": None,
}
```

## Related Entities
- **Destiny.HistoricalStats.DestinyHistoricalStatsValue**: Referenced in this entity
- **Destiny.HistoricalStats.DestinyPlayer**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.HistoricalStats.DestinyLeaderboardEntry":   {
      "type": "object",
      "properties": {
          "rank": {
              "format": "int32",
              "description": "Where this player ranks on the leaderboard. A value of 1 is the top rank.",
              "type": "integer"
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
              "description": "ID of the player's best character for the reported stat.",
              "type": "integer"
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
