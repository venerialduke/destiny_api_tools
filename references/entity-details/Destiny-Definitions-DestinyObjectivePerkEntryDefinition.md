# Destiny.Definitions.DestinyObjectivePerkEntryDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyObjectivePerkEntryDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Defines the conditions under which an intrinsic perk is applied while participating in an Objective.
These perks will generally not be benefit-granting perks, but rather a perk that modifies gameplay in some interesting way.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| perkHash | integer (uint32) | The hash identifier of the DestinySandboxPerkDefinition that will be applied to the character. | No |
| style | integer (int32) | An enumeration indicating whether it will be applied as long as the Objective is active, when it's completed, or until it's completed. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyObjectivePerkEntryDefinition object
const example = {
  perkHash: 123,
  style: 123,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyObjectivePerkEntryDefinition object
example = {
    "perkHash": 123,
    "style": 123,
}
```

## Related Entities
- **Destiny.Definitions.DestinySandboxPerkDefinition**: Referenced in this entity
- **Destiny.DestinyObjectiveGrantStyle**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyObjectivePerkEntryDefinition":   {
      "description": "Defines the conditions under which an intrinsic perk is applied while participating in an Objective.\r\nThese perks will generally not be benefit-granting perks, but rather a perk that modifies gameplay in some interesting way.",
      "type": "object",
      "properties": {
          "perkHash": {
              "format": "uint32",
              "description": "The hash identifier of the DestinySandboxPerkDefinition that will be applied to the character.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinySandboxPerkDefinition"
              }
          },
          "style": {
              "format": "int32",
              "description": "An enumeration indicating whether it will be applied as long as the Objective is active, when it's completed, or until it's completed.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyObjectiveGrantStyle"
              }
          }
      }
  }
}
```
