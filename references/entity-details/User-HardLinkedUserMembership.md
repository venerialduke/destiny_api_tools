# User.HardLinkedUserMembership

## Entity Information
- **Entity Name**: User.HardLinkedUserMembership
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for hardlinkedusermembership operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| membershipType | integer (int32) |  | No |
| membershipId | integer (int64) |  | No |
| CrossSaveOverriddenType | integer (int32) |  | No |
| CrossSaveOverriddenMembershipId | integer (int64) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example User.HardLinkedUserMembership object
const example = {
  membershipType: 123,
  membershipId: 123,
  CrossSaveOverriddenType: 123,
  CrossSaveOverriddenMembershipId: 123,
};
```

### Python
```python
# Example User.HardLinkedUserMembership object
example = {
    "membershipType": 123,
    "membershipId": 123,
    "CrossSaveOverriddenType": 123,
    "CrossSaveOverriddenMembershipId": 123,
}
```

## Related Entities
- **BungieMembershipType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "User.HardLinkedUserMembership":   {
      "type": "object",
      "properties": {
          "membershipType": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/BungieMembershipType"
              }
          },
          "membershipId": {
              "format": "int64",
              "type": "integer"
          },
          "CrossSaveOverriddenType": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/BungieMembershipType"
              }
          },
          "CrossSaveOverriddenMembershipId": {
              "format": "int64",
              "type": "integer"
          }
      }
  }
}
```
