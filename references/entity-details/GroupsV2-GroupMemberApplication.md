# GroupsV2.GroupMemberApplication

## Entity Information
- **Entity Name**: GroupsV2.GroupMemberApplication
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for groupmemberapplication operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| groupId | integer (int64) |  | No |
| creationDate | string (date-time) |  | No |
| resolveState | integer (int32) |  | No |
| resolveDate | string (date-time) |  | No |
| resolvedByMembershipId | integer (int64) |  | No |
| requestMessage | string |  | No |
| resolveMessage | string |  | No |
| destinyUserInfo | GroupsV2.GroupUserInfoCard |  | No |
| bungieNetUserInfo | User.UserInfoCard |  | No |

## Usage Examples

### JavaScript
```javascript
// Example GroupsV2.GroupMemberApplication object
const example = {
  groupId: 123,
  creationDate: "example value",
  resolveState: 123,
  resolveDate: "example value",
  resolvedByMembershipId: 123,
  // ... more properties
};
```

### Python
```python
# Example GroupsV2.GroupMemberApplication object
example = {
    "groupId": 123,
    "creationDate": "example value",
    "resolveState": 123,
    "resolveDate": "example value",
    "resolvedByMembershipId": 123,
    # ... more properties
}
```

## Related Entities
- **GroupsV2.GroupApplicationResolveState**: Referenced in this entity
- **GroupsV2.GroupUserInfoCard**: Referenced in this entity
- **User.UserInfoCard**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "GroupsV2.GroupMemberApplication":   {
      "type": "object",
      "properties": {
          "groupId": {
              "format": "int64",
              "type": "integer"
          },
          "creationDate": {
              "format": "date-time",
              "type": "string"
          },
          "resolveState": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/GroupsV2.GroupApplicationResolveState"
              }
          },
          "resolveDate": {
              "format": "date-time",
              "type": "string"
          },
          "resolvedByMembershipId": {
              "format": "int64",
              "type": "integer"
          },
          "requestMessage": {
              "type": "string"
          },
          "resolveMessage": {
              "type": "string"
          },
          "destinyUserInfo": {
              "$ref": "#/definitions/GroupsV2.GroupUserInfoCard"
          },
          "bungieNetUserInfo": {
              "$ref": "#/definitions/User.UserInfoCard"
          }
      }
  }
}
```
