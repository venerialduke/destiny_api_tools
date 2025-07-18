# Destiny.Definitions.DestinyActivityLoadoutRequirement

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyActivityLoadoutRequirement
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyactivityloadoutrequirement data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| equipmentSlotHash | integer (uint32) |  | No |
| allowedEquippedItemHashes | Array[integer] |  | No |
| allowedWeaponSubTypes | Array[integer] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyActivityLoadoutRequirement object
const example = {
  equipmentSlotHash: 123,
  allowedEquippedItemHashes: [],
  allowedWeaponSubTypes: [],
};
```

### Python
```python
# Example Destiny.Definitions.DestinyActivityLoadoutRequirement object
example = {
    "equipmentSlotHash": 123,
    "allowedEquippedItemHashes": [],
    "allowedWeaponSubTypes": [],
}
```

## Related Entities
- **Destiny.Definitions.DestinyEquipmentSlotDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.DestinyItemSubType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyActivityLoadoutRequirement":   {
      "type": "object",
      "properties": {
          "equipmentSlotHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyEquipmentSlotDefinition"
              }
          },
          "allowedEquippedItemHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "allowedWeaponSubTypes": {
              "type": "array",
              "items": {
                  "format": "int32",
                  "description": "This Enumeration further classifies items by more specific categorizations than DestinyItemType. The \"Sub-Type\" is where we classify and categorize items one step further in specificity: \"Auto Rifle\" instead of just \"Weapon\" for example, or \"Vanguard Bounty\" instead of merely \"Bounty\".\r\nThese sub-types are provided for historical compatibility with Destiny 1, but an ideal alternative is to use DestinyItemCategoryDefinitions and the DestinyItemDefinition.itemCategories property instead. Item Categories allow for arbitrary hierarchies of specificity, and for items to belong to multiple categories across multiple hierarchies simultaneously. For this enum, we pick a single type as a \"best guess\" fit.\r\nNOTE: This is not all of the item types available, and some of these are holdovers from Destiny 1 that may or may not still exist.",
                  "type": "integer",
                  "x-enum-reference": {
                      "$ref": "#/components/schemas/Destiny.DestinyItemSubType"
                  }
              }
          }
      }
  }
}
```
