# Destiny.Definitions.DestinyItemSocketCategoryDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemSocketCategoryDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Sockets are grouped into categories in the UI. These define which category and which sockets are under that category.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| socketCategoryHash | integer (uint32) | The hash for the Socket Category: a quick way to go get the header display information for the category. Use it to look up DestinySocketCategoryDefinition info. | No |
| socketIndexes | Array[integer] | Use these indexes to look up the sockets in the "sockets.socketEntries" property on the item definition. These are the indexes under the category, in game-rendered order. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemSocketCategoryDefinition object
const example = {
  socketCategoryHash: 123,
  socketIndexes: [],
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemSocketCategoryDefinition object
example = {
    "socketCategoryHash": 123,
    "socketIndexes": [],
}
```

## Related Entities
- **Destiny.Definitions.Sockets.DestinySocketCategoryDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyItemSocketCategoryDefinition":   {
      "description": "Sockets are grouped into categories in the UI. These define which category and which sockets are under that category.",
      "type": "object",
      "properties": {
          "socketCategoryHash": {
              "format": "uint32",
              "description": "The hash for the Socket Category: a quick way to go get the header display information for the category. Use it to look up DestinySocketCategoryDefinition info.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Sockets.DestinySocketCategoryDefinition"
              }
          },
          "socketIndexes": {
              "description": "Use these indexes to look up the sockets in the \"sockets.socketEntries\" property on the item definition. These are the indexes under the category, in game-rendered order.",
              "type": "array",
              "items": {
                  "format": "int32",
                  "type": "integer"
              }
          }
      }
  }
}
```
