# Destiny.Definitions.DestinyRaceDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyRaceDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
In Destiny, "Races" are really more like "Species". Sort of. I mean, are the Awoken a separate species from humans? I'm not sure. But either way, they're defined here. You'll see Exo, Awoken, and Human as examples of these Species. Players will choose one for their character.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| raceType | integer (int32) | An enumeration defining the existing, known Races/Species for player characters. This value will be the enum value matching this definition. | No |
| genderedRaceNames | object | A localized string referring to the singular form of the Race's name when referred to in gendered form. Keyed by the DestinyGender. | No |
| genderedRaceNamesByGenderHash | object |  | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyRaceDefinition object
const example = {
  displayProperties: null,
  raceType: 123,
  genderedRaceNames: null,
  genderedRaceNamesByGenderHash: null,
  hash: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyRaceDefinition object
example = {
    "displayProperties": None,
    "raceType": 123,
    "genderedRaceNames": None,
    "genderedRaceNamesByGenderHash": None,
    "hash": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyGenderDefinition**: Referenced in this entity
- **Destiny.DestinyRace**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyRaceDefinition":   {
      "description": "In Destiny, \"Races\" are really more like \"Species\". Sort of. I mean, are the Awoken a separate species from humans? I'm not sure. But either way, they're defined here. You'll see Exo, Awoken, and Human as examples of these Species. Players will choose one for their character.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "raceType": {
              "format": "int32",
              "description": "An enumeration defining the existing, known Races/Species for player characters. This value will be the enum value matching this definition.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyRace"
              }
          },
          "genderedRaceNames": {
              "description": "A localized string referring to the singular form of the Race's name when referred to in gendered form. Keyed by the DestinyGender.",
              "type": "object",
              "additionalProperties": {
                  "type": "string"
              }
          },
          "genderedRaceNamesByGenderHash": {
              "type": "object",
              "additionalProperties": {
                  "type": "string"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyGenderDefinition"
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
      "x-mobile-manifest-name": "Races"
  }
}
```
