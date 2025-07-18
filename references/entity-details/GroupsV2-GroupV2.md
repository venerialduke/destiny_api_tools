# GroupsV2.GroupV2

## Entity Information
- **Entity Name**: GroupsV2.GroupV2
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for groupv2 operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| groupId | integer (int64) |  | No |
| name | string |  | No |
| groupType | integer (int32) |  | No |
| membershipIdCreated | integer (int64) |  | No |
| creationDate | string (date-time) |  | No |
| modificationDate | string (date-time) |  | No |
| about | string |  | No |
| tags | Array[string] |  | No |
| memberCount | integer (int32) |  | No |
| isPublic | boolean |  | No |
| isPublicTopicAdminOnly | boolean |  | No |
| motto | string |  | No |
| allowChat | boolean |  | No |
| isDefaultPostPublic | boolean |  | No |
| chatSecurity | integer (int32) |  | No |
| locale | string |  | No |
| avatarImageIndex | integer (int32) |  | No |
| homepage | integer (int32) |  | No |
| membershipOption | integer (int32) |  | No |
| defaultPublicity | integer (int32) |  | No |
| theme | string |  | No |
| bannerPath | string |  | No |
| avatarPath | string |  | No |
| conversationId | integer (int64) |  | No |
| enableInvitationMessagingForAdmins | boolean |  | No |
| banExpireDate | string (date-time) |  | No |
| features | GroupsV2.GroupFeatures |  | No |
| remoteGroupId | integer (int64) |  | No |
| clanInfo | GroupsV2.GroupV2ClanInfoAndInvestment |  | No |

## Usage Examples

### JavaScript
```javascript
// Example GroupsV2.GroupV2 object
const example = {
  groupId: 123,
  name: "example value",
  groupType: 123,
  membershipIdCreated: 123,
  creationDate: "example value",
  // ... more properties
};
```

### Python
```python
# Example GroupsV2.GroupV2 object
example = {
    "groupId": 123,
    "name": "example value",
    "groupType": 123,
    "membershipIdCreated": 123,
    "creationDate": "example value",
    # ... more properties
}
```

## Related Entities
- **GroupsV2.ChatSecuritySetting**: Referenced in this entity
- **GroupsV2.GroupFeatures**: Referenced in this entity
- **GroupsV2.GroupHomepage**: Referenced in this entity
- **GroupsV2.GroupPostPublicity**: Referenced in this entity
- **GroupsV2.GroupType**: Referenced in this entity
- **GroupsV2.GroupV2ClanInfoAndInvestment**: Referenced in this entity
- **GroupsV2.MembershipOption**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "GroupsV2.GroupV2":   {
      "type": "object",
      "properties": {
          "groupId": {
              "format": "int64",
              "type": "integer"
          },
          "name": {
              "type": "string"
          },
          "groupType": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/GroupsV2.GroupType"
              }
          },
          "membershipIdCreated": {
              "format": "int64",
              "type": "integer"
          },
          "creationDate": {
              "format": "date-time",
              "type": "string"
          },
          "modificationDate": {
              "format": "date-time",
              "type": "string"
          },
          "about": {
              "type": "string"
          },
          "tags": {
              "type": "array",
              "items": {
                  "type": "string"
              }
          },
          "memberCount": {
              "format": "int32",
              "type": "integer"
          },
          "isPublic": {
              "type": "boolean"
          },
          "isPublicTopicAdminOnly": {
              "type": "boolean"
          },
          "motto": {
              "type": "string"
          },
          "allowChat": {
              "type": "boolean"
          },
          "isDefaultPostPublic": {
              "type": "boolean"
          },
          "chatSecurity": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/GroupsV2.ChatSecuritySetting"
              }
          },
          "locale": {
              "type": "string"
          },
          "avatarImageIndex": {
              "format": "int32",
              "type": "integer"
          },
          "homepage": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/GroupsV2.GroupHomepage"
              }
          },
          "membershipOption": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/GroupsV2.MembershipOption"
              }
          },
          "defaultPublicity": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/GroupsV2.GroupPostPublicity"
              }
          },
          "theme": {
              "type": "string"
          },
          "bannerPath": {
              "type": "string"
          },
          "avatarPath": {
              "type": "string"
          },
          "conversationId": {
              "format": "int64",
              "type": "integer"
          },
          "enableInvitationMessagingForAdmins": {
              "type": "boolean"
          },
          "banExpireDate": {
              "format": "date-time",
              "type": "string"
          },
          "features": {
              "$ref": "#/definitions/GroupsV2.GroupFeatures"
          },
          "remoteGroupId": {
              "format": "int64",
              "type": "integer"
          },
          "clanInfo": {
              "$ref": "#/definitions/GroupsV2.GroupV2ClanInfoAndInvestment"
          }
      }
  }
}
```
