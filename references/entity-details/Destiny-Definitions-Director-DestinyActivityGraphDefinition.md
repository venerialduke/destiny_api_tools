# Destiny.Definitions.Director.DestinyActivityGraphDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Director.DestinyActivityGraphDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Represents a Map View in the director: be them overview views, destination views, or other.
They have nodes which map to activities, and other various visual elements that we (or others) may or may not be able to use.
Activity graphs, most importantly, have nodes which can have activities in various states of playability.
Unfortunately, activity graphs are combined at runtime with Game UI-only assets such as fragments of map images, various in-game special effects, decals etc... that we don't get in these definitions.
If we end up having time, we may end up trying to manually populate those here: but the last time we tried that, before the lead-up to D1, it proved to be unmaintainable as the game's content changed. So don't bet the farm on us providing that content in this definition.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| nodes | Array[Destiny.Definitions.Director.DestinyActivityGraphNodeDefinition] | These represent the visual "nodes" on the map's view. These are the activities you can click on in the map. | No |
| artElements | Array[Destiny.Definitions.Director.DestinyActivityGraphArtElementDefinition] | Represents one-off/special UI elements that appear on the map. | No |
| connections | Array[Destiny.Definitions.Director.DestinyActivityGraphConnectionDefinition] | Represents connections between graph nodes. However, it lacks context that we'd need to make good use of it. | No |
| displayObjectives | Array[Destiny.Definitions.Director.DestinyActivityGraphDisplayObjectiveDefinition] | Objectives can display on maps, and this is supposedly metadata for that. I have not had the time to analyze the details of what is useful within however: we could be missing important data to make this work. Expect this property to be expanded on later if possible. | No |
| displayProgressions | Array[Destiny.Definitions.Director.DestinyActivityGraphDisplayProgressionDefinition] | Progressions can also display on maps, but similarly to displayObjectives we appear to lack some required information and context right now. We will have to look into it later and add more data if possible. | No |
| linkedGraphs | Array[Destiny.Definitions.Director.DestinyLinkedGraphDefinition] | Represents links between this Activity Graph and other ones. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Director.DestinyActivityGraphDefinition object
const example = {
  nodes: [],
  artElements: [],
  connections: [],
  displayObjectives: [],
  displayProgressions: [],
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Director.DestinyActivityGraphDefinition object
example = {
    "nodes": [],
    "artElements": [],
    "connections": [],
    "displayObjectives": [],
    "displayProgressions": [],
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Director.DestinyActivityGraphArtElementDefinition**: Referenced in this entity
- **Destiny.Definitions.Director.DestinyActivityGraphConnectionDefinition**: Referenced in this entity
- **Destiny.Definitions.Director.DestinyActivityGraphDisplayObjectiveDefinition**: Referenced in this entity
- **Destiny.Definitions.Director.DestinyActivityGraphDisplayProgressionDefinition**: Referenced in this entity
- **Destiny.Definitions.Director.DestinyActivityGraphNodeDefinition**: Referenced in this entity
- **Destiny.Definitions.Director.DestinyLinkedGraphDefinition**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Director.DestinyActivityGraphDefinition":   {
      "description": "Represents a Map View in the director: be them overview views, destination views, or other.\r\nThey have nodes which map to activities, and other various visual elements that we (or others) may or may not be able to use.\r\nActivity graphs, most importantly, have nodes which can have activities in various states of playability.\r\nUnfortunately, activity graphs are combined at runtime with Game UI-only assets such as fragments of map images, various in-game special effects, decals etc... that we don't get in these definitions.\r\nIf we end up having time, we may end up trying to manually populate those here: but the last time we tried that, before the lead-up to D1, it proved to be unmaintainable as the game's content changed. So don't bet the farm on us providing that content in this definition.",
      "type": "object",
      "properties": {
          "nodes": {
              "description": "These represent the visual \"nodes\" on the map's view. These are the activities you can click on in the map.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Director.DestinyActivityGraphNodeDefinition"
              }
          },
          "artElements": {
              "description": "Represents one-off/special UI elements that appear on the map.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Director.DestinyActivityGraphArtElementDefinition"
              }
          },
          "connections": {
              "description": "Represents connections between graph nodes. However, it lacks context that we'd need to make good use of it.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Director.DestinyActivityGraphConnectionDefinition"
              }
          },
          "displayObjectives": {
              "description": "Objectives can display on maps, and this is supposedly metadata for that. I have not had the time to analyze the details of what is useful within however: we could be missing important data to make this work. Expect this property to be expanded on later if possible.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Director.DestinyActivityGraphDisplayObjectiveDefinition"
              }
          },
          "displayProgressions": {
              "description": "Progressions can also display on maps, but similarly to displayObjectives we appear to lack some required information and context right now. We will have to look into it later and add more data if possible.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Director.DestinyActivityGraphDisplayProgressionDefinition"
              }
          },
          "linkedGraphs": {
              "description": "Represents links between this Activity Graph and other ones.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Director.DestinyLinkedGraphDefinition"
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
      "x-mobile-manifest-name": "ActivityGraphs"
  }
}
```
