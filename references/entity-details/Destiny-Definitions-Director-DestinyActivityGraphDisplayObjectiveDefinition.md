# Destiny.Definitions.Director.DestinyActivityGraphDisplayObjectiveDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Director.DestinyActivityGraphDisplayObjectiveDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
When a Graph needs to show active Objectives, this defines those objectives as well as an identifier.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| id | integer (uint32) | $NOTE $amola 2017-01-19 This field is apparently something that CUI uses to manually wire up objectives to display info. I am unsure how it works. | No |
| objectiveHash | integer (uint32) | The objective being shown on the map. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Director.DestinyActivityGraphDisplayObjectiveDefinition object
const example = {
  id: 123,
  objectiveHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Director.DestinyActivityGraphDisplayObjectiveDefinition object
example = {
    "id": 123,
    "objectiveHash": 123,
}
```

## Related Entities
- **Destiny.Definitions.DestinyObjectiveDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Director.DestinyActivityGraphDisplayObjectiveDefinition":   {
      "description": "When a Graph needs to show active Objectives, this defines those objectives as well as an identifier.",
      "type": "object",
      "properties": {
          "id": {
              "format": "uint32",
              "description": "$NOTE $amola 2017-01-19 This field is apparently something that CUI uses to manually wire up objectives to display info. I am unsure how it works.",
              "type": "integer"
          },
          "objectiveHash": {
              "format": "uint32",
              "description": "The objective being shown on the map.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyObjectiveDefinition"
              }
          }
      }
  }
}
```
