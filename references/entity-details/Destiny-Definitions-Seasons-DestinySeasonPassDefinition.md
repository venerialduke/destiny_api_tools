# Destiny.Definitions.Seasons.DestinySeasonPassDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Seasons.DestinySeasonPassDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Destiny API entity representing destinyseasonpassdefinition data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| rewardProgressionHash | integer (uint32) | This is the progression definition related to the progression for the initial levels 1-100 that provide item rewards for the Season pass. Further experience after you reach the limit is provided in the "Prestige" progression referred to by prestigeProgressionHash. | No |
| prestigeProgressionHash | integer (uint32) | I know what you're thinking, but I promise we're not going to duplicate and drown you. Instead, we're giving you sweet, sweet power bonuses.
 Prestige progression is further progression that you can make on the Season pass after you gain max ranks, that will ultimately increase your power/light level over the theoretical limit. | No |
| linkRedirectPath | string |  | No |
| color | Destiny.Misc.DestinyColor |  | No |
| images | Destiny.Definitions.Seasons.DestinySeasonPassImages |  | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Seasons.DestinySeasonPassDefinition object
const example = {
  displayProperties: null,
  rewardProgressionHash: 123,
  prestigeProgressionHash: 123,
  linkRedirectPath: "example value",
  color: null,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Seasons.DestinySeasonPassDefinition object
example = {
    "displayProperties": None,
    "rewardProgressionHash": 123,
    "prestigeProgressionHash": 123,
    "linkRedirectPath": "example value",
    "color": None,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyProgressionDefinition**: Referenced in this entity
- **Destiny.Definitions.Seasons.DestinySeasonPassImages**: Referenced in this entity
- **Destiny.Misc.DestinyColor**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Seasons.DestinySeasonPassDefinition":   {
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "rewardProgressionHash": {
              "format": "uint32",
              "description": "This is the progression definition related to the progression for the initial levels 1-100 that provide item rewards for the Season pass. Further experience after you reach the limit is provided in the \"Prestige\" progression referred to by prestigeProgressionHash.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyProgressionDefinition"
              }
          },
          "prestigeProgressionHash": {
              "format": "uint32",
              "description": "I know what you're thinking, but I promise we're not going to duplicate and drown you. Instead, we're giving you sweet, sweet power bonuses.\r\n Prestige progression is further progression that you can make on the Season pass after you gain max ranks, that will ultimately increase your power/light level over the theoretical limit.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyProgressionDefinition"
              }
          },
          "linkRedirectPath": {
              "type": "string"
          },
          "color": {
              "$ref": "#/definitions/Destiny.Misc.DestinyColor"
          },
          "images": {
              "$ref": "#/definitions/Destiny.Definitions.Seasons.DestinySeasonPassImages"
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
      "x-mobile-manifest-name": "SeasonPasses"
  }
}
```
