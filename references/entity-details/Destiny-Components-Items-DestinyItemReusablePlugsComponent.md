# Destiny.Components.Items.DestinyItemReusablePlugsComponent

## Entity Information
- **Entity Name**: Destiny.Components.Items.DestinyItemReusablePlugsComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyitemreusableplugscomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| plugs | object | If the item supports reusable plugs, this is the list of plugs that are allowed to be used for the socket, and any relevant information about whether they are "enabled", whether they are allowed to be inserted, and any other information such as objectives.
 A Reusable Plug is a plug that you can always insert into this socket as long as its insertion rules are passed, regardless of whether or not you have the plug in your inventory. An example of it failing an insertion rule would be if it has an Objective that needs to be completed before it can be inserted, and that objective hasn't been completed yet.
 In practice, a socket will *either* have reusable plugs *or* it will allow for plugs in your inventory to be inserted. See DestinyInventoryItemDefinition.socket for more info.
 KEY = The INDEX into the item's list of sockets. VALUE = The set of plugs for that socket.
 If a socket doesn't have any reusable plugs defined at the item scope, there will be no entry for that socket. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Items.DestinyItemReusablePlugsComponent object
const example = {
  plugs: null,
};
```

### Python
```python
# Example Destiny.Components.Items.DestinyItemReusablePlugsComponent object
example = {
    "plugs": None,
}
```

## Related Entities
- **Destiny.Sockets.DestinyItemPlugBase**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Items.DestinyItemReusablePlugsComponent":   {
      "type": "object",
      "properties": {
          "plugs": {
              "description": "If the item supports reusable plugs, this is the list of plugs that are allowed to be used for the socket, and any relevant information about whether they are \"enabled\", whether they are allowed to be inserted, and any other information such as objectives.\r\n A Reusable Plug is a plug that you can always insert into this socket as long as its insertion rules are passed, regardless of whether or not you have the plug in your inventory. An example of it failing an insertion rule would be if it has an Objective that needs to be completed before it can be inserted, and that objective hasn't been completed yet.\r\n In practice, a socket will *either* have reusable plugs *or* it will allow for plugs in your inventory to be inserted. See DestinyInventoryItemDefinition.socket for more info.\r\n KEY = The INDEX into the item's list of sockets. VALUE = The set of plugs for that socket.\r\n If a socket doesn't have any reusable plugs defined at the item scope, there will be no entry for that socket.",
              "type": "object",
              "additionalProperties": {
                  "type": "array",
                  "items": {
                      "$ref": "#/definitions/Destiny.Sockets.DestinyItemPlugBase"
                  }
              }
          }
      },
      "x-destiny-component-type-dependency": "ItemReusablePlugs"
  }
}
```
