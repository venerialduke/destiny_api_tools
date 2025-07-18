# Config.GroupTheme

## Entity Information
- **Entity Name**: Config.GroupTheme
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for grouptheme operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| name | string |  | No |
| folder | string |  | No |
| description | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Config.GroupTheme object
const example = {
  name: "example value",
  folder: "example value",
  description: "example value",
};
```

### Python
```python
# Example Config.GroupTheme object
example = {
    "name": "example value",
    "folder": "example value",
    "description": "example value",
}
```

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Config.GroupTheme":   {
      "type": "object",
      "properties": {
          "name": {
              "type": "string"
          },
          "folder": {
              "type": "string"
          },
          "description": {
              "type": "string"
          }
      }
  }
}
```
