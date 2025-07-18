# Destiny.Definitions.DestinyStatGroupDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyStatGroupDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
When an inventory item (DestinyInventoryItemDefinition) has Stats (such as Attack Power), the item will refer to a Stat Group. This definition enumerates the properties used to transform the item's "Investment" stats into "Display" stats.
See DestinyStatDefinition's documentation for information about the transformation of Stats, and the meaning of an Investment vs. a Display stat.
If you don't want to do these calculations on your own, fear not: pulling live data from the BNet endpoints will return display stat values pre-computed and ready for you to use. I highly recommend this approach, saves a lot of time and also accounts for certain stat modifiers that can't easily be accounted for without live data (such as stat modifiers on Talent Grids and Socket Plugs)

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| maximumValue | integer (int32) | The maximum possible value that any stat in this group can be transformed into.
This is used by stats that *don't* have scaledStats entries below, but that still need to be displayed as a progress bar, in which case this is used as the upper bound for said progress bar. (the lower bound is always 0) | No |
| uiPosition | integer (int32) | This apparently indicates the position of the stats in the UI? I've returned it in case anyone can use it, but it's not of any use to us on BNet. Something's being lost in translation with this value. | No |
| scaledStats | Array[Destiny.Definitions.DestinyStatDisplayDefinition] | Any stat that requires scaling to be transformed from an "Investment" stat to a "Display" stat will have an entry in this list. For more information on what those types of stats mean and the transformation process, see DestinyStatDefinition.
In retrospect, I wouldn't mind if this was a dictionary keyed by the stat hash instead. But I'm going to leave it be because [[After Apple Picking]]. | No |
| overrides | object | The game has the ability to override, based on the stat group, what the localized text is that is displayed for Stats being shown on the item.
Mercifully, no Stat Groups use this feature currently. If they start using them, we'll all need to start using them (and those of you who are more prudent than I am can go ahead and start pre-checking for this.) | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyStatGroupDefinition object
const example = {
  maximumValue: 123,
  uiPosition: 123,
  scaledStats: [],
  overrides: null,
  hash: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyStatGroupDefinition object
example = {
    "maximumValue": 123,
    "uiPosition": 123,
    "scaledStats": [],
    "overrides": None,
    "hash": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyStatDisplayDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyStatOverrideDefinition**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyStatGroupDefinition":   {
      "description": "When an inventory item (DestinyInventoryItemDefinition) has Stats (such as Attack Power), the item will refer to a Stat Group. This definition enumerates the properties used to transform the item's \"Investment\" stats into \"Display\" stats.\r\nSee DestinyStatDefinition's documentation for information about the transformation of Stats, and the meaning of an Investment vs. a Display stat.\r\nIf you don't want to do these calculations on your own, fear not: pulling live data from the BNet endpoints will return display stat values pre-computed and ready for you to use. I highly recommend this approach, saves a lot of time and also accounts for certain stat modifiers that can't easily be accounted for without live data (such as stat modifiers on Talent Grids and Socket Plugs)",
      "type": "object",
      "properties": {
          "maximumValue": {
              "format": "int32",
              "description": "The maximum possible value that any stat in this group can be transformed into.\r\nThis is used by stats that *don't* have scaledStats entries below, but that still need to be displayed as a progress bar, in which case this is used as the upper bound for said progress bar. (the lower bound is always 0)",
              "type": "integer"
          },
          "uiPosition": {
              "format": "int32",
              "description": "This apparently indicates the position of the stats in the UI? I've returned it in case anyone can use it, but it's not of any use to us on BNet. Something's being lost in translation with this value.",
              "type": "integer"
          },
          "scaledStats": {
              "description": "Any stat that requires scaling to be transformed from an \"Investment\" stat to a \"Display\" stat will have an entry in this list. For more information on what those types of stats mean and the transformation process, see DestinyStatDefinition.\r\nIn retrospect, I wouldn't mind if this was a dictionary keyed by the stat hash instead. But I'm going to leave it be because [[After Apple Picking]].",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyStatDisplayDefinition"
              }
          },
          "overrides": {
              "description": "The game has the ability to override, based on the stat group, what the localized text is that is displayed for Stats being shown on the item.\r\nMercifully, no Stat Groups use this feature currently. If they start using them, we'll all need to start using them (and those of you who are more prudent than I am can go ahead and start pre-checking for this.)",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyStatOverrideDefinition"
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
      "x-mobile-manifest-name": "StatGroups"
  }
}
```
