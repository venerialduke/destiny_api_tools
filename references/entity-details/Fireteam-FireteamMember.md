# Fireteam.FireteamMember

## Entity Information
- **Entity Name**: Fireteam.FireteamMember
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for fireteammember operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| destinyUserInfo | Fireteam.FireteamUserInfoCard |  | No |
| bungieNetUserInfo | User.UserInfoCard |  | No |
| characterId | integer (int64) |  | No |
| dateJoined | string (date-time) |  | No |
| hasMicrophone | boolean |  | No |
| lastPlatformInviteAttemptDate | string (date-time) |  | No |
| lastPlatformInviteAttemptResult | integer (byte) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Fireteam.FireteamMember object
const example = {
  destinyUserInfo: null,
  bungieNetUserInfo: null,
  characterId: 123,
  dateJoined: "example value",
  hasMicrophone: true,
  // ... more properties
};
```

### Python
```python
# Example Fireteam.FireteamMember object
example = {
    "destinyUserInfo": None,
    "bungieNetUserInfo": None,
    "characterId": 123,
    "dateJoined": "example value",
    "hasMicrophone": True,
    # ... more properties
}
```

## Related Entities
- **Fireteam.FireteamPlatformInviteResult**: Referenced in this entity
- **Fireteam.FireteamUserInfoCard**: Referenced in this entity
- **User.UserInfoCard**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Fireteam.FireteamMember":   {
      "type": "object",
      "properties": {
          "destinyUserInfo": {
              "$ref": "#/definitions/Fireteam.FireteamUserInfoCard"
          },
          "bungieNetUserInfo": {
              "$ref": "#/definitions/User.UserInfoCard"
          },
          "characterId": {
              "format": "int64",
              "type": "integer"
          },
          "dateJoined": {
              "format": "date-time",
              "type": "string"
          },
          "hasMicrophone": {
              "type": "boolean"
          },
          "lastPlatformInviteAttemptDate": {
              "format": "date-time",
              "type": "string"
          },
          "lastPlatformInviteAttemptResult": {
              "format": "byte",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Fireteam.FireteamPlatformInviteResult"
              }
          }
      }
  }
}
```
