# Destiny.Definitions.Sockets.DestinyPlugWhitelistEntryDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Sockets.DestinyPlugWhitelistEntryDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Defines a plug "Category" that is allowed to be plugged into a socket of this type.
This should be compared against a given plug item's DestinyInventoryItemDefinition.plug.plugCategoryHash, which indicates the plug item's category.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| categoryHash | integer (uint32) | The hash identifier of the Plug Category to compare against the plug item's plug.plugCategoryHash.
Note that this does NOT relate to any Definition in itself, it is only used for comparison purposes. | No |
| categoryIdentifier | string | The string identifier for the category, which is here mostly for debug purposes. | No |
| reinitializationPossiblePlugHashes | Array[integer] | The list of all plug items (DestinyInventoryItemDefinition) that the socket may randomly be populated with when reinitialized.
Which ones you should actually show are determined by the plug being inserted into the socket, and the socket’s type.
When you inspect the plug that could go into a Masterwork Socket, look up the socket type of the socket being inspected and find the DestinySocketTypeDefinition.
Then, look at the Plugs that can fit in that socket. Find the Whitelist in the DestinySocketTypeDefinition that matches the plug item’s categoryhash.
That whitelist entry will potentially have a new “reinitializationPossiblePlugHashes” property.If it does, that means we know what it will roll if you try to insert this plug into this socket. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Sockets.DestinyPlugWhitelistEntryDefinition object
const example = {
  categoryHash: 123,
  categoryIdentifier: "example value",
  reinitializationPossiblePlugHashes: [],
};
```

### Python
```python
# Example Destiny.Definitions.Sockets.DestinyPlugWhitelistEntryDefinition object
example = {
    "categoryHash": 123,
    "categoryIdentifier": "example value",
    "reinitializationPossiblePlugHashes": [],
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Sockets.DestinyPlugWhitelistEntryDefinition":   {
      "description": "Defines a plug \"Category\" that is allowed to be plugged into a socket of this type.\r\nThis should be compared against a given plug item's DestinyInventoryItemDefinition.plug.plugCategoryHash, which indicates the plug item's category.",
      "type": "object",
      "properties": {
          "categoryHash": {
              "format": "uint32",
              "description": "The hash identifier of the Plug Category to compare against the plug item's plug.plugCategoryHash.\r\nNote that this does NOT relate to any Definition in itself, it is only used for comparison purposes.",
              "type": "integer"
          },
          "categoryIdentifier": {
              "description": "The string identifier for the category, which is here mostly for debug purposes.",
              "type": "string"
          },
          "reinitializationPossiblePlugHashes": {
              "description": "The list of all plug items (DestinyInventoryItemDefinition) that the socket may randomly be populated with when reinitialized.\r\nWhich ones you should actually show are determined by the plug being inserted into the socket, and the socket\u2019s type.\r\nWhen you inspect the plug that could go into a Masterwork Socket, look up the socket type of the socket being inspected and find the DestinySocketTypeDefinition.\r\nThen, look at the Plugs that can fit in that socket. Find the Whitelist in the DestinySocketTypeDefinition that matches the plug item\u2019s categoryhash.\r\nThat whitelist entry will potentially have a new \u201creinitializationPossiblePlugHashes\u201d property.If it does, that means we know what it will roll if you try to insert this plug into this socket.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              }
          }
      }
  }
}
```
