# Destiny.Definitions.DestinyRewardSourceDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyRewardSourceDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Represents a heuristically-determined "item source" according to Bungie.net. These item sources are non-canonical: we apply a combination of special configuration and often-fragile heuristics to attempt to discern whether an item should be part of a given "source," but we have known cases of false positives and negatives due to our imperfect heuristics.
Still, they provide a decent approximation for people trying to figure out how an item can be obtained. DestinyInventoryItemDefinition refers to sources in the sourceDatas.sourceHashes property for all sources we determined the item could spawn from.
An example in Destiny 1 of a Source would be "Nightfall". If an item has the "Nightfall" source associated with it, it's extremely likely that you can earn that item while playing Nightfall, either during play or as an after-completion reward.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| category | integer (int32) | Sources are grouped into categories: common ways that items are provided. I hope to see this expand in Destiny 2 once we have time to generate accurate reward source data. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyRewardSourceDefinition object
const example = {
  displayProperties: null,
  category: 123,
  hash: 123,
  index: 123,
  redacted: true,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyRewardSourceDefinition object
example = {
    "displayProperties": None,
    "category": 123,
    "hash": 123,
    "index": 123,
    "redacted": True,
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyRewardSourceCategory**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyRewardSourceDefinition":   {
      "description": "Represents a heuristically-determined \"item source\" according to Bungie.net. These item sources are non-canonical: we apply a combination of special configuration and often-fragile heuristics to attempt to discern whether an item should be part of a given \"source,\" but we have known cases of false positives and negatives due to our imperfect heuristics.\r\nStill, they provide a decent approximation for people trying to figure out how an item can be obtained. DestinyInventoryItemDefinition refers to sources in the sourceDatas.sourceHashes property for all sources we determined the item could spawn from.\r\nAn example in Destiny 1 of a Source would be \"Nightfall\". If an item has the \"Nightfall\" source associated with it, it's extremely likely that you can earn that item while playing Nightfall, either during play or as an after-completion reward.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "category": {
              "format": "int32",
              "description": "Sources are grouped into categories: common ways that items are provided. I hope to see this expand in Destiny 2 once we have time to generate accurate reward source data.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.Definitions.DestinyRewardSourceCategory"
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
      "x-mobile-manifest-name": "RewardSources"
  }
}
```
