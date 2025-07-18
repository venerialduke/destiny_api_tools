# Destiny.Definitions.DestinyPlugItemCraftingRequirements

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyPlugItemCraftingRequirements
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyplugitemcraftingrequirements data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| unlockRequirements | Array[Destiny.Definitions.DestinyPlugItemCraftingUnlockRequirement] |  | No |
| requiredLevel | integer (int32) | If the plug has a known level requirement, it'll be available here. | No |
| materialRequirementHashes | Array[integer] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyPlugItemCraftingRequirements object
const example = {
  unlockRequirements: [],
  requiredLevel: 123,
  materialRequirementHashes: [],
};
```

### Python
```python
# Example Destiny.Definitions.DestinyPlugItemCraftingRequirements object
example = {
    "unlockRequirements": [],
    "requiredLevel": 123,
    "materialRequirementHashes": [],
}
```

## Related Entities
- **Destiny.Definitions.DestinyMaterialRequirementSetDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyPlugItemCraftingUnlockRequirement**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyPlugItemCraftingRequirements":   {
      "type": "object",
      "properties": {
          "unlockRequirements": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyPlugItemCraftingUnlockRequirement"
              }
          },
          "requiredLevel": {
              "format": "int32",
              "description": "If the plug has a known level requirement, it'll be available here.",
              "type": "integer"
          },
          "materialRequirementHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyMaterialRequirementSetDefinition"
              }
          }
      }
  }
}
```
