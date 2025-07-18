# Destiny.Definitions.DestinyItemCraftingBlockDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemCraftingBlockDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
If an item can have an action performed on it (like "Dismantle"), it will be defined here if you care.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| outputItemHash | integer (uint32) | A reference to the item definition that is created when crafting with this 'recipe' item. | No |
| requiredSocketTypeHashes | Array[integer] | A list of socket type hashes that describes which sockets are required for crafting with this recipe. | No |
| failedRequirementStrings | Array[string] |  | No |
| baseMaterialRequirements | integer (uint32) | A reference to the base material requirements for crafting with this recipe. | No |
| bonusPlugs | Array[Destiny.Definitions.DestinyItemCraftingBlockBonusPlugDefinition] | A list of 'bonus' socket plugs that may be available if certain requirements are met. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemCraftingBlockDefinition object
const example = {
  outputItemHash: 123,
  requiredSocketTypeHashes: [],
  failedRequirementStrings: [],
  baseMaterialRequirements: 123,
  bonusPlugs: [],
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemCraftingBlockDefinition object
example = {
    "outputItemHash": 123,
    "requiredSocketTypeHashes": [],
    "failedRequirementStrings": [],
    "baseMaterialRequirements": 123,
    "bonusPlugs": [],
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyItemCraftingBlockBonusPlugDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyMaterialRequirementSetDefinition**: Referenced in this entity
- **Destiny.Definitions.Sockets.DestinySocketTypeDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyItemCraftingBlockDefinition":   {
      "description": "If an item can have an action performed on it (like \"Dismantle\"), it will be defined here if you care.",
      "type": "object",
      "properties": {
          "outputItemHash": {
              "format": "uint32",
              "description": "A reference to the item definition that is created when crafting with this 'recipe' item.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "requiredSocketTypeHashes": {
              "description": "A list of socket type hashes that describes which sockets are required for crafting with this recipe.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Sockets.DestinySocketTypeDefinition"
              }
          },
          "failedRequirementStrings": {
              "type": "array",
              "items": {
                  "type": "string"
              }
          },
          "baseMaterialRequirements": {
              "format": "uint32",
              "description": "A reference to the base material requirements for crafting with this recipe.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyMaterialRequirementSetDefinition"
              }
          },
          "bonusPlugs": {
              "description": "A list of 'bonus' socket plugs that may be available if certain requirements are met.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyItemCraftingBlockBonusPlugDefinition"
              }
          }
      }
  }
}
```
