# Destiny.Entities.Items.DestinyItemTalentGridComponent

## Entity Information
- **Entity Name**: Destiny.Entities.Items.DestinyItemTalentGridComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Well, we're here in Destiny 2, and Talent Grids are unfortunately still around.
The good news is that they're pretty much only being used for certain base information on items and for Builds/Subclasses. The bad news is that they still suck. If you really want this information, grab this component.
An important note is that talent grids are defined as such:
A Grid has 1:M Nodes, which has 1:M Steps.
Any given node can only have a single step active at one time, which represents the actual visual contents and effects of the Node (for instance, if you see a "Super Cool Bonus" node, the actual icon and text for the node is coming from the current Step of that node).
Nodes can be grouped into exclusivity sets *and* as of D2, exclusivity groups (which are collections of exclusivity sets that affect each other).
See DestinyTalentGridDefinition for more information. Brace yourself, the water's cold out there in the deep end.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| talentGridHash | integer (uint32) | Most items don't have useful talent grids anymore, but Builds in particular still do.
You can use this hash to lookup the DestinyTalentGridDefinition attached to this item, which will be crucial for understanding the node values on the item. | No |
| nodes | Array[Destiny.DestinyTalentNode] | Detailed information about the individual nodes in the talent grid.
A node represents a single visual "pip" in the talent grid or Build detail view, though each node may have multiple "steps" which indicate the actual bonuses and visual representation of that node. | No |
| isGridComplete | boolean | Indicates whether the talent grid on this item is completed, and thus whether it should have a gold border around it.
Only will be true if the item actually *has* a talent grid, and only then if it is completed (i.e. every exclusive set has an activated node, and every non-exclusive set node has been activated) | No |
| gridProgression | object | If the item has a progression, it will be detailed here. A progression means that the item can gain experience. Thresholds of experience are what determines whether and when a talent node can be activated. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Entities.Items.DestinyItemTalentGridComponent object
const example = {
  talentGridHash: 123,
  nodes: [],
  isGridComplete: true,
  gridProgression: null,
};
```

### Python
```python
# Example Destiny.Entities.Items.DestinyItemTalentGridComponent object
example = {
    "talentGridHash": 123,
    "nodes": [],
    "isGridComplete": True,
    "gridProgression": None,
}
```

## Related Entities
- **Destiny.Definitions.DestinyTalentGridDefinition**: Referenced in this entity
- **Destiny.DestinyProgression**: Referenced in this entity
- **Destiny.DestinyTalentNode**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Entities.Items.DestinyItemTalentGridComponent":   {
      "description": "Well, we're here in Destiny 2, and Talent Grids are unfortunately still around.\r\nThe good news is that they're pretty much only being used for certain base information on items and for Builds/Subclasses. The bad news is that they still suck. If you really want this information, grab this component.\r\nAn important note is that talent grids are defined as such:\r\nA Grid has 1:M Nodes, which has 1:M Steps.\r\nAny given node can only have a single step active at one time, which represents the actual visual contents and effects of the Node (for instance, if you see a \"Super Cool Bonus\" node, the actual icon and text for the node is coming from the current Step of that node).\r\nNodes can be grouped into exclusivity sets *and* as of D2, exclusivity groups (which are collections of exclusivity sets that affect each other).\r\nSee DestinyTalentGridDefinition for more information. Brace yourself, the water's cold out there in the deep end.",
      "type": "object",
      "properties": {
          "talentGridHash": {
              "format": "uint32",
              "description": "Most items don't have useful talent grids anymore, but Builds in particular still do.\r\nYou can use this hash to lookup the DestinyTalentGridDefinition attached to this item, which will be crucial for understanding the node values on the item.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyTalentGridDefinition"
              }
          },
          "nodes": {
              "description": "Detailed information about the individual nodes in the talent grid.\r\nA node represents a single visual \"pip\" in the talent grid or Build detail view, though each node may have multiple \"steps\" which indicate the actual bonuses and visual representation of that node.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.DestinyTalentNode"
              }
          },
          "isGridComplete": {
              "description": "Indicates whether the talent grid on this item is completed, and thus whether it should have a gold border around it.\r\nOnly will be true if the item actually *has* a talent grid, and only then if it is completed (i.e. every exclusive set has an activated node, and every non-exclusive set node has been activated)",
              "type": "boolean"
          },
          "gridProgression": {
              "description": "If the item has a progression, it will be detailed here. A progression means that the item can gain experience. Thresholds of experience are what determines whether and when a talent node can be activated.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.DestinyProgression"
                  }
              ]
          }
      },
      "x-destiny-component-type-dependency": "ItemTalentGrids"
  }
}
```
