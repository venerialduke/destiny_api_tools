# Social.Friends.BungieFriend

## Entity Information
- **Entity Name**: Social.Friends.BungieFriend
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for bungiefriend operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| lastSeenAsMembershipId | integer (int64) |  | No |
| lastSeenAsBungieMembershipType | integer (int32) |  | No |
| bungieGlobalDisplayName | string |  | No |
| bungieGlobalDisplayNameCode | integer (int16) |  | No |
| onlineStatus | integer (int32) |  | No |
| onlineTitle | integer (int32) |  | No |
| relationship | integer (int32) |  | No |
| bungieNetUser | User.GeneralUser |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Social.Friends.BungieFriend object
const example = {
  lastSeenAsMembershipId: 123,
  lastSeenAsBungieMembershipType: 123,
  bungieGlobalDisplayName: "example value",
  bungieGlobalDisplayNameCode: 123,
  onlineStatus: 123,
  // ... more properties
};
```

### Python
```python
# Example Social.Friends.BungieFriend object
example = {
    "lastSeenAsMembershipId": 123,
    "lastSeenAsBungieMembershipType": 123,
    "bungieGlobalDisplayName": "example value",
    "bungieGlobalDisplayNameCode": 123,
    "onlineStatus": 123,
    # ... more properties
}
```

## Related Entities
- **BungieMembershipType**: Referenced in this entity
- **Social.Friends.FriendRelationshipState**: Referenced in this entity
- **Social.Friends.PresenceOnlineStateFlags**: Referenced in this entity
- **Social.Friends.PresenceStatus**: Referenced in this entity
- **User.GeneralUser**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Social.Friends.BungieFriend":   {
      "type": "object",
      "properties": {
          "lastSeenAsMembershipId": {
              "format": "int64",
              "type": "integer"
          },
          "lastSeenAsBungieMembershipType": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/BungieMembershipType"
              }
          },
          "bungieGlobalDisplayName": {
              "type": "string"
          },
          "bungieGlobalDisplayNameCode": {
              "format": "int16",
              "type": "integer"
          },
          "onlineStatus": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Social.Friends.PresenceStatus"
              }
          },
          "onlineTitle": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Social.Friends.PresenceOnlineStateFlags"
              }
          },
          "relationship": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Social.Friends.FriendRelationshipState"
              }
          },
          "bungieNetUser": {
              "$ref": "#/definitions/User.GeneralUser"
          }
      }
  }
}
```
