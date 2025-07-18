# Destiny.Definitions.DestinyProgressionDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyProgressionDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
A "Progression" in Destiny is best explained by an example.
A Character's "Level" is a progression: it has Experience that can be earned, levels that can be gained, and is evaluated and displayed at various points in the game. A Character's "Faction Reputation" is also a progression for much the same reason.
Progression is used by a variety of systems, and the definition of a Progression will generally only be useful if combining with live data (such as a character's DestinyCharacterProgressionComponent.progressions property, which holds that character's live Progression states).
Fundamentally, a Progression measures your "Level" by evaluating the thresholds in its Steps (one step per level, except for the last step which can be repeated indefinitely for "Levels" that have no ceiling) against the total earned "progression points"/experience. (for simplicity purposes, we will henceforth refer to earned progression points as experience, though it need not be a mechanic that in any way resembles Experience in a traditional sense).
Earned experience is calculated in a variety of ways, determined by the Progression's scope. These go from looking up a stored value to performing exceedingly obtuse calculations. This is why we provide live data in DestinyCharacterProgressionComponent.progressions, so you don't have to worry about those.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.DestinyProgressionDisplayPropertiesDefinition |  | No |
| scope | integer (int32) | The "Scope" of the progression indicates the source of the progression's live data.
See the DestinyProgressionScope enum for more info: but essentially, a Progression can either be backed by a stored value, or it can be a calculated derivative of other values. | No |
| repeatLastStep | boolean | If this is True, then the progression doesn't have a maximum level. | No |
| source | string | If there's a description of how to earn this progression in the local config, this will be that localized description. | No |
| steps | Array[Destiny.Definitions.DestinyProgressionStepDefinition] | Progressions are divided into Steps, which roughly equate to "Levels" in the traditional sense of a Progression. Notably, the last step can be repeated indefinitely if repeatLastStep is true, meaning that the calculation for your level is not as simple as comparing your current progress to the max progress of the steps. 
These and more calculations are done for you if you grab live character progression data, such as in the DestinyCharacterProgressionComponent. | No |
| visible | boolean | If true, the Progression is something worth showing to users.
If false, BNet isn't going to show it. But that doesn't mean you can't. We're all friends here. | No |
| factionHash | integer (uint32) | If the value exists, this is the hash identifier for the Faction that owns this Progression.
This is purely for convenience, if you're looking at a progression and want to know if and who it's related to in terms of Faction Reputation. | No |
| color | object | The #RGB string value for the color related to this progression, if there is one. | No |
| rankIcon | string | For progressions that have it, this is the rank icon we use in the Companion, displayed above the progressions' rank value. | No |
| rewardItems | Array[Destiny.Definitions.DestinyProgressionRewardItemQuantity] |  | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyProgressionDefinition object
const example = {
  displayProperties: null,
  scope: 123,
  repeatLastStep: true,
  source: "example value",
  steps: [],
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyProgressionDefinition object
example = {
    "displayProperties": None,
    "scope": 123,
    "repeatLastStep": True,
    "source": "example value",
    "steps": [],
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyFactionDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyProgressionDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyProgressionRewardItemQuantity**: Referenced in this entity
- **Destiny.Definitions.DestinyProgressionStepDefinition**: Referenced in this entity
- **Destiny.DestinyProgressionScope**: Referenced in this entity
- **Destiny.Misc.DestinyColor**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyProgressionDefinition":   {
      "description": "A \"Progression\" in Destiny is best explained by an example.\r\nA Character's \"Level\" is a progression: it has Experience that can be earned, levels that can be gained, and is evaluated and displayed at various points in the game. A Character's \"Faction Reputation\" is also a progression for much the same reason.\r\nProgression is used by a variety of systems, and the definition of a Progression will generally only be useful if combining with live data (such as a character's DestinyCharacterProgressionComponent.progressions property, which holds that character's live Progression states).\r\nFundamentally, a Progression measures your \"Level\" by evaluating the thresholds in its Steps (one step per level, except for the last step which can be repeated indefinitely for \"Levels\" that have no ceiling) against the total earned \"progression points\"/experience. (for simplicity purposes, we will henceforth refer to earned progression points as experience, though it need not be a mechanic that in any way resembles Experience in a traditional sense).\r\nEarned experience is calculated in a variety of ways, determined by the Progression's scope. These go from looking up a stored value to performing exceedingly obtuse calculations. This is why we provide live data in DestinyCharacterProgressionComponent.progressions, so you don't have to worry about those.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.DestinyProgressionDisplayPropertiesDefinition"
          },
          "scope": {
              "format": "int32",
              "description": "The \"Scope\" of the progression indicates the source of the progression's live data.\r\nSee the DestinyProgressionScope enum for more info: but essentially, a Progression can either be backed by a stored value, or it can be a calculated derivative of other values.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyProgressionScope"
              }
          },
          "repeatLastStep": {
              "description": "If this is True, then the progression doesn't have a maximum level.",
              "type": "boolean"
          },
          "source": {
              "description": "If there's a description of how to earn this progression in the local config, this will be that localized description.",
              "type": "string"
          },
          "steps": {
              "description": "Progressions are divided into Steps, which roughly equate to \"Levels\" in the traditional sense of a Progression. Notably, the last step can be repeated indefinitely if repeatLastStep is true, meaning that the calculation for your level is not as simple as comparing your current progress to the max progress of the steps. \r\nThese and more calculations are done for you if you grab live character progression data, such as in the DestinyCharacterProgressionComponent.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyProgressionStepDefinition"
              }
          },
          "visible": {
              "description": "If true, the Progression is something worth showing to users.\r\nIf false, BNet isn't going to show it. But that doesn't mean you can't. We're all friends here.",
              "type": "boolean"
          },
          "factionHash": {
              "format": "uint32",
              "description": "If the value exists, this is the hash identifier for the Faction that owns this Progression.\r\nThis is purely for convenience, if you're looking at a progression and want to know if and who it's related to in terms of Faction Reputation.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyFactionDefinition"
              }
          },
          "color": {
              "description": "The #RGB string value for the color related to this progression, if there is one.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Misc.DestinyColor"
                  }
              ]
          },
          "rankIcon": {
              "description": "For progressions that have it, this is the rank icon we use in the Companion, displayed above the progressions' rank value.",
              "type": "string"
          },
          "rewardItems": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyProgressionRewardItemQuantity"
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
      "x-mobile-manifest-name": "Progressions"
  }
}
```
