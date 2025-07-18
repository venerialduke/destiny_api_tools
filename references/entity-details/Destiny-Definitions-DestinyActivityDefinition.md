# Destiny.Definitions.DestinyActivityDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyActivityDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
The static data about Activities in Destiny 2.
Note that an Activity must be combined with an ActivityMode to know - from a Gameplay perspective - what the user is "Playing".
In most PvE activities, this is fairly straightforward. A Story Activity can only be played in the Story Activity Mode.
However, in PvP activities, the Activity alone only tells you the map being played, or the Playlist that the user chose to enter. You'll need to know the Activity Mode they're playing to know that they're playing Mode X on Map Y.
Activity Definitions tell a great deal of information about what *could* be relevant to a user: what rewards they can earn, what challenges could be performed, what modifiers could be applied. To figure out which of these properties is actually live, you'll need to combine the definition with "Live" data from one of the Destiny endpoints.
Activities also have Activity Types, but unfortunately in Destiny 2 these are even less reliable of a source of information than they were in Destiny 1. I will be looking into ways to provide more reliable sources for type information as time goes on, but for now we're going to have to deal with the limitations. See DestinyActivityTypeDefinition for more information.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | object | The title, subtitle, and icon for the activity. We do a little post-processing on this to try and account for Activities where the designers have left this data too minimal to determine what activity is actually being played. | No |
| originalDisplayProperties | object | The unadulterated form of the display properties, as they ought to be shown in the Director (if the activity appears in the director). | No |
| selectionScreenDisplayProperties | object | The title, subtitle, and icon for the activity as determined by Selection Screen data, if there is any for this activity. There won't be data in this field if the activity is never shown in a selection/options screen. | No |
| releaseIcon | string | If the activity has an icon associated with a specific release (such as a DLC), this is the path to that release's icon. | No |
| releaseTime | integer (int32) | If the activity will not be visible until a specific and known time, this will be the seconds since the Epoch when it will become visible. | No |
| activityLightLevel | integer (int32) | The recommended light level for this activity. | No |
| destinationHash | integer (uint32) | The hash identifier for the Destination on which this Activity is played. Use it to look up the DestinyDestinationDefinition for human readable info about the destination. A Destination can be thought of as a more specific location than a "Place". For instance, if the "Place" is Earth, the "Destination" would be a specific city or region on Earth. | No |
| placeHash | integer (uint32) | The hash identifier for the "Place" on which this Activity is played. Use it to look up the DestinyPlaceDefinition for human readable info about the Place. A Place is the largest-scoped concept for location information. For instance, if the "Place" is Earth, the "Destination" would be a specific city or region on Earth. | No |
| activityTypeHash | integer (uint32) | The hash identifier for the Activity Type of this Activity. You may use it to look up the DestinyActivityTypeDefinition for human readable info, but be forewarned: Playlists and many PVP Map Activities will map to generic Activity Types. You'll have to use your knowledge of the Activity Mode being played to get more specific information about what the user is playing. | No |
| tier | integer (int32) | The difficulty tier of the activity. | No |
| pgcrImage | string | When Activities are completed, we generate a "Post-Game Carnage Report", or PGCR, with details about what happened in that activity (how many kills someone got, which team won, etc...) We use this image as the background when displaying PGCR information, and often use it when we refer to the Activity in general. | No |
| rewards | Array[Destiny.Definitions.DestinyActivityRewardDefinition] | The expected possible rewards for the activity. These rewards may or may not be accessible for an individual player based on their character state, the account state, and even the game's state overall. But it is a useful reference for possible rewards you can earn in the activity. These match up to rewards displayed when you hover over the Activity in the in-game Director, and often refer to Placeholder or "Dummy" items: items that tell you what you can earn in vague terms rather than what you'll specifically be earning (partly because the game doesn't even know what you'll earn specifically until you roll for it at the end) | No |
| modifiers | Array[Destiny.Definitions.DestinyActivityModifierReferenceDefinition] | Activities can have Modifiers, as defined in DestinyActivityModifierDefinition. These are references to the modifiers that *can* be applied to that activity, along with data that we use to determine if that modifier is actually active at any given point in time. | No |
| isPlaylist | boolean | If True, this Activity is actually a Playlist that refers to multiple possible specific Activities and Activity Modes. For instance, a Crucible Playlist may have references to multiple Activities (Maps) with multiple Activity Modes (specific PvP gameplay modes). If this is true, refer to the playlistItems property for the specific entries in the playlist. | No |
| challenges | Array[Destiny.Definitions.DestinyActivityChallengeDefinition] | An activity can have many Challenges, of which any subset of them may be active for play at any given period of time. This gives the information about the challenges and data that we use to understand when they're active and what rewards they provide. Sadly, at the moment there's no central definition for challenges: much like "Skulls" were in Destiny 1, these are defined on individual activities and there can be many duplicates/near duplicates across the Destiny 2 ecosystem. I have it in mind to centralize these in a future revision of the API, but we are out of time. | No |
| optionalUnlockStrings | Array[Destiny.Definitions.DestinyActivityUnlockStringDefinition] | If there are status strings related to the activity and based on internal state of the game, account, or character, then this will be the definition of those strings and the states needed in order for the strings to be shown. | No |
| activityFamilyHashes | Array[integer] |  | No |
| traitHashes | Array[integer] |  | No |
| requirements | Destiny.Definitions.DestinyActivityRequirementsBlock |  | No |
| difficultyTierCollectionHash | integer (uint32) |  | No |
| selectableSkullCollectionHashes | Array[integer] |  | No |
| playlistItems | Array[Destiny.Definitions.DestinyActivityPlaylistItemDefinition] | Represents all of the possible activities that could be played in the Playlist, along with information that we can use to determine if they are active at the present time. | No |
| activityGraphList | Array[Destiny.Definitions.DestinyActivityGraphListEntryDefinition] | Unfortunately, in practice this is almost never populated. In theory, this is supposed to tell which Activity Graph to show if you bring up the director while in this activity. | No |
| matchmaking | object | This block of data provides information about the Activity's matchmaking attributes: how many people can join and such. | No |
| guidedGame | object | This block of data, if it exists, provides information about the guided game experience and restrictions for this activity. If it doesn't exist, the game is not able to be played as a guided game. | No |
| directActivityModeHash | integer (uint32) | If this activity had an activity mode directly defined on it, this will be the hash of that mode. | No |
| directActivityModeType | integer (int32) | If the activity had an activity mode directly defined on it, this will be the enum value of that mode. | No |
| loadouts | Array[Destiny.Definitions.DestinyActivityLoadoutRequirementSet] | The set of all possible loadout requirements that could be active for this activity. Only one will be active at any given time, and you can discover which one through activity-associated data such as Milestones that have activity info on them. | No |
| activityModeHashes | Array[integer] | The hash identifiers for Activity Modes relevant to this activity.  Note that if this is a playlist, the specific playlist entry chosen will determine the actual activity modes that end up being relevant. | No |
| activityModeTypes | Array[integer] | The activity modes - if any - in enum form. Because we can't seem to escape the enums. | No |
| isPvP | boolean | If true, this activity is a PVP activity or playlist. | No |
| insertionPoints | Array[Destiny.Definitions.DestinyActivityInsertionPointDefinition] | The list of phases or points of entry into an activity, along with information we can use to determine their gating and availability. | No |
| activityLocationMappings | Array[Destiny.Constants.DestinyEnvironmentLocationMapping] | A list of location mappings that are affected by this activity. Pulled out of DestinyLocationDefinitions for our/your lookup convenience. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyActivityDefinition object
const example = {
  displayProperties: null,
  originalDisplayProperties: null,
  selectionScreenDisplayProperties: null,
  releaseIcon: "example value",
  releaseTime: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyActivityDefinition object
example = {
    "displayProperties": None,
    "originalDisplayProperties": None,
    "selectionScreenDisplayProperties": None,
    "releaseIcon": "example value",
    "releaseTime": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Constants.DestinyEnvironmentLocationMapping**: Referenced in this entity
- **Destiny.Definitions.Activities.DestinyActivityDifficultyTierCollectionDefinition**: Referenced in this entity
- **Destiny.Definitions.Activities.DestinyActivityFamilyDefinition**: Referenced in this entity
- **Destiny.Definitions.Activities.DestinyActivitySelectableSkullCollectionDefinition**: Referenced in this entity
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyActivityChallengeDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyActivityGraphListEntryDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyActivityGuidedBlockDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyActivityInsertionPointDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyActivityLoadoutRequirementSet**: Referenced in this entity
- **Destiny.Definitions.DestinyActivityMatchmakingBlockDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyActivityModeDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyActivityModifierReferenceDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyActivityPlaylistItemDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyActivityRequirementsBlock**: Referenced in this entity
- **Destiny.Definitions.DestinyActivityRewardDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyActivityTypeDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyActivityUnlockStringDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyDestinationDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyPlaceDefinition**: Referenced in this entity
- **Destiny.Definitions.Traits.DestinyTraitDefinition**: Referenced in this entity
- **Destiny.HistoricalStats.Definitions.DestinyActivityModeType**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyActivityDefinition":   {
      "description": "The static data about Activities in Destiny 2.\r\nNote that an Activity must be combined with an ActivityMode to know - from a Gameplay perspective - what the user is \"Playing\".\r\nIn most PvE activities, this is fairly straightforward. A Story Activity can only be played in the Story Activity Mode.\r\nHowever, in PvP activities, the Activity alone only tells you the map being played, or the Playlist that the user chose to enter. You'll need to know the Activity Mode they're playing to know that they're playing Mode X on Map Y.\r\nActivity Definitions tell a great deal of information about what *could* be relevant to a user: what rewards they can earn, what challenges could be performed, what modifiers could be applied. To figure out which of these properties is actually live, you'll need to combine the definition with \"Live\" data from one of the Destiny endpoints.\r\nActivities also have Activity Types, but unfortunately in Destiny 2 these are even less reliable of a source of information than they were in Destiny 1. I will be looking into ways to provide more reliable sources for type information as time goes on, but for now we're going to have to deal with the limitations. See DestinyActivityTypeDefinition for more information.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "description": "The title, subtitle, and icon for the activity. We do a little post-processing on this to try and account for Activities where the designers have left this data too minimal to determine what activity is actually being played.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
                  }
              ]
          },
          "originalDisplayProperties": {
              "description": "The unadulterated form of the display properties, as they ought to be shown in the Director (if the activity appears in the director).",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
                  }
              ]
          },
          "selectionScreenDisplayProperties": {
              "description": "The title, subtitle, and icon for the activity as determined by Selection Screen data, if there is any for this activity. There won't be data in this field if the activity is never shown in a selection/options screen.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
                  }
              ]
          },
          "releaseIcon": {
              "description": "If the activity has an icon associated with a specific release (such as a DLC), this is the path to that release's icon.",
              "type": "string"
          },
          "releaseTime": {
              "format": "int32",
              "description": "If the activity will not be visible until a specific and known time, this will be the seconds since the Epoch when it will become visible.",
              "type": "integer"
          },
          "activityLightLevel": {
              "format": "int32",
              "description": "The recommended light level for this activity.",
              "type": "integer"
          },
          "destinationHash": {
              "format": "uint32",
              "description": "The hash identifier for the Destination on which this Activity is played. Use it to look up the DestinyDestinationDefinition for human readable info about the destination. A Destination can be thought of as a more specific location than a \"Place\". For instance, if the \"Place\" is Earth, the \"Destination\" would be a specific city or region on Earth.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyDestinationDefinition"
              }
          },
          "placeHash": {
              "format": "uint32",
              "description": "The hash identifier for the \"Place\" on which this Activity is played. Use it to look up the DestinyPlaceDefinition for human readable info about the Place. A Place is the largest-scoped concept for location information. For instance, if the \"Place\" is Earth, the \"Destination\" would be a specific city or region on Earth.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyPlaceDefinition"
              }
          },
          "activityTypeHash": {
              "format": "uint32",
              "description": "The hash identifier for the Activity Type of this Activity. You may use it to look up the DestinyActivityTypeDefinition for human readable info, but be forewarned: Playlists and many PVP Map Activities will map to generic Activity Types. You'll have to use your knowledge of the Activity Mode being played to get more specific information about what the user is playing.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityTypeDefinition"
              }
          },
          "tier": {
              "format": "int32",
              "description": "The difficulty tier of the activity.",
              "type": "integer"
          },
          "pgcrImage": {
              "description": "When Activities are completed, we generate a \"Post-Game Carnage Report\", or PGCR, with details about what happened in that activity (how many kills someone got, which team won, etc...) We use this image as the background when displaying PGCR information, and often use it when we refer to the Activity in general.",
              "type": "string"
          },
          "rewards": {
              "description": "The expected possible rewards for the activity. These rewards may or may not be accessible for an individual player based on their character state, the account state, and even the game's state overall. But it is a useful reference for possible rewards you can earn in the activity. These match up to rewards displayed when you hover over the Activity in the in-game Director, and often refer to Placeholder or \"Dummy\" items: items that tell you what you can earn in vague terms rather than what you'll specifically be earning (partly because the game doesn't even know what you'll earn specifically until you roll for it at the end)",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityRewardDefinition"
              }
          },
          "modifiers": {
              "description": "Activities can have Modifiers, as defined in DestinyActivityModifierDefinition. These are references to the modifiers that *can* be applied to that activity, along with data that we use to determine if that modifier is actually active at any given point in time.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityModifierReferenceDefinition"
              }
          },
          "isPlaylist": {
              "description": "If True, this Activity is actually a Playlist that refers to multiple possible specific Activities and Activity Modes. For instance, a Crucible Playlist may have references to multiple Activities (Maps) with multiple Activity Modes (specific PvP gameplay modes). If this is true, refer to the playlistItems property for the specific entries in the playlist.",
              "type": "boolean"
          },
          "challenges": {
              "description": "An activity can have many Challenges, of which any subset of them may be active for play at any given period of time. This gives the information about the challenges and data that we use to understand when they're active and what rewards they provide. Sadly, at the moment there's no central definition for challenges: much like \"Skulls\" were in Destiny 1, these are defined on individual activities and there can be many duplicates/near duplicates across the Destiny 2 ecosystem. I have it in mind to centralize these in a future revision of the API, but we are out of time.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityChallengeDefinition"
              }
          },
          "optionalUnlockStrings": {
              "description": "If there are status strings related to the activity and based on internal state of the game, account, or character, then this will be the definition of those strings and the states needed in order for the strings to be shown.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityUnlockStringDefinition"
              }
          },
          "activityFamilyHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Activities.DestinyActivityFamilyDefinition"
              }
          },
          "traitHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Traits.DestinyTraitDefinition"
              }
          },
          "requirements": {
              "$ref": "#/definitions/Destiny.Definitions.DestinyActivityRequirementsBlock"
          },
          "difficultyTierCollectionHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Activities.DestinyActivityDifficultyTierCollectionDefinition"
              }
          },
          "selectableSkullCollectionHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Activities.DestinyActivitySelectableSkullCollectionDefinition"
              }
          },
          "playlistItems": {
              "description": "Represents all of the possible activities that could be played in the Playlist, along with information that we can use to determine if they are active at the present time.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityPlaylistItemDefinition"
              }
          },
          "activityGraphList": {
              "description": "Unfortunately, in practice this is almost never populated. In theory, this is supposed to tell which Activity Graph to show if you bring up the director while in this activity.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityGraphListEntryDefinition"
              }
          },
          "matchmaking": {
              "description": "This block of data provides information about the Activity's matchmaking attributes: how many people can join and such.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.DestinyActivityMatchmakingBlockDefinition"
                  }
              ]
          },
          "guidedGame": {
              "description": "This block of data, if it exists, provides information about the guided game experience and restrictions for this activity. If it doesn't exist, the game is not able to be played as a guided game.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.DestinyActivityGuidedBlockDefinition"
                  }
              ]
          },
          "directActivityModeHash": {
              "format": "uint32",
              "description": "If this activity had an activity mode directly defined on it, this will be the hash of that mode.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityModeDefinition"
              }
          },
          "directActivityModeType": {
              "format": "int32",
              "description": "If the activity had an activity mode directly defined on it, this will be the enum value of that mode.",
              "enum": [
                  "0",
                  "2",
                  "3",
                  "4",
                  "5",
                  "6",
                  "7",
                  "9",
                  "10",
                  "11",
                  "12",
                  "13",
                  "15",
                  "16",
                  "17",
                  "18",
                  "19",
                  "20",
                  "21",
                  "22",
                  "24",
                  "25",
                  "26",
                  "27",
                  "28",
                  "29",
                  "30",
                  "31",
                  "32",
                  "37",
                  "38",
                  "39",
                  "40",
                  "41",
                  "42",
                  "43",
                  "44",
                  "45",
                  "46",
                  "47",
                  "48",
                  "49",
                  "50",
                  "51",
                  "52",
                  "53",
                  "54",
                  "55",
                  "56",
                  "57",
                  "58",
                  "59",
                  "60",
                  "61",
                  "62",
                  "63",
                  "64",
                  "65",
                  "66",
                  "67",
                  "68",
                  "69",
                  "70",
                  "71",
                  "72",
                  "73",
                  "74",
                  "75",
                  "76",
                  "77",
                  "78",
                  "79",
                  "80",
                  "81",
                  "82",
                  "83",
                  "84",
                  "85",
                  "86",
                  "87",
                  "88",
                  "89",
                  "90",
                  "91",
                  "92"
              ],
              "type": "integer",
              "x-enum-values": [
                  {
                      "numericValue": "0",
                      "identifier": "None"
                  },
                  {
                      "numericValue": "2",
                      "identifier": "Story"
                  },
                  {
                      "numericValue": "3",
                      "identifier": "Strike"
                  },
                  {
                      "numericValue": "4",
                      "identifier": "Raid"
                  },
                  {
                      "numericValue": "5",
                      "identifier": "AllPvP"
                  },
                  {
                      "numericValue": "6",
                      "identifier": "Patrol"
                  },
                  {
                      "numericValue": "7",
                      "identifier": "AllPvE"
                  },
                  {
                      "numericValue": "9",
                      "identifier": "Reserved9"
                  },
                  {
                      "numericValue": "10",
                      "identifier": "Control"
                  },
                  {
                      "numericValue": "11",
                      "identifier": "Reserved11"
                  },
                  {
                      "numericValue": "12",
                      "identifier": "Clash",
                      "description": "Clash -> Destiny's name for Team Deathmatch. 4v4 combat, the team with the highest kills at the end of time wins."
                  },
                  {
                      "numericValue": "13",
                      "identifier": "Reserved13"
                  },
                  {
                      "numericValue": "15",
                      "identifier": "CrimsonDoubles"
                  },
                  {
                      "numericValue": "16",
                      "identifier": "Nightfall"
                  },
                  {
                      "numericValue": "17",
                      "identifier": "HeroicNightfall"
                  },
                  {
                      "numericValue": "18",
                      "identifier": "AllStrikes"
                  },
                  {
                      "numericValue": "19",
                      "identifier": "IronBanner"
                  },
                  {
                      "numericValue": "20",
                      "identifier": "Reserved20"
                  },
                  {
                      "numericValue": "21",
                      "identifier": "Reserved21"
                  },
                  {
                      "numericValue": "22",
                      "identifier": "Reserved22"
                  },
                  {
                      "numericValue": "24",
                      "identifier": "Reserved24"
                  },
                  {
                      "numericValue": "25",
                      "identifier": "AllMayhem"
                  },
                  {
                      "numericValue": "26",
                      "identifier": "Reserved26"
                  },
                  {
                      "numericValue": "27",
                      "identifier": "Reserved27"
                  },
                  {
                      "numericValue": "28",
                      "identifier": "Reserved28"
                  },
                  {
                      "numericValue": "29",
                      "identifier": "Reserved29"
                  },
                  {
                      "numericValue": "30",
                      "identifier": "Reserved30"
                  },
                  {
                      "numericValue": "31",
                      "identifier": "Supremacy"
                  },
                  {
                      "numericValue": "32",
                      "identifier": "PrivateMatchesAll"
                  },
                  {
                      "numericValue": "37",
                      "identifier": "Survival"
                  },
                  {
                      "numericValue": "38",
                      "identifier": "Countdown"
                  },
                  {
                      "numericValue": "39",
                      "identifier": "TrialsOfTheNine"
                  },
                  {
                      "numericValue": "40",
                      "identifier": "Social"
                  },
                  {
                      "numericValue": "41",
                      "identifier": "TrialsCountdown"
                  },
                  {
                      "numericValue": "42",
                      "identifier": "TrialsSurvival"
                  },
                  {
                      "numericValue": "43",
                      "identifier": "IronBannerControl"
                  },
                  {
                      "numericValue": "44",
                      "identifier": "IronBannerClash"
                  },
                  {
                      "numericValue": "45",
                      "identifier": "IronBannerSupremacy"
                  },
                  {
                      "numericValue": "46",
                      "identifier": "ScoredNightfall"
                  },
                  {
                      "numericValue": "47",
                      "identifier": "ScoredHeroicNightfall"
                  },
                  {
                      "numericValue": "48",
                      "identifier": "Rumble"
                  },
                  {
                      "numericValue": "49",
                      "identifier": "AllDoubles"
                  },
                  {
                      "numericValue": "50",
                      "identifier": "Doubles"
                  },
                  {
                      "numericValue": "51",
                      "identifier": "PrivateMatchesClash"
                  },
                  {
                      "numericValue": "52",
                      "identifier": "PrivateMatchesControl"
                  },
                  {
                      "numericValue": "53",
                      "identifier": "PrivateMatchesSupremacy"
                  },
                  {
                      "numericValue": "54",
                      "identifier": "PrivateMatchesCountdown"
                  },
                  {
                      "numericValue": "55",
                      "identifier": "PrivateMatchesSurvival"
                  },
                  {
                      "numericValue": "56",
                      "identifier": "PrivateMatchesMayhem"
                  },
                  {
                      "numericValue": "57",
                      "identifier": "PrivateMatchesRumble"
                  },
                  {
                      "numericValue": "58",
                      "identifier": "HeroicAdventure"
                  },
                  {
                      "numericValue": "59",
                      "identifier": "Showdown"
                  },
                  {
                      "numericValue": "60",
                      "identifier": "Lockdown"
                  },
                  {
                      "numericValue": "61",
                      "identifier": "Scorched"
                  },
                  {
                      "numericValue": "62",
                      "identifier": "ScorchedTeam"
                  },
                  {
                      "numericValue": "63",
                      "identifier": "Gambit"
                  },
                  {
                      "numericValue": "64",
                      "identifier": "AllPvECompetitive"
                  },
                  {
                      "numericValue": "65",
                      "identifier": "Breakthrough"
                  },
                  {
                      "numericValue": "66",
                      "identifier": "BlackArmoryRun"
                  },
                  {
                      "numericValue": "67",
                      "identifier": "Salvage"
                  },
                  {
                      "numericValue": "68",
                      "identifier": "IronBannerSalvage"
                  },
                  {
                      "numericValue": "69",
                      "identifier": "PvPCompetitive"
                  },
                  {
                      "numericValue": "70",
                      "identifier": "PvPQuickplay"
                  },
                  {
                      "numericValue": "71",
                      "identifier": "ClashQuickplay"
                  },
                  {
                      "numericValue": "72",
                      "identifier": "ClashCompetitive"
                  },
                  {
                      "numericValue": "73",
                      "identifier": "ControlQuickplay"
                  },
                  {
                      "numericValue": "74",
                      "identifier": "ControlCompetitive"
                  },
                  {
                      "numericValue": "75",
                      "identifier": "GambitPrime"
                  },
                  {
                      "numericValue": "76",
                      "identifier": "Reckoning"
                  },
                  {
                      "numericValue": "77",
                      "identifier": "Menagerie"
                  },
                  {
                      "numericValue": "78",
                      "identifier": "VexOffensive"
                  },
                  {
                      "numericValue": "79",
                      "identifier": "NightmareHunt"
                  },
                  {
                      "numericValue": "80",
                      "identifier": "Elimination"
                  },
                  {
                      "numericValue": "81",
                      "identifier": "Momentum"
                  },
                  {
                      "numericValue": "82",
                      "identifier": "Dungeon"
                  },
                  {
                      "numericValue": "83",
                      "identifier": "Sundial"
                  },
                  {
                      "numericValue": "84",
                      "identifier": "TrialsOfOsiris"
                  },
                  {
                      "numericValue": "85",
                      "identifier": "Dares"
                  },
                  {
                      "numericValue": "86",
                      "identifier": "Offensive"
                  },
                  {
                      "numericValue": "87",
                      "identifier": "LostSector"
                  },
                  {
                      "numericValue": "88",
                      "identifier": "Rift"
                  },
                  {
                      "numericValue": "89",
                      "identifier": "ZoneControl"
                  },
                  {
                      "numericValue": "90",
                      "identifier": "IronBannerRift"
                  },
                  {
                      "numericValue": "91",
                      "identifier": "IronBannerZoneControl"
                  },
                  {
                      "numericValue": "92",
                      "identifier": "Relic"
                  }
              ]
          },
          "loadouts": {
              "description": "The set of all possible loadout requirements that could be active for this activity. Only one will be active at any given time, and you can discover which one through activity-associated data such as Milestones that have activity info on them.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityLoadoutRequirementSet"
              }
          },
          "activityModeHashes": {
              "description": "The hash identifiers for Activity Modes relevant to this activity.  Note that if this is a playlist, the specific playlist entry chosen will determine the actual activity modes that end up being relevant.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityModeDefinition"
              }
          },
          "activityModeTypes": {
              "description": "The activity modes - if any - in enum form. Because we can't seem to escape the enums.",
              "type": "array",
              "items": {
                  "format": "int32",
                  "description": "For historical reasons, this list will have both D1 and D2-relevant Activity Modes in it. Please don't take this to mean that some D1-only feature is coming back!",
                  "type": "integer",
                  "x-enum-reference": {
                      "$ref": "#/components/schemas/Destiny.HistoricalStats.Definitions.DestinyActivityModeType"
                  }
              }
          },
          "isPvP": {
              "description": "If true, this activity is a PVP activity or playlist.",
              "type": "boolean"
          },
          "insertionPoints": {
              "description": "The list of phases or points of entry into an activity, along with information we can use to determine their gating and availability.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityInsertionPointDefinition"
              }
          },
          "activityLocationMappings": {
              "description": "A list of location mappings that are affected by this activity. Pulled out of DestinyLocationDefinitions for our/your lookup convenience.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Constants.DestinyEnvironmentLocationMapping"
              }
          },
          "hash": {
              "format": "uint32",
              "description": "The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.\r\nWhen entities refer to each other in Destiny content, it is this hash that they are referring to.",
              "type": "integer"
          },
          "index": {
              "format": "int32",
              "description": "The index of the entity as it was found in the investment tables.",
              "type": "integer"
          },
          "redacted": {
              "description": "If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!",
              "type": "boolean"
          }
      },
      "x-mobile-manifest-name": "Activities"
  }
}
```
