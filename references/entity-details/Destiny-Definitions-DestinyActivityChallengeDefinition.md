# Destiny.Definitions.DestinyActivityChallengeDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyActivityChallengeDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Represents a reference to a Challenge, which for now is just an Objective.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| objectiveHash | integer (uint32) | The hash for the Objective that matches this challenge. Use it to look up the DestinyObjectiveDefinition. | No |
| dummyRewards | Array[Destiny.DestinyItemQuantity] | The rewards as they're represented in the UI. Note that they generally link to "dummy" items that give a summary of rewards rather than direct, real items themselves.
If the quantity is 0, don't show the quantity. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyActivityChallengeDefinition object
const example = {
  objectiveHash: 123,
  dummyRewards: [],
};
```

### Python
```python
# Example Destiny.Definitions.DestinyActivityChallengeDefinition object
example = {
    "objectiveHash": 123,
    "dummyRewards": [],
}
```

## Related Entities
- **Destiny.Definitions.DestinyObjectiveDefinition**: Referenced in this entity
- **Destiny.DestinyItemQuantity**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyActivityChallengeDefinition":   {
      "description": "Represents a reference to a Challenge, which for now is just an Objective.",
      "type": "object",
      "properties": {
          "objectiveHash": {
              "format": "uint32",
              "description": "The hash for the Objective that matches this challenge. Use it to look up the DestinyObjectiveDefinition.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyObjectiveDefinition"
              }
          },
          "dummyRewards": {
              "description": "The rewards as they're represented in the UI. Note that they generally link to \"dummy\" items that give a summary of rewards rather than direct, real items themselves.\r\nIf the quantity is 0, don't show the quantity.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.DestinyItemQuantity"
              }
          }
      }
  }
}
```
