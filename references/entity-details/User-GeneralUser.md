# User.GeneralUser

## Entity Information
- **Entity Name**: User.GeneralUser
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for generaluser operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| membershipId | integer (int64) |  | No |
| uniqueName | string |  | No |
| normalizedName | string |  | No |
| displayName | string |  | No |
| profilePicture | integer (int32) |  | No |
| profileTheme | integer (int32) |  | No |
| userTitle | integer (int32) |  | No |
| successMessageFlags | integer (int64) |  | No |
| isDeleted | boolean |  | No |
| about | string |  | No |
| firstAccess | string (date-time) |  | No |
| lastUpdate | string (date-time) |  | No |
| legacyPortalUID | integer (int64) |  | No |
| context | User.UserToUserContext |  | No |
| psnDisplayName | string |  | No |
| xboxDisplayName | string |  | No |
| fbDisplayName | string |  | No |
| showActivity | boolean |  | No |
| locale | string |  | No |
| localeInheritDefault | boolean |  | No |
| lastBanReportId | integer (int64) |  | No |
| showGroupMessaging | boolean |  | No |
| profilePicturePath | string |  | No |
| profilePictureWidePath | string |  | No |
| profileThemeName | string |  | No |
| userTitleDisplay | string |  | No |
| statusText | string |  | No |
| statusDate | string (date-time) |  | No |
| profileBanExpire | string (date-time) |  | No |
| blizzardDisplayName | string |  | No |
| steamDisplayName | string |  | No |
| stadiaDisplayName | string |  | No |
| twitchDisplayName | string |  | No |
| cachedBungieGlobalDisplayName | string |  | No |
| cachedBungieGlobalDisplayNameCode | integer (int16) |  | No |
| egsDisplayName | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example User.GeneralUser object
const example = {
  membershipId: 123,
  uniqueName: "example value",
  normalizedName: "example value",
  displayName: "example value",
  profilePicture: 123,
  // ... more properties
};
```

### Python
```python
# Example User.GeneralUser object
example = {
    "membershipId": 123,
    "uniqueName": "example value",
    "normalizedName": "example value",
    "displayName": "example value",
    "profilePicture": 123,
    # ... more properties
}
```

## Related Entities
- **User.UserToUserContext**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "User.GeneralUser":   {
      "type": "object",
      "properties": {
          "membershipId": {
              "format": "int64",
              "type": "integer"
          },
          "uniqueName": {
              "type": "string"
          },
          "normalizedName": {
              "type": "string"
          },
          "displayName": {
              "type": "string"
          },
          "profilePicture": {
              "format": "int32",
              "type": "integer"
          },
          "profileTheme": {
              "format": "int32",
              "type": "integer"
          },
          "userTitle": {
              "format": "int32",
              "type": "integer"
          },
          "successMessageFlags": {
              "format": "int64",
              "type": "integer"
          },
          "isDeleted": {
              "type": "boolean"
          },
          "about": {
              "type": "string"
          },
          "firstAccess": {
              "format": "date-time",
              "type": "string"
          },
          "lastUpdate": {
              "format": "date-time",
              "type": "string"
          },
          "legacyPortalUID": {
              "format": "int64",
              "type": "integer"
          },
          "context": {
              "$ref": "#/definitions/User.UserToUserContext"
          },
          "psnDisplayName": {
              "type": "string"
          },
          "xboxDisplayName": {
              "type": "string"
          },
          "fbDisplayName": {
              "type": "string"
          },
          "showActivity": {
              "type": "boolean"
          },
          "locale": {
              "type": "string"
          },
          "localeInheritDefault": {
              "type": "boolean"
          },
          "lastBanReportId": {
              "format": "int64",
              "type": "integer"
          },
          "showGroupMessaging": {
              "type": "boolean"
          },
          "profilePicturePath": {
              "type": "string"
          },
          "profilePictureWidePath": {
              "type": "string"
          },
          "profileThemeName": {
              "type": "string"
          },
          "userTitleDisplay": {
              "type": "string"
          },
          "statusText": {
              "type": "string"
          },
          "statusDate": {
              "format": "date-time",
              "type": "string"
          },
          "profileBanExpire": {
              "format": "date-time",
              "type": "string"
          },
          "blizzardDisplayName": {
              "type": "string"
          },
          "steamDisplayName": {
              "type": "string"
          },
          "stadiaDisplayName": {
              "type": "string"
          },
          "twitchDisplayName": {
              "type": "string"
          },
          "cachedBungieGlobalDisplayName": {
              "type": "string"
          },
          "cachedBungieGlobalDisplayNameCode": {
              "format": "int16",
              "type": "integer"
          },
          "egsDisplayName": {
              "type": "string"
          }
      }
  }
}
```
