# Destiny.Definitions.Records.DestinyRecordIntervalObjective

## Entity Information
- **Entity Name**: Destiny.Definitions.Records.DestinyRecordIntervalObjective
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyrecordintervalobjective data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| intervalObjectiveHash | integer (uint32) |  | No |
| intervalScoreValue | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Records.DestinyRecordIntervalObjective object
const example = {
  intervalObjectiveHash: 123,
  intervalScoreValue: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Records.DestinyRecordIntervalObjective object
example = {
    "intervalObjectiveHash": 123,
    "intervalScoreValue": 123,
}
```

## Related Entities
- **Destiny.Definitions.DestinyObjectiveDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Records.DestinyRecordIntervalObjective":   {
      "type": "object",
      "properties": {
          "intervalObjectiveHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyObjectiveDefinition"
              }
          },
          "intervalScoreValue": {
              "format": "int32",
              "type": "integer"
          }
      }
  }
}
```
