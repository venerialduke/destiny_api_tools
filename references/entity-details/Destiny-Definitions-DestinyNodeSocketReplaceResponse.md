# Destiny.Definitions.DestinyNodeSocketReplaceResponse

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyNodeSocketReplaceResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
This is a bit of an odd duck. Apparently, if talent nodes steps have this data, the game will go through on step activation and alter the first Socket it finds on the item that has a type matching the given socket type, inserting the indicated plug item.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| socketTypeHash | integer (uint32) | The hash identifier of the socket type to find amidst the item's sockets (the item to which this talent grid is attached). See DestinyInventoryItemDefinition.sockets.socketEntries to find the socket type of sockets on the item in question. | No |
| plugItemHash | integer (uint32) | The hash identifier of the plug item that will be inserted into the socket found. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyNodeSocketReplaceResponse object
const example = {
  socketTypeHash: 123,
  plugItemHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyNodeSocketReplaceResponse object
example = {
    "socketTypeHash": 123,
    "plugItemHash": 123,
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
  "Destiny.Definitions.DestinyNodeSocketReplaceResponse":   {
      "description": "This is a bit of an odd duck. Apparently, if talent nodes steps have this data, the game will go through on step activation and alter the first Socket it finds on the item that has a type matching the given socket type, inserting the indicated plug item.",
      "type": "object",
      "properties": {
          "socketTypeHash": {
              "format": "uint32",
              "description": "The hash identifier of the socket type to find amidst the item's sockets (the item to which this talent grid is attached). See DestinyInventoryItemDefinition.sockets.socketEntries to find the socket type of sockets on the item in question.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Sockets.DestinySocketTypeDefinition"
              }
          },
          "plugItemHash": {
              "format": "uint32",
              "description": "The hash identifier of the plug item that will be inserted into the socket found.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          }
      }
  }
}
```
