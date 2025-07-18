# Content.Models.TagMetadataDefinition

## Entity Information
- **Entity Name**: Content.Models.TagMetadataDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for tagmetadatadefinition operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| description | string |  | No |
| order | integer (int32) |  | No |
| items | Array[Content.Models.TagMetadataItem] |  | No |
| datatype | string |  | No |
| name | string |  | No |
| isRequired | boolean |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Content.Models.TagMetadataDefinition object
const example = {
  description: "example value",
  order: 123,
  items: [],
  datatype: "example value",
  name: "example value",
  // ... more properties
};
```

### Python
```python
# Example Content.Models.TagMetadataDefinition object
example = {
    "description": "example value",
    "order": 123,
    "items": [],
    "datatype": "example value",
    "name": "example value",
    # ... more properties
}
```

## Related Entities
- **Content.Models.TagMetadataItem**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Content.Models.TagMetadataDefinition":   {
      "type": "object",
      "properties": {
          "description": {
              "type": "string"
          },
          "order": {
              "format": "int32",
              "type": "integer"
          },
          "items": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Content.Models.TagMetadataItem"
              }
          },
          "datatype": {
              "type": "string"
          },
          "name": {
              "type": "string"
          },
          "isRequired": {
              "type": "boolean"
          }
      }
  }
}
```
