# Destiny.Definitions.DestinyProgressionSocketPlugOverride

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyProgressionSocketPlugOverride
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The information for how progression item definitions should override a given socket with custom plug data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| socketTypeHash | integer (uint32) |  | No |
| overrideSingleItemHash | integer (uint32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyProgressionSocketPlugOverride object
const example = {
  socketTypeHash: 123,
  overrideSingleItemHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyProgressionSocketPlugOverride object
example = {
    "socketTypeHash": 123,
    "overrideSingleItemHash": 123,
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
  "Destiny.Definitions.DestinyProgressionSocketPlugOverride":   {
      "description": "The information for how progression item definitions should override a given socket with custom plug data.",
      "type": "object",
      "properties": {
          "socketTypeHash": {
              "format": "uint32",
              "type": "integer"
          },
          "overrideSingleItemHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          }
      }
  }
}
```
