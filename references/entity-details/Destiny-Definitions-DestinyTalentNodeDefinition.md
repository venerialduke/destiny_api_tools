# Destiny.Definitions.DestinyTalentNodeDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyTalentNodeDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Talent Grids on items have Nodes. These nodes have positions in the talent grid's UI, and contain "Steps" (DestinyTalentNodeStepDefinition), one of whom will be the "Current" step.
The Current Step determines the visual properties of the node, as well as what the node grants when it is activated.
See DestinyTalentGridDefinition for a more complete overview of how Talent Grids work, and how they are used in Destiny 2 (and how they were used in Destiny 1).

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| nodeIndex | integer (int32) | The index into the DestinyTalentGridDefinition's "nodes" property where this node is located. Used to uniquely identify the node within the Talent Grid. Note that this is content version dependent: make sure you have the latest version of content before trying to use these properties. | No |
| nodeHash | integer (uint32) | The hash identifier for the node, which unfortunately is also content version dependent but can be (and ideally, should be) used instead of the nodeIndex to uniquely identify the node.
The two exist side-by-side for backcompat reasons due to the Great Talent Node Restructuring of Destiny 1, and I ran out of time to remove one of them and standardize on the other. Sorry! | No |
| row | integer (int32) | The visual "row" where the node should be shown in the UI. If negative, then the node is hidden. | No |
| column | integer (int32) | The visual "column" where the node should be shown in the UI. If negative, the node is hidden. | No |
| prerequisiteNodeIndexes | Array[integer] | Indexes into the DestinyTalentGridDefinition.nodes property for any nodes that must be activated before this one is allowed to be activated.
I would have liked to change this to hashes for Destiny 2, but we have run out of time. | No |
| binaryPairNodeIndex | integer (int32) | At one point, Talent Nodes supported the idea of "Binary Pairs": nodes that overlapped each other visually, and where activating one deactivated the other. They ended up not being used, mostly because Exclusive Sets are *almost* a superset of this concept, but the potential for it to be used still exists in theory.
If this is ever used, this will be the index into the DestinyTalentGridDefinition.nodes property for the node that is the binary pair match to this node. Activating one deactivates the other. | No |
| autoUnlocks | boolean | If true, this node will automatically unlock when the Talent Grid's level reaches the required level of the current step of this node. | No |
| lastStepRepeats | boolean | At one point, Nodes were going to be able to be activated multiple times, changing the current step and potentially piling on multiple effects from the previously activated steps. This property would indicate if the last step could be activated multiple times. 
This is not currently used, but it isn't out of the question that this could end up being used again in a theoretical future. | No |
| isRandom | boolean | If this is true, the node's step is determined randomly rather than the first step being chosen. | No |
| randomActivationRequirement | object | At one point, you were going to be able to repurchase talent nodes that had random steps, to "re-roll" the current step of the node (and thus change the properties of your item). This was to be the activation requirement for performing that re-roll.
The system still exists to do this, as far as I know, so it may yet come back around! | No |
| isRandomRepurchasable | boolean | If this is true, the node can be "re-rolled" to acquire a different random current step. This is not used, but still exists for a theoretical future of talent grids. | No |
| steps | Array[Destiny.Definitions.DestinyNodeStepDefinition] | At this point, "steps" have been obfuscated into conceptual entities, aggregating the underlying notions of "properties" and "true steps".
If you need to know a step as it truly exists - such as when recreating Node logic when processing Vendor data - you'll have to use the "realSteps" property below. | No |
| exclusiveWithNodeHashes | Array[integer] | The nodeHash values for nodes that are in an Exclusive Set with this node.
See DestinyTalentGridDefinition.exclusiveSets for more info about exclusive sets.
Again, note that these are nodeHashes and *not* nodeIndexes. | No |
| randomStartProgressionBarAtProgression | integer (int32) | If the node's step is randomly selected, this is the amount of the Talent Grid's progression experience at which the progression bar for the node should be shown. | No |
| layoutIdentifier | string | A string identifier for a custom visual layout to apply to this talent node. Unfortunately, we do not have any data for rendering these custom layouts. It will be up to you to interpret these strings and change your UI if you want to have custom UI matching these layouts. | No |
| groupHash | integer (uint32) | As of Destiny 2, nodes can exist as part of "Exclusive Groups". These differ from exclusive sets in that, within the group, many nodes can be activated. But the act of activating any node in the group will cause "opposing" nodes (nodes in groups that are not allowed to be activated at the same time as this group) to deactivate.
See DestinyTalentExclusiveGroup for more information on the details. This is an identifier for this node's group, if it is part of one. | No |
| loreHash | integer (uint32) | Talent nodes can be associated with a piece of Lore, generally rendered in a tooltip. This is the hash identifier of the lore element to show, if there is one to be show. | No |
| nodeStyleIdentifier | string | Comes from the talent grid node style: this identifier should be used to determine how to render the node in the UI. | No |
| ignoreForCompletion | boolean | Comes from the talent grid node style: if true, then this node should be ignored for determining whether the grid is complete. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyTalentNodeDefinition object
const example = {
  nodeIndex: 123,
  nodeHash: 123,
  row: 123,
  column: 123,
  prerequisiteNodeIndexes: [],
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyTalentNodeDefinition object
example = {
    "nodeIndex": 123,
    "nodeHash": 123,
    "row": 123,
    "column": 123,
    "prerequisiteNodeIndexes": [],
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyNodeActivationRequirement**: Referenced in this entity
- **Destiny.Definitions.DestinyNodeStepDefinition**: Referenced in this entity
- **Destiny.Definitions.Lore.DestinyLoreDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyTalentNodeDefinition":   {
      "description": "Talent Grids on items have Nodes. These nodes have positions in the talent grid's UI, and contain \"Steps\" (DestinyTalentNodeStepDefinition), one of whom will be the \"Current\" step.\r\nThe Current Step determines the visual properties of the node, as well as what the node grants when it is activated.\r\nSee DestinyTalentGridDefinition for a more complete overview of how Talent Grids work, and how they are used in Destiny 2 (and how they were used in Destiny 1).",
      "type": "object",
      "properties": {
          "nodeIndex": {
              "format": "int32",
              "description": "The index into the DestinyTalentGridDefinition's \"nodes\" property where this node is located. Used to uniquely identify the node within the Talent Grid. Note that this is content version dependent: make sure you have the latest version of content before trying to use these properties.",
              "type": "integer"
          },
          "nodeHash": {
              "format": "uint32",
              "description": "The hash identifier for the node, which unfortunately is also content version dependent but can be (and ideally, should be) used instead of the nodeIndex to uniquely identify the node.\r\nThe two exist side-by-side for backcompat reasons due to the Great Talent Node Restructuring of Destiny 1, and I ran out of time to remove one of them and standardize on the other. Sorry!",
              "type": "integer"
          },
          "row": {
              "format": "int32",
              "description": "The visual \"row\" where the node should be shown in the UI. If negative, then the node is hidden.",
              "type": "integer"
          },
          "column": {
              "format": "int32",
              "description": "The visual \"column\" where the node should be shown in the UI. If negative, the node is hidden.",
              "type": "integer"
          },
          "prerequisiteNodeIndexes": {
              "description": "Indexes into the DestinyTalentGridDefinition.nodes property for any nodes that must be activated before this one is allowed to be activated.\r\nI would have liked to change this to hashes for Destiny 2, but we have run out of time.",
              "type": "array",
              "items": {
                  "format": "int32",
                  "type": "integer"
              }
          },
          "binaryPairNodeIndex": {
              "format": "int32",
              "description": "At one point, Talent Nodes supported the idea of \"Binary Pairs\": nodes that overlapped each other visually, and where activating one deactivated the other. They ended up not being used, mostly because Exclusive Sets are *almost* a superset of this concept, but the potential for it to be used still exists in theory.\r\nIf this is ever used, this will be the index into the DestinyTalentGridDefinition.nodes property for the node that is the binary pair match to this node. Activating one deactivates the other.",
              "type": "integer"
          },
          "autoUnlocks": {
              "description": "If true, this node will automatically unlock when the Talent Grid's level reaches the required level of the current step of this node.",
              "type": "boolean"
          },
          "lastStepRepeats": {
              "description": "At one point, Nodes were going to be able to be activated multiple times, changing the current step and potentially piling on multiple effects from the previously activated steps. This property would indicate if the last step could be activated multiple times. \r\nThis is not currently used, but it isn't out of the question that this could end up being used again in a theoretical future.",
              "type": "boolean"
          },
          "isRandom": {
              "description": "If this is true, the node's step is determined randomly rather than the first step being chosen.",
              "type": "boolean"
          },
          "randomActivationRequirement": {
              "description": "At one point, you were going to be able to repurchase talent nodes that had random steps, to \"re-roll\" the current step of the node (and thus change the properties of your item). This was to be the activation requirement for performing that re-roll.\r\nThe system still exists to do this, as far as I know, so it may yet come back around!",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.DestinyNodeActivationRequirement"
                  }
              ]
          },
          "isRandomRepurchasable": {
              "description": "If this is true, the node can be \"re-rolled\" to acquire a different random current step. This is not used, but still exists for a theoretical future of talent grids.",
              "type": "boolean"
          },
          "steps": {
              "description": "At this point, \"steps\" have been obfuscated into conceptual entities, aggregating the underlying notions of \"properties\" and \"true steps\".\r\nIf you need to know a step as it truly exists - such as when recreating Node logic when processing Vendor data - you'll have to use the \"realSteps\" property below.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyNodeStepDefinition"
              }
          },
          "exclusiveWithNodeHashes": {
              "description": "The nodeHash values for nodes that are in an Exclusive Set with this node.\r\nSee DestinyTalentGridDefinition.exclusiveSets for more info about exclusive sets.\r\nAgain, note that these are nodeHashes and *not* nodeIndexes.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              }
          },
          "randomStartProgressionBarAtProgression": {
              "format": "int32",
              "description": "If the node's step is randomly selected, this is the amount of the Talent Grid's progression experience at which the progression bar for the node should be shown.",
              "type": "integer"
          },
          "layoutIdentifier": {
              "description": "A string identifier for a custom visual layout to apply to this talent node. Unfortunately, we do not have any data for rendering these custom layouts. It will be up to you to interpret these strings and change your UI if you want to have custom UI matching these layouts.",
              "type": "string"
          },
          "groupHash": {
              "format": "uint32",
              "description": "As of Destiny 2, nodes can exist as part of \"Exclusive Groups\". These differ from exclusive sets in that, within the group, many nodes can be activated. But the act of activating any node in the group will cause \"opposing\" nodes (nodes in groups that are not allowed to be activated at the same time as this group) to deactivate.\r\nSee DestinyTalentExclusiveGroup for more information on the details. This is an identifier for this node's group, if it is part of one.",
              "type": "integer"
          },
          "loreHash": {
              "format": "uint32",
              "description": "Talent nodes can be associated with a piece of Lore, generally rendered in a tooltip. This is the hash identifier of the lore element to show, if there is one to be show.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Lore.DestinyLoreDefinition"
              }
          },
          "nodeStyleIdentifier": {
              "description": "Comes from the talent grid node style: this identifier should be used to determine how to render the node in the UI.",
              "type": "string"
          },
          "ignoreForCompletion": {
              "description": "Comes from the talent grid node style: if true, then this node should be ignored for determining whether the grid is complete.",
              "type": "boolean"
          }
      }
  }
}
```
