# GroupsV2.GroupMember

## Entity Information
- **Entity Name**: GroupsV2.GroupMember
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for groupmember operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| memberType | integer (int32) |  | No |
| isOnline | boolean |  | No |
| lastOnlineStatusChange | integer (int64) |  | No |
| groupId | integer (int64) |  | No |
| destinyUserInfo | GroupsV2.GroupUserInfoCard |  | No |
| bungieNetUserInfo | User.UserInfoCard |  | No |
| joinDate | string (date-time) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example GroupsV2.GroupMember object
const example = {
  memberType: 123,
  isOnline: true,
  lastOnlineStatusChange: 123,
  groupId: 123,
  destinyUserInfo: null,
  // ... more properties
};
```

### Python
```python
# Example GroupsV2.GroupMember object
example = {
    "memberType": 123,
    "isOnline": True,
    "lastOnlineStatusChange": 123,
    "groupId": 123,
    "destinyUserInfo": None,
    # ... more properties
}
```

## Related Entities
- **GroupsV2.GroupUserInfoCard**: Referenced in this entity
- **GroupsV2.RuntimeGroupMemberType**: Referenced in this entity
- **User.UserInfoCard**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "GroupsV2.GroupMember":   {
      "type": "object",
      "properties": {
          "memberType": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/GroupsV2.RuntimeGroupMemberType"
              }
          },
          "isOnline": {
              "type": "boolean"
          },
          "lastOnlineStatusChange": {
              "format": "int64",
              "type": "integer"
          },
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
