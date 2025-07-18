# Destiny.Components.Inventory.DestinyMaterialRequirementSetState

## Entity Information
- **Entity Name**: Destiny.Components.Inventory.DestinyMaterialRequirementSetState
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinymaterialrequirementsetstate data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| materialRequirementSetHash | integer (uint32) | The hash identifier of the material requirement set. Use it to look up the DestinyMaterialRequirementSetDefinition. | No |
| materialRequirementStates | Array[Destiny.Components.Inventory.DestinyMaterialRequirementState] | The dynamic state values for individual material requirements. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Inventory.DestinyMaterialRequirementSetState object
const example = {
  materialRequirementSetHash: 123,
  materialRequirementStates: [],
};
```

### Python
```python
# Example Destiny.Components.Inventory.DestinyMaterialRequirementSetState object
example = {
    "materialRequirementSetHash": 123,
    "materialRequirementStates": [],
}
```

## Related Entities
- **Destiny.Components.Inventory.DestinyMaterialRequirementState**: Referenced in this entity
- **Destiny.Definitions.DestinyMaterialRequirementSetDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Inventory.DestinyMaterialRequirementSetState":   {
      "type": "object",
      "properties": {
          "materialRequirementSetHash": {
              "format": "uint32",
              "description": "The hash identifier of the material requirement set. Use it to look up the DestinyMaterialRequirementSetDefinition.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyMaterialRequirementSetDefinition"
              }
          },
          "materialRequirementStates": {
              "description": "The dynamic state values for individual material requirements.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Components.Inventory.DestinyMaterialRequirementState"
              }
          }
      }
  }
}
```
