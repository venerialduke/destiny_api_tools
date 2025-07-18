# Destiny.HistoricalStats.DestinyHistoricalStatsActivity

## Entity Information
- **Entity Name**: Destiny.HistoricalStats.DestinyHistoricalStatsActivity
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Summary information about the activity that was played.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| referenceId | integer (uint32) | The unique hash identifier of the DestinyActivityDefinition that was played. If I had this to do over, it'd be named activityHash. Too late now. | No |
| directorActivityHash | integer (uint32) | The unique hash identifier of the DestinyActivityDefinition that was played. | No |
| instanceId | integer (int64) | The unique identifier for this *specific* match that was played.
This value can be used to get additional data about this activity such as who else was playing via the GetPostGameCarnageReport endpoint. | No |
| mode | integer (int32) | Indicates the most specific game mode of the activity that we could find. | No |
| modes | Array[integer] | The list of all Activity Modes to which this activity applies, including aggregates. This will let you see, for example, whether the activity was both Clash and part of the Trials of the Nine event. | No |
| isPrivate | boolean | Whether or not the match was a private match. | No |
| membershipType | integer (int32) | The Membership Type indicating the platform on which this match was played. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.HistoricalStats.DestinyHistoricalStatsActivity object
const example = {
  referenceId: 123,
  directorActivityHash: 123,
  instanceId: 123,
  mode: 123,
  modes: [],
  // ... more properties
};
```

### Python
```python
# Example Destiny.HistoricalStats.DestinyHistoricalStatsActivity object
example = {
    "referenceId": 123,
    "directorActivityHash": 123,
    "instanceId": 123,
    "mode": 123,
    "modes": [],
    # ... more properties
}
```

## Related Entities
- **BungieMembershipType**: Referenced in this entity
- **Destiny.Definitions.DestinyActivityDefinition**: Referenced in this entity
- **Destiny.HistoricalStats.Definitions.DestinyActivityModeType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.HistoricalStats.DestinyHistoricalStatsActivity":   {
      "description": "Summary information about the activity that was played.",
      "type": "object",
      "properties": {
          "referenceId": {
              "format": "uint32",
              "description": "The unique hash identifier of the DestinyActivityDefinition that was played. If I had this to do over, it'd be named activityHash. Too late now.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityDefinition"
              }
          },
          "directorActivityHash": {
              "format": "uint32",
              "description": "The unique hash identifier of the DestinyActivityDefinition that was played.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityDefinition"
              }
          },
          "instanceId": {
              "format": "int64",
              "description": "The unique identifier for this *specific* match that was played.\r\nThis value can be used to get additional data about this activity such as who else was playing via the GetPostGameCarnageReport endpoint.",
              "type": "integer"
          },
          "mode": {
              "format": "int32",
              "description": "Indicates the most specific game mode of the activity that we could find.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.HistoricalStats.Definitions.DestinyActivityModeType"
              }
          },
          "modes": {
              "description": "The list of all Activity Modes to which this activity applies, including aggregates. This will let you see, for example, whether the activity was both Clash and part of the Trials of the Nine event.",
              "type": "array",
              "items": {
                  "format": "int32",
                  "description": "For historical reasons, this list will have both D1 and D2-relevant Activity Modes in it. Please don't take this to mean that some D1-only feature is coming back!",
                  "type": "integer",
                  "x-enum-reference": {
                      "$ref": "#/components/schemas/Destiny.HistoricalStats.Definitions.DestinyActivityModeType"
                  }
              }
          },
          "isPrivate": {
              "description": "Whether or not the match was a private match.",
              "type": "boolean"
          },
          "membershipType": {
              "format": "int32",
              "description": "The Membership Type indicating the platform on which this match was played.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/BungieMembershipType"
              }
          }
      }
  }
}
```
