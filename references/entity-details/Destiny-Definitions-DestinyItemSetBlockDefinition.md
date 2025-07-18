# Destiny.Definitions.DestinyItemSetBlockDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemSetBlockDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Primarily for Quests, this is the definition of properties related to the item if it is a quest and its various quest steps.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| itemList | Array[Destiny.Definitions.DestinyItemSetBlockEntryDefinition] | A collection of hashes of set items, for items such as Quest Metadata items that possess this data. | No |
| requireOrderedSetItemAdd | boolean | If true, items in the set can only be added in increasing order, and adding an item will remove any previous item. For Quests, this is by necessity true. Only one quest step is present at a time, and previous steps are removed as you advance in the quest. | No |
| setIsFeatured | boolean | If true, the UI should treat this quest as "featured" | No |
| setType | string | A string identifier we can use to attempt to identify the category of the Quest. | No |
| questLineName | string | The name of the quest line that this quest step is a part of. | No |
| questLineDescription | string | The description of the quest line that this quest step is a part of. | No |
| questStepSummary | string | An additional summary of this step in the quest line. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemSetBlockDefinition object
const example = {
  itemList: [],
  requireOrderedSetItemAdd: true,
  setIsFeatured: true,
  setType: "example value",
  questLineName: "example value",
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemSetBlockDefinition object
example = {
    "itemList": [],
    "requireOrderedSetItemAdd": True,
    "setIsFeatured": True,
    "setType": "example value",
    "questLineName": "example value",
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyItemSetBlockEntryDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyItemSetBlockDefinition":   {
      "description": "Primarily for Quests, this is the definition of properties related to the item if it is a quest and its various quest steps.",
      "type": "object",
      "properties": {
          "itemList": {
              "description": "A collection of hashes of set items, for items such as Quest Metadata items that possess this data.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyItemSetBlockEntryDefinition"
              }
          },
          "requireOrderedSetItemAdd": {
              "description": "If true, items in the set can only be added in increasing order, and adding an item will remove any previous item. For Quests, this is by necessity true. Only one quest step is present at a time, and previous steps are removed as you advance in the quest.",
              "type": "boolean"
          },
          "setIsFeatured": {
              "description": "If true, the UI should treat this quest as \"featured\"",
              "type": "boolean"
          },
          "setType": {
              "description": "A string identifier we can use to attempt to identify the category of the Quest.",
              "type": "string"
          },
          "questLineName": {
              "description": "The name of the quest line that this quest step is a part of.",
              "type": "string"
          },
          "questLineDescription": {
              "description": "The description of the quest line that this quest step is a part of.",
              "type": "string"
          },
          "questStepSummary": {
              "description": "An additional summary of this step in the quest line.",
              "type": "string"
          }
      }
  }
}
```
