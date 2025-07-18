# Destiny.Definitions.DestinyActivityPlaylistItemDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyActivityPlaylistItemDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
If the activity is a playlist, this is the definition for a specific entry in the playlist: a single possible combination of Activity and Activity Mode that can be chosen.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| activityHash | integer (uint32) | The hash identifier of the Activity that can be played. Use it to look up the DestinyActivityDefinition. | No |
| directActivityModeHash | integer (uint32) | If this playlist entry had an activity mode directly defined on it, this will be the hash of that mode. | No |
| directActivityModeType | integer (int32) | If the playlist entry had an activity mode directly defined on it, this will be the enum value of that mode. | No |
| activityModeHashes | Array[integer] | The hash identifiers for Activity Modes relevant to this entry. | No |
| activityModeTypes | Array[integer] | The activity modes - if any - in enum form. Because we can't seem to escape the enums. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyActivityPlaylistItemDefinition object
const example = {
  activityHash: 123,
  directActivityModeHash: 123,
  directActivityModeType: 123,
  activityModeHashes: [],
  activityModeTypes: [],
};
```

### Python
```python
# Example Destiny.Definitions.DestinyActivityPlaylistItemDefinition object
example = {
    "activityHash": 123,
    "directActivityModeHash": 123,
    "directActivityModeType": 123,
    "activityModeHashes": [],
    "activityModeTypes": [],
}
```

## Related Entities
- **Destiny.Definitions.DestinyActivityDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyActivityModeDefinition**: Referenced in this entity
- **Destiny.HistoricalStats.Definitions.DestinyActivityModeType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyActivityPlaylistItemDefinition":   {
      "description": "If the activity is a playlist, this is the definition for a specific entry in the playlist: a single possible combination of Activity and Activity Mode that can be chosen.",
      "type": "object",
      "properties": {
          "activityHash": {
              "format": "uint32",
              "description": "The hash identifier of the Activity that can be played. Use it to look up the DestinyActivityDefinition.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityDefinition"
              }
          },
          "directActivityModeHash": {
              "format": "uint32",
              "description": "If this playlist entry had an activity mode directly defined on it, this will be the hash of that mode.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityModeDefinition"
              }
          },
          "directActivityModeType": {
              "format": "int32",
              "description": "If the playlist entry had an activity mode directly defined on it, this will be the enum value of that mode.",
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
          "activityModeHashes": {
              "description": "The hash identifiers for Activity Modes relevant to this entry.",
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
          }
      }
  }
}
```
