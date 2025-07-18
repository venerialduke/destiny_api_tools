# Destiny.Entities.Characters.DestinyCharacterProgressionComponent

## Entity Information
- **Entity Name**: Destiny.Entities.Characters.DestinyCharacterProgressionComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
This component returns anything that could be considered "Progression" on a user: data where the user is gaining levels, reputation, completions, rewards, etc...

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| progressions | object | A Dictionary of all known progressions for the Character, keyed by the Progression's hash.
Not all progressions have user-facing data, but those who do will have that data contained in the DestinyProgressionDefinition. | No |
| factions | object | A dictionary of all known Factions, keyed by the Faction's hash. It contains data about this character's status with the faction. | No |
| milestones | object | Milestones are related to the simple progressions shown in the game, but return additional and hopefully helpful information for users about the specifics of the Milestone's status. | No |
| quests | Array[Destiny.Quests.DestinyQuestStatus] | If the user has any active quests, the quests' statuses will be returned here.
 Note that quests have been largely supplanted by Milestones, but that doesn't mean that they won't make a comeback independent of milestones at some point.
 (Fun fact: quests came back as I feared they would, but we never looped back to populate this... I'm going to put that in the backlog.) | No |
| uninstancedItemObjectives | object | Sometimes, you have items in your inventory that don't have instances, but still have Objective information. This provides you that objective information for uninstanced items. 
This dictionary is keyed by the item's hash: which you can use to look up the name and description for the overall task(s) implied by the objective. The value is the list of objectives for this item, and their statuses. | No |
| uninstancedItemPerks | object | Sometimes, you have items in your inventory that don't have instances, but still have perks (for example: Trials passage cards). This gives you the perk information for uninstanced items.
This dictionary is keyed by item hash, which you can use to look up the corresponding item definition. The value is the list of perks states for the item. | No |
| checklists | object | The set of checklists that can be examined for this specific character, keyed by the hash identifier of the Checklist (DestinyChecklistDefinition)
For each checklist returned, its value is itself a Dictionary keyed by the checklist's hash identifier with the value being a boolean indicating if it's been discovered yet. | No |
| seasonalArtifact | object | Data related to your progress on the current season's artifact that can vary per character. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Entities.Characters.DestinyCharacterProgressionComponent object
const example = {
  progressions: null,
  factions: null,
  milestones: null,
  quests: [],
  uninstancedItemObjectives: null,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Entities.Characters.DestinyCharacterProgressionComponent object
example = {
    "progressions": None,
    "factions": None,
    "milestones": None,
    "quests": [],
    "uninstancedItemObjectives": None,
    # ... more properties
}
```

## Related Entities
- **Destiny.Artifacts.DestinyArtifactCharacterScoped**: Referenced in this entity
- **Destiny.Definitions.Checklists.DestinyChecklistDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyFactionDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyProgressionDefinition**: Referenced in this entity
- **Destiny.Definitions.Milestones.DestinyMilestoneDefinition**: Referenced in this entity
- **Destiny.DestinyProgression**: Referenced in this entity
- **Destiny.Entities.Items.DestinyItemPerksComponent**: Referenced in this entity
- **Destiny.Milestones.DestinyMilestone**: Referenced in this entity
- **Destiny.Progression.DestinyFactionProgression**: Referenced in this entity
- **Destiny.Quests.DestinyObjectiveProgress**: Referenced in this entity
- **Destiny.Quests.DestinyQuestStatus**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Entities.Characters.DestinyCharacterProgressionComponent":   {
      "description": "This component returns anything that could be considered \"Progression\" on a user: data where the user is gaining levels, reputation, completions, rewards, etc...",
      "type": "object",
      "properties": {
          "progressions": {
              "description": "A Dictionary of all known progressions for the Character, keyed by the Progression's hash.\r\nNot all progressions have user-facing data, but those who do will have that data contained in the DestinyProgressionDefinition.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.DestinyProgression"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyProgressionDefinition"
              }
          },
          "factions": {
              "description": "A dictionary of all known Factions, keyed by the Faction's hash. It contains data about this character's status with the faction.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.Progression.DestinyFactionProgression"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyFactionDefinition"
              }
          },
          "milestones": {
              "description": "Milestones are related to the simple progressions shown in the game, but return additional and hopefully helpful information for users about the specifics of the Milestone's status.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.Milestones.DestinyMilestone"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Milestones.DestinyMilestoneDefinition"
              }
          },
          "quests": {
              "description": "If the user has any active quests, the quests' statuses will be returned here.\r\n Note that quests have been largely supplanted by Milestones, but that doesn't mean that they won't make a comeback independent of milestones at some point.\r\n (Fun fact: quests came back as I feared they would, but we never looped back to populate this... I'm going to put that in the backlog.)",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Quests.DestinyQuestStatus"
              }
          },
          "uninstancedItemObjectives": {
              "description": "Sometimes, you have items in your inventory that don't have instances, but still have Objective information. This provides you that objective information for uninstanced items. \r\nThis dictionary is keyed by the item's hash: which you can use to look up the name and description for the overall task(s) implied by the objective. The value is the list of objectives for this item, and their statuses.",
              "type": "object",
              "additionalProperties": {
                  "type": "array",
                  "items": {
                      "$ref": "#/definitions/Destiny.Quests.DestinyObjectiveProgress"
                  }
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "uninstancedItemPerks": {
              "description": "Sometimes, you have items in your inventory that don't have instances, but still have perks (for example: Trials passage cards). This gives you the perk information for uninstanced items.\r\nThis dictionary is keyed by item hash, which you can use to look up the corresponding item definition. The value is the list of perks states for the item.",
              "type": "object",
              "additionalProperties": {
                  "x-destiny-component-type-dependency": "ItemPerks",
                  "$ref": "#/definitions/Destiny.Entities.Items.DestinyItemPerksComponent"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "checklists": {
              "description": "The set of checklists that can be examined for this specific character, keyed by the hash identifier of the Checklist (DestinyChecklistDefinition)\r\nFor each checklist returned, its value is itself a Dictionary keyed by the checklist's hash identifier with the value being a boolean indicating if it's been discovered yet.",
              "type": "object",
              "additionalProperties": {
                  "type": "object",
                  "additionalProperties": {
                      "type": "boolean"
                  }
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Checklists.DestinyChecklistDefinition"
              }
          },
          "seasonalArtifact": {
              "description": "Data related to your progress on the current season's artifact that can vary per character.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Artifacts.DestinyArtifactCharacterScoped"
                  }
              ]
          }
      },
      "x-destiny-component-type-dependency": "CharacterProgressions"
  }
}
```
