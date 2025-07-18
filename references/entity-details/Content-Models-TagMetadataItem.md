# Content.Models.TagMetadataItem

## Entity Information
- **Entity Name**: Content.Models.TagMetadataItem
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for tagmetadataitem operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| description | string |  | No |
| tagText | string |  | No |
| groups | Array[string] |  | No |
| isDefault | boolean |  | No |
| name | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Content.Models.TagMetadataItem object
const example = {
  description: "example value",
  tagText: "example value",
  groups: [],
  isDefault: true,
  name: "example value",
};
```

### Python
```python
# Example Content.Models.TagMetadataItem object
example = {
    "description": "example value",
    "tagText": "example value",
    "groups": [],
    "isDefault": True,
    "name": "example value",
}
```

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Content.Models.TagMetadataItem":   {
      "type": "object",
      "properties": {
          "description": {
              "type": "string"
          },
          "tagText": {
              "type": "string"
          },
          "groups": {
              "type": "array",
              "items": {
                  "type": "string"
              }
          },
          "isDefault": {
              "type": "boolean"
          },
          "name": {
              "type": "string"
          }
      }
  }
}
```
