# Destiny.Definitions.Activities.DestinyActivitySelectableSkull

## Entity Information
- **Entity Name**: Destiny.Definitions.Activities.DestinyActivitySelectableSkull
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyactivityselectableskull data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| requiredTraitHash | integer (uint32) |  | No |
| requiredTraitExistence | boolean |  | No |
| isEmptySkull | boolean |  | No |
| loadoutRestrictionHash | integer (uint32) |  | No |
| activitySkull | Destiny.Definitions.Activities.DestinyActivitySkull |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Activities.DestinyActivitySelectableSkull object
const example = {
  requiredTraitHash: 123,
  requiredTraitExistence: true,
  isEmptySkull: true,
  loadoutRestrictionHash: 123,
  activitySkull: null,
};
```

### Python
```python
# Example Destiny.Definitions.Activities.DestinyActivitySelectableSkull object
example = {
    "requiredTraitHash": 123,
    "requiredTraitExistence": True,
    "isEmptySkull": True,
    "loadoutRestrictionHash": 123,
    "activitySkull": None,
}
```

## Related Entities
- **Destiny.Definitions.Activities.DestinyActivityLoadoutRestrictionDefinition**: Referenced in this entity
- **Destiny.Definitions.Activities.DestinyActivitySkull**: Referenced in this entity
- **Destiny.Definitions.Traits.DestinyTraitDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Activities.DestinyActivitySelectableSkull":   {
      "type": "object",
      "properties": {
          "requiredTraitHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Traits.DestinyTraitDefinition"
              }
          },
          "requiredTraitExistence": {
              "type": "boolean"
          },
          "isEmptySkull": {
              "type": "boolean"
          },
          "loadoutRestrictionHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Activities.DestinyActivityLoadoutRestrictionDefinition"
              }
          },
          "activitySkull": {
              "$ref": "#/definitions/Destiny.Definitions.Activities.DestinyActivitySkull"
          }
      }
  }
}
```
