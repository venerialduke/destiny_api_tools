# User.EmailViewDefinition

## Entity Information
- **Entity Name**: User.EmailViewDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Represents a data-driven view for Email settings. Web/Mobile UI can use this data to show new EMail settings consistently without further manual work.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| name | string | The identifier for this view. | No |
| viewSettings | Array[User.EmailViewDefinitionSetting] | The ordered list of settings to show in this view. | No |

## Usage Examples

### JavaScript
```javascript
// Example User.EmailViewDefinition object
const example = {
  name: "example value",
  viewSettings: [],
};
```

### Python
```python
# Example User.EmailViewDefinition object
example = {
    "name": "example value",
    "viewSettings": [],
}
```

## Related Entities
- **User.EmailViewDefinitionSetting**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "User.EmailViewDefinition":   {
      "description": "Represents a data-driven view for Email settings. Web/Mobile UI can use this data to show new EMail settings consistently without further manual work.",
      "type": "object",
      "properties": {
          "name": {
              "description": "The identifier for this view.",
              "type": "string"
          },
          "viewSettings": {
              "description": "The ordered list of settings to show in this view.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/User.EmailViewDefinitionSetting"
              }
          }
      }
  }
}
```
