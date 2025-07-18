# Destiny.Definitions.DestinyActivityRequirementsBlock

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyActivityRequirementsBlock
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyactivityrequirementsblock data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| leaderRequirementLabels | Array[Destiny.Definitions.DestinyActivityRequirementLabel] | If being a fireteam Leader in this activity is gated, this is the gate being checked. | No |
| fireteamRequirementLabels | Array[Destiny.Definitions.DestinyActivityRequirementLabel] | If being a fireteam member in this activity is gated, this is the gate being checked. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyActivityRequirementsBlock object
const example = {
  leaderRequirementLabels: [],
  fireteamRequirementLabels: [],
};
```

### Python
```python
# Example Destiny.Definitions.DestinyActivityRequirementsBlock object
example = {
    "leaderRequirementLabels": [],
    "fireteamRequirementLabels": [],
}
```

## Related Entities
- **Destiny.Definitions.DestinyActivityRequirementLabel**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyActivityRequirementsBlock":   {
      "type": "object",
      "properties": {
          "leaderRequirementLabels": {
              "description": "If being a fireteam Leader in this activity is gated, this is the gate being checked.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityRequirementLabel"
              }
          },
          "fireteamRequirementLabels": {
              "description": "If being a fireteam member in this activity is gated, this is the gate being checked.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityRequirementLabel"
              }
          }
      }
  }
}
```
