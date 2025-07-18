# Content.Models.ContentTypeDefaultValue

## Entity Information
- **Entity Name**: Content.Models.ContentTypeDefaultValue
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for contenttypedefaultvalue operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| whenClause | string |  | No |
| whenValue | string |  | No |
| defaultValue | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Content.Models.ContentTypeDefaultValue object
const example = {
  whenClause: "example value",
  whenValue: "example value",
  defaultValue: "example value",
};
```

### Python
```python
# Example Content.Models.ContentTypeDefaultValue object
example = {
    "whenClause": "example value",
    "whenValue": "example value",
    "defaultValue": "example value",
}
```

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Content.Models.ContentTypeDefaultValue":   {
      "type": "object",
      "properties": {
          "whenClause": {
              "type": "string"
          },
          "whenValue": {
              "type": "string"
          },
          "defaultValue": {
              "type": "string"
          }
      }
  }
}
```
