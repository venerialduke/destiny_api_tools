# Destiny.Entities.Items.DestinyItemInstanceComponent

## Entity Information
- **Entity Name**: Destiny.Entities.Items.DestinyItemInstanceComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
If an item is "instanced", this will contain information about the item's instance that doesn't fit easily into other components. One might say this is the "essential" instance data for the item.
Items are instanced if they require information or state that can vary. For instance, weapons are Instanced: they are given a unique identifier, uniquely generated stats, and can have their properties altered. Non-instanced items have none of these things: for instance, Glimmer has no unique properties aside from how much of it you own.
You can tell from an item's definition whether it will be instanced or not by looking at the DestinyInventoryItemDefinition's definition.inventory.isInstanceItem property.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| damageType | integer (int32) | If the item has a damage type, this is the item's current damage type. | No |
| damageTypeHash | integer (uint32) | The current damage type's hash, so you can look up localized info and icons for it. | No |
| primaryStat | object | The item stat that we consider to be "primary" for the item. For instance, this would be "Attack" for Weapons or "Defense" for armor. | No |
| itemLevel | integer (int32) | The Item's "Level" has the most significant bearing on its stats, such as Light and Power. | No |
| quality | integer (int32) | The "Quality" of the item has a lesser - but still impactful - bearing on stats like Light and Power. | No |
| isEquipped | boolean | Is the item currently equipped on the given character? | No |
| canEquip | boolean | If this is an equippable item, you can check it here. There are permanent as well as transitory reasons why an item might not be able to be equipped: check cannotEquipReason for details. | No |
| equipRequiredLevel | integer (int32) | If the item cannot be equipped until you reach a certain level, that level will be reflected here. | No |
| unlockHashesRequiredToEquip | Array[integer] | Sometimes, there are limitations to equipping that are represented by character-level flags called "unlocks".
This is a list of flags that they need in order to equip the item that the character has not met. Use these to look up the descriptions to show in your UI by looking up the relevant DestinyUnlockDefinitions for the hashes. | No |
| cannotEquipReason | integer (int32) | If you cannot equip the item, this is a flags enum that enumerates all of the reasons why you couldn't equip the item. You may need to refine your UI further by using unlockHashesRequiredToEquip and equipRequiredLevel. | No |
| breakerType | integer (int32) | If populated, this item has a breaker type corresponding to the given value. See DestinyBreakerTypeDefinition for more details. | No |
| breakerTypeHash | integer (uint32) | If populated, this is the hash identifier for the item's breaker type. See DestinyBreakerTypeDefinition for more details. | No |
| energy | object | IF populated, this item supports Energy mechanics (i.e. Armor 2.0), and these are the current details of its energy type and available capacity to spend energy points. | No |
| gearTier | integer (int32) | Gear Tier, if applicable, fished up from the unlock value items.gear_tier | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Entities.Items.DestinyItemInstanceComponent object
const example = {
  damageType: 123,
  damageTypeHash: 123,
  primaryStat: null,
  itemLevel: 123,
  quality: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Entities.Items.DestinyItemInstanceComponent object
example = {
    "damageType": 123,
    "damageTypeHash": 123,
    "primaryStat": None,
    "itemLevel": 123,
    "quality": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.DamageType**: Referenced in this entity
- **Destiny.Definitions.BreakerTypes.DestinyBreakerTypeDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyDamageTypeDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyUnlockDefinition**: Referenced in this entity
- **Destiny.DestinyStat**: Referenced in this entity
- **Destiny.Entities.Items.DestinyItemInstanceEnergy**: Referenced in this entity
- **Destiny.EquipFailureReason**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Entities.Items.DestinyItemInstanceComponent":   {
      "description": "If an item is \"instanced\", this will contain information about the item's instance that doesn't fit easily into other components. One might say this is the \"essential\" instance data for the item.\r\nItems are instanced if they require information or state that can vary. For instance, weapons are Instanced: they are given a unique identifier, uniquely generated stats, and can have their properties altered. Non-instanced items have none of these things: for instance, Glimmer has no unique properties aside from how much of it you own.\r\nYou can tell from an item's definition whether it will be instanced or not by looking at the DestinyInventoryItemDefinition's definition.inventory.isInstanceItem property.",
      "type": "object",
      "properties": {
          "damageType": {
              "format": "int32",
              "description": "If the item has a damage type, this is the item's current damage type.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DamageType"
              }
          },
          "damageTypeHash": {
              "format": "uint32",
              "description": "The current damage type's hash, so you can look up localized info and icons for it.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyDamageTypeDefinition"
              }
          },
          "primaryStat": {
              "description": "The item stat that we consider to be \"primary\" for the item. For instance, this would be \"Attack\" for Weapons or \"Defense\" for armor.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.DestinyStat"
                  }
              ]
          },
          "itemLevel": {
              "format": "int32",
              "description": "The Item's \"Level\" has the most significant bearing on its stats, such as Light and Power.",
              "type": "integer"
          },
          "quality": {
              "format": "int32",
              "description": "The \"Quality\" of the item has a lesser - but still impactful - bearing on stats like Light and Power.",
              "type": "integer"
          },
          "isEquipped": {
              "description": "Is the item currently equipped on the given character?",
              "type": "boolean"
          },
          "canEquip": {
              "description": "If this is an equippable item, you can check it here. There are permanent as well as transitory reasons why an item might not be able to be equipped: check cannotEquipReason for details.",
              "type": "boolean"
          },
          "equipRequiredLevel": {
              "format": "int32",
              "description": "If the item cannot be equipped until you reach a certain level, that level will be reflected here.",
              "type": "integer"
          },
          "unlockHashesRequiredToEquip": {
              "description": "Sometimes, there are limitations to equipping that are represented by character-level flags called \"unlocks\".\r\nThis is a list of flags that they need in order to equip the item that the character has not met. Use these to look up the descriptions to show in your UI by looking up the relevant DestinyUnlockDefinitions for the hashes.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyUnlockDefinition"
              }
          },
          "cannotEquipReason": {
              "format": "int32",
              "description": "If you cannot equip the item, this is a flags enum that enumerates all of the reasons why you couldn't equip the item. You may need to refine your UI further by using unlockHashesRequiredToEquip and equipRequiredLevel.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.EquipFailureReason"
              }
          },
          "breakerType": {
              "format": "int32",
              "description": "If populated, this item has a breaker type corresponding to the given value. See DestinyBreakerTypeDefinition for more details.",
              "enum": [
                  "0",
                  "1",
                  "2",
                  "3"
              ],
              "type": "integer",
              "x-enum-values": [
                  {
                      "numericValue": "0",
                      "identifier": "None"
                  },
                  {
                      "numericValue": "1",
                      "identifier": "ShieldPiercing"
                  },
                  {
                      "numericValue": "2",
                      "identifier": "Disruption"
                  },
                  {
                      "numericValue": "3",
                      "identifier": "Stagger"
                  }
              ]
          },
          "breakerTypeHash": {
              "format": "uint32",
              "description": "If populated, this is the hash identifier for the item's breaker type. See DestinyBreakerTypeDefinition for more details.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.BreakerTypes.DestinyBreakerTypeDefinition"
              }
          },
          "energy": {
              "description": "IF populated, this item supports Energy mechanics (i.e. Armor 2.0), and these are the current details of its energy type and available capacity to spend energy points.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Entities.Items.DestinyItemInstanceEnergy"
                  }
              ]
          },
          "gearTier": {
              "format": "int32",
              "description": "Gear Tier, if applicable, fished up from the unlock value items.gear_tier",
              "type": "integer"
          }
      },
      "x-destiny-component-type-dependency": "ItemInstances"
  }
}
```
