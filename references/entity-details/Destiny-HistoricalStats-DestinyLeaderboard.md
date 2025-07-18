# Destiny.HistoricalStats.DestinyLeaderboard

## Entity Information
- **Entity Name**: Destiny.HistoricalStats.DestinyLeaderboard
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyleaderboard data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| statId | string |  | No |
| entries | Array[Destiny.HistoricalStats.DestinyLeaderboardEntry] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.HistoricalStats.DestinyLeaderboard object
const example = {
  statId: "example value",
  entries: [],
};
```

### Python
```python
# Example Destiny.HistoricalStats.DestinyLeaderboard object
example = {
    "statId": "example value",
    "entries": [],
}
```

## Related Entities
- **Destiny.HistoricalStats.DestinyLeaderboardEntry**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.HistoricalStats.DestinyLeaderboard":   {
      "type": "object",
      "properties": {
          "statId": {
              "type": "string"
          },
          "entries": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.HistoricalStats.DestinyLeaderboardEntry"
              }
          }
      }
  }
}
```
