# Destiny.Definitions.DestinyTalentExclusiveGroup

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyTalentExclusiveGroup
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
As of Destiny 2, nodes can exist as part of "Exclusive Groups". These differ from exclusive sets in that, within the group, many nodes can be activated. But the act of activating any node in the group will cause "opposing" nodes (nodes in groups that are not allowed to be activated at the same time as this group) to deactivate.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| groupHash | integer (uint32) | The identifier for this exclusive group. Only guaranteed unique within the talent grid, not globally. | No |
| loreHash | integer (uint32) | If this group has an associated piece of lore to show next to it, this will be the identifier for that DestinyLoreDefinition. | No |
| nodeHashes | Array[integer] | A quick reference of the talent nodes that are part of this group, by their Talent Node hashes. (See DestinyTalentNodeDefinition.nodeHash) | No |
| opposingGroupHashes | Array[integer] | A quick reference of Groups whose nodes will be deactivated if any node in this group is activated. | No |
| opposingNodeHashes | Array[integer] | A quick reference of Nodes that will be deactivated if any node in this group is activated, by their Talent Node hashes. (See DestinyTalentNodeDefinition.nodeHash) | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyTalentExclusiveGroup object
const example = {
  groupHash: 123,
  loreHash: 123,
  nodeHashes: [],
  opposingGroupHashes: [],
  opposingNodeHashes: [],
};
```

### Python
```python
# Example Destiny.Definitions.DestinyTalentExclusiveGroup object
example = {
    "groupHash": 123,
    "loreHash": 123,
    "nodeHashes": [],
    "opposingGroupHashes": [],
    "opposingNodeHashes": [],
}
```

## Related Entities
- **Destiny.Definitions.Lore.DestinyLoreDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyTalentExclusiveGroup":   {
      "description": "As of Destiny 2, nodes can exist as part of \"Exclusive Groups\". These differ from exclusive sets in that, within the group, many nodes can be activated. But the act of activating any node in the group will cause \"opposing\" nodes (nodes in groups that are not allowed to be activated at the same time as this group) to deactivate.",
      "type": "object",
      "properties": {
          "groupHash": {
              "format": "uint32",
              "description": "The identifier for this exclusive group. Only guaranteed unique within the talent grid, not globally.",
              "type": "integer"
          },
          "loreHash": {
              "format": "uint32",
              "description": "If this group has an associated piece of lore to show next to it, this will be the identifier for that DestinyLoreDefinition.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Lore.DestinyLoreDefinition"
              }
          },
          "nodeHashes": {
              "description": "A quick reference of the talent nodes that are part of this group, by their Talent Node hashes. (See DestinyTalentNodeDefinition.nodeHash)",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              }
          },
          "opposingGroupHashes": {
              "description": "A quick reference of Groups whose nodes will be deactivated if any node in this group is activated.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              }
          },
          "opposingNodeHashes": {
              "description": "A quick reference of Nodes that will be deactivated if any node in this group is activated, by their Talent Node hashes. (See DestinyTalentNodeDefinition.nodeHash)",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              }
          }
      }
  }
}
```
