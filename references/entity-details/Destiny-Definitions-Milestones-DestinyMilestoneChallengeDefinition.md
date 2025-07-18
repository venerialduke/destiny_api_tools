# Destiny.Definitions.Milestones.DestinyMilestoneChallengeDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Milestones.DestinyMilestoneChallengeDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinymilestonechallengedefinition data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| challengeObjectiveHash | integer (uint32) | The challenge related to this milestone. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Milestones.DestinyMilestoneChallengeDefinition object
const example = {
  challengeObjectiveHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Milestones.DestinyMilestoneChallengeDefinition object
example = {
    "challengeObjectiveHash": 123,
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
  "Destiny.Definitions.Milestones.DestinyMilestoneChallengeDefinition":   {
      "type": "object",
      "properties": {
          "challengeObjectiveHash": {
              "format": "uint32",
              "description": "The challenge related to this milestone.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyObjectiveDefinition"
              }
          }
      }
  }
}
```
