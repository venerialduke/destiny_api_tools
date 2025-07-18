# Destiny.DestinyActivity

## Entity Information
- **Entity Name**: Destiny.DestinyActivity
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Represents the "Live" data that we can obtain about a Character's status with a specific Activity. This will tell you whether the character can participate in the activity, as well as some other basic mutable information. 
Meant to be combined with static DestinyActivityDefinition data for a full picture of the Activity.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| activityHash | integer (uint32) | The hash identifier of the Activity. Use this to look up the DestinyActivityDefinition of the activity. | No |
| isNew | boolean | If true, then the activity should have a "new" indicator in the Director UI. | No |
| canLead | boolean | If true, the user is allowed to lead a Fireteam into this activity. | No |
| canJoin | boolean | If true, the user is allowed to join with another Fireteam in this activity. | No |
| isCompleted | boolean | If true, we both have the ability to know that the user has completed this activity and they have completed it. Unfortunately, we can't necessarily know this for all activities. As such, this should probably only be used if you already know in advance which specific activities you wish to check. | No |
| isVisible | boolean | If true, the user should be able to see this activity. | No |
| displayLevel | integer (int32) | The difficulty level of the activity, if applicable. | No |
| recommendedLight | integer (int32) | The recommended light level for the activity, if applicable. | No |
| difficultyTier | integer (int32) | A DestinyActivityDifficultyTier enum value indicating the difficulty of the activity. | No |
| challenges | Array[Destiny.Challenges.DestinyChallengeStatus] |  | No |
| modifierHashes | Array[integer] | If the activity has modifiers, this will be the list of modifiers that all variants have in common. Perform lookups against DestinyActivityModifierDefinition which defines the modifier being applied to get at the modifier data.
Note that, in the DestiyActivityDefinition, you will see many more modifiers than this being referred to: those are all *possible* modifiers for the activity, not the active ones. Use only the active ones to match what's really live. | No |
| booleanActivityOptions | object | The set of activity options for this activity, keyed by an identifier that's unique for this activity (not guaranteed to be unique between or across all activities, though should be unique for every *variant* of a given *conceptual* activity: for instance, the original D2 Raid has many variant DestinyActivityDefinitions. While other activities could potentially have the same option hashes, for any given D2 base Raid variant the hash will be unique).
As a concrete example of this data, the hashes you get for Raids will correspond to the currently active "Challenge Mode".
We don't have any human readable information for these, but saavy 3rd party app users could manually associate the key (a hash identifier for the "option" that is enabled/disabled) and the value (whether it's enabled or disabled presently)
On our side, we don't necessarily even know what these are used for (the game designers know, but we don't), and we have no human readable data for them. In order to use them, you will have to do some experimentation. | No |
| loadoutRequirementIndex | integer (int32) | If returned, this is the index into the DestinyActivityDefinition's "loadouts" property, indicating the currently active loadout requirements. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.DestinyActivity object
const example = {
  activityHash: 123,
  isNew: true,
  canLead: true,
  canJoin: true,
  isCompleted: true,
  // ... more properties
};
```

### Python
```python
# Example Destiny.DestinyActivity object
example = {
    "activityHash": 123,
    "isNew": True,
    "canLead": True,
    "canJoin": True,
    "isCompleted": True,
    # ... more properties
}
```

## Related Entities
- **Destiny.Challenges.DestinyChallengeStatus**: Referenced in this entity
- **Destiny.Definitions.ActivityModifiers.DestinyActivityModifierDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyActivityDefinition**: Referenced in this entity
- **Destiny.DestinyActivityDifficultyTier**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyActivity":   {
      "description": "Represents the \"Live\" data that we can obtain about a Character's status with a specific Activity. This will tell you whether the character can participate in the activity, as well as some other basic mutable information. \r\nMeant to be combined with static DestinyActivityDefinition data for a full picture of the Activity.",
      "type": "object",
      "properties": {
          "activityHash": {
              "format": "uint32",
              "description": "The hash identifier of the Activity. Use this to look up the DestinyActivityDefinition of the activity.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityDefinition"
              }
          },
          "isNew": {
              "description": "If true, then the activity should have a \"new\" indicator in the Director UI.",
              "type": "boolean"
          },
          "canLead": {
              "description": "If true, the user is allowed to lead a Fireteam into this activity.",
              "type": "boolean"
          },
          "canJoin": {
              "description": "If true, the user is allowed to join with another Fireteam in this activity.",
              "type": "boolean"
          },
          "isCompleted": {
              "description": "If true, we both have the ability to know that the user has completed this activity and they have completed it. Unfortunately, we can't necessarily know this for all activities. As such, this should probably only be used if you already know in advance which specific activities you wish to check.",
              "type": "boolean"
          },
          "isVisible": {
              "description": "If true, the user should be able to see this activity.",
              "type": "boolean"
          },
          "displayLevel": {
              "format": "int32",
              "description": "The difficulty level of the activity, if applicable.",
              "type": "integer"
          },
          "recommendedLight": {
              "format": "int32",
              "description": "The recommended light level for the activity, if applicable.",
              "type": "integer"
          },
          "difficultyTier": {
              "format": "int32",
              "description": "A DestinyActivityDifficultyTier enum value indicating the difficulty of the activity.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyActivityDifficultyTier"
              }
          },
          "challenges": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Challenges.DestinyChallengeStatus"
              }
          },
          "modifierHashes": {
              "description": "If the activity has modifiers, this will be the list of modifiers that all variants have in common. Perform lookups against DestinyActivityModifierDefinition which defines the modifier being applied to get at the modifier data.\r\nNote that, in the DestiyActivityDefinition, you will see many more modifiers than this being referred to: those are all *possible* modifiers for the activity, not the active ones. Use only the active ones to match what's really live.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.ActivityModifiers.DestinyActivityModifierDefinition"
              }
          },
          "booleanActivityOptions": {
              "description": "The set of activity options for this activity, keyed by an identifier that's unique for this activity (not guaranteed to be unique between or across all activities, though should be unique for every *variant* of a given *conceptual* activity: for instance, the original D2 Raid has many variant DestinyActivityDefinitions. While other activities could potentially have the same option hashes, for any given D2 base Raid variant the hash will be unique).\r\nAs a concrete example of this data, the hashes you get for Raids will correspond to the currently active \"Challenge Mode\".\r\nWe don't have any human readable information for these, but saavy 3rd party app users could manually associate the key (a hash identifier for the \"option\" that is enabled/disabled) and the value (whether it's enabled or disabled presently)\r\nOn our side, we don't necessarily even know what these are used for (the game designers know, but we don't), and we have no human readable data for them. In order to use them, you will have to do some experimentation.",
              "type": "object",
              "additionalProperties": {
                  "type": "boolean"
              }
          },
          "loadoutRequirementIndex": {
              "format": "int32",
              "description": "If returned, this is the index into the DestinyActivityDefinition's \"loadouts\" property, indicating the currently active loadout requirements.",
              "type": "integer"
          }
      }
  }
}
```
