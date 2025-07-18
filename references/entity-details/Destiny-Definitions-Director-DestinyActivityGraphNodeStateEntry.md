# Destiny.Definitions.Director.DestinyActivityGraphNodeStateEntry

## Entity Information
- **Entity Name**: Destiny.Definitions.Director.DestinyActivityGraphNodeStateEntry
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Represents a single state that a graph node might end up in. Depending on what's going on in the game, graph nodes could be shown in different ways or even excluded from view entirely.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| state | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Director.DestinyActivityGraphNodeStateEntry object
const example = {
  state: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Director.DestinyActivityGraphNodeStateEntry object
example = {
    "state": 123,
}
```

## Related Entities
- **Destiny.DestinyGraphNodeState**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Director.DestinyActivityGraphNodeStateEntry":   {
      "description": "Represents a single state that a graph node might end up in. Depending on what's going on in the game, graph nodes could be shown in different ways or even excluded from view entirely.",
      "type": "object",
      "properties": {
          "state": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyGraphNodeState"
              }
          }
      }
  }
}
```
