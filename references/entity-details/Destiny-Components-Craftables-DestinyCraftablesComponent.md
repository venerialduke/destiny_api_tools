# Destiny.Components.Craftables.DestinyCraftablesComponent

## Entity Information
- **Entity Name**: Destiny.Components.Craftables.DestinyCraftablesComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinycraftablescomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| craftables | object | A map of craftable item hashes to craftable item state components. | No |
| craftingRootNodeHash | integer (uint32) | The hash for the root presentation node definition of craftable item categories. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Craftables.DestinyCraftablesComponent object
const example = {
  craftables: null,
  craftingRootNodeHash: 123,
};
```

### Python
```python
# Example Destiny.Components.Craftables.DestinyCraftablesComponent object
example = {
    "craftables": None,
    "craftingRootNodeHash": 123,
}
```

## Related Entities
- **Destiny.Components.Craftables.DestinyCraftableComponent**: Referenced in this entity
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Craftables.DestinyCraftablesComponent":   {
      "type": "object",
      "properties": {
          "craftables": {
              "description": "A map of craftable item hashes to craftable item state components.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.Components.Craftables.DestinyCraftableComponent"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "craftingRootNodeHash": {
              "format": "uint32",
              "description": "The hash for the root presentation node definition of craftable item categories.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
              }
          }
      },
      "x-destiny-component-type-dependency": "Craftables"
  }
}
```
