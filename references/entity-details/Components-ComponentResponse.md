# Components.ComponentResponse

## Entity Information
- **Entity Name**: Components.ComponentResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The base class for any component-returning object that may need to indicate information about the state of the component being returned.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| privacy | integer (int32) |  | No |
| disabled | boolean | If true, this component is disabled. | No |

## Usage Examples

### JavaScript
```javascript
// Example Components.ComponentResponse object
const example = {
  privacy: 123,
  disabled: true,
};
```

### Python
```python
# Example Components.ComponentResponse object
example = {
    "privacy": 123,
    "disabled": True,
}
```

## Related Entities
- **Components.ComponentPrivacySetting**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Components.ComponentResponse":   {
      "description": "The base class for any component-returning object that may need to indicate information about the state of the component being returned.",
      "type": "object",
      "properties": {
          "privacy": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Components.ComponentPrivacySetting"
              }
          },
          "disabled": {
              "description": "If true, this component is disabled.",
              "type": "boolean"
          }
      }
  }
}
```
