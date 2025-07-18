# Destiny.Definitions.DestinyItemStatBlockDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemStatBlockDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Information about the item's calculated stats, with as much data as we can find for the stats without having an actual instance of the item.
Note that this means the entire concept of providing these stats is fundamentally insufficient: we cannot predict with 100% accuracy the conditions under which an item can spawn, so we use various heuristics to attempt to simulate the conditions as accurately as possible. Actual stats for items in-game can and will vary, but these should at least be useful base points for comparison and display.
It is also worth noting that some stats, like Magazine size, have further calculations performed on them by scripts in-game and on the game servers that BNet does not have access to. We cannot know how those stats are further transformed, and thus some stats will be inaccurate even on instances of items in BNet vs. how they appear in-game. This is a known limitation of our item statistics, without any planned fix.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| disablePrimaryStatDisplay | boolean | If true, the game won't show the "primary" stat on this item when you inspect it.
NOTE: This is being manually mapped, because I happen to want it in a block that isn't going to directly create this derivative block. | No |
| statGroupHash | integer (uint32) | If the item's stats are meant to be modified by a DestinyStatGroupDefinition, this will be the identifier for that definition.
If you are using live data or precomputed stats data on the DestinyInventoryItemDefinition.stats.stats property, you don't have to worry about statGroupHash and how it alters stats: the already altered stats are provided to you. But if you want to see how the sausage gets made, or perform computations yourself, this is valuable information. | No |
| stats | object | If you are looking for precomputed values for the stats on a weapon, this is where they are stored. Technically these are the "Display" stat values. Please see DestinyStatsDefinition for what Display Stat Values means, it's a very long story... but essentially these are the closest values BNet can get to the item stats that you see in-game.
These stats are keyed by the DestinyStatDefinition's hash identifier for the stat that's found on the item. | No |
| hasDisplayableStats | boolean | A quick and lazy way to determine whether any stat other than the "primary" stat is actually visible on the item. Items often have stats that we return in case people find them useful, but they're not part of the "Stat Group" and thus we wouldn't display them in our UI. If this is False, then we're not going to display any of these stats other than the primary one. | No |
| primaryBaseStatHash | integer (uint32) | This stat is determined to be the "primary" stat, and can be looked up in the stats or any other stat collection related to the item.
Use this hash to look up the stat's value using DestinyInventoryItemDefinition.stats.stats, and the renderable data for the primary stat in the related DestinyStatDefinition. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemStatBlockDefinition object
const example = {
  disablePrimaryStatDisplay: true,
  statGroupHash: 123,
  stats: null,
  hasDisplayableStats: true,
  primaryBaseStatHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemStatBlockDefinition object
example = {
    "disablePrimaryStatDisplay": True,
    "statGroupHash": 123,
    "stats": None,
    "hasDisplayableStats": True,
    "primaryBaseStatHash": 123,
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryItemStatDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyStatDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyStatGroupDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyItemStatBlockDefinition":   {
      "description": "Information about the item's calculated stats, with as much data as we can find for the stats without having an actual instance of the item.\r\nNote that this means the entire concept of providing these stats is fundamentally insufficient: we cannot predict with 100% accuracy the conditions under which an item can spawn, so we use various heuristics to attempt to simulate the conditions as accurately as possible. Actual stats for items in-game can and will vary, but these should at least be useful base points for comparison and display.\r\nIt is also worth noting that some stats, like Magazine size, have further calculations performed on them by scripts in-game and on the game servers that BNet does not have access to. We cannot know how those stats are further transformed, and thus some stats will be inaccurate even on instances of items in BNet vs. how they appear in-game. This is a known limitation of our item statistics, without any planned fix.",
      "type": "object",
      "properties": {
          "disablePrimaryStatDisplay": {
              "description": "If true, the game won't show the \"primary\" stat on this item when you inspect it.\r\nNOTE: This is being manually mapped, because I happen to want it in a block that isn't going to directly create this derivative block.",
              "type": "boolean"
          },
          "statGroupHash": {
              "format": "uint32",
              "description": "If the item's stats are meant to be modified by a DestinyStatGroupDefinition, this will be the identifier for that definition.\r\nIf you are using live data or precomputed stats data on the DestinyInventoryItemDefinition.stats.stats property, you don't have to worry about statGroupHash and how it alters stats: the already altered stats are provided to you. But if you want to see how the sausage gets made, or perform computations yourself, this is valuable information.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyStatGroupDefinition"
              }
          },
          "stats": {
              "description": "If you are looking for precomputed values for the stats on a weapon, this is where they are stored. Technically these are the \"Display\" stat values. Please see DestinyStatsDefinition for what Display Stat Values means, it's a very long story... but essentially these are the closest values BNet can get to the item stats that you see in-game.\r\nThese stats are keyed by the DestinyStatDefinition's hash identifier for the stat that's found on the item.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemStatDefinition"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyStatDefinition"
              }
          },
          "hasDisplayableStats": {
              "description": "A quick and lazy way to determine whether any stat other than the \"primary\" stat is actually visible on the item. Items often have stats that we return in case people find them useful, but they're not part of the \"Stat Group\" and thus we wouldn't display them in our UI. If this is False, then we're not going to display any of these stats other than the primary one.",
              "type": "boolean"
          },
          "primaryBaseStatHash": {
              "format": "uint32",
              "description": "This stat is determined to be the \"primary\" stat, and can be looked up in the stats or any other stat collection related to the item.\r\nUse this hash to look up the stat's value using DestinyInventoryItemDefinition.stats.stats, and the renderable data for the primary stat in the related DestinyStatDefinition.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyStatDefinition"
              }
          }
      }
  }
}
```
