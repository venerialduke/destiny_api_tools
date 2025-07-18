# Destiny.HistoricalStats.DestinyLeaderboardResults

## Entity Information
- **Entity Name**: Destiny.HistoricalStats.DestinyLeaderboardResults
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyleaderboardresults data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| focusMembershipId | integer (int64) | Indicate the membership ID of the account that is the focal point of the provided leaderboards. | No |
| focusCharacterId | integer (int64) | Indicate the character ID of the character that is the focal point of the provided leaderboards. May be null, in which case any character from the focus membership can appear in the provided leaderboards. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.HistoricalStats.DestinyLeaderboardResults object
const example = {
  focusMembershipId: 123,
  focusCharacterId: 123,
};
```

### Python
```python
# Example Destiny.HistoricalStats.DestinyLeaderboardResults object
example = {
    "focusMembershipId": 123,
    "focusCharacterId": 123,
}
```

## Related Entities
- **Destiny.HistoricalStats.DestinyLeaderboard**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.HistoricalStats.DestinyLeaderboardResults":   {
      "type": "object",
      "properties": {
          "focusMembershipId": {
              "format": "int64",
              "description": "Indicate the membership ID of the account that is the focal point of the provided leaderboards.",
              "type": "integer"
          },
          "focusCharacterId": {
              "format": "int64",
              "description": "Indicate the character ID of the character that is the focal point of the provided leaderboards. May be null, in which case any character from the focus membership can appear in the provided leaderboards.",
              "type": "integer"
          }
      },
      "additionalProperties": {
          "type": "object",
          "additionalProperties": {
              "$ref": "#/definitions/Destiny.HistoricalStats.DestinyLeaderboard"
          }
      }
  }
}
```
