# Destiny.Definitions.DestinyMaterialRequirement

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyMaterialRequirement
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Many actions relating to items require you to expend materials: - Activating a talent node - Inserting a plug into a socket The items will refer to material requirements by a materialRequirementsHash in these cases, and this is the definition for those requirements in terms of the item required, how much of it is required and other interesting info. This is one of the rare/strange times where a single contract class is used both in definitions *and* in live data response contracts. I'm not sure yet whether I regret that.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| itemHash | integer (uint32) | The hash identifier of the material required. Use it to look up the material's DestinyInventoryItemDefinition. | No |
| deleteOnAction | boolean | If True, the material will be removed from the character's inventory when the action is performed. | No |
| count | integer (int32) | The amount of the material required. | No |
| countIsConstant | boolean | If true, the material requirement count value is constant. Since The Witch Queen expansion, some material requirement counts can be dynamic and will need to be returned with an API call. | No |
| omitFromRequirements | boolean | If True, this requirement is "silent": don't bother showing it in a material requirements display. I mean, I'm not your mom: I'm not going to tell you you *can't* show it. But we won't show it in our UI. | No |
| hasVirtualStackSize | boolean | If true, this material requirement references a virtual item stack size value. You can get that value from a corresponding DestinyMaterialRequirementSetState. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyMaterialRequirement object
const example = {
  itemHash: 123,
  deleteOnAction: true,
  count: 123,
  countIsConstant: true,
  omitFromRequirements: true,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyMaterialRequirement object
example = {
    "itemHash": 123,
    "deleteOnAction": True,
    "count": 123,
    "countIsConstant": True,
    "omitFromRequirements": True,
    # ... more properties
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
  "Destiny.Definitions.DestinyMaterialRequirement":   {
      "description": "Many actions relating to items require you to expend materials: - Activating a talent node - Inserting a plug into a socket The items will refer to material requirements by a materialRequirementsHash in these cases, and this is the definition for those requirements in terms of the item required, how much of it is required and other interesting info. This is one of the rare/strange times where a single contract class is used both in definitions *and* in live data response contracts. I'm not sure yet whether I regret that.",
      "type": "object",
      "properties": {
          "itemHash": {
              "format": "uint32",
              "description": "The hash identifier of the material required. Use it to look up the material's DestinyInventoryItemDefinition.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "deleteOnAction": {
              "description": "If True, the material will be removed from the character's inventory when the action is performed.",
              "type": "boolean"
          },
          "count": {
              "format": "int32",
              "description": "The amount of the material required.",
              "type": "integer"
          },
          "countIsConstant": {
              "description": "If true, the material requirement count value is constant. Since The Witch Queen expansion, some material requirement counts can be dynamic and will need to be returned with an API call.",
              "type": "boolean"
          },
          "omitFromRequirements": {
              "description": "If True, this requirement is \"silent\": don't bother showing it in a material requirements display. I mean, I'm not your mom: I'm not going to tell you you *can't* show it. But we won't show it in our UI.",
              "type": "boolean"
          },
          "hasVirtualStackSize": {
              "description": "If true, this material requirement references a virtual item stack size value. You can get that value from a corresponding DestinyMaterialRequirementSetState.",
              "type": "boolean"
          }
      }
  }
}
```
