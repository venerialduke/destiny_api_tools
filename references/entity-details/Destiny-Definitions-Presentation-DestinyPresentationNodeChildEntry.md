# Destiny.Definitions.Presentation.DestinyPresentationNodeChildEntry

## Entity Information
- **Entity Name**: Destiny.Definitions.Presentation.DestinyPresentationNodeChildEntry
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinypresentationnodechildentry data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| presentationNodeHash | integer (uint32) |  | No |
| nodeDisplayPriority | integer (uint32) | Use this value to sort the presentation node children in ascending order. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Presentation.DestinyPresentationNodeChildEntry object
const example = {
  presentationNodeHash: 123,
  nodeDisplayPriority: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Presentation.DestinyPresentationNodeChildEntry object
example = {
    "presentationNodeHash": 123,
    "nodeDisplayPriority": 123,
}
```

## Related Entities
- **Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Presentation.DestinyPresentationNodeChildEntry":   {
      "type": "object",
      "properties": {
          "presentationNodeHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
              }
          },
          "nodeDisplayPriority": {
              "format": "uint32",
              "description": "Use this value to sort the presentation node children in ascending order.",
              "type": "integer"
          }
      }
  }
}
```
