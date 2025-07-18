# GroupsV2.GroupUserBase

## Entity Information
- **Entity Name**: GroupsV2.GroupUserBase
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for groupuserbase operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| groupId | integer (int64) |  | No |
| destinyUserInfo | GroupsV2.GroupUserInfoCard |  | No |
| bungieNetUserInfo | User.UserInfoCard |  | No |
| joinDate | string (date-time) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example GroupsV2.GroupUserBase object
const example = {
  groupId: 123,
  destinyUserInfo: null,
  bungieNetUserInfo: null,
  joinDate: "example value",
};
```

### Python
```python
# Example GroupsV2.GroupUserBase object
example = {
    "groupId": 123,
    "destinyUserInfo": None,
    "bungieNetUserInfo": None,
    "joinDate": "example value",
}
```

## Related Entities
- **GroupsV2.GroupUserInfoCard**: Referenced in this entity
- **User.UserInfoCard**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "GroupsV2.GroupUserBase":   {
      "type": "object",
      "properties": {
          "groupId": {
              "format": "int64",
              "type": "integer"
          },
          "destinyUserInfo": {
              "$ref": "#/definitions/GroupsV2.GroupUserInfoCard"
          },
          "bungieNetUserInfo": {
              "$ref": "#/definitions/User.UserInfoCard"
          },
          "joinDate": {
              "format": "date-time",
              "type": "string"
          }
      }
  }
}
```
