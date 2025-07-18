# Destiny.Definitions.Presentation.DestinyPresentationNodeCraftableChildEntry

## Entity Information
- **Entity Name**: Destiny.Definitions.Presentation.DestinyPresentationNodeCraftableChildEntry
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinypresentationnodecraftablechildentry data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| craftableItemHash | integer (uint32) |  | No |
| nodeDisplayPriority | integer (uint32) | Use this value to sort the presentation node children in ascending order. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Presentation.DestinyPresentationNodeCraftableChildEntry object
const example = {
  craftableItemHash: 123,
  nodeDisplayPriority: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Presentation.DestinyPresentationNodeCraftableChildEntry object
example = {
    "craftableItemHash": 123,
    "nodeDisplayPriority": 123,
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Presentation.DestinyPresentationNodeCraftableChildEntry":   {
      "type": "object",
      "properties": {
          "craftableItemHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
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
