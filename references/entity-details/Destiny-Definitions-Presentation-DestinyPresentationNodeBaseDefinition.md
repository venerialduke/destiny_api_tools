# Destiny.Definitions.Presentation.DestinyPresentationNodeBaseDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Presentation.DestinyPresentationNodeBaseDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
This is the base class for all presentation system children. Presentation Nodes, Records, Collectibles, and Metrics.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
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
// Example Destiny.Definitions.Presentation.DestinyPresentationNodeBaseDefinition object
const example = {
  presentationNodeType: 123,
  traitIds: [],
  traitHashes: [],
  parentNodeHashes: [],
  hash: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Presentation.DestinyPresentationNodeBaseDefinition object
example = {
    "presentationNodeType": 123,
    "traitIds": [],
    "traitHashes": [],
    "parentNodeHashes": [],
    "hash": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition**: Referenced in this entity
- **Destiny.Definitions.Traits.DestinyTraitDefinition**: Referenced in this entity
- **Destiny.DestinyPresentationNodeType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Presentation.DestinyPresentationNodeBaseDefinition":   {
      "description": "This is the base class for all presentation system children. Presentation Nodes, Records, Collectibles, and Metrics.",
      "type": "object",
      "properties": {
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
      }
  }
}
```
