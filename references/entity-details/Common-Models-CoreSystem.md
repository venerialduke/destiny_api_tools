# Common.Models.CoreSystem

## Entity Information
- **Entity Name**: Common.Models.CoreSystem
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for coresystem operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| enabled | boolean |  | No |
| parameters | object |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Common.Models.CoreSystem object
const example = {
  enabled: true,
  parameters: null,
};
```

### Python
```python
# Example Common.Models.CoreSystem object
example = {
    "enabled": True,
    "parameters": None,
}
```

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Common.Models.CoreSystem":   {
      "type": "object",
      "properties": {
          "enabled": {
              "type": "boolean"
          },
          "parameters": {
              "type": "object",
              "additionalProperties": {
                  "type": "string"
              }
          }
      }
  }
}
```
