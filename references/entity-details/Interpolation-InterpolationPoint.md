# Interpolation.InterpolationPoint

## Entity Information
- **Entity Name**: Interpolation.InterpolationPoint
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for interpolationpoint operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| value | integer (int32) |  | No |
| weight | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Interpolation.InterpolationPoint object
const example = {
  value: 123,
  weight: 123,
};
```

### Python
```python
# Example Interpolation.InterpolationPoint object
example = {
    "value": 123,
    "weight": 123,
}
```

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Interpolation.InterpolationPoint":   {
      "type": "object",
      "properties": {
          "value": {
              "format": "int32",
              "type": "integer"
          },
          "weight": {
              "format": "int32",
              "type": "integer"
          }
      }
  }
}
```
