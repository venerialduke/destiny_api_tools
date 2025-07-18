# Social.Friends.PlatformFriend

## Entity Information
- **Entity Name**: Social.Friends.PlatformFriend
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for platformfriend operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| platformDisplayName | string |  | No |
| friendPlatform | integer (int32) |  | No |
| destinyMembershipId | integer (int64) |  | No |
| destinyMembershipType | integer (int32) |  | No |
| bungieNetMembershipId | integer (int64) |  | No |
| bungieGlobalDisplayName | string |  | No |
| bungieGlobalDisplayNameCode | integer (int16) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Social.Friends.PlatformFriend object
const example = {
  platformDisplayName: "example value",
  friendPlatform: 123,
  destinyMembershipId: 123,
  destinyMembershipType: 123,
  bungieNetMembershipId: 123,
  // ... more properties
};
```

### Python
```python
# Example Social.Friends.PlatformFriend object
example = {
    "platformDisplayName": "example value",
    "friendPlatform": 123,
    "destinyMembershipId": 123,
    "destinyMembershipType": 123,
    "bungieNetMembershipId": 123,
    # ... more properties
}
```

## Related Entities
- **Social.Friends.PlatformFriendType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Social.Friends.PlatformFriend":   {
      "type": "object",
      "properties": {
          "platformDisplayName": {
              "type": "string"
          },
          "friendPlatform": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Social.Friends.PlatformFriendType"
              }
          },
          "destinyMembershipId": {
              "format": "int64",
              "type": "integer"
          },
          "destinyMembershipType": {
              "format": "int32",
              "enum": [
                  "0",
                  "1",
                  "2",
                  "3",
                  "4",
                  "5",
                  "6",
                  "10",
                  "20",
                  "254",
                  "-1"
              ],
              "type": "integer",
              "x-enum-values": [
                  {
                      "numericValue": "0",
                      "identifier": "None"
                  },
                  {
                      "numericValue": "1",
                      "identifier": "TigerXbox"
                  },
                  {
                      "numericValue": "2",
                      "identifier": "TigerPsn"
                  },
                  {
                      "numericValue": "3",
                      "identifier": "TigerSteam"
                  },
                  {
                      "numericValue": "4",
                      "identifier": "TigerBlizzard"
                  },
                  {
                      "numericValue": "5",
                      "identifier": "TigerStadia"
                  },
                  {
                      "numericValue": "6",
                      "identifier": "TigerEgs"
                  },
                  {
                      "numericValue": "10",
                      "identifier": "TigerDemon"
                  },
                  {
                      "numericValue": "20",
                      "identifier": "GoliathGame"
                  },
                  {
                      "numericValue": "254",
                      "identifier": "BungieNext"
                  },
                  {
                      "numericValue": "-1",
                      "identifier": "All",
                      "description": "\"All\" is only valid for searching capabilities: you need to pass the actual matching BungieMembershipType for any query where you pass a known membershipId."
                  }
              ]
          },
          "bungieNetMembershipId": {
              "format": "int64",
              "type": "integer"
          },
          "bungieGlobalDisplayName": {
              "type": "string"
          },
          "bungieGlobalDisplayNameCode": {
              "format": "int16",
              "type": "integer"
          }
      }
  }
}
```
