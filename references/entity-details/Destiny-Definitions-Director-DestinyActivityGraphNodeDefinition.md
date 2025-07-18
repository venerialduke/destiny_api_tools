# Destiny.Definitions.Director.DestinyActivityGraphNodeDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Director.DestinyActivityGraphNodeDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
This is the position and other data related to nodes in the activity graph that you can click to launch activities. An Activity Graph node will only have one active Activity at a time, which will determine the activity to be launched (and, unless overrideDisplay information is provided, will also determine the tooltip and other UI related to the node)

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| nodeId | integer (uint32) | An identifier for the Activity Graph Node, only guaranteed to be unique within its parent Activity Graph. | No |
| overrideDisplay | object | The node *may* have display properties that override the active Activity's display properties. | No |
| position | object | The position on the map for this node. | No |
| featuringStates | Array[Destiny.Definitions.Director.DestinyActivityGraphNodeFeaturingStateDefinition] | The node may have various visual accents placed on it, or styles applied. These are the list of possible styles that the Node can have. The game iterates through each, looking for the first one that passes a check of the required game/character/account state in order to show that style, and then renders the node in that style. | No |
| activities | Array[Destiny.Definitions.Director.DestinyActivityGraphNodeActivityDefinition] | The node may have various possible activities that could be active for it, however only one may be active at a time. See the DestinyActivityGraphNodeActivityDefinition for details. | No |
| states | Array[Destiny.Definitions.Director.DestinyActivityGraphNodeStateEntry] | Represents possible states that the graph node can be in. These are combined with some checking that happens in the game client and server to determine which state is actually active at any given time. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Director.DestinyActivityGraphNodeDefinition object
const example = {
  nodeId: 123,
  overrideDisplay: null,
  position: null,
  featuringStates: [],
  activities: [],
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Director.DestinyActivityGraphNodeDefinition object
example = {
    "nodeId": 123,
    "overrideDisplay": None,
    "position": None,
    "featuringStates": [],
    "activities": [],
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.Common.DestinyPositionDefinition**: Referenced in this entity
- **Destiny.Definitions.Director.DestinyActivityGraphNodeActivityDefinition**: Referenced in this entity
- **Destiny.Definitions.Director.DestinyActivityGraphNodeFeaturingStateDefinition**: Referenced in this entity
- **Destiny.Definitions.Director.DestinyActivityGraphNodeStateEntry**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Director.DestinyActivityGraphNodeDefinition":   {
      "description": "This is the position and other data related to nodes in the activity graph that you can click to launch activities. An Activity Graph node will only have one active Activity at a time, which will determine the activity to be launched (and, unless overrideDisplay information is provided, will also determine the tooltip and other UI related to the node)",
      "type": "object",
      "properties": {
          "nodeId": {
              "format": "uint32",
              "description": "An identifier for the Activity Graph Node, only guaranteed to be unique within its parent Activity Graph.",
              "type": "integer"
          },
          "overrideDisplay": {
              "description": "The node *may* have display properties that override the active Activity's display properties.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
                  }
              ]
          },
          "position": {
              "description": "The position on the map for this node.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Common.DestinyPositionDefinition"
                  }
              ]
          },
          "featuringStates": {
              "description": "The node may have various visual accents placed on it, or styles applied. These are the list of possible styles that the Node can have. The game iterates through each, looking for the first one that passes a check of the required game/character/account state in order to show that style, and then renders the node in that style.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Director.DestinyActivityGraphNodeFeaturingStateDefinition"
              }
          },
          "activities": {
              "description": "The node may have various possible activities that could be active for it, however only one may be active at a time. See the DestinyActivityGraphNodeActivityDefinition for details.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Director.DestinyActivityGraphNodeActivityDefinition"
              }
          },
          "states": {
              "description": "Represents possible states that the graph node can be in. These are combined with some checking that happens in the game client and server to determine which state is actually active at any given time.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Director.DestinyActivityGraphNodeStateEntry"
              }
          }
      }
  }
}
```
