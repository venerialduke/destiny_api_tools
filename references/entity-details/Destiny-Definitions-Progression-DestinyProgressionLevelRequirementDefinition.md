# Destiny.Definitions.Progression.DestinyProgressionLevelRequirementDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Progression.DestinyProgressionLevelRequirementDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
These are pre-constructed collections of data that can be used to determine the Level Requirement for an item given a Progression to be tested (such as the Character's level).
For instance, say a character receives a new Auto Rifle, and that Auto Rifle's DestinyInventoryItemDefinition.quality.progressionLevelRequirementHash property is pointing at one of these DestinyProgressionLevelRequirementDefinitions. Let's pretend also that the progressionHash it is pointing at is the Character Level progression. In that situation, the character's level will be used to interpolate a value in the requirementCurve property. The value picked up from that interpolation will be the required level for the item.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| requirementCurve | Array[Interpolation.InterpolationPointFloat] | A curve of level requirements, weighted by the related progressions' level.
Interpolate against this curve with the character's progression level to determine what the level requirement of the generated item that is using this data will be. | No |
| progressionHash | integer (uint32) | The progression whose level should be used to determine the level requirement.
Look up the DestinyProgressionDefinition with this hash for more information about the progression in question. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Progression.DestinyProgressionLevelRequirementDefinition object
const example = {
  requirementCurve: [],
  progressionHash: 123,
  hash: 123,
  index: 123,
  redacted: true,
};
```

### Python
```python
# Example Destiny.Definitions.Progression.DestinyProgressionLevelRequirementDefinition object
example = {
    "requirementCurve": [],
    "progressionHash": 123,
    "hash": 123,
    "index": 123,
    "redacted": True,
}
```

## Related Entities
- **Destiny.Definitions.DestinyProgressionDefinition**: Referenced in this entity
- **Interpolation.InterpolationPointFloat**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Progression.DestinyProgressionLevelRequirementDefinition":   {
      "description": "These are pre-constructed collections of data that can be used to determine the Level Requirement for an item given a Progression to be tested (such as the Character's level).\r\nFor instance, say a character receives a new Auto Rifle, and that Auto Rifle's DestinyInventoryItemDefinition.quality.progressionLevelRequirementHash property is pointing at one of these DestinyProgressionLevelRequirementDefinitions. Let's pretend also that the progressionHash it is pointing at is the Character Level progression. In that situation, the character's level will be used to interpolate a value in the requirementCurve property. The value picked up from that interpolation will be the required level for the item.",
      "type": "object",
      "properties": {
          "requirementCurve": {
              "description": "A curve of level requirements, weighted by the related progressions' level.\r\nInterpolate against this curve with the character's progression level to determine what the level requirement of the generated item that is using this data will be.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Interpolation.InterpolationPointFloat"
              }
          },
          "progressionHash": {
              "format": "uint32",
              "description": "The progression whose level should be used to determine the level requirement.\r\nLook up the DestinyProgressionDefinition with this hash for more information about the progression in question.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyProgressionDefinition"
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
      "x-mobile-manifest-name": "ProgressionLevelRequirements"
  }
}
```
