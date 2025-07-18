# Destiny.Definitions.DestinyItemInventoryBlockDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemInventoryBlockDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
If the item can exist in an inventory - the overwhelming majority of them can and do - then this is the basic properties regarding the item's relationship with the inventory.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| stackUniqueLabel | string | If this string is populated, you can't have more than one stack with this label in a given inventory. Note that this is different from the equipping block's unique label, which is used for equipping uniqueness. | No |
| maxStackSize | integer (int32) | The maximum quantity of this item that can exist in a stack. | No |
| bucketTypeHash | integer (uint32) | The hash identifier for the DestinyInventoryBucketDefinition to which this item belongs. I should have named this "bucketHash", but too many things refer to it now. Sigh. | No |
| recoveryBucketTypeHash | integer (uint32) | If the item is picked up by the lost loot queue, this is the hash identifier for the DestinyInventoryBucketDefinition into which it will be placed. Again, I should have named this recoveryBucketHash instead. | No |
| tierTypeHash | integer (uint32) | The hash identifier for the Tier Type of the item, use to look up its DestinyItemTierTypeDefinition if you need to show localized data for the item's tier. | No |
| isInstanceItem | boolean | If TRUE, this item is instanced. Otherwise, it is a generic item that merely has a quantity in a stack (like Glimmer). | No |
| tierTypeName | string | The localized name of the tier type, which is a useful shortcut so you don't have to look up the definition every time. However, it's mostly a holdover from days before we had a DestinyItemTierTypeDefinition to refer to. | No |
| tierType | integer (int32) | The enumeration matching the tier type of the item to known values, again for convenience sake. | No |
| expirationTooltip | string | The tooltip message to show, if any, when the item expires. | No |
| expiredInActivityMessage | string | If the item expires while playing in an activity, we show a different message. | No |
| expiredInOrbitMessage | string | If the item expires in orbit, we show a... more different message. ("Consummate V's, consummate!") | No |
| suppressExpirationWhenObjectivesComplete | boolean |  | No |
| recipeItemHash | integer (uint32) | A reference to the associated crafting 'recipe' item definition, if this item can be crafted. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemInventoryBlockDefinition object
const example = {
  stackUniqueLabel: "example value",
  maxStackSize: 123,
  bucketTypeHash: 123,
  recoveryBucketTypeHash: 123,
  tierTypeHash: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemInventoryBlockDefinition object
example = {
    "stackUniqueLabel": "example value",
    "maxStackSize": 123,
    "bucketTypeHash": 123,
    "recoveryBucketTypeHash": 123,
    "tierTypeHash": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryBucketDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.Items.DestinyItemTierTypeDefinition**: Referenced in this entity
- **Destiny.TierType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyItemInventoryBlockDefinition":   {
      "description": "If the item can exist in an inventory - the overwhelming majority of them can and do - then this is the basic properties regarding the item's relationship with the inventory.",
      "type": "object",
      "properties": {
          "stackUniqueLabel": {
              "description": "If this string is populated, you can't have more than one stack with this label in a given inventory. Note that this is different from the equipping block's unique label, which is used for equipping uniqueness.",
              "type": "string"
          },
          "maxStackSize": {
              "format": "int32",
              "description": "The maximum quantity of this item that can exist in a stack.",
              "type": "integer"
          },
          "bucketTypeHash": {
              "format": "uint32",
              "description": "The hash identifier for the DestinyInventoryBucketDefinition to which this item belongs. I should have named this \"bucketHash\", but too many things refer to it now. Sigh.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryBucketDefinition"
              }
          },
          "recoveryBucketTypeHash": {
              "format": "uint32",
              "description": "If the item is picked up by the lost loot queue, this is the hash identifier for the DestinyInventoryBucketDefinition into which it will be placed. Again, I should have named this recoveryBucketHash instead.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryBucketDefinition"
              }
          },
          "tierTypeHash": {
              "format": "uint32",
              "description": "The hash identifier for the Tier Type of the item, use to look up its DestinyItemTierTypeDefinition if you need to show localized data for the item's tier.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Items.DestinyItemTierTypeDefinition"
              }
          },
          "isInstanceItem": {
              "description": "If TRUE, this item is instanced. Otherwise, it is a generic item that merely has a quantity in a stack (like Glimmer).",
              "type": "boolean"
          },
          "tierTypeName": {
              "description": "The localized name of the tier type, which is a useful shortcut so you don't have to look up the definition every time. However, it's mostly a holdover from days before we had a DestinyItemTierTypeDefinition to refer to.",
              "type": "string"
          },
          "tierType": {
              "format": "int32",
              "description": "The enumeration matching the tier type of the item to known values, again for convenience sake.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.TierType"
              }
          },
          "expirationTooltip": {
              "description": "The tooltip message to show, if any, when the item expires.",
              "type": "string"
          },
          "expiredInActivityMessage": {
              "description": "If the item expires while playing in an activity, we show a different message.",
              "type": "string"
          },
          "expiredInOrbitMessage": {
              "description": "If the item expires in orbit, we show a... more different message. (\"Consummate V's, consummate!\")",
              "type": "string"
          },
          "suppressExpirationWhenObjectivesComplete": {
              "type": "boolean"
          },
          "recipeItemHash": {
              "format": "uint32",
              "description": "A reference to the associated crafting 'recipe' item definition, if this item can be crafted.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          }
      }
  }
}
```
