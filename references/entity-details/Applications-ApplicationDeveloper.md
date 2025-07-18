# Applications.ApplicationDeveloper

## Entity Information
- **Entity Name**: Applications.ApplicationDeveloper
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for applicationdeveloper operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| role | integer (int32) |  | No |
| apiEulaVersion | integer (int32) |  | No |
| user | User.UserInfoCard |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Applications.ApplicationDeveloper object
const example = {
  role: 123,
  apiEulaVersion: 123,
  user: null,
};
```

### Python
```python
# Example Applications.ApplicationDeveloper object
example = {
    "role": 123,
    "apiEulaVersion": 123,
    "user": None,
}
```

## Related Entities
- **Applications.DeveloperRole**: Referenced in this entity
- **User.UserInfoCard**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Applications.ApplicationDeveloper":   {
      "type": "object",
      "properties": {
          "role": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Applications.DeveloperRole"
              }
          },
          "apiEulaVersion": {
              "format": "int32",
              "type": "integer"
          },
          "user": {
              "$ref": "#/definitions/User.UserInfoCard"
          }
      }
  }
}
```
