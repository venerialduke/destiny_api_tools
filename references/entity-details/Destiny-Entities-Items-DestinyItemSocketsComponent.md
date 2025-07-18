# Destiny.Entities.Items.DestinyItemSocketsComponent

## Entity Information
- **Entity Name**: Destiny.Entities.Items.DestinyItemSocketsComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Instanced items can have sockets, which are slots on the item where plugs can be inserted.
Sockets are a bit complex: be sure to examine the documentation on the DestinyInventoryItemDefinition's "socket" block and elsewhere on these objects for more details.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| sockets | Array[Destiny.Entities.Items.DestinyItemSocketState] | The list of all sockets on the item, and their status information. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Entities.Items.DestinyItemSocketsComponent object
const example = {
  sockets: [],
};
```

### Python
```python
# Example Destiny.Entities.Items.DestinyItemSocketsComponent object
example = {
    "sockets": [],
}
```

## Related Entities
- **Destiny.Entities.Items.DestinyItemSocketState**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Entities.Items.DestinyItemSocketsComponent":   {
      "description": "Instanced items can have sockets, which are slots on the item where plugs can be inserted.\r\nSockets are a bit complex: be sure to examine the documentation on the DestinyInventoryItemDefinition's \"socket\" block and elsewhere on these objects for more details.",
      "type": "object",
      "properties": {
          "sockets": {
              "description": "The list of all sockets on the item, and their status information.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Entities.Items.DestinyItemSocketState"
              }
          }
      },
      "x-destiny-component-type-dependency": "ItemSockets"
  }
}
```
