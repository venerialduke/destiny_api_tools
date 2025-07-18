# Destiny.Definitions.DestinyTalentNodeExclusiveSetDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyTalentNodeExclusiveSetDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The list of indexes into the Talent Grid's "nodes" property for nodes in this exclusive set. (See DestinyTalentNodeDefinition.nodeIndex)

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| nodeIndexes | Array[integer] | The list of node indexes for the exclusive set. Historically, these were indexes. I would have liked to replace this with nodeHashes for consistency, but it's way too late for that. (9:09 PM, he's right!) | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyTalentNodeExclusiveSetDefinition object
const example = {
  nodeIndexes: [],
};
```

### Python
```python
# Example Destiny.Definitions.DestinyTalentNodeExclusiveSetDefinition object
example = {
    "nodeIndexes": [],
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyTalentNodeExclusiveSetDefinition":   {
      "description": "The list of indexes into the Talent Grid's \"nodes\" property for nodes in this exclusive set. (See DestinyTalentNodeDefinition.nodeIndex)",
      "type": "object",
      "properties": {
          "nodeIndexes": {
              "description": "The list of node indexes for the exclusive set. Historically, these were indexes. I would have liked to replace this with nodeHashes for consistency, but it's way too late for that. (9:09 PM, he's right!)",
              "type": "array",
              "items": {
                  "format": "int32",
                  "type": "integer"
              }
          }
      }
  }
}
```
