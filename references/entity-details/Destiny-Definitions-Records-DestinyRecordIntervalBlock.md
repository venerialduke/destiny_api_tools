# Destiny.Definitions.Records.DestinyRecordIntervalBlock

## Entity Information
- **Entity Name**: Destiny.Definitions.Records.DestinyRecordIntervalBlock
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyrecordintervalblock data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| intervalObjectives | Array[Destiny.Definitions.Records.DestinyRecordIntervalObjective] |  | No |
| intervalRewards | Array[Destiny.Definitions.Records.DestinyRecordIntervalRewards] |  | No |
| originalObjectiveArrayInsertionIndex | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Records.DestinyRecordIntervalBlock object
const example = {
  intervalObjectives: [],
  intervalRewards: [],
  originalObjectiveArrayInsertionIndex: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Records.DestinyRecordIntervalBlock object
example = {
    "intervalObjectives": [],
    "intervalRewards": [],
    "originalObjectiveArrayInsertionIndex": 123,
}
```

## Related Entities
- **Destiny.Definitions.Records.DestinyRecordIntervalObjective**: Referenced in this entity
- **Destiny.Definitions.Records.DestinyRecordIntervalRewards**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Records.DestinyRecordIntervalBlock":   {
      "type": "object",
      "properties": {
          "intervalObjectives": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Records.DestinyRecordIntervalObjective"
              }
          },
          "intervalRewards": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Records.DestinyRecordIntervalRewards"
              }
          },
          "originalObjectiveArrayInsertionIndex": {
              "format": "int32",
              "type": "integer"
          }
      }
  }
}
```
