# Destiny.Definitions.Artifacts.DestinyArtifactDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Artifacts.DestinyArtifactDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Represents known info about a Destiny Artifact.
We cannot guarantee that artifact definitions will be immutable between seasons - in fact, we've been told that they will be replaced between seasons. But this definition is built both to minimize the amount of lookups for related data that have to occur, and is built in hope that, if this plan changes, we will be able to accommodate it more easily.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | object | Any basic display info we know about the Artifact. Currently sourced from a related inventory item, but the source of this data is subject to change. | No |
| translationBlock | object | Any Geometry/3D info we know about the Artifact. Currently sourced from a related inventory item's gearset information, but the source of this data is subject to change. | No |
| tiers | Array[Destiny.Definitions.Artifacts.DestinyArtifactTierDefinition] | Any Tier/Rank data related to this artifact, listed in display order.  Currently sourced from a Vendor, but this source is subject to change. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Artifacts.DestinyArtifactDefinition object
const example = {
  displayProperties: null,
  translationBlock: null,
  tiers: [],
  hash: 123,
  index: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Artifacts.DestinyArtifactDefinition object
example = {
    "displayProperties": None,
    "translationBlock": None,
    "tiers": [],
    "hash": 123,
    "index": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Artifacts.DestinyArtifactTierDefinition**: Referenced in this entity
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyItemTranslationBlockDefinition**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Artifacts.DestinyArtifactDefinition":   {
      "description": "Represents known info about a Destiny Artifact.\r\nWe cannot guarantee that artifact definitions will be immutable between seasons - in fact, we've been told that they will be replaced between seasons. But this definition is built both to minimize the amount of lookups for related data that have to occur, and is built in hope that, if this plan changes, we will be able to accommodate it more easily.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "description": "Any basic display info we know about the Artifact. Currently sourced from a related inventory item, but the source of this data is subject to change.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
                  }
              ]
          },
          "translationBlock": {
              "description": "Any Geometry/3D info we know about the Artifact. Currently sourced from a related inventory item's gearset information, but the source of this data is subject to change.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.DestinyItemTranslationBlockDefinition"
                  }
              ]
          },
          "tiers": {
              "description": "Any Tier/Rank data related to this artifact, listed in display order.  Currently sourced from a Vendor, but this source is subject to change.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Artifacts.DestinyArtifactTierDefinition"
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
      "x-mobile-manifest-name": "Artifacts"
  }
}
```
