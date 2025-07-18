# Destiny.HistoricalStats.Definitions.DestinyActivityModeType

## Entity Information
- **Entity Name**: Destiny.HistoricalStats.Definitions.DestinyActivityModeType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
For historical reasons, this list will have both D1 and D2-relevant Activity Modes in it. Please don't take this to mean that some D1-only feature is coming back!

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 2 | Story |  |
| 3 | Strike |  |
| 4 | Raid |  |
| 5 | AllPvP |  |
| 6 | Patrol |  |
| 7 | AllPvE |  |
| 9 | Reserved9 |  |
| 10 | Control |  |
| 11 | Reserved11 |  |
| 12 | Clash | Clash -> Destiny's name for Team Deathmatch. 4v4 combat, the team with the highest kills at the end of time wins. |
| 13 | Reserved13 |  |
| 15 | CrimsonDoubles |  |
| 16 | Nightfall |  |
| 17 | HeroicNightfall |  |
| 18 | AllStrikes |  |
| 19 | IronBanner |  |
| 20 | Reserved20 |  |
| 21 | Reserved21 |  |
| 22 | Reserved22 |  |
| 24 | Reserved24 |  |
| 25 | AllMayhem |  |
| 26 | Reserved26 |  |
| 27 | Reserved27 |  |
| 28 | Reserved28 |  |
| 29 | Reserved29 |  |
| 30 | Reserved30 |  |
| 31 | Supremacy |  |
| 32 | PrivateMatchesAll |  |
| 37 | Survival |  |
| 38 | Countdown |  |
| 39 | TrialsOfTheNine |  |
| 40 | Social |  |
| 41 | TrialsCountdown |  |
| 42 | TrialsSurvival |  |
| 43 | IronBannerControl |  |
| 44 | IronBannerClash |  |
| 45 | IronBannerSupremacy |  |
| 46 | ScoredNightfall |  |
| 47 | ScoredHeroicNightfall |  |
| 48 | Rumble |  |
| 49 | AllDoubles |  |
| 50 | Doubles |  |
| 51 | PrivateMatchesClash |  |
| 52 | PrivateMatchesControl |  |
| 53 | PrivateMatchesSupremacy |  |
| 54 | PrivateMatchesCountdown |  |
| 55 | PrivateMatchesSurvival |  |
| 56 | PrivateMatchesMayhem |  |
| 57 | PrivateMatchesRumble |  |
| 58 | HeroicAdventure |  |
| 59 | Showdown |  |
| 60 | Lockdown |  |
| 61 | Scorched |  |
| 62 | ScorchedTeam |  |
| 63 | Gambit |  |
| 64 | AllPvECompetitive |  |
| 65 | Breakthrough |  |
| 66 | BlackArmoryRun |  |
| 67 | Salvage |  |
| 68 | IronBannerSalvage |  |
| 69 | PvPCompetitive |  |
| 70 | PvPQuickplay |  |
| 71 | ClashQuickplay |  |
| 72 | ClashCompetitive |  |
| 73 | ControlQuickplay |  |
| 74 | ControlCompetitive |  |
| 75 | GambitPrime |  |
| 76 | Reckoning |  |
| 77 | Menagerie |  |
| 78 | VexOffensive |  |
| 79 | NightmareHunt |  |
| 80 | Elimination |  |
| 81 | Momentum |  |
| 82 | Dungeon |  |
| 83 | Sundial |  |
| 84 | TrialsOfOsiris |  |
| 85 | Dares |  |
| 86 | Offensive |  |
| 87 | LostSector |  |
| 88 | Rift |  |
| 89 | ZoneControl |  |
| 90 | IronBannerRift |  |
| 91 | IronBannerZoneControl |  |
| 92 | Relic |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.HistoricalStats.Definitions.DestinyActivityModeType enumeration values
const DestinyActivityModeType = {
  None: 0,
  Story: 2,
  Strike: 3,
  // ... more values
};

// Using the enumeration
const value = DestinyActivityModeType.None;
```

### Python
```python
# Destiny.HistoricalStats.Definitions.DestinyActivityModeType enumeration values
class DestinyActivityModeType:
    NONE = 0
    STORY = 2
    STRIKE = 3
    # ... more values

# Using the enumeration
value = DestinyActivityModeType.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.HistoricalStats.Definitions.DestinyActivityModeType":   {
      "format": "int32",
      "description": "For historical reasons, this list will have both D1 and D2-relevant Activity Modes in it. Please don't take this to mean that some D1-only feature is coming back!",
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
      "type": "integer"
  }
}
```
