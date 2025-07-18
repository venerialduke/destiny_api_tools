# Interpolation.InterpolationPointFloat

## Entity Information
- **Entity Name**: Interpolation.InterpolationPointFloat
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for interpolationpointfloat operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| value | number (float) |  | No |
| weight | number (float) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Interpolation.InterpolationPointFloat object
const example = {
  value: 123.45,
  weight: 123.45,
};
```

### Python
```python
# Example Interpolation.InterpolationPointFloat object
example = {
    "value": 123.45,
    "weight": 123.45,
}
```

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Interpolation.InterpolationPointFloat":   {
      "type": "object",
      "properties": {
          "value": {
              "format": "float",
              "type": "number"
          },
          "weight": {
              "format": "float",
              "type": "number"
          }
      }
  }
}
```
