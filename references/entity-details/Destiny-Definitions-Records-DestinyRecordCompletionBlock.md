# Destiny.Definitions.Records.DestinyRecordCompletionBlock

## Entity Information
- **Entity Name**: Destiny.Definitions.Records.DestinyRecordCompletionBlock
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyrecordcompletionblock data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| partialCompletionObjectiveCountThreshold | integer (int32) | The number of objectives that must be completed before the objective is considered "complete" | No |
| ScoreValue | integer (int32) |  | No |
| shouldFireToast | boolean |  | No |
| toastStyle | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Records.DestinyRecordCompletionBlock object
const example = {
  partialCompletionObjectiveCountThreshold: 123,
  ScoreValue: 123,
  shouldFireToast: true,
  toastStyle: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Records.DestinyRecordCompletionBlock object
example = {
    "partialCompletionObjectiveCountThreshold": 123,
    "ScoreValue": 123,
    "shouldFireToast": True,
    "toastStyle": 123,
}
```

## Related Entities
- **Destiny.DestinyRecordToastStyle**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Records.DestinyRecordCompletionBlock":   {
      "type": "object",
      "properties": {
          "partialCompletionObjectiveCountThreshold": {
              "format": "int32",
              "description": "The number of objectives that must be completed before the objective is considered \"complete\"",
              "type": "integer"
          },
          "ScoreValue": {
              "format": "int32",
              "type": "integer"
          },
          "shouldFireToast": {
              "type": "boolean"
          },
          "toastStyle": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyRecordToastStyle"
              }
          }
      }
  }
}
```
