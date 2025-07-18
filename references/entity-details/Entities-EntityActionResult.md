# Entities.EntityActionResult

## Entity Information
- **Entity Name**: Entities.EntityActionResult
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for entityactionresult operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| entityId | integer (int64) |  | No |
| result | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Entities.EntityActionResult object
const example = {
  entityId: 123,
  result: 123,
};
```

### Python
```python
# Example Entities.EntityActionResult object
example = {
    "entityId": 123,
    "result": 123,
}
```

## Related Entities
- **Exceptions.PlatformErrorCodes**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Entities.EntityActionResult":   {
      "type": "object",
      "properties": {
          "entityId": {
              "format": "int64",
              "type": "integer"
          },
          "result": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Exceptions.PlatformErrorCodes"
              }
          }
      }
  }
}
```
