# Destiny.Definitions.DestinyObjectiveStatEntryDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyObjectiveStatEntryDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Defines the conditions under which stat modifications will be applied to a Character while participating in an objective.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| stat | object | The stat being modified, and the value used. | No |
| style | integer (int32) | Whether it will be applied as long as the objective is active, when it's completed, or until it's completed. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyObjectiveStatEntryDefinition object
const example = {
  stat: null,
  style: 123,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyObjectiveStatEntryDefinition object
example = {
    "stat": None,
    "style": 123,
}
```

## Related Entities
- **Destiny.Definitions.DestinyItemInvestmentStatDefinition**: Referenced in this entity
- **Destiny.DestinyObjectiveGrantStyle**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyObjectiveStatEntryDefinition":   {
      "description": "Defines the conditions under which stat modifications will be applied to a Character while participating in an objective.",
      "type": "object",
      "properties": {
          "stat": {
              "description": "The stat being modified, and the value used.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.DestinyItemInvestmentStatDefinition"
                  }
              ]
          },
          "style": {
              "format": "int32",
              "description": "Whether it will be applied as long as the objective is active, when it's completed, or until it's completed.",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyObjectiveGrantStyle"
              }
          }
      }
  }
}
```
