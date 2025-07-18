# User.EMailSettingLocalization

## Entity Information
- **Entity Name**: User.EMailSettingLocalization
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Localized text relevant to a given EMail setting in a given localization.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| title | string |  | No |
| description | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example User.EMailSettingLocalization object
const example = {
  title: "example value",
  description: "example value",
};
```

### Python
```python
# Example User.EMailSettingLocalization object
example = {
    "title": "example value",
    "description": "example value",
}
```

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "User.EMailSettingLocalization":   {
      "description": "Localized text relevant to a given EMail setting in a given localization.",
      "type": "object",
      "properties": {
          "title": {
              "type": "string"
          },
          "description": {
              "type": "string"
          }
      }
  }
}
```
