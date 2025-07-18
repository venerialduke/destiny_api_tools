# Destiny.Definitions.Items.DestinyItemSetPerkDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Items.DestinyItemSetPerkDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyitemsetperkdefinition data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| requiredSetCount | integer (int32) | The number of set pieces required to activate the perk. | No |
| sandboxPerkHash | integer (uint32) | The perk this set confers. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Items.DestinyItemSetPerkDefinition object
const example = {
  requiredSetCount: 123,
  sandboxPerkHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Items.DestinyItemSetPerkDefinition object
example = {
    "requiredSetCount": 123,
    "sandboxPerkHash": 123,
}
```

## Related Entities
- **Destiny.Definitions.DestinySandboxPerkDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Items.DestinyItemSetPerkDefinition":   {
      "type": "object",
      "properties": {
          "requiredSetCount": {
              "format": "int32",
              "description": "The number of set pieces required to activate the perk.",
              "type": "integer"
          },
          "sandboxPerkHash": {
              "format": "uint32",
              "description": "The perk this set confers.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinySandboxPerkDefinition"
              }
          }
      }
  }
}
```
