# User.UserToUserContext

## Entity Information
- **Entity Name**: User.UserToUserContext
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for usertousercontext operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| isFollowing | boolean |  | No |
| ignoreStatus | Ignores.IgnoreResponse |  | No |
| globalIgnoreEndDate | string (date-time) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example User.UserToUserContext object
const example = {
  isFollowing: true,
  ignoreStatus: null,
  globalIgnoreEndDate: "example value",
};
```

### Python
```python
# Example User.UserToUserContext object
example = {
    "isFollowing": True,
    "ignoreStatus": None,
    "globalIgnoreEndDate": "example value",
}
```

## Related Entities
- **Ignores.IgnoreResponse**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "User.UserToUserContext":   {
      "type": "object",
      "properties": {
          "isFollowing": {
              "type": "boolean"
          },
          "ignoreStatus": {
              "$ref": "#/definitions/Ignores.IgnoreResponse"
          },
          "globalIgnoreEndDate": {
              "format": "date-time",
              "type": "string"
          }
      }
  }
}
```
