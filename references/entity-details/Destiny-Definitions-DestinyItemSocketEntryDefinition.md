# Destiny.Definitions.DestinyItemSocketEntryDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemSocketEntryDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The definition information for a specific socket on an item. This will determine how the socket behaves in-game.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| socketTypeHash | integer (uint32) | All sockets have a type, and this is the hash identifier for this particular type. Use it to look up the DestinySocketTypeDefinition: read there for more information on how socket types affect the behavior of the socket. | No |
| singleInitialItemHash | integer (uint32) | If a valid hash, this is the hash identifier for the DestinyInventoryItemDefinition representing the Plug that will be initially inserted into the item on item creation. Otherwise, this Socket will either start without a plug inserted, or will have one randomly inserted. | No |
| reusablePlugItems | Array[Destiny.Definitions.DestinyItemSocketEntryPlugItemDefinition] | This is a list of pre-determined plugs that can *always* be plugged into this socket, without the character having the plug in their inventory.
If this list is populated, you will not be allowed to plug an arbitrary item in the socket: you will only be able to choose from one of these reusable plugs. | No |
| preventInitializationOnVendorPurchase | boolean | If this is true, then the socket will not be initialized with a plug if the item is purchased from a Vendor.
Remember that Vendors are much more than conceptual vendors: they include "Collection Kiosks" and other entities. See DestinyVendorDefinition for more information. | No |
| hidePerksInItemTooltip | boolean | If this is true, the perks provided by this socket shouldn't be shown in the item's tooltip. This might be useful if it's providing a hidden bonus, or if the bonus is less important than other benefits on the item. | No |
| plugSources | integer (int32) | Indicates where you should go to get plugs for this socket. This will affect how you populate your UI, as well as what plugs are valid for this socket. It's an alternative to having to check for the existence of certain properties (reusablePlugItems for example) to infer where plugs should come from. | No |
| reusablePlugSetHash | integer (uint32) | If this socket's plugs come from a reusable DestinyPlugSetDefinition, this is the identifier for that set. We added this concept to reduce some major duplication that's going to come from sockets as replacements for what was once implemented as large sets of items and kiosks (like Emotes).
 As of Shadowkeep, these will come up much more frequently and be driven by game content rather than custom curation. | No |
| randomizedPlugSetHash | integer (uint32) | This field replaces "randomizedPlugItems" as of Shadowkeep launch. If a socket has randomized plugs, this is a pointer to the set of plugs that could be used, as defined in DestinyPlugSetDefinition.
 If null, the item has no randomized plugs. | No |
| defaultVisible | boolean | If true, then this socket is visible in the item's "default" state. If you have an instance, you should always check the runtime state, as that can override this visibility setting: but if you're looking at the item on a conceptual level, this property can be useful for hiding data such as legacy sockets - which remain defined on items for infrastructure purposes, but can be confusing for users to see. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemSocketEntryDefinition object
const example = {
  socketTypeHash: 123,
  singleInitialItemHash: 123,
  reusablePlugItems: [],
  preventInitializationOnVendorPurchase: true,
  hidePerksInItemTooltip: true,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemSocketEntryDefinition object
example = {
    "socketTypeHash": 123,
    "singleInitialItemHash": 123,
    "reusablePlugItems": [],
    "preventInitializationOnVendorPurchase": True,
    "hidePerksInItemTooltip": True,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyItemSocketEntryPlugItemDefinition**: Referenced in this entity
- **Destiny.Definitions.Sockets.DestinyPlugSetDefinition**: Referenced in this entity
- **Destiny.Definitions.Sockets.DestinySocketTypeDefinition**: Referenced in this entity
- **Destiny.SocketPlugSources**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyItemSocketEntryDefinition":   {
      "description": "The definition information for a specific socket on an item. This will determine how the socket behaves in-game.",
      "type": "object",
      "properties": {
          "socketTypeHash": {
              "format": "uint32",
              "description": "All sockets have a type, and this is the hash identifier for this particular type. Use it to look up the DestinySocketTypeDefinition: read there for more information on how socket types affect the behavior of the socket.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Sockets.DestinySocketTypeDefinition"
              }
          },
          "singleInitialItemHash": {
              "format": "uint32",
              "description": "If a valid hash, this is the hash identifier for the DestinyInventoryItemDefinition representing the Plug that will be initially inserted into the item on item creation. Otherwise, this Socket will either start without a plug inserted, or will have one randomly inserted.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "reusablePlugItems": {
              "description": "This is a list of pre-determined plugs that can *always* be plugged into this socket, without the character having the plug in their inventory.\r\nIf this list is populated, you will not be allowed to plug an arbitrary item in the socket: you will only be able to choose from one of these reusable plugs.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyItemSocketEntryPlugItemDefinition"
              }
          },
          "preventInitializationOnVendorPurchase": {
              "description": "If this is true, then the socket will not be initialized with a plug if the item is purchased from a Vendor.\r\nRemember that Vendors are much more than conceptual vendors: they include \"Collection Kiosks\" and other entities. See DestinyVendorDefinition for more information.",
              "type": "boolean"
          },
          "hidePerksInItemTooltip": {
              "description": "If this is true, the perks provided by this socket shouldn't be shown in the item's tooltip. This might be useful if it's providing a hidden bonus, or if the bonus is less important than other benefits on the item.",
              "type": "boolean"
          },
          "plugSources": {
              "format": "int32",
              "description": "Indicates where you should go to get plugs for this socket. This will affect how you populate your UI, as well as what plugs are valid for this socket. It's an alternative to having to check for the existence of certain properties (reusablePlugItems for example) to infer where plugs should come from.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.SocketPlugSources"
              }
          },
          "reusablePlugSetHash": {
              "format": "uint32",
              "description": "If this socket's plugs come from a reusable DestinyPlugSetDefinition, this is the identifier for that set. We added this concept to reduce some major duplication that's going to come from sockets as replacements for what was once implemented as large sets of items and kiosks (like Emotes).\r\n As of Shadowkeep, these will come up much more frequently and be driven by game content rather than custom curation.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Sockets.DestinyPlugSetDefinition"
              }
          },
          "randomizedPlugSetHash": {
              "format": "uint32",
              "description": "This field replaces \"randomizedPlugItems\" as of Shadowkeep launch. If a socket has randomized plugs, this is a pointer to the set of plugs that could be used, as defined in DestinyPlugSetDefinition.\r\n If null, the item has no randomized plugs.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Sockets.DestinyPlugSetDefinition"
              }
          },
          "defaultVisible": {
              "description": "If true, then this socket is visible in the item's \"default\" state. If you have an instance, you should always check the runtime state, as that can override this visibility setting: but if you're looking at the item on a conceptual level, this property can be useful for hiding data such as legacy sockets - which remain defined on items for infrastructure purposes, but can be confusing for users to see.",
              "type": "boolean"
          }
      }
  }
}
```
