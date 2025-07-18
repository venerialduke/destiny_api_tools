# GroupsV2.GroupBanRequest

## Entity Information
- **Entity Name**: GroupsV2.GroupBanRequest
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for groupbanrequest operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| comment | string |  | No |
| length | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example GroupsV2.GroupBanRequest object
const example = {
  comment: "example value",
  length: 123,
};
```

### Python
```python
# Example GroupsV2.GroupBanRequest object
example = {
    "comment": "example value",
    "length": 123,
}
```

## Related Entities
- **Ignores.IgnoreLength**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "GroupsV2.GroupBanRequest":   {
      "type": "object",
      "properties": {
          "comment": {
              "type": "string"
          },
          "length": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Ignores.IgnoreLength"
              }
          }
      }
  }
}
```
