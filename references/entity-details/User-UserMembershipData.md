# User.UserMembershipData

## Entity Information
- **Entity Name**: User.UserMembershipData
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for usermembershipdata operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| destinyMemberships | Array[GroupsV2.GroupUserInfoCard] | this allows you to see destiny memberships that are visible and linked to this account (regardless of whether or not they have characters on the world server) | No |
| primaryMembershipId | integer (int64) | If this property is populated, it will have the membership ID of the account considered to be "primary" in this user's cross save relationship.
 If null, this user has no cross save relationship, nor primary account. | No |
| marathonMembershipId | integer (int64) | If this property is populated, it will have the membershipId for the Marathon Membership on this user's account
 If null, this user has no Marathon (i.e. "GoliathGame") membership. | No |
| bungieNetUser | User.GeneralUser |  | No |

## Usage Examples

### JavaScript
```javascript
// Example User.UserMembershipData object
const example = {
  destinyMemberships: [],
  primaryMembershipId: 123,
  marathonMembershipId: 123,
  bungieNetUser: null,
};
```

### Python
```python
# Example User.UserMembershipData object
example = {
    "destinyMemberships": [],
    "primaryMembershipId": 123,
    "marathonMembershipId": 123,
    "bungieNetUser": None,
}
```

## Related Entities
- **GroupsV2.GroupUserInfoCard**: Referenced in this entity
- **User.GeneralUser**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "User.UserMembershipData":   {
      "type": "object",
      "properties": {
          "destinyMemberships": {
              "description": "this allows you to see destiny memberships that are visible and linked to this account (regardless of whether or not they have characters on the world server)",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/GroupsV2.GroupUserInfoCard"
              }
          },
          "primaryMembershipId": {
              "format": "int64",
              "description": "If this property is populated, it will have the membership ID of the account considered to be \"primary\" in this user's cross save relationship.\r\n If null, this user has no cross save relationship, nor primary account.",
              "type": "integer"
          },
          "marathonMembershipId": {
              "format": "int64",
              "description": "If this property is populated, it will have the membershipId for the Marathon Membership on this user's account\r\n If null, this user has no Marathon (i.e. \"GoliathGame\") membership.",
              "type": "integer"
          },
          "bungieNetUser": {
              "$ref": "#/definitions/User.GeneralUser"
          }
      }
  }
}
```
