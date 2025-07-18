# Destiny.Definitions.DestinyItemGearsetBlockDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemGearsetBlockDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
If an item has a related gearset, this is the list of items in that set, and an unlock expression that evaluates to a number representing the progress toward gearset completion (a very rare use for unlock expressions!)

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| trackingValueMax | integer (int32) | The maximum possible number of items that can be collected. | No |
| itemList | Array[integer] | The list of hashes for items in the gearset. Use them to look up DestinyInventoryItemDefinition entries for the items in the set. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemGearsetBlockDefinition object
const example = {
  trackingValueMax: 123,
  itemList: [],
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemGearsetBlockDefinition object
example = {
    "trackingValueMax": 123,
    "itemList": [],
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
  "Destiny.Definitions.DestinyItemGearsetBlockDefinition":   {
      "description": "If an item has a related gearset, this is the list of items in that set, and an unlock expression that evaluates to a number representing the progress toward gearset completion (a very rare use for unlock expressions!)",
      "type": "object",
      "properties": {
          "trackingValueMax": {
              "format": "int32",
              "description": "The maximum possible number of items that can be collected.",
              "type": "integer"
          },
          "itemList": {
              "description": "The list of hashes for items in the gearset. Use them to look up DestinyInventoryItemDefinition entries for the items in the set.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          }
      }
  }
}
```
