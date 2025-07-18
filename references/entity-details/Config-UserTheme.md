# Config.UserTheme

## Entity Information
- **Entity Name**: Config.UserTheme
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for usertheme operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| userThemeId | integer (int32) |  | No |
| userThemeName | string |  | No |
| userThemeDescription | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Config.UserTheme object
const example = {
  userThemeId: 123,
  userThemeName: "example value",
  userThemeDescription: "example value",
};
```

### Python
```python
# Example Config.UserTheme object
example = {
    "userThemeId": 123,
    "userThemeName": "example value",
    "userThemeDescription": "example value",
}
```

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Config.UserTheme":   {
      "type": "object",
      "properties": {
          "userThemeId": {
              "format": "int32",
              "type": "integer"
          },
          "userThemeName": {
              "type": "string"
          },
          "userThemeDescription": {
              "type": "string"
          }
      }
  }
}
```
