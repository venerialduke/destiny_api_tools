# Content.Models.ContentPreview

## Entity Information
- **Entity Name**: Content.Models.ContentPreview
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for contentpreview operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| name | string |  | No |
| path | string |  | No |
| itemInSet | boolean |  | No |
| setTag | string |  | No |
| setNesting | integer (int32) |  | No |
| useSetId | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Content.Models.ContentPreview object
const example = {
  name: "example value",
  path: "example value",
  itemInSet: true,
  setTag: "example value",
  setNesting: 123,
  // ... more properties
};
```

### Python
```python
# Example Content.Models.ContentPreview object
example = {
    "name": "example value",
    "path": "example value",
    "itemInSet": True,
    "setTag": "example value",
    "setNesting": 123,
    # ... more properties
}
```

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Content.Models.ContentPreview":   {
      "type": "object",
      "properties": {
          "name": {
              "type": "string"
          },
          "path": {
              "type": "string"
          },
          "itemInSet": {
              "type": "boolean"
          },
          "setTag": {
              "type": "string"
          },
          "setNesting": {
              "format": "int32",
              "type": "integer"
          },
          "useSetId": {
              "format": "int32",
              "type": "integer"
          }
      }
  }
}
```
