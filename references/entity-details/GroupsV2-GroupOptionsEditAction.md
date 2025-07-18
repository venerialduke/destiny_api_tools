# GroupsV2.GroupOptionsEditAction

## Entity Information
- **Entity Name**: GroupsV2.GroupOptionsEditAction
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for groupoptionseditaction operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| InvitePermissionOverride | boolean | Minimum Member Level allowed to invite new members to group
Always Allowed: Founder, Acting Founder
True means admins have this power, false means they don't
Default is false for clans, true for groups. | No |
| UpdateCulturePermissionOverride | boolean | Minimum Member Level allowed to update group culture
Always Allowed: Founder, Acting Founder
True means admins have this power, false means they don't
Default is false for clans, true for groups. | No |
| HostGuidedGamePermissionOverride | integer (int32) | Minimum Member Level allowed to host guided games
Always Allowed: Founder, Acting Founder, Admin
Allowed Overrides: None, Member, Beginner
Default is Member for clans, None for groups, although this means nothing for groups. | No |
| UpdateBannerPermissionOverride | boolean | Minimum Member Level allowed to update banner
Always Allowed: Founder, Acting Founder
True means admins have this power, false means they don't
Default is false for clans, true for groups. | No |
| JoinLevel | integer (int32) | Level to join a member at when accepting an invite, application, or joining an open clan
Default is Beginner. | No |

## Usage Examples

### JavaScript
```javascript
// Example GroupsV2.GroupOptionsEditAction object
const example = {
  InvitePermissionOverride: true,
  UpdateCulturePermissionOverride: true,
  HostGuidedGamePermissionOverride: 123,
  UpdateBannerPermissionOverride: true,
  JoinLevel: 123,
};
```

### Python
```python
# Example GroupsV2.GroupOptionsEditAction object
example = {
    "InvitePermissionOverride": True,
    "UpdateCulturePermissionOverride": True,
    "HostGuidedGamePermissionOverride": 123,
    "UpdateBannerPermissionOverride": True,
    "JoinLevel": 123,
}
```

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "GroupsV2.GroupOptionsEditAction":   {
      "type": "object",
      "properties": {
          "InvitePermissionOverride": {
              "description": "Minimum Member Level allowed to invite new members to group\r\nAlways Allowed: Founder, Acting Founder\r\nTrue means admins have this power, false means they don't\r\nDefault is false for clans, true for groups.",
              "type": "boolean"
          },
          "UpdateCulturePermissionOverride": {
              "description": "Minimum Member Level allowed to update group culture\r\nAlways Allowed: Founder, Acting Founder\r\nTrue means admins have this power, false means they don't\r\nDefault is false for clans, true for groups.",
              "type": "boolean"
          },
          "HostGuidedGamePermissionOverride": {
              "format": "int32",
              "description": "Minimum Member Level allowed to host guided games\r\nAlways Allowed: Founder, Acting Founder, Admin\r\nAllowed Overrides: None, Member, Beginner\r\nDefault is Member for clans, None for groups, although this means nothing for groups.",
              "enum": [
                  "0",
                  "1",
                  "2"
              ],
              "type": "integer",
              "x-enum-values": [
                  {
                      "numericValue": "0",
                      "identifier": "None"
                  },
                  {
                      "numericValue": "1",
                      "identifier": "Beginner"
                  },
                  {
                      "numericValue": "2",
                      "identifier": "Member"
                  }
              ]
          },
          "UpdateBannerPermissionOverride": {
              "description": "Minimum Member Level allowed to update banner\r\nAlways Allowed: Founder, Acting Founder\r\nTrue means admins have this power, false means they don't\r\nDefault is false for clans, true for groups.",
              "type": "boolean"
          },
          "JoinLevel": {
              "format": "int32",
              "description": "Level to join a member at when accepting an invite, application, or joining an open clan\r\nDefault is Beginner.",
              "enum": [
                  "0",
                  "1",
                  "2",
                  "3",
                  "4",
                  "5"
              ],
              "type": "integer",
              "x-enum-values": [
                  {
                      "numericValue": "0",
                      "identifier": "None"
                  },
                  {
                      "numericValue": "1",
                      "identifier": "Beginner"
                  },
                  {
                      "numericValue": "2",
                      "identifier": "Member"
                  },
                  {
                      "numericValue": "3",
                      "identifier": "Admin"
                  },
                  {
                      "numericValue": "4",
                      "identifier": "ActingFounder"
                  },
                  {
                      "numericValue": "5",
                      "identifier": "Founder"
                  }
              ]
          }
      }
  }
}
```
