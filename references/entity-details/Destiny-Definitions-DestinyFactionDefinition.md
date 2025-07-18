# Destiny.Definitions.DestinyFactionDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyFactionDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
These definitions represent Factions in the game. Factions have ended up unilaterally being related to Vendors that represent them, but that need not necessarily be the case.
A Faction is really just an entity that has a related progression for which a character can gain experience. In Destiny 1, Dead Orbit was an example of a Faction: there happens to be a Vendor that represents Dead Orbit (and indeed, DestinyVendorDefinition.factionHash defines to this relationship), but Dead Orbit could theoretically exist without the Vendor that provides rewards.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| progressionHash | integer (uint32) | The hash identifier for the DestinyProgressionDefinition that indicates the character's relationship with this faction in terms of experience and levels. | No |
| tokenValues | object | The faction token item hashes, and their respective progression values. | No |
| rewardItemHash | integer (uint32) | The faction reward item hash, usually an engram. | No |
| rewardVendorHash | integer (uint32) | The faction reward vendor hash, used for faction engram previews. | No |
| vendors | Array[Destiny.Definitions.DestinyFactionVendorDefinition] | List of vendors that are associated with this faction. The last vendor that passes the unlock flag checks is the one that should be shown. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyFactionDefinition object
const example = {
  displayProperties: null,
  progressionHash: 123,
  tokenValues: null,
  rewardItemHash: 123,
  rewardVendorHash: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyFactionDefinition object
example = {
    "displayProperties": None,
    "progressionHash": 123,
    "tokenValues": None,
    "rewardItemHash": 123,
    "rewardVendorHash": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyFactionVendorDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyProgressionDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyVendorDefinition**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyFactionDefinition":   {
      "description": "These definitions represent Factions in the game. Factions have ended up unilaterally being related to Vendors that represent them, but that need not necessarily be the case.\r\nA Faction is really just an entity that has a related progression for which a character can gain experience. In Destiny 1, Dead Orbit was an example of a Faction: there happens to be a Vendor that represents Dead Orbit (and indeed, DestinyVendorDefinition.factionHash defines to this relationship), but Dead Orbit could theoretically exist without the Vendor that provides rewards.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "progressionHash": {
              "format": "uint32",
              "description": "The hash identifier for the DestinyProgressionDefinition that indicates the character's relationship with this faction in terms of experience and levels.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyProgressionDefinition"
              }
          },
          "tokenValues": {
              "description": "The faction token item hashes, and their respective progression values.",
              "type": "object",
              "additionalProperties": {
                  "format": "uint32",
                  "type": "integer"
              }
          },
          "rewardItemHash": {
              "format": "uint32",
              "description": "The faction reward item hash, usually an engram.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "rewardVendorHash": {
              "format": "uint32",
              "description": "The faction reward vendor hash, used for faction engram previews.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyVendorDefinition"
              }
          },
          "vendors": {
              "description": "List of vendors that are associated with this faction. The last vendor that passes the unlock flag checks is the one that should be shown.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyFactionVendorDefinition"
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
      "x-mobile-manifest-name": "Factions"
  }
}
```
