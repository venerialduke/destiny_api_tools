# GroupsV2.GroupV2Card

## Entity Information
- **Entity Name**: GroupsV2.GroupV2Card
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
A small infocard of group information, usually used for when a list of groups are returned

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| groupId | integer (int64) |  | No |
| name | string |  | No |
| groupType | integer (int32) |  | No |
| creationDate | string (date-time) |  | No |
| about | string |  | No |
| motto | string |  | No |
| memberCount | integer (int32) |  | No |
| locale | string |  | No |
| membershipOption | integer (int32) |  | No |
| capabilities | integer (int32) |  | No |
| remoteGroupId | integer (int64) |  | No |
| clanInfo | GroupsV2.GroupV2ClanInfo |  | No |
| avatarPath | string |  | No |
| theme | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example GroupsV2.GroupV2Card object
const example = {
  groupId: 123,
  name: "example value",
  groupType: 123,
  creationDate: "example value",
  about: "example value",
  // ... more properties
};
```

### Python
```python
# Example GroupsV2.GroupV2Card object
example = {
    "groupId": 123,
    "name": "example value",
    "groupType": 123,
    "creationDate": "example value",
    "about": "example value",
    # ... more properties
}
```

## Related Entities
- **GroupsV2.Capabilities**: Referenced in this entity
- **GroupsV2.GroupType**: Referenced in this entity
- **GroupsV2.GroupV2ClanInfo**: Referenced in this entity
- **GroupsV2.MembershipOption**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "GroupsV2.GroupV2Card":   {
      "description": "A small infocard of group information, usually used for when a list of groups are returned",
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
          "creationDate": {
              "format": "date-time",
              "type": "string"
          },
          "about": {
              "type": "string"
          },
          "motto": {
              "type": "string"
          },
          "memberCount": {
              "format": "int32",
              "type": "integer"
          },
          "locale": {
              "type": "string"
          },
          "membershipOption": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/GroupsV2.MembershipOption"
              }
          },
          "capabilities": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/GroupsV2.Capabilities"
              }
          },
          "remoteGroupId": {
              "format": "int64",
              "type": "integer"
          },
          "clanInfo": {
              "$ref": "#/definitions/GroupsV2.GroupV2ClanInfo"
          },
          "avatarPath": {
              "type": "string"
          },
          "theme": {
              "type": "string"
          }
      }
  }
}
```
