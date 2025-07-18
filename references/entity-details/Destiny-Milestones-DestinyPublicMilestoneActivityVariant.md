# Destiny.Milestones.DestinyPublicMilestoneActivityVariant

## Entity Information
- **Entity Name**: Destiny.Milestones.DestinyPublicMilestoneActivityVariant
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Represents a variant of an activity that's relevant to a milestone.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| activityHash | integer (uint32) | The hash identifier of this activity variant. Examine the activity's definition in the Manifest database to determine what makes it a distinct variant. Usually it will be difficulty level or whether or not it is a guided game variant of the activity, but theoretically it could be distinguished in any arbitrary way. | No |
| activityModeHash | integer (uint32) | The hash identifier of the most specific Activity Mode under which this activity is played. This is useful for situations where the activity in question is - for instance - a PVP map, but it's not clear what mode the PVP map is being played under. If it's a playlist, this will be less specific: but hopefully useful in some way. | No |
| activityModeType | integer (int32) | The enumeration equivalent of the most specific Activity Mode under which this activity is played. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Milestones.DestinyPublicMilestoneActivityVariant object
const example = {
  activityHash: 123,
  activityModeHash: 123,
  activityModeType: 123,
};
```

### Python
```python
# Example Destiny.Milestones.DestinyPublicMilestoneActivityVariant object
example = {
    "activityHash": 123,
    "activityModeHash": 123,
    "activityModeType": 123,
}
```

## Related Entities
- **Destiny.Definitions.DestinyActivityDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyActivityModeDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Milestones.DestinyPublicMilestoneActivityVariant":   {
      "description": "Represents a variant of an activity that's relevant to a milestone.",
      "type": "object",
      "properties": {
          "activityHash": {
              "format": "uint32",
              "description": "The hash identifier of this activity variant. Examine the activity's definition in the Manifest database to determine what makes it a distinct variant. Usually it will be difficulty level or whether or not it is a guided game variant of the activity, but theoretically it could be distinguished in any arbitrary way.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityDefinition"
              }
          },
          "activityModeHash": {
              "format": "uint32",
              "description": "The hash identifier of the most specific Activity Mode under which this activity is played. This is useful for situations where the activity in question is - for instance - a PVP map, but it's not clear what mode the PVP map is being played under. If it's a playlist, this will be less specific: but hopefully useful in some way.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityModeDefinition"
              }
          },
          "activityModeType": {
              "format": "int32",
              "description": "The enumeration equivalent of the most specific Activity Mode under which this activity is played.",
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
          }
      }
  }
}
```
