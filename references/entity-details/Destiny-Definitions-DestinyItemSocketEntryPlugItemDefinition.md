# Destiny.Definitions.DestinyItemSocketEntryPlugItemDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemSocketEntryPlugItemDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The definition of a known, reusable plug that can be applied to a socket.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| plugItemHash | integer (uint32) | The hash identifier of a DestinyInventoryItemDefinition representing the plug that can be inserted. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemSocketEntryPlugItemDefinition object
const example = {
  plugItemHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemSocketEntryPlugItemDefinition object
example = {
    "plugItemHash": 123,
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyItemSocketEntryPlugItemDefinition":   {
      "description": "The definition of a known, reusable plug that can be applied to a socket.",
      "type": "object",
      "properties": {
          "plugItemHash": {
              "format": "uint32",
              "description": "The hash identifier of a DestinyInventoryItemDefinition representing the plug that can be inserted.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          }
      }
  }
}
```
