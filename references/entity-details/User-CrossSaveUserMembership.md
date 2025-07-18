# User.CrossSaveUserMembership

## Entity Information
- **Entity Name**: User.CrossSaveUserMembership
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Very basic info about a user as returned by the Account server, but including CrossSave information. Do NOT use as a request contract.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| crossSaveOverride | integer (int32) | If there is a cross save override in effect, this value will tell you the type that is overridding this one. | No |
| applicableMembershipTypes | Array[integer] | The list of Membership Types indicating the platforms on which this Membership can be used.
 Not in Cross Save = its original membership type. Cross Save Primary = Any membership types it is overridding, and its original membership type Cross Save Overridden = Empty list | No |
| isPublic | boolean | If True, this is a public user membership. | No |
| membershipType | integer (int32) | Type of the membership. Not necessarily the native type. | No |
| membershipId | integer (int64) | Membership ID as they user is known in the Accounts service | No |
| displayName | string | Display Name the player has chosen for themselves. The display name is optional when the data type is used as input to a platform API. | No |
| bungieGlobalDisplayName | string | The bungie global display name, if set. | No |
| bungieGlobalDisplayNameCode | integer (int16) | The bungie global display name code, if set. | No |

## Usage Examples

### JavaScript
```javascript
// Example User.CrossSaveUserMembership object
const example = {
  crossSaveOverride: 123,
  applicableMembershipTypes: [],
  isPublic: true,
  membershipType: 123,
  membershipId: 123,
  // ... more properties
};
```

### Python
```python
# Example User.CrossSaveUserMembership object
example = {
    "crossSaveOverride": 123,
    "applicableMembershipTypes": [],
    "isPublic": True,
    "membershipType": 123,
    "membershipId": 123,
    # ... more properties
}
```

## Related Entities
- **BungieMembershipType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "User.CrossSaveUserMembership":   {
      "description": "Very basic info about a user as returned by the Account server, but including CrossSave information. Do NOT use as a request contract.",
      "type": "object",
      "properties": {
          "crossSaveOverride": {
              "format": "int32",
              "description": "If there is a cross save override in effect, this value will tell you the type that is overridding this one.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/BungieMembershipType"
              }
          },
          "applicableMembershipTypes": {
              "description": "The list of Membership Types indicating the platforms on which this Membership can be used.\r\n Not in Cross Save = its original membership type. Cross Save Primary = Any membership types it is overridding, and its original membership type Cross Save Overridden = Empty list",
              "type": "array",
              "items": {
                  "format": "int32",
                  "description": "The types of membership the Accounts system supports. This is the external facing enum used in place of the internal-only Bungie.SharedDefinitions.MembershipType.",
                  "type": "integer",
                  "x-enum-reference": {
                      "$ref": "#/components/schemas/BungieMembershipType"
                  }
              }
          },
          "isPublic": {
              "description": "If True, this is a public user membership.",
              "type": "boolean"
          },
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
