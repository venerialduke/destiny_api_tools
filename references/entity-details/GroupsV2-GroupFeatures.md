# GroupsV2.GroupFeatures

## Entity Information
- **Entity Name**: GroupsV2.GroupFeatures
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for groupfeatures operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| maximumMembers | integer (int32) |  | No |
| maximumMembershipsOfGroupType | integer (int32) | Maximum number of groups of this type a typical membership may join. For example, a user may join about 50 General groups with their Bungie.net account. They may join one clan per Destiny membership. | No |
| capabilities | integer (int32) |  | No |
| membershipTypes | Array[integer] |  | No |
| invitePermissionOverride | boolean | Minimum Member Level allowed to invite new members to group
Always Allowed: Founder, Acting Founder
True means admins have this power, false means they don't
Default is false for clans, true for groups. | No |
| updateCulturePermissionOverride | boolean | Minimum Member Level allowed to update group culture
Always Allowed: Founder, Acting Founder
True means admins have this power, false means they don't
Default is false for clans, true for groups. | No |
| hostGuidedGamePermissionOverride | integer (int32) | Minimum Member Level allowed to host guided games
Always Allowed: Founder, Acting Founder, Admin
Allowed Overrides: None, Member, Beginner
Default is Member for clans, None for groups, although this means nothing for groups. | No |
| updateBannerPermissionOverride | boolean | Minimum Member Level allowed to update banner
Always Allowed: Founder, Acting Founder
True means admins have this power, false means they don't
Default is false for clans, true for groups. | No |
| joinLevel | integer (int32) | Level to join a member at when accepting an invite, application, or joining an open clan
Default is Beginner. | No |

## Usage Examples

### JavaScript
```javascript
// Example GroupsV2.GroupFeatures object
const example = {
  maximumMembers: 123,
  maximumMembershipsOfGroupType: 123,
  capabilities: 123,
  membershipTypes: [],
  invitePermissionOverride: true,
  // ... more properties
};
```

### Python
```python
# Example GroupsV2.GroupFeatures object
example = {
    "maximumMembers": 123,
    "maximumMembershipsOfGroupType": 123,
    "capabilities": 123,
    "membershipTypes": [],
    "invitePermissionOverride": True,
    # ... more properties
}
```

## Related Entities
- **BungieMembershipType**: Referenced in this entity
- **GroupsV2.Capabilities**: Referenced in this entity
- **GroupsV2.HostGuidedGamesPermissionLevel**: Referenced in this entity
- **GroupsV2.RuntimeGroupMemberType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "GroupsV2.GroupFeatures":   {
      "type": "object",
      "properties": {
          "maximumMembers": {
              "format": "int32",
              "type": "integer"
          },
          "maximumMembershipsOfGroupType": {
              "format": "int32",
              "description": "Maximum number of groups of this type a typical membership may join. For example, a user may join about 50 General groups with their Bungie.net account. They may join one clan per Destiny membership.",
              "type": "integer"
          },
          "capabilities": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/GroupsV2.Capabilities"
              }
          },
          "membershipTypes": {
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
          "invitePermissionOverride": {
              "description": "Minimum Member Level allowed to invite new members to group\r\nAlways Allowed: Founder, Acting Founder\r\nTrue means admins have this power, false means they don't\r\nDefault is false for clans, true for groups.",
              "type": "boolean"
          },
          "updateCulturePermissionOverride": {
              "description": "Minimum Member Level allowed to update group culture\r\nAlways Allowed: Founder, Acting Founder\r\nTrue means admins have this power, false means they don't\r\nDefault is false for clans, true for groups.",
              "type": "boolean"
          },
          "hostGuidedGamePermissionOverride": {
              "format": "int32",
              "description": "Minimum Member Level allowed to host guided games\r\nAlways Allowed: Founder, Acting Founder, Admin\r\nAllowed Overrides: None, Member, Beginner\r\nDefault is Member for clans, None for groups, although this means nothing for groups.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/GroupsV2.HostGuidedGamesPermissionLevel"
              }
          },
          "updateBannerPermissionOverride": {
              "description": "Minimum Member Level allowed to update banner\r\nAlways Allowed: Founder, Acting Founder\r\nTrue means admins have this power, false means they don't\r\nDefault is false for clans, true for groups.",
              "type": "boolean"
          },
          "joinLevel": {
              "format": "int32",
              "description": "Level to join a member at when accepting an invite, application, or joining an open clan\r\nDefault is Beginner.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/GroupsV2.RuntimeGroupMemberType"
              }
          }
      }
  }
}
```
