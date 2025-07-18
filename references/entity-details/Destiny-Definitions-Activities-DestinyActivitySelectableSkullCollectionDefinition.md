# Destiny.Definitions.Activities.DestinyActivitySelectableSkullCollectionDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Activities.DestinyActivitySelectableSkullCollectionDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Destiny API entity representing destinyactivityselectableskullcollectiondefinition data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| skullSubcategoryHashes | Array[integer] |  | No |
| selectionType | Destiny.Definitions.Activities.DestinyActivitySelectableSkullCollectionSelectionType |  | No |
| selectableActivitySkulls | Array[Destiny.Definitions.Activities.DestinyActivitySelectableSkull] |  | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Activities.DestinyActivitySelectableSkullCollectionDefinition object
const example = {
  displayProperties: null,
  skullSubcategoryHashes: [],
  selectionType: null,
  selectableActivitySkulls: [],
  hash: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Activities.DestinyActivitySelectableSkullCollectionDefinition object
example = {
    "displayProperties": None,
    "skullSubcategoryHashes": [],
    "selectionType": None,
    "selectableActivitySkulls": [],
    "hash": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Activities.DestinyActivitySelectableSkull**: Referenced in this entity
- **Destiny.Definitions.Activities.DestinyActivitySelectableSkullCollectionSelectionType**: Referenced in this entity
- **Destiny.Definitions.Activities.DestinyActivitySkullSubcategoryDefinition**: Referenced in this entity
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Activities.DestinyActivitySelectableSkullCollectionDefinition":   {
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "skullSubcategoryHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Activities.DestinyActivitySkullSubcategoryDefinition"
              }
          },
          "selectionType": {
              "$ref": "#/definitions/Destiny.Definitions.Activities.DestinyActivitySelectableSkullCollectionSelectionType"
          },
          "selectableActivitySkulls": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Activities.DestinyActivitySelectableSkull"
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
      "x-mobile-manifest-name": "ActivitySelectableSkullCollections"
  }
}
```
