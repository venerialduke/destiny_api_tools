# Destiny.Entities.Profiles.DestinyProfileComponent

## Entity Information
- **Entity Name**: Destiny.Entities.Profiles.DestinyProfileComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The most essential summary information about a Profile (in Destiny 1, we called these "Accounts").

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| userInfo | object | If you need to render the Profile (their platform name, icon, etc...) somewhere, this property contains that information. | No |
| dateLastPlayed | string (date-time) | The last time the user played with any character on this Profile. | No |
| versionsOwned | integer (int32) | If you want to know what expansions they own, this will contain that data.
 IMPORTANT: This field may not return the data you're interested in for Cross-Saved users. It returns the last ownership data we saw for this account - which is to say, what they've purchased on the platform on which they last played, which now could be a different platform.
 If you don't care about per-platform ownership and only care about whatever platform it seems they are playing on most recently, then this should be "good enough." Otherwise, this should be considered deprecated. We do not have a good alternative to provide at this time with platform specific ownership data for DLC. | No |
| characterIds | Array[integer] | A list of the character IDs, for further querying on your part. | No |
| seasonHashes | Array[integer] | A list of seasons that this profile owns. Unlike versionsOwned, these stay with the profile across Platforms, and thus will be valid.
 It turns out that Stadia Pro subscriptions will give access to seasons but only while playing on Stadia and with an active subscription. So some users (users who have Stadia Pro but choose to play on some other platform) won't see these as available: it will be whatever seasons are available for the platform on which they last played. | No |
| eventCardHashesOwned | Array[integer] | A list of hashes for event cards that a profile owns. Unlike most values in versionsOwned, these stay with the profile across all platforms. | No |
| currentSeasonHash | integer (uint32) | If populated, this is a reference to the season that is currently active. | No |
| currentSeasonRewardPowerCap | integer (int32) | If populated, this is the reward power cap for the current season. | No |
| activeEventCardHash | integer (uint32) | If populated, this is a reference to the event card that is currently active. | No |
| currentGuardianRank | integer (int32) | The 'current' Guardian Rank value, which starts at rank 1. This rank value will drop at the start of a new season to your 'renewed' rank from the previous season. | No |
| lifetimeHighestGuardianRank | integer (int32) | The 'lifetime highest' Guardian Rank value, which starts at rank 1. This rank value should never go down. | No |
| renewedGuardianRank | integer (int32) | The seasonal 'renewed' Guardian Rank value. This rank value resets at the start of each new season to the highest-earned non-advanced rank. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Entities.Profiles.DestinyProfileComponent object
const example = {
  userInfo: null,
  dateLastPlayed: "example value",
  versionsOwned: 123,
  characterIds: [],
  seasonHashes: [],
  // ... more properties
};
```

### Python
```python
# Example Destiny.Entities.Profiles.DestinyProfileComponent object
example = {
    "userInfo": None,
    "dateLastPlayed": "example value",
    "versionsOwned": 123,
    "characterIds": [],
    "seasonHashes": [],
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.GuardianRanks.DestinyGuardianRankDefinition**: Referenced in this entity
- **Destiny.Definitions.Seasons.DestinyEventCardDefinition**: Referenced in this entity
- **Destiny.Definitions.Seasons.DestinySeasonDefinition**: Referenced in this entity
- **Destiny.DestinyGameVersions**: Referenced in this entity
- **User.UserInfoCard**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Entities.Profiles.DestinyProfileComponent":   {
      "description": "The most essential summary information about a Profile (in Destiny 1, we called these \"Accounts\").",
      "type": "object",
      "properties": {
          "userInfo": {
              "description": "If you need to render the Profile (their platform name, icon, etc...) somewhere, this property contains that information.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/User.UserInfoCard"
                  }
              ]
          },
          "dateLastPlayed": {
              "format": "date-time",
              "description": "The last time the user played with any character on this Profile.",
              "type": "string"
          },
          "versionsOwned": {
              "format": "int32",
              "description": "If you want to know what expansions they own, this will contain that data.\r\n IMPORTANT: This field may not return the data you're interested in for Cross-Saved users. It returns the last ownership data we saw for this account - which is to say, what they've purchased on the platform on which they last played, which now could be a different platform.\r\n If you don't care about per-platform ownership and only care about whatever platform it seems they are playing on most recently, then this should be \"good enough.\" Otherwise, this should be considered deprecated. We do not have a good alternative to provide at this time with platform specific ownership data for DLC.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyGameVersions"
              }
          },
          "characterIds": {
              "description": "A list of the character IDs, for further querying on your part.",
              "type": "array",
              "items": {
                  "format": "int64",
                  "type": "integer"
              }
          },
          "seasonHashes": {
              "description": "A list of seasons that this profile owns. Unlike versionsOwned, these stay with the profile across Platforms, and thus will be valid.\r\n It turns out that Stadia Pro subscriptions will give access to seasons but only while playing on Stadia and with an active subscription. So some users (users who have Stadia Pro but choose to play on some other platform) won't see these as available: it will be whatever seasons are available for the platform on which they last played.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Seasons.DestinySeasonDefinition"
              }
          },
          "eventCardHashesOwned": {
              "description": "A list of hashes for event cards that a profile owns. Unlike most values in versionsOwned, these stay with the profile across all platforms.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Seasons.DestinyEventCardDefinition"
              }
          },
          "currentSeasonHash": {
              "format": "uint32",
              "description": "If populated, this is a reference to the season that is currently active.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Seasons.DestinySeasonDefinition"
              }
          },
          "currentSeasonRewardPowerCap": {
              "format": "int32",
              "description": "If populated, this is the reward power cap for the current season.",
              "type": "integer"
          },
          "activeEventCardHash": {
              "format": "uint32",
              "description": "If populated, this is a reference to the event card that is currently active.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Seasons.DestinyEventCardDefinition"
              }
          },
          "currentGuardianRank": {
              "format": "int32",
              "description": "The 'current' Guardian Rank value, which starts at rank 1. This rank value will drop at the start of a new season to your 'renewed' rank from the previous season.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.GuardianRanks.DestinyGuardianRankDefinition"
              }
          },
          "lifetimeHighestGuardianRank": {
              "format": "int32",
              "description": "The 'lifetime highest' Guardian Rank value, which starts at rank 1. This rank value should never go down.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.GuardianRanks.DestinyGuardianRankDefinition"
              }
          },
          "renewedGuardianRank": {
              "format": "int32",
              "description": "The seasonal 'renewed' Guardian Rank value. This rank value resets at the start of each new season to the highest-earned non-advanced rank.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.GuardianRanks.DestinyGuardianRankDefinition"
              }
          }
      },
      "x-destiny-component-type-dependency": "Profiles"
  }
}
```
