# User.UserMembership

## Entity Information
- **Entity Name**: User.UserMembership
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Very basic info about a user as returned by the Account server.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| membershipType | integer (int32) | Type of the membership. Not necessarily the native type. | No |
| membershipId | integer (int64) | Membership ID as they user is known in the Accounts service | No |
| displayName | string | Display Name the player has chosen for themselves. The display name is optional when the data type is used as input to a platform API. | No |
| bungieGlobalDisplayName | string | The bungie global display name, if set. | No |
| bungieGlobalDisplayNameCode | integer (int16) | The bungie global display name code, if set. | No |

## Usage Examples

### JavaScript
```javascript
// Example User.UserMembership object
const example = {
  membershipType: 123,
  membershipId: 123,
  displayName: "example value",
  bungieGlobalDisplayName: "example value",
  bungieGlobalDisplayNameCode: 123,
};
```

### Python
```python
# Example User.UserMembership object
example = {
    "membershipType": 123,
    "membershipId": 123,
    "displayName": "example value",
    "bungieGlobalDisplayName": "example value",
    "bungieGlobalDisplayNameCode": 123,
}
```

## Related Entities
- **BungieMembershipType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "User.UserMembership":   {
      "description": "Very basic info about a user as returned by the Account server.",
      "type": "object",
      "properties": {
          "membershipType": {
              "format": "int32",
              "description": "Type of the membership. Not necessarily the native type.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/BungieMembershipType"
              }
          },
          "membershipId": {
              "format": "int64",
              "description": "Membership ID as they user is known in the Accounts service",
              "type": "integer"
          },
          "displayName": {
              "description": "Display Name the player has chosen for themselves. The display name is optional when the data type is used as input to a platform API.",
              "type": "string"
          },
          "bungieGlobalDisplayName": {
              "description": "The bungie global display name, if set.",
              "type": "string"
          },
          "bungieGlobalDisplayNameCode": {
              "format": "int16",
              "description": "The bungie global display name code, if set.",
              "type": "integer"
          }
      }
  }
}
```
