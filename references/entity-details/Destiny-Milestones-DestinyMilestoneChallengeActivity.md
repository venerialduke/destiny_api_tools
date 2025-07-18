# Destiny.Milestones.DestinyMilestoneChallengeActivity

## Entity Information
- **Entity Name**: Destiny.Milestones.DestinyMilestoneChallengeActivity
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinymilestonechallengeactivity data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| activityHash | integer (uint32) |  | No |
| challenges | Array[Destiny.Challenges.DestinyChallengeStatus] |  | No |
| modifierHashes | Array[integer] | If the activity has modifiers, this will be the list of modifiers that all variants have in common. Perform lookups against DestinyActivityModifierDefinition which defines the modifier being applied to get at the modifier data.
Note that, in the DestiyActivityDefinition, you will see many more modifiers than this being referred to: those are all *possible* modifiers for the activity, not the active ones. Use only the active ones to match what's really live. | No |
| booleanActivityOptions | object | The set of activity options for this activity, keyed by an identifier that's unique for this activity (not guaranteed to be unique between or across all activities, though should be unique for every *variant* of a given *conceptual* activity: for instance, the original D2 Raid has many variant DestinyActivityDefinitions. While other activities could potentially have the same option hashes, for any given D2 base Raid variant the hash will be unique).
As a concrete example of this data, the hashes you get for Raids will correspond to the currently active "Challenge Mode".
We don't have any human readable information for these, but saavy 3rd party app users could manually associate the key (a hash identifier for the "option" that is enabled/disabled) and the value (whether it's enabled or disabled presently)
On our side, we don't necessarily even know what these are used for (the game designers know, but we don't), and we have no human readable data for them. In order to use them, you will have to do some experimentation. | No |
| loadoutRequirementIndex | integer (int32) | If returned, this is the index into the DestinyActivityDefinition's "loadouts" property, indicating the currently active loadout requirements. | No |
| phases | Array[Destiny.Milestones.DestinyMilestoneActivityPhase] | If the Activity has discrete "phases" that we can track, that info will be here. Otherwise, this value will be NULL. Note that this is a list and not a dictionary: the order implies the ascending order of phases or progression in this activity. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Milestones.DestinyMilestoneChallengeActivity object
const example = {
  activityHash: 123,
  challenges: [],
  modifierHashes: [],
  booleanActivityOptions: null,
  loadoutRequirementIndex: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Milestones.DestinyMilestoneChallengeActivity object
example = {
    "activityHash": 123,
    "challenges": [],
    "modifierHashes": [],
    "booleanActivityOptions": None,
    "loadoutRequirementIndex": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Challenges.DestinyChallengeStatus**: Referenced in this entity
- **Destiny.Definitions.ActivityModifiers.DestinyActivityModifierDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyActivityDefinition**: Referenced in this entity
- **Destiny.Milestones.DestinyMilestoneActivityPhase**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Milestones.DestinyMilestoneChallengeActivity":   {
      "type": "object",
      "properties": {
          "activityHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityDefinition"
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
          },
          "phases": {
              "description": "If the Activity has discrete \"phases\" that we can track, that info will be here. Otherwise, this value will be NULL. Note that this is a list and not a dictionary: the order implies the ascending order of phases or progression in this activity.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Milestones.DestinyMilestoneActivityPhase"
              }
          }
      }
  }
}
```
