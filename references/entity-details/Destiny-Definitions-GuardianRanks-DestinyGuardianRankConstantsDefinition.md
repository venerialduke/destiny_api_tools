# Destiny.Definitions.GuardianRanks.DestinyGuardianRankConstantsDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.GuardianRanks.DestinyGuardianRankConstantsDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Destiny API entity representing destinyguardianrankconstantsdefinition data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| rankCount | integer (int32) |  | No |
| guardianRankHashes | Array[integer] |  | No |
| rootNodeHash | integer (uint32) |  | No |
| iconBackgrounds | Destiny.Definitions.GuardianRanks.DestinyGuardianRankIconBackgroundsDefinition |  | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.GuardianRanks.DestinyGuardianRankConstantsDefinition object
const example = {
  displayProperties: null,
  rankCount: 123,
  guardianRankHashes: [],
  rootNodeHash: 123,
  iconBackgrounds: null,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.GuardianRanks.DestinyGuardianRankConstantsDefinition object
example = {
    "displayProperties": None,
    "rankCount": 123,
    "guardianRankHashes": [],
    "rootNodeHash": 123,
    "iconBackgrounds": None,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.GuardianRanks.DestinyGuardianRankDefinition**: Referenced in this entity
- **Destiny.Definitions.GuardianRanks.DestinyGuardianRankIconBackgroundsDefinition**: Referenced in this entity
- **Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.GuardianRanks.DestinyGuardianRankConstantsDefinition":   {
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "rankCount": {
              "format": "int32",
              "type": "integer"
          },
          "guardianRankHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.GuardianRanks.DestinyGuardianRankDefinition"
              }
          },
          "rootNodeHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
              }
          },
          "iconBackgrounds": {
              "$ref": "#/definitions/Destiny.Definitions.GuardianRanks.DestinyGuardianRankIconBackgroundsDefinition"
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
      "x-mobile-manifest-name": "GuardianRankConstants"
  }
}
```
