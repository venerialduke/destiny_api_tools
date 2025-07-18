# Destiny.Config.ImagePyramidEntry

## Entity Information
- **Entity Name**: Destiny.Config.ImagePyramidEntry
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing imagepyramidentry data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| name | string | The name of the subfolder where these images are located. | No |
| factor | number (float) | The factor by which the original image size has been reduced. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Config.ImagePyramidEntry object
const example = {
  name: "example value",
  factor: 123.45,
};
```

### Python
```python
# Example Destiny.Config.ImagePyramidEntry object
example = {
    "name": "example value",
    "factor": 123.45,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Config.ImagePyramidEntry":   {
      "type": "object",
      "properties": {
          "name": {
              "description": "The name of the subfolder where these images are located.",
              "type": "string"
          },
          "factor": {
              "format": "float",
              "description": "The factor by which the original image size has been reduced.",
              "type": "number"
          }
      }
  }
}
```
