# Content.ContentRepresentation

## Entity Information
- **Entity Name**: Content.ContentRepresentation
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for contentrepresentation operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| name | string |  | No |
| path | string |  | No |
| validationString | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Content.ContentRepresentation object
const example = {
  name: "example value",
  path: "example value",
  validationString: "example value",
};
```

### Python
```python
# Example Content.ContentRepresentation object
example = {
    "name": "example value",
    "path": "example value",
    "validationString": "example value",
}
```

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Content.ContentRepresentation":   {
      "type": "object",
      "properties": {
          "name": {
              "type": "string"
          },
          "path": {
              "type": "string"
          },
          "validationString": {
              "type": "string"
          }
      }
  }
}
```
