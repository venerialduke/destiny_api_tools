# Destiny.Components.PlugSets.DestinyPlugSetsComponent

## Entity Information
- **Entity Name**: Destiny.Components.PlugSets.DestinyPlugSetsComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Sockets may refer to a "Plug Set": a set of reusable plugs that may be shared across multiple sockets (or even, in theory, multiple sockets over multiple items).
This is the set of those plugs that we came across in the users' inventory, along with the values for plugs in the set. Any given set in this component may be represented in Character and Profile-level, as some plugs may be Profile-level restricted, and some character-level restricted. (note that the ones that are even more specific will remain on the actual socket component itself, as they cannot be reused)

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| plugs | object | The shared list of plugs for each relevant PlugSet, keyed by the hash identifier of the PlugSet (DestinyPlugSetDefinition). | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.PlugSets.DestinyPlugSetsComponent object
const example = {
  plugs: null,
};
```

### Python
```python
# Example Destiny.Components.PlugSets.DestinyPlugSetsComponent object
example = {
    "plugs": None,
}
```

## Related Entities
- **Destiny.Definitions.Sockets.DestinyPlugSetDefinition**: Referenced in this entity
- **Destiny.Sockets.DestinyItemPlug**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.PlugSets.DestinyPlugSetsComponent":   {
      "description": "Sockets may refer to a \"Plug Set\": a set of reusable plugs that may be shared across multiple sockets (or even, in theory, multiple sockets over multiple items).\r\nThis is the set of those plugs that we came across in the users' inventory, along with the values for plugs in the set. Any given set in this component may be represented in Character and Profile-level, as some plugs may be Profile-level restricted, and some character-level restricted. (note that the ones that are even more specific will remain on the actual socket component itself, as they cannot be reused)",
      "type": "object",
      "properties": {
          "plugs": {
              "description": "The shared list of plugs for each relevant PlugSet, keyed by the hash identifier of the PlugSet (DestinyPlugSetDefinition).",
              "type": "object",
              "additionalProperties": {
                  "type": "array",
                  "items": {
                      "$ref": "#/definitions/Destiny.Sockets.DestinyItemPlug"
                  }
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Sockets.DestinyPlugSetDefinition"
              }
          }
      },
      "x-destiny-component-type-dependency": "ItemSockets"
  }
}
```
