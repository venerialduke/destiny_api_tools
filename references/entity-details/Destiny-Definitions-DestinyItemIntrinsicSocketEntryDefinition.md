# Destiny.Definitions.DestinyItemIntrinsicSocketEntryDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemIntrinsicSocketEntryDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Represents a socket that has a plug associated with it intrinsically. This is useful for situations where the weapon needs to have a visual plug/Mod on it, but that plug/Mod should never change.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| plugItemHash | integer (uint32) | Indicates the plug that is intrinsically inserted into this socket. | No |
| socketTypeHash | integer (uint32) | Indicates the type of this intrinsic socket. | No |
| defaultVisible | boolean | If true, then this socket is visible in the item's "default" state. If you have an instance, you should always check the runtime state, as that can override this visibility setting: but if you're looking at the item on a conceptual level, this property can be useful for hiding data such as legacy sockets - which remain defined on items for infrastructure purposes, but can be confusing for users to see. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemIntrinsicSocketEntryDefinition object
const example = {
  plugItemHash: 123,
  socketTypeHash: 123,
  defaultVisible: true,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemIntrinsicSocketEntryDefinition object
example = {
    "plugItemHash": 123,
    "socketTypeHash": 123,
    "defaultVisible": True,
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.Sockets.DestinySocketTypeDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyItemIntrinsicSocketEntryDefinition":   {
      "description": "Represents a socket that has a plug associated with it intrinsically. This is useful for situations where the weapon needs to have a visual plug/Mod on it, but that plug/Mod should never change.",
      "type": "object",
      "properties": {
          "plugItemHash": {
              "format": "uint32",
              "description": "Indicates the plug that is intrinsically inserted into this socket.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "socketTypeHash": {
              "format": "uint32",
              "description": "Indicates the type of this intrinsic socket.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Sockets.DestinySocketTypeDefinition"
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
