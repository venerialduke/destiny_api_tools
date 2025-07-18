# GroupsV2.GroupEditAction

## Entity Information
- **Entity Name**: GroupsV2.GroupEditAction
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for groupeditaction operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| name | string |  | No |
| about | string |  | No |
| motto | string |  | No |
| theme | string |  | No |
| avatarImageIndex | integer (int32) |  | No |
| tags | string |  | No |
| isPublic | boolean |  | No |
| membershipOption | integer (int32) |  | No |
| isPublicTopicAdminOnly | boolean |  | No |
| allowChat | boolean |  | No |
| chatSecurity | integer (int32) |  | No |
| callsign | string |  | No |
| locale | string |  | No |
| homepage | integer (int32) |  | No |
| enableInvitationMessagingForAdmins | boolean |  | No |
| defaultPublicity | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example GroupsV2.GroupEditAction object
const example = {
  name: "example value",
  about: "example value",
  motto: "example value",
  theme: "example value",
  avatarImageIndex: 123,
  // ... more properties
};
```

### Python
```python
# Example GroupsV2.GroupEditAction object
example = {
    "name": "example value",
    "about": "example value",
    "motto": "example value",
    "theme": "example value",
    "avatarImageIndex": 123,
    # ... more properties
}
```

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "GroupsV2.GroupEditAction":   {
      "type": "object",
      "properties": {
          "name": {
              "type": "string"
          },
          "about": {
              "type": "string"
          },
          "motto": {
              "type": "string"
          },
          "theme": {
              "type": "string"
          },
          "avatarImageIndex": {
              "format": "int32",
              "type": "integer"
          },
          "tags": {
              "type": "string"
          },
          "isPublic": {
              "type": "boolean"
          },
          "membershipOption": {
              "format": "int32",
              "enum": [
                  "0",
                  "1",
                  "2"
              ],
              "type": "integer",
              "x-enum-values": [
                  {
                      "numericValue": "0",
                      "identifier": "Reviewed"
                  },
                  {
                      "numericValue": "1",
                      "identifier": "Open"
                  },
                  {
                      "numericValue": "2",
                      "identifier": "Closed"
                  }
              ]
          },
          "isPublicTopicAdminOnly": {
              "type": "boolean"
          },
          "allowChat": {
              "type": "boolean"
          },
          "chatSecurity": {
              "format": "int32",
              "enum": [
                  "0",
                  "1"
              ],
              "type": "integer",
              "x-enum-values": [
                  {
                      "numericValue": "0",
                      "identifier": "Group"
                  },
                  {
                      "numericValue": "1",
                      "identifier": "Admins"
                  }
              ]
          },
          "callsign": {
              "type": "string"
          },
          "locale": {
              "type": "string"
          },
          "homepage": {
              "format": "int32",
              "enum": [
                  "0",
                  "1",
                  "2"
              ],
              "type": "integer",
              "x-enum-values": [
                  {
                      "numericValue": "0",
                      "identifier": "Wall"
                  },
                  {
                      "numericValue": "1",
                      "identifier": "Forum"
                  },
                  {
                      "numericValue": "2",
                      "identifier": "AllianceForum"
                  }
              ]
          },
          "enableInvitationMessagingForAdmins": {
              "type": "boolean"
          },
          "defaultPublicity": {
              "format": "int32",
              "enum": [
                  "0",
                  "1",
                  "2"
              ],
              "type": "integer",
              "x-enum-values": [
                  {
                      "numericValue": "0",
                      "identifier": "Public"
                  },
                  {
                      "numericValue": "1",
                      "identifier": "Alliance"
                  },
                  {
                      "numericValue": "2",
                      "identifier": "Private"
                  }
              ]
          }
      }
  }
}
```
