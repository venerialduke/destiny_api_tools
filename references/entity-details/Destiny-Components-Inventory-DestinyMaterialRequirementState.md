# Destiny.Components.Inventory.DestinyMaterialRequirementState

## Entity Information
- **Entity Name**: Destiny.Components.Inventory.DestinyMaterialRequirementState
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinymaterialrequirementstate data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| itemHash | integer (uint32) | The hash identifier of the material required. Use it to look up the material's DestinyInventoryItemDefinition. | No |
| count | integer (int32) | The amount of the material required. | No |
| stackSize | integer (int32) | A value for the amount of a (possibly virtual) material on some scope. For example: Dawning cookie baking material requirements. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Inventory.DestinyMaterialRequirementState object
const example = {
  itemHash: 123,
  count: 123,
  stackSize: 123,
};
```

### Python
```python
# Example Destiny.Components.Inventory.DestinyMaterialRequirementState object
example = {
    "itemHash": 123,
    "count": 123,
    "stackSize": 123,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Inventory.DestinyMaterialRequirementState":   {
      "type": "object",
      "properties": {
          "itemHash": {
              "format": "uint32",
              "description": "The hash identifier of the material required. Use it to look up the material's DestinyInventoryItemDefinition.",
              "type": "integer"
          },
          "count": {
              "format": "int32",
              "description": "The amount of the material required.",
              "type": "integer"
          },
          "stackSize": {
              "format": "int32",
              "description": "A value for the amount of a (possibly virtual) material on some scope. For example: Dawning cookie baking material requirements.",
              "type": "integer"
          }
      }
  }
}
```
