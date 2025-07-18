# Destiny.Responses.DestinyLinkedProfilesResponse

## Entity Information
- **Entity Name**: Destiny.Responses.DestinyLinkedProfilesResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
I know what you seek. You seek linked accounts. Found them, you have.
This contract returns a minimal amount of data about Destiny Accounts that are linked through your Bungie.Net account. We will not return accounts in this response whose

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| profiles | Array[Destiny.Responses.DestinyProfileUserInfoCard] | Any Destiny account for whom we could successfully pull characters will be returned here, as the Platform-level summary of user data. (no character data, no Destiny account data other than the Membership ID and Type so you can make further queries) | No |
| bnetMembership | object | If the requested membership had a linked Bungie.Net membership ID, this is the basic information about that BNet account.
I know, Tetron; I know this is mixing UserServices concerns with DestinyServices concerns. But it's so damn convenient! https://www.youtube.com/watch?v=X5R-bB-gKVI | No |
| profilesWithErrors | Array[Destiny.Responses.DestinyErrorProfile] | This is brief summary info for profiles that we believe have valid Destiny info, but who failed to return data for some other reason and thus we know that subsequent calls for their info will also fail. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Responses.DestinyLinkedProfilesResponse object
const example = {
  profiles: [],
  bnetMembership: null,
  profilesWithErrors: [],
};
```

### Python
```python
# Example Destiny.Responses.DestinyLinkedProfilesResponse object
example = {
    "profiles": [],
    "bnetMembership": None,
    "profilesWithErrors": [],
}
```

## Related Entities
- **Destiny.Responses.DestinyErrorProfile**: Referenced in this entity
- **Destiny.Responses.DestinyProfileUserInfoCard**: Referenced in this entity
- **User.UserInfoCard**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Responses.DestinyLinkedProfilesResponse":   {
      "description": "I know what you seek. You seek linked accounts. Found them, you have.\r\nThis contract returns a minimal amount of data about Destiny Accounts that are linked through your Bungie.Net account. We will not return accounts in this response whose",
      "type": "object",
      "properties": {
          "profiles": {
              "description": "Any Destiny account for whom we could successfully pull characters will be returned here, as the Platform-level summary of user data. (no character data, no Destiny account data other than the Membership ID and Type so you can make further queries)",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Responses.DestinyProfileUserInfoCard"
              }
          },
          "bnetMembership": {
              "description": "If the requested membership had a linked Bungie.Net membership ID, this is the basic information about that BNet account.\r\nI know, Tetron; I know this is mixing UserServices concerns with DestinyServices concerns. But it's so damn convenient! https://www.youtube.com/watch?v=X5R-bB-gKVI",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/User.UserInfoCard"
                  }
              ]
          },
          "profilesWithErrors": {
              "description": "This is brief summary info for profiles that we believe have valid Destiny info, but who failed to return data for some other reason and thus we know that subsequent calls for their info will also fail.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Responses.DestinyErrorProfile"
              }
          }
      }
  }
}
```
