# Destiny.Definitions.DestinyVendorItemSocketOverride

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyVendorItemSocketOverride
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The information for how the vendor purchase should override a given socket with custom plug data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| singleItemHash | integer (uint32) | If this is populated, the socket will be overridden with a specific plug.
If this isn't populated, it's being overridden by something more complicated that is only known by the Game Server and God, which means we can't tell you in advance what it'll be. | No |
| randomizedOptionsCount | integer (int32) | If this is greater than -1, the number of randomized plugs on this socket will be set to this quantity instead of whatever it's set to by default. | No |
| socketTypeHash | integer (uint32) | This appears to be used to select which socket ultimately gets the override defined here. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyVendorItemSocketOverride object
const example = {
  singleItemHash: 123,
  randomizedOptionsCount: 123,
  socketTypeHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyVendorItemSocketOverride object
example = {
    "singleItemHash": 123,
    "randomizedOptionsCount": 123,
    "socketTypeHash": 123,
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
  "Destiny.Definitions.DestinyVendorItemSocketOverride":   {
      "description": "The information for how the vendor purchase should override a given socket with custom plug data.",
      "type": "object",
      "properties": {
          "singleItemHash": {
              "format": "uint32",
              "description": "If this is populated, the socket will be overridden with a specific plug.\r\nIf this isn't populated, it's being overridden by something more complicated that is only known by the Game Server and God, which means we can't tell you in advance what it'll be.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "randomizedOptionsCount": {
              "format": "int32",
              "description": "If this is greater than -1, the number of randomized plugs on this socket will be set to this quantity instead of whatever it's set to by default.",
              "type": "integer"
          },
          "socketTypeHash": {
              "format": "uint32",
              "description": "This appears to be used to select which socket ultimately gets the override defined here.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Sockets.DestinySocketTypeDefinition"
              }
          }
      }
  }
}
```
