# Destiny.Definitions.DestinyObjectiveDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyObjectiveDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Defines an "Objective".
An objective is a specific task you should accomplish in the game. These are referred to by:
- Quest Steps (which are DestinyInventoryItemDefinition entities with Objectives)
- Challenges (which are Objectives defined on an DestinyActivityDefintion)
- Milestones (which refer to Objectives that are defined on both Quest Steps and Activities)
- Anything else that the designers decide to do later.
Objectives have progress, a notion of having been Completed, human readable data describing the task to be accomplished, and a lot of optional tack-on data that can enhance the information provided about the task.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | object | Ideally, this should tell you what your task is. I'm not going to lie to you though. Sometimes this doesn't have useful information at all. Which sucks, but there's nothing either of us can do about it. | No |
| completionValue | integer (int32) | The value that the unlock value defined in unlockValueHash must reach in order for the objective to be considered Completed. Used in calculating progress and completion status. | No |
| scope | integer (int32) | A shortcut for determining the most restrictive gating that this Objective is set to use. This includes both the dynamic determination of progress and of completion values. See the DestinyGatingScope enum's documentation for more details. | No |
| locationHash | integer (uint32) | OPTIONAL: a hash identifier for the location at which this objective must be accomplished, if there is a location defined. Look up the DestinyLocationDefinition for this hash for that additional location info. | No |
| allowNegativeValue | boolean | If true, the value is allowed to go negative. | No |
| allowValueChangeWhenCompleted | boolean | If true, you can effectively "un-complete" this objective if you lose progress after crossing the completion threshold. 
If False, once you complete the task it will remain completed forever by locking the value. | No |
| isCountingDownward | boolean | If true, completion means having an unlock value less than or equal to the completionValue.
If False, completion means having an unlock value greater than or equal to the completionValue. | No |
| valueStyle | integer (int32) | The UI style applied to the objective. It's an enum, take a look at DestinyUnlockValueUIStyle for details of the possible styles. Use this info as you wish to customize your UI.
DEPRECATED: This is no longer populated by Destiny 2 game content. Please use inProgressValueStyle and completedValueStyle instead. | No |
| progressDescription | string | Text to describe the progress bar. | No |
| perks | object | If this objective enables Perks intrinsically, the conditions for that enabling are defined here. | No |
| stats | object | If this objective enables modifications on a player's stats intrinsically, the conditions are defined here. | No |
| minimumVisibilityThreshold | integer (int32) | If nonzero, this is the minimum value at which the objective's progression should be shown. Otherwise, don't show it yet. | No |
| allowOvercompletion | boolean | If True, the progress will continue even beyond the point where the objective met its minimum completion requirements. Your UI will have to accommodate it. | No |
| showValueOnComplete | boolean | If True, you should continue showing the progression value in the UI after it's complete. I mean, we already do that in BNet anyways, but if you want to be better behaved than us you could honor this flag. | No |
| completedValueStyle | integer (int32) | The style to use when the objective is completed. | No |
| inProgressValueStyle | integer (int32) | The style to use when the objective is still in progress. | No |
| uiLabel | string | Objectives can have arbitrary UI-defined identifiers that define the style applied to objectives. For convenience, known UI labels will be defined in the uiStyle enum value. | No |
| uiStyle | integer (int32) | If the objective has a known UI label value, this property will represent it. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyObjectiveDefinition object
const example = {
  displayProperties: null,
  completionValue: 123,
  scope: 123,
  locationHash: 123,
  allowNegativeValue: true,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyObjectiveDefinition object
example = {
    "displayProperties": None,
    "completionValue": 123,
    "scope": 123,
    "locationHash": 123,
    "allowNegativeValue": True,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyLocationDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyObjectivePerkEntryDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyObjectiveStatEntryDefinition**: Referenced in this entity
- **Destiny.DestinyGatingScope**: Referenced in this entity
- **Destiny.DestinyObjectiveUiStyle**: Referenced in this entity
- **Destiny.DestinyUnlockValueUIStyle**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyObjectiveDefinition":   {
      "description": "Defines an \"Objective\".\r\nAn objective is a specific task you should accomplish in the game. These are referred to by:\r\n- Quest Steps (which are DestinyInventoryItemDefinition entities with Objectives)\r\n- Challenges (which are Objectives defined on an DestinyActivityDefintion)\r\n- Milestones (which refer to Objectives that are defined on both Quest Steps and Activities)\r\n- Anything else that the designers decide to do later.\r\nObjectives have progress, a notion of having been Completed, human readable data describing the task to be accomplished, and a lot of optional tack-on data that can enhance the information provided about the task.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "description": "Ideally, this should tell you what your task is. I'm not going to lie to you though. Sometimes this doesn't have useful information at all. Which sucks, but there's nothing either of us can do about it.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
                  }
              ]
          },
          "completionValue": {
              "format": "int32",
              "description": "The value that the unlock value defined in unlockValueHash must reach in order for the objective to be considered Completed. Used in calculating progress and completion status.",
              "type": "integer"
          },
          "scope": {
              "format": "int32",
              "description": "A shortcut for determining the most restrictive gating that this Objective is set to use. This includes both the dynamic determination of progress and of completion values. See the DestinyGatingScope enum's documentation for more details.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyGatingScope"
              }
          },
          "locationHash": {
              "format": "uint32",
              "description": "OPTIONAL: a hash identifier for the location at which this objective must be accomplished, if there is a location defined. Look up the DestinyLocationDefinition for this hash for that additional location info.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyLocationDefinition"
              }
          },
          "allowNegativeValue": {
              "description": "If true, the value is allowed to go negative.",
              "type": "boolean"
          },
          "allowValueChangeWhenCompleted": {
              "description": "If true, you can effectively \"un-complete\" this objective if you lose progress after crossing the completion threshold. \r\nIf False, once you complete the task it will remain completed forever by locking the value.",
              "type": "boolean"
          },
          "isCountingDownward": {
              "description": "If true, completion means having an unlock value less than or equal to the completionValue.\r\nIf False, completion means having an unlock value greater than or equal to the completionValue.",
              "type": "boolean"
          },
          "valueStyle": {
              "format": "int32",
              "description": "The UI style applied to the objective. It's an enum, take a look at DestinyUnlockValueUIStyle for details of the possible styles. Use this info as you wish to customize your UI.\r\nDEPRECATED: This is no longer populated by Destiny 2 game content. Please use inProgressValueStyle and completedValueStyle instead.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyUnlockValueUIStyle"
              }
          },
          "progressDescription": {
              "description": "Text to describe the progress bar.",
              "type": "string"
          },
          "perks": {
              "description": "If this objective enables Perks intrinsically, the conditions for that enabling are defined here.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.DestinyObjectivePerkEntryDefinition"
                  }
              ]
          },
          "stats": {
              "description": "If this objective enables modifications on a player's stats intrinsically, the conditions are defined here.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.DestinyObjectiveStatEntryDefinition"
                  }
              ]
          },
          "minimumVisibilityThreshold": {
              "format": "int32",
              "description": "If nonzero, this is the minimum value at which the objective's progression should be shown. Otherwise, don't show it yet.",
              "type": "integer"
          },
          "allowOvercompletion": {
              "description": "If True, the progress will continue even beyond the point where the objective met its minimum completion requirements. Your UI will have to accommodate it.",
              "type": "boolean"
          },
          "showValueOnComplete": {
              "description": "If True, you should continue showing the progression value in the UI after it's complete. I mean, we already do that in BNet anyways, but if you want to be better behaved than us you could honor this flag.",
              "type": "boolean"
          },
          "completedValueStyle": {
              "format": "int32",
              "description": "The style to use when the objective is completed.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyUnlockValueUIStyle"
              }
          },
          "inProgressValueStyle": {
              "format": "int32",
              "description": "The style to use when the objective is still in progress.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyUnlockValueUIStyle"
              }
          },
          "uiLabel": {
              "description": "Objectives can have arbitrary UI-defined identifiers that define the style applied to objectives. For convenience, known UI labels will be defined in the uiStyle enum value.",
              "type": "string"
          },
          "uiStyle": {
              "format": "int32",
              "description": "If the objective has a known UI label value, this property will represent it.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyObjectiveUiStyle"
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
      "x-mobile-manifest-name": "Objectives"
  }
}
```
