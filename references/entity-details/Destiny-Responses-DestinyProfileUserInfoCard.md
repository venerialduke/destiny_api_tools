# Destiny.Responses.DestinyProfileUserInfoCard

## Entity Information
- **Entity Name**: Destiny.Responses.DestinyProfileUserInfoCard
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyprofileuserinfocard data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| dateLastPlayed | string (date-time) |  | No |
| isOverridden | boolean | If this profile is being overridden/obscured by Cross Save, this will be set to true. We will still return the profile for display purposes where users need to know the info: it is up to any given area of the app/site to determine if this profile should still be shown. | No |
| isCrossSavePrimary | boolean | If true, this account is hooked up as the "Primary" cross save account for one or more platforms. | No |
| platformSilver | object | This is the silver available on this Profile across any platforms on which they have purchased silver.
 This is only available if you are requesting yourself. | No |
| unpairedGameVersions | integer (int32) | If this profile is not in a cross save pairing, this will return the game versions that we believe this profile has access to.
 For the time being, we will not return this information for any membership that is in a cross save pairing. The gist is that, once the pairing occurs, we do not currently have a consistent way to get that information for the profile's original Platform, and thus gameVersions would be too inconsistent (based on the last platform they happened to play on) for the info to be useful.
 If we ever can get this data, this field will be deprecated and replaced with data on the DestinyLinkedProfileResponse itself, with game versions per linked Platform. But since we can't get that, we have this as a stop-gap measure for getting the data in the only situation that we currently need it. | No |
| supplementalDisplayName | string | A platform specific additional display name - ex: psn Real Name, bnet Unique Name, etc. | No |
| iconPath | string | URL the Icon if available. | No |
| crossSaveOverride | integer (int32) | If there is a cross save override in effect, this value will tell you the type that is overridding this one. | No |
| applicableMembershipTypes | Array[integer] | The list of Membership Types indicating the platforms on which this Membership can be used.
 Not in Cross Save = its original membership type. Cross Save Primary = Any membership types it is overridding, and its original membership type Cross Save Overridden = Empty list | No |
| isPublic | boolean | If True, this is a public user membership. | No |
| membershipType | integer (int32) | Type of the membership. Not necessarily the native type. | No |
| membershipId | integer (int64) | Membership ID as they user is known in the Accounts service | No |
| displayName | string | Display Name the player has chosen for themselves. The display name is optional when the data type is used as input to a platform API. | No |
| bungieGlobalDisplayName | string | The bungie global display name, if set. | No |
| bungieGlobalDisplayNameCode | integer (int16) | The bungie global display name code, if set. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Responses.DestinyProfileUserInfoCard object
const example = {
  dateLastPlayed: "example value",
  isOverridden: true,
  isCrossSavePrimary: true,
  platformSilver: null,
  unpairedGameVersions: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Responses.DestinyProfileUserInfoCard object
example = {
    "dateLastPlayed": "example value",
    "isOverridden": True,
    "isCrossSavePrimary": True,
    "platformSilver": None,
    "unpairedGameVersions": 123,
    # ... more properties
}
```

## Related Entities
- **BungieMembershipType**: Referenced in this entity
- **Destiny.Components.Inventory.DestinyPlatformSilverComponent**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Responses.DestinyProfileUserInfoCard":   {
      "type": "object",
      "properties": {
          "dateLastPlayed": {
              "format": "date-time",
              "type": "string"
          },
          "isOverridden": {
              "description": "If this profile is being overridden/obscured by Cross Save, this will be set to true. We will still return the profile for display purposes where users need to know the info: it is up to any given area of the app/site to determine if this profile should still be shown.",
              "type": "boolean"
          },
          "isCrossSavePrimary": {
              "description": "If true, this account is hooked up as the \"Primary\" cross save account for one or more platforms.",
              "type": "boolean"
          },
          "platformSilver": {
              "description": "This is the silver available on this Profile across any platforms on which they have purchased silver.\r\n This is only available if you are requesting yourself.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Components.Inventory.DestinyPlatformSilverComponent"
                  }
              ]
          },
          "unpairedGameVersions": {
              "format": "int32",
              "description": "If this profile is not in a cross save pairing, this will return the game versions that we believe this profile has access to.\r\n For the time being, we will not return this information for any membership that is in a cross save pairing. The gist is that, once the pairing occurs, we do not currently have a consistent way to get that information for the profile's original Platform, and thus gameVersions would be too inconsistent (based on the last platform they happened to play on) for the info to be useful.\r\n If we ever can get this data, this field will be deprecated and replaced with data on the DestinyLinkedProfileResponse itself, with game versions per linked Platform. But since we can't get that, we have this as a stop-gap measure for getting the data in the only situation that we currently need it.",
              "enum": [
                  "0",
                  "1",
                  "2",
                  "4",
                  "8",
                  "16",
                  "32",
                  "64",
                  "128",
                  "256",
                  "512",
                  "1024",
                  "28535",
                  "28536"
              ],
              "type": "integer",
              "x-enum-values": [
                  {
                      "numericValue": "0",
                      "identifier": "None"
                  },
                  {
                      "numericValue": "1",
                      "identifier": "Destiny2"
                  },
                  {
                      "numericValue": "2",
                      "identifier": "DLC1"
                  },
                  {
                      "numericValue": "4",
                      "identifier": "DLC2"
                  },
                  {
                      "numericValue": "8",
                      "identifier": "Forsaken"
                  },
                  {
                      "numericValue": "16",
                      "identifier": "YearTwoAnnualPass"
                  },
                  {
                      "numericValue": "32",
                      "identifier": "Shadowkeep"
                  },
                  {
                      "numericValue": "64",
                      "identifier": "BeyondLight"
                  },
                  {
                      "numericValue": "128",
                      "identifier": "Anniversary30th"
                  },
                  {
                      "numericValue": "256",
                      "identifier": "TheWitchQueen"
                  },
                  {
                      "numericValue": "512",
                      "identifier": "Lightfall"
                  },
                  {
                      "numericValue": "1024",
                      "identifier": "TheFinalShape"
                  },
                  {
                      "numericValue": "28535",
                      "identifier": "EdgeOfFate"
                  },
                  {
                      "numericValue": "28536",
                      "identifier": "Renegades"
                  }
              ]
          },
          "supplementalDisplayName": {
              "description": "A platform specific additional display name - ex: psn Real Name, bnet Unique Name, etc.",
              "type": "string"
          },
          "iconPath": {
              "description": "URL the Icon if available.",
              "type": "string"
          },
          "crossSaveOverride": {
              "format": "int32",
              "description": "If there is a cross save override in effect, this value will tell you the type that is overridding this one.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/BungieMembershipType"
              }
          },
          "applicableMembershipTypes": {
              "description": "The list of Membership Types indicating the platforms on which this Membership can be used.\r\n Not in Cross Save = its original membership type. Cross Save Primary = Any membership types it is overridding, and its original membership type Cross Save Overridden = Empty list",
              "type": "array",
              "items": {
                  "format": "int32",
                  "description": "The types of membership the Accounts system supports. This is the external facing enum used in place of the internal-only Bungie.SharedDefinitions.MembershipType.",
                  "type": "integer",
                  "x-enum-reference": {
                      "$ref": "#/components/schemas/BungieMembershipType"
                  }
              }
          },
          "isPublic": {
              "description": "If True, this is a public user membership.",
              "type": "boolean"
          },
          "membershipType": {
              "format": "int32",
              "description": "Type of the membership. Not necessarily the native type.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/BungieMembershipType"
              }
          },
          "membershipId": {
              "format": "int64",
              "description": "Membership ID as they user is known in the Accounts service",
              "type": "integer"
          },
          "displayName": {
              "description": "Display Name the player has chosen for themselves. The display name is optional when the data type is used as input to a platform API.",
              "type": "string"
          },
          "bungieGlobalDisplayName": {
              "description": "The bungie global display name, if set.",
              "type": "string"
          },
          "bungieGlobalDisplayNameCode": {
              "format": "int16",
              "description": "The bungie global display name code, if set.",
              "type": "integer"
          }
      }
  }
}
```
