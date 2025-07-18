# Ignores.IgnoreResponse

## Entity Information
- **Entity Name**: Ignores.IgnoreResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for ignoreresponse operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| isIgnored | boolean |  | No |
| ignoreFlags | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Ignores.IgnoreResponse object
const example = {
  isIgnored: true,
  ignoreFlags: 123,
};
```

### Python
```python
# Example Ignores.IgnoreResponse object
example = {
    "isIgnored": True,
    "ignoreFlags": 123,
}
```

## Related Entities
- **Ignores.IgnoreStatus**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Ignores.IgnoreResponse":   {
      "type": "object",
      "properties": {
          "isIgnored": {
              "type": "boolean"
          },
          "ignoreFlags": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Ignores.IgnoreStatus"
              }
          }
      }
  }
}
```
