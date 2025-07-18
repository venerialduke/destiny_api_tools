# User.UserSearchResponseDetail

## Entity Information
- **Entity Name**: User.UserSearchResponseDetail
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for usersearchresponsedetail operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| bungieGlobalDisplayName | string |  | No |
| bungieGlobalDisplayNameCode | integer (int16) |  | No |
| bungieNetMembershipId | integer (int64) |  | No |
| destinyMemberships | Array[User.UserInfoCard] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example User.UserSearchResponseDetail object
const example = {
  bungieGlobalDisplayName: "example value",
  bungieGlobalDisplayNameCode: 123,
  bungieNetMembershipId: 123,
  destinyMemberships: [],
};
```

### Python
```python
# Example User.UserSearchResponseDetail object
example = {
    "bungieGlobalDisplayName": "example value",
    "bungieGlobalDisplayNameCode": 123,
    "bungieNetMembershipId": 123,
    "destinyMemberships": [],
}
```

## Related Entities
- **User.UserInfoCard**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "User.UserSearchResponseDetail":   {
      "type": "object",
      "properties": {
          "bungieGlobalDisplayName": {
              "type": "string"
          },
          "bungieGlobalDisplayNameCode": {
              "format": "int16",
              "type": "integer"
          },
          "bungieNetMembershipId": {
              "format": "int64",
              "type": "integer"
          },
          "destinyMemberships": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/User.UserInfoCard"
              }
          }
      }
  }
}
```
