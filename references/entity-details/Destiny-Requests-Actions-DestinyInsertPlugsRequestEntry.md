# Destiny.Requests.Actions.DestinyInsertPlugsRequestEntry

## Entity Information
- **Entity Name**: Destiny.Requests.Actions.DestinyInsertPlugsRequestEntry
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Represents all of the data related to a single plug to be inserted.
Note that, while you *can* point to a socket that represents infusion, you will receive an error if you attempt to do so. Come on guys, let's play nice.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| socketIndex | integer (int32) | The index into the socket array, which identifies the specific socket being operated on. We also need to know the socketArrayType in order to uniquely identify the socket.
Don't point to or try to insert a plug into an infusion socket. It won't work. | No |
| socketArrayType | integer (int32) | This property, combined with the socketIndex, tells us which socket we are referring to (since operations can be performed on both Intrinsic and "default" sockets, and they occupy different arrays in the Inventory Item Definition). I know, I know. Don't give me that look. | No |
| plugItemHash | integer (uint32) | Plugs are never instanced (except in infusion). So with the hash alone, we should be able to: 1) Infer whether the player actually needs to have the item, or if it's a reusable plug 2) Perform any operation needed to use the Plug, including removing the plug item and running reward sheets. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Requests.Actions.DestinyInsertPlugsRequestEntry object
const example = {
  socketIndex: 123,
  socketArrayType: 123,
  plugItemHash: 123,
};
```

### Python
```python
# Example Destiny.Requests.Actions.DestinyInsertPlugsRequestEntry object
example = {
    "socketIndex": 123,
    "socketArrayType": 123,
    "plugItemHash": 123,
}
```

## Related Entities
- **Destiny.Requests.Actions.DestinySocketArrayType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Requests.Actions.DestinyInsertPlugsRequestEntry":   {
      "description": "Represents all of the data related to a single plug to be inserted.\r\nNote that, while you *can* point to a socket that represents infusion, you will receive an error if you attempt to do so. Come on guys, let's play nice.",
      "type": "object",
      "properties": {
          "socketIndex": {
              "format": "int32",
              "description": "The index into the socket array, which identifies the specific socket being operated on. We also need to know the socketArrayType in order to uniquely identify the socket.\r\nDon't point to or try to insert a plug into an infusion socket. It won't work.",
              "type": "integer"
          },
          "socketArrayType": {
              "format": "int32",
              "description": "This property, combined with the socketIndex, tells us which socket we are referring to (since operations can be performed on both Intrinsic and \"default\" sockets, and they occupy different arrays in the Inventory Item Definition). I know, I know. Don't give me that look.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.Requests.Actions.DestinySocketArrayType"
              }
          },
          "plugItemHash": {
              "format": "uint32",
              "description": "Plugs are never instanced (except in infusion). So with the hash alone, we should be able to: 1) Infer whether the player actually needs to have the item, or if it's a reusable plug 2) Perform any operation needed to use the Plug, including removing the plug item and running reward sheets.",
              "type": "integer"
          }
      }
  }
}
```
