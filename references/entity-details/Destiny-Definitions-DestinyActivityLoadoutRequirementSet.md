# Destiny.Definitions.DestinyActivityLoadoutRequirementSet

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyActivityLoadoutRequirementSet
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyactivityloadoutrequirementset data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| requirements | Array[Destiny.Definitions.DestinyActivityLoadoutRequirement] | The set of requirements that will be applied on the activity if this requirement set is active. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyActivityLoadoutRequirementSet object
const example = {
  requirements: [],
};
```

### Python
```python
# Example Destiny.Definitions.DestinyActivityLoadoutRequirementSet object
example = {
    "requirements": [],
}
```

## Related Entities
- **Destiny.Definitions.DestinyActivityLoadoutRequirement**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyActivityLoadoutRequirementSet":   {
      "type": "object",
      "properties": {
          "requirements": {
              "description": "The set of requirements that will be applied on the activity if this requirement set is active.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityLoadoutRequirement"
              }
          }
      }
  }
}
```
