# GroupsV2.GroupApplicationResponse

## Entity Information
- **Entity Name**: GroupsV2.GroupApplicationResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for groupapplicationresponse operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| resolution | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example GroupsV2.GroupApplicationResponse object
const example = {
  resolution: 123,
};
```

### Python
```python
# Example GroupsV2.GroupApplicationResponse object
example = {
    "resolution": 123,
}
```

## Related Entities
- **GroupsV2.GroupApplicationResolveState**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "GroupsV2.GroupApplicationResponse":   {
      "type": "object",
      "properties": {
          "resolution": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/GroupsV2.GroupApplicationResolveState"
              }
          }
      }
  }
}
```
