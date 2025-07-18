# Destiny.Components.Profiles.DestinyProfileTransitoryCurrentActivity

## Entity Information
- **Entity Name**: Destiny.Components.Profiles.DestinyProfileTransitoryCurrentActivity
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
If you are playing in an activity, this is some information about it.
Note that we cannot guarantee any of this resembles what ends up in the PGCR in any way. They are sourced by two entirely separate systems with their own logic, and the one we source this data from should be considered non-authoritative in comparison.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| startTime | string (date-time) | When the activity started. | No |
| endTime | string (date-time) | If you're still in it but it "ended" (like when folks are dancing around the loot after they beat a boss), this is when the activity ended. | No |
| score | number (float) | This is what our non-authoritative source thought the score was. | No |
| highestOpposingFactionScore | number (float) | If you have human opponents, this is the highest opposing team's score. | No |
| numberOfOpponents | integer (int32) | This is how many human or poorly crafted aimbot opponents you have. | No |
| numberOfPlayers | integer (int32) | This is how many human or poorly crafted aimbots are on your team. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Profiles.DestinyProfileTransitoryCurrentActivity object
const example = {
  startTime: "example value",
  endTime: "example value",
  score: 123.45,
  highestOpposingFactionScore: 123.45,
  numberOfOpponents: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Components.Profiles.DestinyProfileTransitoryCurrentActivity object
example = {
    "startTime": "example value",
    "endTime": "example value",
    "score": 123.45,
    "highestOpposingFactionScore": 123.45,
    "numberOfOpponents": 123,
    # ... more properties
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Profiles.DestinyProfileTransitoryCurrentActivity":   {
      "description": "If you are playing in an activity, this is some information about it.\r\nNote that we cannot guarantee any of this resembles what ends up in the PGCR in any way. They are sourced by two entirely separate systems with their own logic, and the one we source this data from should be considered non-authoritative in comparison.",
      "type": "object",
      "properties": {
          "startTime": {
              "format": "date-time",
              "description": "When the activity started.",
              "type": "string"
          },
          "endTime": {
              "format": "date-time",
              "description": "If you're still in it but it \"ended\" (like when folks are dancing around the loot after they beat a boss), this is when the activity ended.",
              "type": "string"
          },
          "score": {
              "format": "float",
              "description": "This is what our non-authoritative source thought the score was.",
              "type": "number"
          },
          "highestOpposingFactionScore": {
              "format": "float",
              "description": "If you have human opponents, this is the highest opposing team's score.",
              "type": "number"
          },
          "numberOfOpponents": {
              "format": "int32",
              "description": "This is how many human or poorly crafted aimbot opponents you have.",
              "type": "integer"
          },
          "numberOfPlayers": {
              "format": "int32",
              "description": "This is how many human or poorly crafted aimbots are on your team.",
              "type": "integer"
          }
      }
  }
}
```
