# Destiny.Definitions.DestinyInventoryItemStatDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyInventoryItemStatDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Defines a specific stat value on an item, and the minimum/maximum range that we could compute for the item based on our heuristics for how the item might be generated.
Not guaranteed to match real-world instances of the item, but should hopefully at least be close. If it's not close, let us know on the Bungie API forums.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| statHash | integer (uint32) | The hash for the DestinyStatDefinition representing this stat. | No |
| value | integer (int32) | This value represents the stat value assuming the minimum possible roll but accounting for any mandatory bonuses that should be applied to the stat on item creation.
In Destiny 1, this was different from the "minimum" value because there were certain conditions where an item could be theoretically lower level/value than the initial roll. 
In Destiny 2, this is not possible unless Talent Grids begin to be used again for these purposes or some other system change occurs... thus in practice, value and minimum should be the same in Destiny 2. Good riddance. | No |
| minimum | integer (int32) | The minimum possible value for this stat that we think the item can roll. | No |
| maximum | integer (int32) | The maximum possible value for this stat that we think the item can roll.
WARNING: In Destiny 1, this field was calculated using the potential stat rolls on the item's talent grid. In Destiny 2, items no longer have meaningful talent grids and instead have sockets: but the calculation of this field was never altered to adapt to this change. As such, this field should be considered deprecated until we can address this oversight. | No |
| displayMaximum | integer (int32) | The maximum possible value for the stat as shown in the UI, if it is being shown somewhere that reveals maximum in the UI (such as a bar chart-style view).
This is pulled directly from the item's DestinyStatGroupDefinition, and placed here for convenience.
If not returned, there is no maximum to use (and thus the stat should not be shown in a way that assumes there is a limit to the stat) | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyInventoryItemStatDefinition object
const example = {
  statHash: 123,
  value: 123,
  minimum: 123,
  maximum: 123,
  displayMaximum: 123,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyInventoryItemStatDefinition object
example = {
    "statHash": 123,
    "value": 123,
    "minimum": 123,
    "maximum": 123,
    "displayMaximum": 123,
}
```

## Related Entities
- **Destiny.Definitions.DestinyStatDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyInventoryItemStatDefinition":   {
      "description": "Defines a specific stat value on an item, and the minimum/maximum range that we could compute for the item based on our heuristics for how the item might be generated.\r\nNot guaranteed to match real-world instances of the item, but should hopefully at least be close. If it's not close, let us know on the Bungie API forums.",
      "type": "object",
      "properties": {
          "statHash": {
              "format": "uint32",
              "description": "The hash for the DestinyStatDefinition representing this stat.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyStatDefinition"
              }
          },
          "value": {
              "format": "int32",
              "description": "This value represents the stat value assuming the minimum possible roll but accounting for any mandatory bonuses that should be applied to the stat on item creation.\r\nIn Destiny 1, this was different from the \"minimum\" value because there were certain conditions where an item could be theoretically lower level/value than the initial roll. \r\nIn Destiny 2, this is not possible unless Talent Grids begin to be used again for these purposes or some other system change occurs... thus in practice, value and minimum should be the same in Destiny 2. Good riddance.",
              "type": "integer"
          },
          "minimum": {
              "format": "int32",
              "description": "The minimum possible value for this stat that we think the item can roll.",
              "type": "integer"
          },
          "maximum": {
              "format": "int32",
              "description": "The maximum possible value for this stat that we think the item can roll.\r\nWARNING: In Destiny 1, this field was calculated using the potential stat rolls on the item's talent grid. In Destiny 2, items no longer have meaningful talent grids and instead have sockets: but the calculation of this field was never altered to adapt to this change. As such, this field should be considered deprecated until we can address this oversight.",
              "type": "integer"
          },
          "displayMaximum": {
              "format": "int32",
              "description": "The maximum possible value for the stat as shown in the UI, if it is being shown somewhere that reveals maximum in the UI (such as a bar chart-style view).\r\nThis is pulled directly from the item's DestinyStatGroupDefinition, and placed here for convenience.\r\nIf not returned, there is no maximum to use (and thus the stat should not be shown in a way that assumes there is a limit to the stat)",
              "type": "integer"
          }
      }
  }
}
```
