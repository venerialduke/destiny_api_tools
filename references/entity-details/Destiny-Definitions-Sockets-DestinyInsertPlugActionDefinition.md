# Destiny.Definitions.Sockets.DestinyInsertPlugActionDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Sockets.DestinyInsertPlugActionDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Data related to what happens while a plug is being inserted, mostly for UI purposes.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| actionExecuteSeconds | integer (int32) | How long it takes for the Plugging of the item to be completed once it is initiated, if you care. | No |
| actionType | integer (int32) | The type of action being performed when you act on this Socket Type. The most common value is "insert plug", but there are others as well (for instance, a "Masterwork" socket may allow for Re-initialization, and an Infusion socket allows for items to be consumed to upgrade the item) | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Sockets.DestinyInsertPlugActionDefinition object
const example = {
  actionExecuteSeconds: 123,
  actionType: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Sockets.DestinyInsertPlugActionDefinition object
example = {
    "actionExecuteSeconds": 123,
    "actionType": 123,
}
```

## Related Entities
- **Destiny.SocketTypeActionType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Sockets.DestinyInsertPlugActionDefinition":   {
      "description": "Data related to what happens while a plug is being inserted, mostly for UI purposes.",
      "type": "object",
      "properties": {
          "actionExecuteSeconds": {
              "format": "int32",
              "description": "How long it takes for the Plugging of the item to be completed once it is initiated, if you care.",
              "type": "integer"
          },
          "actionType": {
              "format": "int32",
              "description": "The type of action being performed when you act on this Socket Type. The most common value is \"insert plug\", but there are others as well (for instance, a \"Masterwork\" socket may allow for Re-initialization, and an Infusion socket allows for items to be consumed to upgrade the item)",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.SocketTypeActionType"
              }
          }
      }
  }
}
```
