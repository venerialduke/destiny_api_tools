# GroupsV2.GroupPotentialMember

## Entity Information
- **Entity Name**: GroupsV2.GroupPotentialMember
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for grouppotentialmember operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| potentialStatus | integer (int32) |  | No |
| groupId | integer (int64) |  | No |
| destinyUserInfo | GroupsV2.GroupUserInfoCard |  | No |
| bungieNetUserInfo | User.UserInfoCard |  | No |
| joinDate | string (date-time) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example GroupsV2.GroupPotentialMember object
const example = {
  potentialStatus: 123,
  groupId: 123,
  destinyUserInfo: null,
  bungieNetUserInfo: null,
  joinDate: "example value",
};
```

### Python
```python
# Example GroupsV2.GroupPotentialMember object
example = {
    "potentialStatus": 123,
    "groupId": 123,
    "destinyUserInfo": None,
    "bungieNetUserInfo": None,
    "joinDate": "example value",
}
```

## Related Entities
- **GroupsV2.GroupPotentialMemberStatus**: Referenced in this entity
- **GroupsV2.GroupUserInfoCard**: Referenced in this entity
- **User.UserInfoCard**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "GroupsV2.GroupPotentialMember":   {
      "type": "object",
      "properties": {
          "potentialStatus": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/GroupsV2.GroupPotentialMemberStatus"
              }
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
