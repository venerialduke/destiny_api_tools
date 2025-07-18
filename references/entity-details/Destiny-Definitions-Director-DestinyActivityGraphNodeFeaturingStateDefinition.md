# Destiny.Definitions.Director.DestinyActivityGraphNodeFeaturingStateDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Director.DestinyActivityGraphNodeFeaturingStateDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Nodes can have different visual states. This object represents a single visual state ("highlight type") that a node can be in, and the unlock expression condition to determine whether it should be set.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| highlightType | integer (int32) | The node can be highlighted in a variety of ways - the game iterates through these and finds the first FeaturingState that is valid at the present moment given the Game, Account, and Character state, and renders the node in that state. See the ActivityGraphNodeHighlightType enum for possible values. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Director.DestinyActivityGraphNodeFeaturingStateDefinition object
const example = {
  highlightType: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Director.DestinyActivityGraphNodeFeaturingStateDefinition object
example = {
    "highlightType": 123,
}
```

## Related Entities
- **Destiny.ActivityGraphNodeHighlightType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Director.DestinyActivityGraphNodeFeaturingStateDefinition":   {
      "description": "Nodes can have different visual states. This object represents a single visual state (\"highlight type\") that a node can be in, and the unlock expression condition to determine whether it should be set.",
      "type": "object",
      "properties": {
          "highlightType": {
              "format": "int32",
              "description": "The node can be highlighted in a variety of ways - the game iterates through these and finds the first FeaturingState that is valid at the present moment given the Game, Account, and Character state, and renders the node in that state. See the ActivityGraphNodeHighlightType enum for possible values.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.ActivityGraphNodeHighlightType"
              }
          }
      }
  }
}
```
