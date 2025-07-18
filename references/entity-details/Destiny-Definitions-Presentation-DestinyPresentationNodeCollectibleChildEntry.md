# Destiny.Definitions.Presentation.DestinyPresentationNodeCollectibleChildEntry

## Entity Information
- **Entity Name**: Destiny.Definitions.Presentation.DestinyPresentationNodeCollectibleChildEntry
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinypresentationnodecollectiblechildentry data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| collectibleHash | integer (uint32) |  | No |
| nodeDisplayPriority | integer (uint32) | Use this value to sort the presentation node children in ascending order. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Presentation.DestinyPresentationNodeCollectibleChildEntry object
const example = {
  collectibleHash: 123,
  nodeDisplayPriority: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Presentation.DestinyPresentationNodeCollectibleChildEntry object
example = {
    "collectibleHash": 123,
    "nodeDisplayPriority": 123,
}
```

## Related Entities
- **Destiny.Definitions.Collectibles.DestinyCollectibleDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Presentation.DestinyPresentationNodeCollectibleChildEntry":   {
      "type": "object",
      "properties": {
          "collectibleHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Collectibles.DestinyCollectibleDefinition"
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
