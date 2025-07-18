# Destiny.Components.Craftables.DestinyCraftableSocketComponent

## Entity Information
- **Entity Name**: Destiny.Components.Craftables.DestinyCraftableSocketComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinycraftablesocketcomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| plugSetHash | integer (uint32) |  | No |
| plugs | Array[Destiny.Components.Craftables.DestinyCraftableSocketPlugComponent] | Unlock state for plugs in the socket plug set definition | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Craftables.DestinyCraftableSocketComponent object
const example = {
  plugSetHash: 123,
  plugs: [],
};
```

### Python
```python
# Example Destiny.Components.Craftables.DestinyCraftableSocketComponent object
example = {
    "plugSetHash": 123,
    "plugs": [],
}
```

## Related Entities
- **Destiny.Components.Craftables.DestinyCraftableSocketPlugComponent**: Referenced in this entity
- **Destiny.Definitions.Sockets.DestinyPlugSetDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Craftables.DestinyCraftableSocketComponent":   {
      "type": "object",
      "properties": {
          "plugSetHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Sockets.DestinyPlugSetDefinition"
              }
          },
          "plugs": {
              "description": "Unlock state for plugs in the socket plug set definition",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Components.Craftables.DestinyCraftableSocketPlugComponent"
              }
          }
      }
  }
}
```
