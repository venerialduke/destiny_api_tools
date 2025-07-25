# Destiny.Definitions.Sockets.DestinyPlugSetDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Sockets.DestinyPlugSetDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Sometimes, we have large sets of reusable plugs that are defined identically and thus can (and in some cases, are so large that they *must*) be shared across the places where they are used. These are the definitions for those reusable sets of plugs. 
 See DestinyItemSocketEntryDefinition.plugSource and reusablePlugSetHash for the relationship between these reusable plug sets and the sockets that leverage them (for starters, Emotes).
 As of the release of Shadowkeep (Late 2019), these will begin to be sourced from game content directly - which means there will be many more of them, but it also means we may not get all data that we used to get for them.
 DisplayProperties, in particular, will no longer be guaranteed to contain valid information. We will make a best effort to guess what ought to be populated there where possible, but it will be invalid for many/most plug sets.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | object | If you want to show these plugs in isolation, these are the display properties for them. | No |
| reusablePlugItems | Array[Destiny.Definitions.DestinyItemSocketEntryPlugItemRandomizedDefinition] | This is a list of pre-determined plugs that can be plugged into this socket, without the character having the plug in their inventory.
If this list is populated, you will not be allowed to plug an arbitrary item in the socket: you will only be able to choose from one of these reusable plugs. | No |
| isFakePlugSet | boolean | Mostly for our debugging or reporting bugs, BNet is making "fake" plug sets in a desperate effort to reduce socket sizes.
 If this is true, the plug set was generated by BNet: if it looks wrong, that's a good indicator that it's bungie.net that fucked this up. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Sockets.DestinyPlugSetDefinition object
const example = {
  displayProperties: null,
  reusablePlugItems: [],
  isFakePlugSet: true,
  hash: 123,
  index: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Sockets.DestinyPlugSetDefinition object
example = {
    "displayProperties": None,
    "reusablePlugItems": [],
    "isFakePlugSet": True,
    "hash": 123,
    "index": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyItemSocketEntryPlugItemRandomizedDefinition**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Sockets.DestinyPlugSetDefinition":   {
      "description": "Sometimes, we have large sets of reusable plugs that are defined identically and thus can (and in some cases, are so large that they *must*) be shared across the places where they are used. These are the definitions for those reusable sets of plugs. \r\n See DestinyItemSocketEntryDefinition.plugSource and reusablePlugSetHash for the relationship between these reusable plug sets and the sockets that leverage them (for starters, Emotes).\r\n As of the release of Shadowkeep (Late 2019), these will begin to be sourced from game content directly - which means there will be many more of them, but it also means we may not get all data that we used to get for them.\r\n DisplayProperties, in particular, will no longer be guaranteed to contain valid information. We will make a best effort to guess what ought to be populated there where possible, but it will be invalid for many/most plug sets.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "description": "If you want to show these plugs in isolation, these are the display properties for them.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
                  }
              ]
          },
          "reusablePlugItems": {
              "description": "This is a list of pre-determined plugs that can be plugged into this socket, without the character having the plug in their inventory.\r\nIf this list is populated, you will not be allowed to plug an arbitrary item in the socket: you will only be able to choose from one of these reusable plugs.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyItemSocketEntryPlugItemRandomizedDefinition"
              }
          },
          "isFakePlugSet": {
              "description": "Mostly for our debugging or reporting bugs, BNet is making \"fake\" plug sets in a desperate effort to reduce socket sizes.\r\n If this is true, the plug set was generated by BNet: if it looks wrong, that's a good indicator that it's bungie.net that fucked this up.",
              "type": "boolean"
          },
          "hash": {
              "format": "uint32",
              "description": "The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.\r\nWhen entities refer to each other in Destiny content, it is this hash that they are referring to.",
              "type": "integer"
          },
          "index": {
              "format": "int32",
              "description": "The index of the entity as it was found in the investment tables.",
              "type": "integer"
          },
          "redacted": {
              "description": "If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!",
              "type": "boolean"
          }
      },
      "x-mobile-manifest-name": "PlugSets"
  }
}
```
