# Destiny.Components.Records.DestinyRecordComponent

## Entity Information
- **Entity Name**: Destiny.Components.Records.DestinyRecordComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyrecordcomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| state | integer (int32) |  | No |
| objectives | Array[Destiny.Quests.DestinyObjectiveProgress] |  | No |
| intervalObjectives | Array[Destiny.Quests.DestinyObjectiveProgress] |  | No |
| intervalsRedeemedCount | integer (int32) |  | No |
| completedCount | integer (int32) | If available, this is the number of times this record has been completed. For example, the number of times a seal title has been gilded. | No |
| rewardVisibilty | Array[boolean] | If available, a list that describes which reward rewards should be shown (true) or hidden (false). This property is for regular record rewards, and not for interval objective rewards. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Records.DestinyRecordComponent object
const example = {
  state: 123,
  objectives: [],
  intervalObjectives: [],
  intervalsRedeemedCount: 123,
  completedCount: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Components.Records.DestinyRecordComponent object
example = {
    "state": 123,
    "objectives": [],
    "intervalObjectives": [],
    "intervalsRedeemedCount": 123,
    "completedCount": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.DestinyRecordState**: Referenced in this entity
- **Destiny.Quests.DestinyObjectiveProgress**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Records.DestinyRecordComponent":   {
      "type": "object",
      "properties": {
          "state": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyRecordState"
              }
          },
          "objectives": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Quests.DestinyObjectiveProgress"
              }
          },
          "intervalObjectives": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Quests.DestinyObjectiveProgress"
              }
          },
          "intervalsRedeemedCount": {
              "format": "int32",
              "type": "integer"
          },
          "completedCount": {
              "format": "int32",
              "description": "If available, this is the number of times this record has been completed. For example, the number of times a seal title has been gilded.",
              "type": "integer"
          },
          "rewardVisibilty": {
              "description": "If available, a list that describes which reward rewards should be shown (true) or hidden (false). This property is for regular record rewards, and not for interval objective rewards.",
              "type": "array",
              "items": {
                  "type": "boolean"
              }
          }
      }
  }
}
```
