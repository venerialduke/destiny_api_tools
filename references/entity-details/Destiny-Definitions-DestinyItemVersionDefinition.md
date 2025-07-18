# Destiny.Definitions.DestinyItemVersionDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemVersionDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The version definition currently just holds a reference to the power cap.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| powerCapHash | integer (uint32) | A reference to the power cap for this item version. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemVersionDefinition object
const example = {
  powerCapHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemVersionDefinition object
example = {
    "powerCapHash": 123,
}
```

## Related Entities
- **Destiny.Definitions.PowerCaps.DestinyPowerCapDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyItemVersionDefinition":   {
      "description": "The version definition currently just holds a reference to the power cap.",
      "type": "object",
      "properties": {
          "powerCapHash": {
              "format": "uint32",
              "description": "A reference to the power cap for this item version.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.PowerCaps.DestinyPowerCapDefinition"
              }
          }
      }
  }
}
```
