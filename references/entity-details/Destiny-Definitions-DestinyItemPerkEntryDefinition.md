# Destiny.Definitions.DestinyItemPerkEntryDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemPerkEntryDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
An intrinsic perk on an item, and the requirements for it to be activated.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| requirementDisplayString | string | If this perk is not active, this is the string to show for why it's not providing its benefits. | No |
| perkHash | integer (uint32) | A hash identifier for the DestinySandboxPerkDefinition being provided on the item. | No |
| perkVisibility | integer (int32) | Indicates whether this perk should be shown, or if it should be shown disabled. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemPerkEntryDefinition object
const example = {
  requirementDisplayString: "example value",
  perkHash: 123,
  perkVisibility: 123,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemPerkEntryDefinition object
example = {
    "requirementDisplayString": "example value",
    "perkHash": 123,
    "perkVisibility": 123,
}
```

## Related Entities
- **Destiny.Definitions.DestinySandboxPerkDefinition**: Referenced in this entity
- **Destiny.ItemPerkVisibility**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyItemPerkEntryDefinition":   {
      "description": "An intrinsic perk on an item, and the requirements for it to be activated.",
      "type": "object",
      "properties": {
          "requirementDisplayString": {
              "description": "If this perk is not active, this is the string to show for why it's not providing its benefits.",
              "type": "string"
          },
          "perkHash": {
              "format": "uint32",
              "description": "A hash identifier for the DestinySandboxPerkDefinition being provided on the item.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinySandboxPerkDefinition"
              }
          },
          "perkVisibility": {
              "format": "int32",
              "description": "Indicates whether this perk should be shown, or if it should be shown disabled.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.ItemPerkVisibility"
              }
          }
      }
  }
}
```
