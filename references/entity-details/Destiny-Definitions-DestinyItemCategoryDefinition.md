# Destiny.Definitions.DestinyItemCategoryDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemCategoryDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
In an attempt to categorize items by type, usage, and other interesting properties, we created DestinyItemCategoryDefinition: information about types that is assembled using a set of heuristics that examine the properties of an item such as what inventory bucket it's in, its item type name, and whether it has or is missing certain blocks of data.
This heuristic is imperfect, however. If you find an item miscategorized, let us know on the Bungie API forums!
We then populate all of the categories that we think an item belongs to in its DestinyInventoryItemDefinition.itemCategoryHashes property. You can use that to provide your own custom item filtering, sorting, aggregating... go nuts on it! And let us know if you see more categories that you wish would be added!

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| visible | boolean | If True, this category should be visible in UI. Sometimes we make categories that we don't think are interesting externally. It's up to you if you want to skip on showing them. | No |
| deprecated | boolean | If True, this category has been deprecated: it may have no items left, or there may be only legacy items that remain in it which are no longer relevant to the game. | No |
| shortTitle | string | A shortened version of the title. The reason why we have this is because the Armory in German had titles that were too long to display in our UI, so these were localized abbreviated versions of those categories. The property still exists today, even though the Armory doesn't exist for D2... yet. | No |
| itemTypeRegex | string | The janky regular expression we used against the item type to try and discern whether the item belongs to this category. | No |
| grantDestinyBreakerType | integer (int32) | If the item in question has this category, it also should have this breaker type. | No |
| plugCategoryIdentifier | string | If the item is a plug, this is the identifier we expect to find associated with it if it is in this category. | No |
| itemTypeRegexNot | string | If the item type matches this janky regex, it does *not* belong to this category. | No |
| originBucketIdentifier | string | If the item belongs to this bucket, it does belong to this category. | No |
| grantDestinyItemType | integer (int32) | If an item belongs to this category, it will also receive this item type. This is now how DestinyItemType is populated for items: it used to be an even jankier process, but that's a story that requires more alcohol. | No |
| grantDestinySubType | integer (int32) | If an item belongs to this category, it will also receive this subtype enum value.
I know what you're thinking - what if it belongs to multiple categories that provide sub-types?
The last one processed wins, as is the case with all of these "grant" enums. Now you can see one reason why we moved away from these enums... but they're so convenient when they work, aren't they? | No |
| grantDestinyClass | integer (int32) | If an item belongs to this category, it will also get this class restriction enum value.
See the other "grant"-prefixed properties on this definition for my color commentary. | No |
| traitId | string | The traitId that can be found on items that belong to this category. | No |
| groupedCategoryHashes | Array[integer] | If this category is a "parent" category of other categories, those children will have their hashes listed in rendering order here, and can be looked up using these hashes against DestinyItemCategoryDefinition.
In this way, you can build up a visual hierarchy of item categories. That's what we did, and you can do it too. I believe in you. Yes, you, Carl.
(I hope someone named Carl reads this someday) | No |
| parentCategoryHashes | Array[integer] | All item category hashes of "parent" categories: categories that contain this as a child through the hierarchy of groupedCategoryHashes. It's a bit redundant, but having this child-centric list speeds up some calculations. | No |
| groupCategoryOnly | boolean | If true, this category is only used for grouping, and should not be evaluated with its own checks. Rather, the item only has this category if it has one of its child categories. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemCategoryDefinition object
const example = {
  displayProperties: null,
  visible: true,
  deprecated: true,
  shortTitle: "example value",
  itemTypeRegex: "example value",
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemCategoryDefinition object
example = {
    "displayProperties": None,
    "visible": True,
    "deprecated": True,
    "shortTitle": "example value",
    "itemTypeRegex": "example value",
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyItemCategoryDefinition**: Referenced in this entity
- **Destiny.DestinyBreakerType**: Referenced in this entity
- **Destiny.DestinyClass**: Referenced in this entity
- **Destiny.DestinyItemSubType**: Referenced in this entity
- **Destiny.DestinyItemType**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyItemCategoryDefinition":   {
      "description": "In an attempt to categorize items by type, usage, and other interesting properties, we created DestinyItemCategoryDefinition: information about types that is assembled using a set of heuristics that examine the properties of an item such as what inventory bucket it's in, its item type name, and whether it has or is missing certain blocks of data.\r\nThis heuristic is imperfect, however. If you find an item miscategorized, let us know on the Bungie API forums!\r\nWe then populate all of the categories that we think an item belongs to in its DestinyInventoryItemDefinition.itemCategoryHashes property. You can use that to provide your own custom item filtering, sorting, aggregating... go nuts on it! And let us know if you see more categories that you wish would be added!",
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "visible": {
              "description": "If True, this category should be visible in UI. Sometimes we make categories that we don't think are interesting externally. It's up to you if you want to skip on showing them.",
              "type": "boolean"
          },
          "deprecated": {
              "description": "If True, this category has been deprecated: it may have no items left, or there may be only legacy items that remain in it which are no longer relevant to the game.",
              "type": "boolean"
          },
          "shortTitle": {
              "description": "A shortened version of the title. The reason why we have this is because the Armory in German had titles that were too long to display in our UI, so these were localized abbreviated versions of those categories. The property still exists today, even though the Armory doesn't exist for D2... yet.",
              "type": "string"
          },
          "itemTypeRegex": {
              "description": "The janky regular expression we used against the item type to try and discern whether the item belongs to this category.",
              "type": "string"
          },
          "grantDestinyBreakerType": {
              "format": "int32",
              "description": "If the item in question has this category, it also should have this breaker type.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyBreakerType"
              }
          },
          "plugCategoryIdentifier": {
              "description": "If the item is a plug, this is the identifier we expect to find associated with it if it is in this category.",
              "type": "string"
          },
          "itemTypeRegexNot": {
              "description": "If the item type matches this janky regex, it does *not* belong to this category.",
              "type": "string"
          },
          "originBucketIdentifier": {
              "description": "If the item belongs to this bucket, it does belong to this category.",
              "type": "string"
          },
          "grantDestinyItemType": {
              "format": "int32",
              "description": "If an item belongs to this category, it will also receive this item type. This is now how DestinyItemType is populated for items: it used to be an even jankier process, but that's a story that requires more alcohol.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyItemType"
              }
          },
          "grantDestinySubType": {
              "format": "int32",
              "description": "If an item belongs to this category, it will also receive this subtype enum value.\r\nI know what you're thinking - what if it belongs to multiple categories that provide sub-types?\r\nThe last one processed wins, as is the case with all of these \"grant\" enums. Now you can see one reason why we moved away from these enums... but they're so convenient when they work, aren't they?",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyItemSubType"
              }
          },
          "grantDestinyClass": {
              "format": "int32",
              "description": "If an item belongs to this category, it will also get this class restriction enum value.\r\nSee the other \"grant\"-prefixed properties on this definition for my color commentary.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyClass"
              }
          },
          "traitId": {
              "description": "The traitId that can be found on items that belong to this category.",
              "type": "string"
          },
          "groupedCategoryHashes": {
              "description": "If this category is a \"parent\" category of other categories, those children will have their hashes listed in rendering order here, and can be looked up using these hashes against DestinyItemCategoryDefinition.\r\nIn this way, you can build up a visual hierarchy of item categories. That's what we did, and you can do it too. I believe in you. Yes, you, Carl.\r\n(I hope someone named Carl reads this someday)",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyItemCategoryDefinition"
              }
          },
          "parentCategoryHashes": {
              "description": "All item category hashes of \"parent\" categories: categories that contain this as a child through the hierarchy of groupedCategoryHashes. It's a bit redundant, but having this child-centric list speeds up some calculations.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              }
          },
          "groupCategoryOnly": {
              "description": "If true, this category is only used for grouping, and should not be evaluated with its own checks. Rather, the item only has this category if it has one of its child categories.",
              "type": "boolean"
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
      "x-mobile-manifest-name": "ItemCategories"
  }
}
```
