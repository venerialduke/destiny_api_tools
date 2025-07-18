# Destiny.Definitions.Checklists.DestinyChecklistDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Checklists.DestinyChecklistDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
By public demand, Checklists are loose sets of "things to do/things you have done" in Destiny that we were actually able to track. They include easter eggs you find in the world, unique chests you unlock, and other such data where the first time you do it is significant enough to be tracked, and you have the potential to "get them all".
These may be account-wide, or may be per character. The status of these will be returned in related "Checklist" data coming down from API requests such as GetProfile or GetCharacter.
Generally speaking, the items in a checklist can be completed in any order: we return an ordered list which only implies the way we are showing them in our own UI, and you can feel free to alter it as you wish.
Note that, in the future, there will be something resembling the old D1 Record Books in at least some vague form. When that is created, it may be that it will supercede much or all of this Checklist data. It remains to be seen if that will be the case, so for now assume that the Checklists will still exist even after the release of D2: Forsaken.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| viewActionString | string | A localized string prompting you to view the checklist. | No |
| scope | integer (int32) | Indicates whether you will find this checklist on the Profile or Character components. | No |
| entries | Array[Destiny.Definitions.Checklists.DestinyChecklistEntryDefinition] | The individual checklist items. Gotta catch 'em all. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Checklists.DestinyChecklistDefinition object
const example = {
  displayProperties: null,
  viewActionString: "example value",
  scope: 123,
  entries: [],
  hash: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Checklists.DestinyChecklistDefinition object
example = {
    "displayProperties": None,
    "viewActionString": "example value",
    "scope": 123,
    "entries": [],
    "hash": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Checklists.DestinyChecklistEntryDefinition**: Referenced in this entity
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.DestinyScope**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Checklists.DestinyChecklistDefinition":   {
      "description": "By public demand, Checklists are loose sets of \"things to do/things you have done\" in Destiny that we were actually able to track. They include easter eggs you find in the world, unique chests you unlock, and other such data where the first time you do it is significant enough to be tracked, and you have the potential to \"get them all\".\r\nThese may be account-wide, or may be per character. The status of these will be returned in related \"Checklist\" data coming down from API requests such as GetProfile or GetCharacter.\r\nGenerally speaking, the items in a checklist can be completed in any order: we return an ordered list which only implies the way we are showing them in our own UI, and you can feel free to alter it as you wish.\r\nNote that, in the future, there will be something resembling the old D1 Record Books in at least some vague form. When that is created, it may be that it will supercede much or all of this Checklist data. It remains to be seen if that will be the case, so for now assume that the Checklists will still exist even after the release of D2: Forsaken.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "viewActionString": {
              "description": "A localized string prompting you to view the checklist.",
              "type": "string"
          },
          "scope": {
              "format": "int32",
              "description": "Indicates whether you will find this checklist on the Profile or Character components.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyScope"
              }
          },
          "entries": {
              "description": "The individual checklist items. Gotta catch 'em all.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Checklists.DestinyChecklistEntryDefinition"
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
      "x-mobile-manifest-name": "Checklists"
  }
}
```
