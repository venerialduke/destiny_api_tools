# Destiny.Definitions.DestinySandboxPerkDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinySandboxPerkDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Perks are modifiers to a character or item that can be applied situationally.
- Perks determine a weapon's damage type.
- Perks put the Mods in Modifiers (they are literally the entity that bestows the Sandbox benefit for whatever fluff text about the modifier in the Socket, Plug or Talent Node)
- Perks are applied for unique alterations of state in Objectives
Anyways, I'm sure you can see why perks are so interesting.
What Perks often don't have is human readable information, so we attempt to reverse engineer that by pulling that data from places that uniquely refer to these perks: namely, Talent Nodes and Plugs. That only gives us a subset of perks that are human readable, but those perks are the ones people generally care about anyways. The others are left as a mystery, their true purpose mostly unknown and undocumented.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | object | These display properties are by no means guaranteed to be populated. Usually when it is, it's only because we back-filled them with the displayProperties of some Talent Node or Plug item that happened to be uniquely providing that perk. | No |
| perkIdentifier | string | The string identifier for the perk. | No |
| isDisplayable | boolean | If true, you can actually show the perk in the UI. Otherwise, it doesn't have useful player-facing information. | No |
| damageType | integer (int32) | If this perk grants a damage type to a weapon, the damage type will be defined here.
Unless you have a compelling reason to use this enum value, use the damageTypeHash instead to look up the actual DestinyDamageTypeDefinition. | No |
| damageTypeHash | integer (uint32) | The hash identifier for looking up the DestinyDamageTypeDefinition, if this perk has a damage type.
This is preferred over using the damageType enumeration value, which has been left purely because it is occasionally convenient. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinySandboxPerkDefinition object
const example = {
  displayProperties: null,
  perkIdentifier: "example value",
  isDisplayable: true,
  damageType: 123,
  damageTypeHash: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinySandboxPerkDefinition object
example = {
    "displayProperties": None,
    "perkIdentifier": "example value",
    "isDisplayable": True,
    "damageType": 123,
    "damageTypeHash": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.DamageType**: Referenced in this entity
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyDamageTypeDefinition**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinySandboxPerkDefinition":   {
      "description": "Perks are modifiers to a character or item that can be applied situationally.\r\n- Perks determine a weapon's damage type.\r\n- Perks put the Mods in Modifiers (they are literally the entity that bestows the Sandbox benefit for whatever fluff text about the modifier in the Socket, Plug or Talent Node)\r\n- Perks are applied for unique alterations of state in Objectives\r\nAnyways, I'm sure you can see why perks are so interesting.\r\nWhat Perks often don't have is human readable information, so we attempt to reverse engineer that by pulling that data from places that uniquely refer to these perks: namely, Talent Nodes and Plugs. That only gives us a subset of perks that are human readable, but those perks are the ones people generally care about anyways. The others are left as a mystery, their true purpose mostly unknown and undocumented.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "description": "These display properties are by no means guaranteed to be populated. Usually when it is, it's only because we back-filled them with the displayProperties of some Talent Node or Plug item that happened to be uniquely providing that perk.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
                  }
              ]
          },
          "perkIdentifier": {
              "description": "The string identifier for the perk.",
              "type": "string"
          },
          "isDisplayable": {
              "description": "If true, you can actually show the perk in the UI. Otherwise, it doesn't have useful player-facing information.",
              "type": "boolean"
          },
          "damageType": {
              "format": "int32",
              "description": "If this perk grants a damage type to a weapon, the damage type will be defined here.\r\nUnless you have a compelling reason to use this enum value, use the damageTypeHash instead to look up the actual DestinyDamageTypeDefinition.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DamageType"
              }
          },
          "damageTypeHash": {
              "format": "uint32",
              "description": "The hash identifier for looking up the DestinyDamageTypeDefinition, if this perk has a damage type.\r\nThis is preferred over using the damageType enumeration value, which has been left purely because it is occasionally convenient.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyDamageTypeDefinition"
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
      "x-mobile-manifest-name": "SandboxPerks"
  }
}
```
