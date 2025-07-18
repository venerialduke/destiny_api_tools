# Destiny.SocketPlugSources

## Entity Information
- **Entity Name**: Destiny.SocketPlugSources
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Indicates how a socket is populated, and where you should look for valid plug data.
 This is a flags enumeration/bitmask field, as you may have to look in multiple sources across multiple components for valid plugs.
 For instance, a socket could have plugs that are sourced from its own definition, as well as plugs that are sourced from Character-scoped AND profile-scoped Plug Sets. Only by combining plug data for every indicated source will you be able to know all of the plugs available for a socket.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None | If there's no way we can detect to insert new plugs. |
| 1 | InventorySourced | Use plugs found in the player's inventory, based on the socket type rules (see DestinySocketTypeDefinition for more info)
Note that a socket - like Shaders - can have *both* reusable plugs and inventory items inserted theoretically. |
| 2 | ReusablePlugItems | Use the DestinyItemSocketsComponent.sockets.reusablePlugs property to determine which plugs are valid for this socket. This may have to be combined with other sources, such as plug sets, if those flags are set.
 Note that "Reusable" plugs may not necessarily come from a plug set, nor from the "reusablePlugItems" in the socket's Definition data. They can sometimes be "randomized" in which case the only source of truth at the moment is still the runtime DestinyItemSocketsComponent.sockets.reusablePlugs property. |
| 4 | ProfilePlugSet | Use the ProfilePlugSets (DestinyProfileResponse.profilePlugSets) component data to determine which plugs are valid for this socket. |
| 8 | CharacterPlugSet | Use the CharacterPlugSets (DestinyProfileResponse.characterPlugSets) component data to determine which plugs are valid for this socket. |

## Usage Examples

### JavaScript
```javascript
// Destiny.SocketPlugSources enumeration values
const SocketPlugSources = {
  None: 0,
  InventorySourced: 1,
  ReusablePlugItems: 2,
  // ... more values
};

// Using the enumeration
const value = SocketPlugSources.None;
```

### Python
```python
# Destiny.SocketPlugSources enumeration values
class SocketPlugSources:
    NONE = 0
    INVENTORYSOURCED = 1
    REUSABLEPLUGITEMS = 2
    # ... more values

# Using the enumeration
value = SocketPlugSources.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.SocketPlugSources":   {
      "format": "int32",
      "description": "Indicates how a socket is populated, and where you should look for valid plug data.\r\n This is a flags enumeration/bitmask field, as you may have to look in multiple sources across multiple components for valid plugs.\r\n For instance, a socket could have plugs that are sourced from its own definition, as well as plugs that are sourced from Character-scoped AND profile-scoped Plug Sets. Only by combining plug data for every indicated source will you be able to know all of the plugs available for a socket.",
      "enum": [
          "0",
          "1",
          "2",
          "4",
          "8"
      ],
      "type": "integer"
  }
}
```
