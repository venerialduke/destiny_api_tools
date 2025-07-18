# Destiny.Definitions.Activities.DestinyActivityInteractableDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Activities.DestinyActivityInteractableDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
There are times in every Activity's life when interacting with an object in the world will result in another Activity activating. Well, not every Activity. Just certain ones.
Anyways, this defines a set of interactable components, the activities that they spawn when you interact with them, and the conditions under which they can be interacted with.
Sadly, we don't get any *really* good data for them, like positional data... yet. I have hopes for future data that we could put on this.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| entries | Array[Destiny.Definitions.Activities.DestinyActivityInteractableEntryDefinition] | The possible interactables in this activity interactable definition. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Activities.DestinyActivityInteractableDefinition object
const example = {
  entries: [],
  hash: 123,
  index: 123,
  redacted: true,
};
```

### Python
```python
# Example Destiny.Definitions.Activities.DestinyActivityInteractableDefinition object
example = {
    "entries": [],
    "hash": 123,
    "index": 123,
    "redacted": True,
}
```

## Related Entities
- **Destiny.Definitions.Activities.DestinyActivityInteractableEntryDefinition**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Activities.DestinyActivityInteractableDefinition":   {
      "description": "There are times in every Activity's life when interacting with an object in the world will result in another Activity activating. Well, not every Activity. Just certain ones.\r\nAnyways, this defines a set of interactable components, the activities that they spawn when you interact with them, and the conditions under which they can be interacted with.\r\nSadly, we don't get any *really* good data for them, like positional data... yet. I have hopes for future data that we could put on this.",
      "type": "object",
      "properties": {
          "entries": {
              "description": "The possible interactables in this activity interactable definition.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Activities.DestinyActivityInteractableEntryDefinition"
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
      "x-mobile-manifest-name": "ActivityInteractables"
  }
}
```
