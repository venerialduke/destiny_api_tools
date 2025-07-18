# Common.Models.CoreSetting

## Entity Information
- **Entity Name**: Common.Models.CoreSetting
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for coresetting operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| identifier | string |  | No |
| isDefault | boolean |  | No |
| displayName | string |  | No |
| summary | string |  | No |
| imagePath | string |  | No |
| childSettings | Array[Common.Models.CoreSetting] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Common.Models.CoreSetting object
const example = {
  identifier: "example value",
  isDefault: true,
  displayName: "example value",
  summary: "example value",
  imagePath: "example value",
  // ... more properties
};
```

### Python
```python
# Example Common.Models.CoreSetting object
example = {
    "identifier": "example value",
    "isDefault": True,
    "displayName": "example value",
    "summary": "example value",
    "imagePath": "example value",
    # ... more properties
}
```

## Related Entities
- **Common.Models.CoreSetting**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Common.Models.CoreSetting":   {
      "type": "object",
      "properties": {
          "identifier": {
              "type": "string"
          },
          "isDefault": {
              "type": "boolean"
          },
          "displayName": {
              "type": "string"
          },
          "summary": {
              "type": "string"
          },
          "imagePath": {
              "type": "string"
          },
          "childSettings": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Common.Models.CoreSetting"
              }
          }
      }
  }
}
```
