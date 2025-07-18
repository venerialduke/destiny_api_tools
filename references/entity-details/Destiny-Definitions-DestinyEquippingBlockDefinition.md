# Destiny.Definitions.DestinyEquippingBlockDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyEquippingBlockDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Items that can be equipped define this block. It contains information we need to understand how and when the item can be equipped.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| gearsetItemHash | integer (uint32) | If the item is part of a gearset, this is a reference to that gearset item. | No |
| uniqueLabel | string | If defined, this is the label used to check if the item has other items of matching types already equipped. 
For instance, when you aren't allowed to equip more than one Exotic Weapon, that's because all exotic weapons have identical uniqueLabels and the game checks the to-be-equipped item's uniqueLabel vs. all other already equipped items (other than the item in the slot that's about to be occupied). | No |
| uniqueLabelHash | integer (uint32) | The hash of that unique label. Does not point to a specific definition. | No |
| equipmentSlotTypeHash | integer (uint32) | An equipped item *must* be equipped in an Equipment Slot. This is the hash identifier of the DestinyEquipmentSlotDefinition into which it must be equipped. | No |
| attributes | integer (int32) | These are custom attributes on the equippability of the item.
For now, this can only be "equip on acquire", which would mean that the item will be automatically equipped as soon as you pick it up. | No |
| ammoType | integer (int32) | Ammo type used by a weapon is no longer determined by the bucket in which it is contained. If the item has an ammo type - i.e. if it is a weapon - this will be the type of ammunition expected. | No |
| displayStrings | Array[string] | These are strings that represent the possible Game/Account/Character state failure conditions that can occur when trying to equip the item. They match up one-to-one with requiredUnlockExpressions. | No |
| equipableItemSetHash | integer (uint32) | If this item is part of an item set with bonus perks, this will the hash of that set. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyEquippingBlockDefinition object
const example = {
  gearsetItemHash: 123,
  uniqueLabel: "example value",
  uniqueLabelHash: 123,
  equipmentSlotTypeHash: 123,
  attributes: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyEquippingBlockDefinition object
example = {
    "gearsetItemHash": 123,
    "uniqueLabel": "example value",
    "uniqueLabelHash": 123,
    "equipmentSlotTypeHash": 123,
    "attributes": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyEquipmentSlotDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.Items.DestinyEquipableItemSetDefinition**: Referenced in this entity
- **Destiny.DestinyAmmunitionType**: Referenced in this entity
- **Destiny.EquippingItemBlockAttributes**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyEquippingBlockDefinition":   {
      "description": "Items that can be equipped define this block. It contains information we need to understand how and when the item can be equipped.",
      "type": "object",
      "properties": {
          "gearsetItemHash": {
              "format": "uint32",
              "description": "If the item is part of a gearset, this is a reference to that gearset item.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "uniqueLabel": {
              "description": "If defined, this is the label used to check if the item has other items of matching types already equipped. \r\nFor instance, when you aren't allowed to equip more than one Exotic Weapon, that's because all exotic weapons have identical uniqueLabels and the game checks the to-be-equipped item's uniqueLabel vs. all other already equipped items (other than the item in the slot that's about to be occupied).",
              "type": "string"
          },
          "uniqueLabelHash": {
              "format": "uint32",
              "description": "The hash of that unique label. Does not point to a specific definition.",
              "type": "integer"
          },
          "equipmentSlotTypeHash": {
              "format": "uint32",
              "description": "An equipped item *must* be equipped in an Equipment Slot. This is the hash identifier of the DestinyEquipmentSlotDefinition into which it must be equipped.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyEquipmentSlotDefinition"
              }
          },
          "attributes": {
              "format": "int32",
              "description": "These are custom attributes on the equippability of the item.\r\nFor now, this can only be \"equip on acquire\", which would mean that the item will be automatically equipped as soon as you pick it up.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.EquippingItemBlockAttributes"
              }
          },
          "ammoType": {
              "format": "int32",
              "description": "Ammo type used by a weapon is no longer determined by the bucket in which it is contained. If the item has an ammo type - i.e. if it is a weapon - this will be the type of ammunition expected.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyAmmunitionType"
              }
          },
          "displayStrings": {
              "description": "These are strings that represent the possible Game/Account/Character state failure conditions that can occur when trying to equip the item. They match up one-to-one with requiredUnlockExpressions.",
              "type": "array",
              "items": {
                  "type": "string"
              }
          },
          "equipableItemSetHash": {
              "format": "uint32",
              "description": "If this item is part of an item set with bonus perks, this will the hash of that set.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Items.DestinyEquipableItemSetDefinition"
              }
          }
      }
  }
}
```
