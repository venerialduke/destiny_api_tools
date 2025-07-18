# Destiny.Components.Profiles.DestinyProfileTransitoryPartyMember

## Entity Information
- **Entity Name**: Destiny.Components.Profiles.DestinyProfileTransitoryPartyMember
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
This is some bare minimum information about a party member in a Fireteam. Unfortunately, without great computational expense on our side we can only get at the data contained here. I'd like to give you a character ID for example, but we don't have it. But we do have these three pieces of information. May they help you on your quest to show meaningful data about current Fireteams.
Notably, we don't and can't feasibly return info on characters. If you can, try to use just the data below for your UI and purposes. Only hit us with further queries if you absolutely must know the character ID of the currently playing character. Pretty please with sugar on top.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| membershipId | integer (int64) | The Membership ID that matches the party member. | No |
| emblemHash | integer (uint32) | The identifier for the DestinyInventoryItemDefinition of the player's emblem. | No |
| displayName | string | The player's last known display name. | No |
| status | integer (int32) | A Flags Enumeration value indicating the states that the player is in relevant to being on a fireteam. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Profiles.DestinyProfileTransitoryPartyMember object
const example = {
  membershipId: 123,
  emblemHash: 123,
  displayName: "example value",
  status: 123,
};
```

### Python
```python
# Example Destiny.Components.Profiles.DestinyProfileTransitoryPartyMember object
example = {
    "membershipId": 123,
    "emblemHash": 123,
    "displayName": "example value",
    "status": 123,
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.DestinyPartyMemberStates**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Profiles.DestinyProfileTransitoryPartyMember":   {
      "description": "This is some bare minimum information about a party member in a Fireteam. Unfortunately, without great computational expense on our side we can only get at the data contained here. I'd like to give you a character ID for example, but we don't have it. But we do have these three pieces of information. May they help you on your quest to show meaningful data about current Fireteams.\r\nNotably, we don't and can't feasibly return info on characters. If you can, try to use just the data below for your UI and purposes. Only hit us with further queries if you absolutely must know the character ID of the currently playing character. Pretty please with sugar on top.",
      "type": "object",
      "properties": {
          "membershipId": {
              "format": "int64",
              "description": "The Membership ID that matches the party member.",
              "type": "integer"
          },
          "emblemHash": {
              "format": "uint32",
              "description": "The identifier for the DestinyInventoryItemDefinition of the player's emblem.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "displayName": {
              "description": "The player's last known display name.",
              "type": "string"
          },
          "status": {
              "format": "int32",
              "description": "A Flags Enumeration value indicating the states that the player is in relevant to being on a fireteam.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyPartyMemberStates"
              }
          }
      }
  }
}
```
