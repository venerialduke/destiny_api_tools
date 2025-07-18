# Tags.Models.Contracts.TagResponse

## Entity Information
- **Entity Name**: Tags.Models.Contracts.TagResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for tagresponse operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| tagText | string |  | No |
| ignoreStatus | Ignores.IgnoreResponse |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Tags.Models.Contracts.TagResponse object
const example = {
  tagText: "example value",
  ignoreStatus: null,
};
```

### Python
```python
# Example Tags.Models.Contracts.TagResponse object
example = {
    "tagText": "example value",
    "ignoreStatus": None,
}
```

## Related Entities
- **Ignores.IgnoreResponse**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Tags.Models.Contracts.TagResponse":   {
      "type": "object",
      "properties": {
          "tagText": {
              "type": "string"
          },
          "ignoreStatus": {
              "$ref": "#/definitions/Ignores.IgnoreResponse"
          }
      }
  }
}
```
