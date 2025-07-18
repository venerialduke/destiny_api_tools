# Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
A PresentationNode is an entity that represents a logical grouping of other entities visually/organizationally.
For now, Presentation Nodes may contain the following... but it may be used for more in the future:
- Collectibles - Records (Or, as the public will call them, "Triumphs." Don't ask me why we're overloading the term "Triumph", it still hurts me to think about it) - Metrics (aka Stat Trackers) - Other Presentation Nodes, allowing a tree of Presentation Nodes to be created
Part of me wants to break these into conceptual definitions per entity being collected, but the possibility of these different types being mixed in the same UI and the possibility that it could actually be more useful to return the "bare metal" presentation node concept has resulted in me deciding against that for the time being.
We'll see if I come to regret this as well.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| originalIcon | string | The original icon for this presentation node, before we futzed with it. | No |
| rootViewIcon | string | Some presentation nodes are meant to be explicitly shown on the "root" or "entry" screens for the feature to which they are related. You should use this icon when showing them on such a view, if you have a similar "entry point" view in your UI. If you don't have a UI, then I guess it doesn't matter either way does it? | No |
| nodeType | integer (int32) |  | No |
| isSeasonal | boolean | Primarily for Guardian Ranks, this property if the contents of this node are tied to the current season. These nodes are shown with a different color for the in-game Guardian Ranks display. | No |
| scope | integer (int32) | Indicates whether this presentation node's state is determined on a per-character or on an account-wide basis. | No |
| objectiveHash | integer (uint32) | If this presentation node shows a related objective (for instance, if it tracks the progress of its children), the objective being tracked is indicated here. | No |
| completionRecordHash | integer (uint32) | If this presentation node has an associated "Record" that you can accomplish for completing its children, this is the identifier of that Record. | No |
| children | object | The child entities contained by this presentation node. | No |
| displayStyle | integer (int32) | A hint for how to display this presentation node when it's shown in a list. | No |
| screenStyle | integer (int32) | A hint for how to display this presentation node when it's shown in its own detail screen. | No |
| requirements | object | The requirements for being able to interact with this presentation node and its children. | No |
| disableChildSubscreenNavigation | boolean | If this presentation node has children, but the game doesn't let you inspect the details of those children, that is indicated here. | No |
| maxCategoryRecordScore | integer (int32) |  | No |
| presentationNodeType | integer (int32) |  | No |
| traitIds | Array[string] |  | No |
| traitHashes | Array[integer] |  | No |
| parentNodeHashes | Array[integer] | A quick reference to presentation nodes that have this node as a child. Presentation nodes can be parented under multiple parents. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition object
const example = {
  displayProperties: null,
  originalIcon: "example value",
  rootViewIcon: "example value",
  nodeType: 123,
  isSeasonal: true,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition object
example = {
    "displayProperties": None,
    "originalIcon": "example value",
    "rootViewIcon": "example value",
    "nodeType": 123,
    "isSeasonal": True,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyObjectiveDefinition**: Referenced in this entity
- **Destiny.Definitions.Presentation.DestinyPresentationNodeChildrenBlock**: Referenced in this entity
- **Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition**: Referenced in this entity
- **Destiny.Definitions.Presentation.DestinyPresentationNodeRequirementsBlock**: Referenced in this entity
- **Destiny.Definitions.Records.DestinyRecordDefinition**: Referenced in this entity
- **Destiny.Definitions.Traits.DestinyTraitDefinition**: Referenced in this entity
- **Destiny.DestinyPresentationDisplayStyle**: Referenced in this entity
- **Destiny.DestinyPresentationNodeType**: Referenced in this entity
- **Destiny.DestinyPresentationScreenStyle**: Referenced in this entity
- **Destiny.DestinyScope**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition":   {
      "description": "A PresentationNode is an entity that represents a logical grouping of other entities visually/organizationally.\r\nFor now, Presentation Nodes may contain the following... but it may be used for more in the future:\r\n- Collectibles - Records (Or, as the public will call them, \"Triumphs.\" Don't ask me why we're overloading the term \"Triumph\", it still hurts me to think about it) - Metrics (aka Stat Trackers) - Other Presentation Nodes, allowing a tree of Presentation Nodes to be created\r\nPart of me wants to break these into conceptual definitions per entity being collected, but the possibility of these different types being mixed in the same UI and the possibility that it could actually be more useful to return the \"bare metal\" presentation node concept has resulted in me deciding against that for the time being.\r\nWe'll see if I come to regret this as well.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "originalIcon": {
              "description": "The original icon for this presentation node, before we futzed with it.",
              "type": "string"
          },
          "rootViewIcon": {
              "description": "Some presentation nodes are meant to be explicitly shown on the \"root\" or \"entry\" screens for the feature to which they are related. You should use this icon when showing them on such a view, if you have a similar \"entry point\" view in your UI. If you don't have a UI, then I guess it doesn't matter either way does it?",
              "type": "string"
          },
          "nodeType": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyPresentationNodeType"
              }
          },
          "isSeasonal": {
              "description": "Primarily for Guardian Ranks, this property if the contents of this node are tied to the current season. These nodes are shown with a different color for the in-game Guardian Ranks display.",
              "type": "boolean"
          },
          "scope": {
              "format": "int32",
              "description": "Indicates whether this presentation node's state is determined on a per-character or on an account-wide basis.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyScope"
              }
          },
          "objectiveHash": {
              "format": "uint32",
              "description": "If this presentation node shows a related objective (for instance, if it tracks the progress of its children), the objective being tracked is indicated here.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyObjectiveDefinition"
              }
          },
          "completionRecordHash": {
              "format": "uint32",
              "description": "If this presentation node has an associated \"Record\" that you can accomplish for completing its children, this is the identifier of that Record.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Records.DestinyRecordDefinition"
              }
          },
          "children": {
              "description": "The child entities contained by this presentation node.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeChildrenBlock"
                  }
              ]
          },
          "displayStyle": {
              "format": "int32",
              "description": "A hint for how to display this presentation node when it's shown in a list.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyPresentationDisplayStyle"
              }
          },
          "screenStyle": {
              "format": "int32",
              "description": "A hint for how to display this presentation node when it's shown in its own detail screen.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyPresentationScreenStyle"
              }
          },
          "requirements": {
              "description": "The requirements for being able to interact with this presentation node and its children.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeRequirementsBlock"
                  }
              ]
          },
          "disableChildSubscreenNavigation": {
              "description": "If this presentation node has children, but the game doesn't let you inspect the details of those children, that is indicated here.",
              "type": "boolean"
          },
          "maxCategoryRecordScore": {
              "format": "int32",
              "type": "integer"
          },
          "presentationNodeType": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyPresentationNodeType"
              }
          },
          "traitIds": {
              "type": "array",
              "items": {
                  "type": "string"
              }
          },
          "traitHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Traits.DestinyTraitDefinition"
              }
          },
          "parentNodeHashes": {
              "description": "A quick reference to presentation nodes that have this node as a child. Presentation nodes can be parented under multiple parents.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
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
      "x-mobile-manifest-name": "PresentationNodes"
  }
}
```
