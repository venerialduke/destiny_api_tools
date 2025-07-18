# Destiny.Definitions.DestinyItemQualityBlockDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemQualityBlockDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
An item's "Quality" determines its calculated stats. The Level at which the item spawns is combined with its "qualityLevel" along with some additional calculations to determine the value of those stats.
In Destiny 2, most items don't have default item levels and quality, making this property less useful: these apparently are almost always determined by the complex mechanisms of the Reward system rather than statically. They are still provided here in case they are still useful for people. This also contains some information about Infusion.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| itemLevels | Array[integer] | The "base" defined level of an item. This is a list because, in theory, each Expansion could define its own base level for an item.
In practice, not only was that never done in Destiny 1, but now this isn't even populated at all. When it's not populated, the level at which it spawns has to be inferred by Reward information, of which BNet receives an imperfect view and will only be reliable on instanced data as a result. | No |
| qualityLevel | integer (int32) | qualityLevel is used in combination with the item's level to calculate stats like Attack and Defense. It plays a role in that calculation, but not nearly as large as itemLevel does. | No |
| infusionCategoryName | string | The string identifier for this item's "infusability", if any. 
Items that match the same infusionCategoryName are allowed to infuse with each other.
DEPRECATED: Items can now have multiple infusion categories. Please use infusionCategoryHashes instead. | No |
| infusionCategoryHash | integer (uint32) | The hash identifier for the infusion. It does not map to a Definition entity.
DEPRECATED: Items can now have multiple infusion categories. Please use infusionCategoryHashes instead. | No |
| infusionCategoryHashes | Array[integer] | If any one of these hashes matches any value in another item's infusionCategoryHashes, the two can infuse with each other. | No |
| progressionLevelRequirementHash | integer (uint32) | An item can refer to pre-set level requirements. They are defined in DestinyProgressionLevelRequirementDefinition, and you can use this hash to find the appropriate definition. | No |
| currentVersion | integer (uint32) | The latest version available for this item. | No |
| versions | Array[Destiny.Definitions.DestinyItemVersionDefinition] | The list of versions available for this item. | No |
| displayVersionWatermarkIcons | Array[string] | Icon overlays to denote the item version and power cap status. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemQualityBlockDefinition object
const example = {
  itemLevels: [],
  qualityLevel: 123,
  infusionCategoryName: "example value",
  infusionCategoryHash: 123,
  infusionCategoryHashes: [],
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemQualityBlockDefinition object
example = {
    "itemLevels": [],
    "qualityLevel": 123,
    "infusionCategoryName": "example value",
    "infusionCategoryHash": 123,
    "infusionCategoryHashes": [],
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyItemVersionDefinition**: Referenced in this entity
- **Destiny.Definitions.Progression.DestinyProgressionLevelRequirementDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyItemQualityBlockDefinition":   {
      "description": "An item's \"Quality\" determines its calculated stats. The Level at which the item spawns is combined with its \"qualityLevel\" along with some additional calculations to determine the value of those stats.\r\nIn Destiny 2, most items don't have default item levels and quality, making this property less useful: these apparently are almost always determined by the complex mechanisms of the Reward system rather than statically. They are still provided here in case they are still useful for people. This also contains some information about Infusion.",
      "type": "object",
      "properties": {
          "itemLevels": {
              "description": "The \"base\" defined level of an item. This is a list because, in theory, each Expansion could define its own base level for an item.\r\nIn practice, not only was that never done in Destiny 1, but now this isn't even populated at all. When it's not populated, the level at which it spawns has to be inferred by Reward information, of which BNet receives an imperfect view and will only be reliable on instanced data as a result.",
              "type": "array",
              "items": {
                  "format": "int32",
                  "type": "integer"
              }
          },
          "qualityLevel": {
              "format": "int32",
              "description": "qualityLevel is used in combination with the item's level to calculate stats like Attack and Defense. It plays a role in that calculation, but not nearly as large as itemLevel does.",
              "type": "integer"
          },
          "infusionCategoryName": {
              "description": "The string identifier for this item's \"infusability\", if any. \r\nItems that match the same infusionCategoryName are allowed to infuse with each other.\r\nDEPRECATED: Items can now have multiple infusion categories. Please use infusionCategoryHashes instead.",
              "type": "string"
          },
          "infusionCategoryHash": {
              "format": "uint32",
              "description": "The hash identifier for the infusion. It does not map to a Definition entity.\r\nDEPRECATED: Items can now have multiple infusion categories. Please use infusionCategoryHashes instead.",
              "type": "integer"
          },
          "infusionCategoryHashes": {
              "description": "If any one of these hashes matches any value in another item's infusionCategoryHashes, the two can infuse with each other.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              }
          },
          "progressionLevelRequirementHash": {
              "format": "uint32",
              "description": "An item can refer to pre-set level requirements. They are defined in DestinyProgressionLevelRequirementDefinition, and you can use this hash to find the appropriate definition.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Progression.DestinyProgressionLevelRequirementDefinition"
              }
          },
          "currentVersion": {
              "format": "uint32",
              "description": "The latest version available for this item.",
              "type": "integer"
          },
          "versions": {
              "description": "The list of versions available for this item.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyItemVersionDefinition"
              }
          },
          "displayVersionWatermarkIcons": {
              "description": "Icon overlays to denote the item version and power cap status.",
              "type": "array",
              "items": {
                  "type": "string"
              }
          }
      }
  }
}
```
