# Destiny.Milestones.DestinyPublicMilestoneChallengeActivity

## Entity Information
- **Entity Name**: Destiny.Milestones.DestinyPublicMilestoneChallengeActivity
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinypublicmilestonechallengeactivity data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| activityHash | integer (uint32) |  | No |
| challengeObjectiveHashes | Array[integer] |  | No |
| modifierHashes | Array[integer] | If the activity has modifiers, this will be the list of modifiers that all variants have in common. Perform lookups against DestinyActivityModifierDefinition which defines the modifier being applied to get at the modifier data.
Note that, in the DestiyActivityDefinition, you will see many more modifiers than this being referred to: those are all *possible* modifiers for the activity, not the active ones. Use only the active ones to match what's really live. | No |
| loadoutRequirementIndex | integer (int32) | If returned, this is the index into the DestinyActivityDefinition's "loadouts" property, indicating the currently active loadout requirements. | No |
| phaseHashes | Array[integer] | The ordered list of phases for this activity, if any. Note that we have no human readable info for phases, nor any entities to relate them to: relating these hashes to something human readable is up to you unfortunately. | No |
| booleanActivityOptions | object | The set of activity options for this activity, keyed by an identifier that's unique for this activity (not guaranteed to be unique between or across all activities, though should be unique for every *variant* of a given *conceptual* activity: for instance, the original D2 Raid has many variant DestinyActivityDefinitions. While other activities could potentially have the same option hashes, for any given D2 base Raid variant the hash will be unique).
As a concrete example of this data, the hashes you get for Raids will correspond to the currently active "Challenge Mode".
We have no human readable information for this data, so it's up to you if you want to associate it with such info to show it. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Milestones.DestinyPublicMilestoneChallengeActivity object
const example = {
  activityHash: 123,
  challengeObjectiveHashes: [],
  modifierHashes: [],
  loadoutRequirementIndex: 123,
  phaseHashes: [],
  // ... more properties
};
```

### Python
```python
# Example Destiny.Milestones.DestinyPublicMilestoneChallengeActivity object
example = {
    "activityHash": 123,
    "challengeObjectiveHashes": [],
    "modifierHashes": [],
    "loadoutRequirementIndex": 123,
    "phaseHashes": [],
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.ActivityModifiers.DestinyActivityModifierDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyActivityDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Milestones.DestinyPublicMilestoneChallengeActivity":   {
      "type": "object",
      "properties": {
          "activityHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityDefinition"
              }
          },
          "challengeObjectiveHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
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
          "loadoutRequirementIndex": {
              "format": "int32",
              "description": "If returned, this is the index into the DestinyActivityDefinition's \"loadouts\" property, indicating the currently active loadout requirements.",
              "type": "integer"
          },
          "phaseHashes": {
              "description": "The ordered list of phases for this activity, if any. Note that we have no human readable info for phases, nor any entities to relate them to: relating these hashes to something human readable is up to you unfortunately.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              }
          },
          "booleanActivityOptions": {
              "description": "The set of activity options for this activity, keyed by an identifier that's unique for this activity (not guaranteed to be unique between or across all activities, though should be unique for every *variant* of a given *conceptual* activity: for instance, the original D2 Raid has many variant DestinyActivityDefinitions. While other activities could potentially have the same option hashes, for any given D2 base Raid variant the hash will be unique).\r\nAs a concrete example of this data, the hashes you get for Raids will correspond to the currently active \"Challenge Mode\".\r\nWe have no human readable information for this data, so it's up to you if you want to associate it with such info to show it.",
              "type": "object",
              "additionalProperties": {
                  "type": "boolean"
              }
          }
      }
  }
}
```
