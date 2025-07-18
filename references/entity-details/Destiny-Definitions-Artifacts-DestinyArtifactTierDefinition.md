# Destiny.Definitions.Artifacts.DestinyArtifactTierDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Artifacts.DestinyArtifactTierDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyartifacttierdefinition data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| tierHash | integer (uint32) | An identifier, unique within the Artifact, for this specific tier. | No |
| displayTitle | string | The human readable title of this tier, if any. | No |
| progressRequirementMessage | string | A string representing the localized minimum requirement text for this Tier, if any. | No |
| items | Array[Destiny.Definitions.Artifacts.DestinyArtifactTierItemDefinition] | The items that can be earned within this tier. | No |
| minimumUnlockPointsUsedRequirement | integer (int32) | The minimum number of "unlock points" that you must have used before you can unlock items from this tier. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Artifacts.DestinyArtifactTierDefinition object
const example = {
  tierHash: 123,
  displayTitle: "example value",
  progressRequirementMessage: "example value",
  items: [],
  minimumUnlockPointsUsedRequirement: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Artifacts.DestinyArtifactTierDefinition object
example = {
    "tierHash": 123,
    "displayTitle": "example value",
    "progressRequirementMessage": "example value",
    "items": [],
    "minimumUnlockPointsUsedRequirement": 123,
}
```

## Related Entities
- **Destiny.Definitions.Artifacts.DestinyArtifactTierItemDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Artifacts.DestinyArtifactTierDefinition":   {
      "type": "object",
      "properties": {
          "tierHash": {
              "format": "uint32",
              "description": "An identifier, unique within the Artifact, for this specific tier.",
              "type": "integer"
          },
          "displayTitle": {
              "description": "The human readable title of this tier, if any.",
              "type": "string"
          },
          "progressRequirementMessage": {
              "description": "A string representing the localized minimum requirement text for this Tier, if any.",
              "type": "string"
          },
          "items": {
              "description": "The items that can be earned within this tier.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Artifacts.DestinyArtifactTierItemDefinition"
              }
          },
          "minimumUnlockPointsUsedRequirement": {
              "format": "int32",
              "description": "The minimum number of \"unlock points\" that you must have used before you can unlock items from this tier.",
              "type": "integer"
          }
      }
  }
}
```
