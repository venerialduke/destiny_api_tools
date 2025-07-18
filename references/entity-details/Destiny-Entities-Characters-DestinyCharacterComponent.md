# Destiny.Entities.Characters.DestinyCharacterComponent

## Entity Information
- **Entity Name**: Destiny.Entities.Characters.DestinyCharacterComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
This component contains base properties of the character. You'll probably want to always request this component, but hey you do you.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| membershipId | integer (int64) | Every Destiny Profile has a membershipId. This is provided on the character as well for convenience. | No |
| membershipType | integer (int32) | membershipType tells you the platform on which the character plays. Examine the BungieMembershipType enumeration for possible values. | No |
| characterId | integer (int64) | The unique identifier for the character. | No |
| dateLastPlayed | string (date-time) | The last date that the user played Destiny. | No |
| minutesPlayedThisSession | integer (int64) | If the user is currently playing, this is how long they've been playing. | No |
| minutesPlayedTotal | integer (int64) | If this value is 525,600, then they played Destiny for a year. Or they're a very dedicated Rent fan. Note that this includes idle time, not just time spent actually in activities shooting things. | No |
| light | integer (int32) | The user's calculated "Light Level". Light level is an indicator of your power that mostly matters in the end game, once you've reached the maximum character level: it's a level that's dependent on the average Attack/Defense power of your items. | No |
| stats | object | Your character's stats, such as Agility, Resilience, etc... *not* historical stats.
You'll have to call a different endpoint for those. | No |
| raceHash | integer (uint32) | Use this hash to look up the character's DestinyRaceDefinition. | No |
| genderHash | integer (uint32) | Use this hash to look up the character's DestinyGenderDefinition. | No |
| classHash | integer (uint32) | Use this hash to look up the character's DestinyClassDefinition. | No |
| raceType | integer (int32) | Mostly for historical purposes at this point, this is an enumeration for the character's race.
It'll be preferable in the general case to look up the related definition: but for some people this was too convenient to remove. | No |
| classType | integer (int32) | Mostly for historical purposes at this point, this is an enumeration for the character's class.
It'll be preferable in the general case to look up the related definition: but for some people this was too convenient to remove. | No |
| genderType | integer (int32) | Mostly for historical purposes at this point, this is an enumeration for the character's Gender.
It'll be preferable in the general case to look up the related definition: but for some people this was too convenient to remove. And yeah, it's an enumeration and not a boolean. Fight me. | No |
| emblemPath | string | A shortcut path to the user's currently equipped emblem image. If you're just showing summary info for a user, this is more convenient than examining their equipped emblem and looking up the definition. | No |
| emblemBackgroundPath | string | A shortcut path to the user's currently equipped emblem background image. If you're just showing summary info for a user, this is more convenient than examining their equipped emblem and looking up the definition. | No |
| emblemHash | integer (uint32) | The hash of the currently equipped emblem for the user. Can be used to look up the DestinyInventoryItemDefinition. | No |
| emblemColor | object | A shortcut for getting the background color of the user's currently equipped emblem without having to do a DestinyInventoryItemDefinition lookup. | No |
| levelProgression | object | The progression that indicates your character's level. Not their light level, but their character level: you know, the thing you max out a couple hours in and then ignore for the sake of light level. | No |
| baseCharacterLevel | integer (int32) | The "base" level of your character, not accounting for any light level. | No |
| percentToNextLevel | number (float) | A number between 0 and 100, indicating the whole and fractional % remaining to get to the next character level. | No |
| titleRecordHash | integer (uint32) | If this Character has a title assigned to it, this is the identifier of the DestinyRecordDefinition that has that title information. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Entities.Characters.DestinyCharacterComponent object
const example = {
  membershipId: 123,
  membershipType: 123,
  characterId: 123,
  dateLastPlayed: "example value",
  minutesPlayedThisSession: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Entities.Characters.DestinyCharacterComponent object
example = {
    "membershipId": 123,
    "membershipType": 123,
    "characterId": 123,
    "dateLastPlayed": "example value",
    "minutesPlayedThisSession": 123,
    # ... more properties
}
```

## Related Entities
- **BungieMembershipType**: Referenced in this entity
- **Destiny.Definitions.DestinyClassDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyGenderDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyRaceDefinition**: Referenced in this entity
- **Destiny.Definitions.Records.DestinyRecordDefinition**: Referenced in this entity
- **Destiny.DestinyClass**: Referenced in this entity
- **Destiny.DestinyGender**: Referenced in this entity
- **Destiny.DestinyProgression**: Referenced in this entity
- **Destiny.DestinyRace**: Referenced in this entity
- **Destiny.Misc.DestinyColor**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Entities.Characters.DestinyCharacterComponent":   {
      "description": "This component contains base properties of the character. You'll probably want to always request this component, but hey you do you.",
      "type": "object",
      "properties": {
          "membershipId": {
              "format": "int64",
              "description": "Every Destiny Profile has a membershipId. This is provided on the character as well for convenience.",
              "type": "integer"
          },
          "membershipType": {
              "format": "int32",
              "description": "membershipType tells you the platform on which the character plays. Examine the BungieMembershipType enumeration for possible values.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/BungieMembershipType"
              }
          },
          "characterId": {
              "format": "int64",
              "description": "The unique identifier for the character.",
              "type": "integer"
          },
          "dateLastPlayed": {
              "format": "date-time",
              "description": "The last date that the user played Destiny.",
              "type": "string"
          },
          "minutesPlayedThisSession": {
              "format": "int64",
              "description": "If the user is currently playing, this is how long they've been playing.",
              "type": "integer"
          },
          "minutesPlayedTotal": {
              "format": "int64",
              "description": "If this value is 525,600, then they played Destiny for a year. Or they're a very dedicated Rent fan. Note that this includes idle time, not just time spent actually in activities shooting things.",
              "type": "integer"
          },
          "light": {
              "format": "int32",
              "description": "The user's calculated \"Light Level\". Light level is an indicator of your power that mostly matters in the end game, once you've reached the maximum character level: it's a level that's dependent on the average Attack/Defense power of your items.",
              "type": "integer"
          },
          "stats": {
              "description": "Your character's stats, such as Agility, Resilience, etc... *not* historical stats.\r\nYou'll have to call a different endpoint for those.",
              "type": "object",
              "additionalProperties": {
                  "format": "int32",
                  "type": "integer"
              }
          },
          "raceHash": {
              "format": "uint32",
              "description": "Use this hash to look up the character's DestinyRaceDefinition.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyRaceDefinition"
              }
          },
          "genderHash": {
              "format": "uint32",
              "description": "Use this hash to look up the character's DestinyGenderDefinition.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyGenderDefinition"
              }
          },
          "classHash": {
              "format": "uint32",
              "description": "Use this hash to look up the character's DestinyClassDefinition.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyClassDefinition"
              }
          },
          "raceType": {
              "format": "int32",
              "description": "Mostly for historical purposes at this point, this is an enumeration for the character's race.\r\nIt'll be preferable in the general case to look up the related definition: but for some people this was too convenient to remove.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyRace"
              }
          },
          "classType": {
              "format": "int32",
              "description": "Mostly for historical purposes at this point, this is an enumeration for the character's class.\r\nIt'll be preferable in the general case to look up the related definition: but for some people this was too convenient to remove.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyClass"
              }
          },
          "genderType": {
              "format": "int32",
              "description": "Mostly for historical purposes at this point, this is an enumeration for the character's Gender.\r\nIt'll be preferable in the general case to look up the related definition: but for some people this was too convenient to remove. And yeah, it's an enumeration and not a boolean. Fight me.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyGender"
              }
          },
          "emblemPath": {
              "description": "A shortcut path to the user's currently equipped emblem image. If you're just showing summary info for a user, this is more convenient than examining their equipped emblem and looking up the definition.",
              "type": "string"
          },
          "emblemBackgroundPath": {
              "description": "A shortcut path to the user's currently equipped emblem background image. If you're just showing summary info for a user, this is more convenient than examining their equipped emblem and looking up the definition.",
              "type": "string"
          },
          "emblemHash": {
              "format": "uint32",
              "description": "The hash of the currently equipped emblem for the user. Can be used to look up the DestinyInventoryItemDefinition.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "emblemColor": {
              "description": "A shortcut for getting the background color of the user's currently equipped emblem without having to do a DestinyInventoryItemDefinition lookup.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Misc.DestinyColor"
                  }
              ]
          },
          "levelProgression": {
              "description": "The progression that indicates your character's level. Not their light level, but their character level: you know, the thing you max out a couple hours in and then ignore for the sake of light level.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.DestinyProgression"
                  }
              ]
          },
          "baseCharacterLevel": {
              "format": "int32",
              "description": "The \"base\" level of your character, not accounting for any light level.",
              "type": "integer"
          },
          "percentToNextLevel": {
              "format": "float",
              "description": "A number between 0 and 100, indicating the whole and fractional % remaining to get to the next character level.",
              "type": "number"
          },
          "titleRecordHash": {
              "format": "uint32",
              "description": "If this Character has a title assigned to it, this is the identifier of the DestinyRecordDefinition that has that title information.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Records.DestinyRecordDefinition"
              }
          }
      },
      "x-destiny-component-type-dependency": "Characters"
  }
}
```
