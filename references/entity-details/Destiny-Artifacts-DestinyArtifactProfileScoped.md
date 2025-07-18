# Destiny.Artifacts.DestinyArtifactProfileScoped

## Entity Information
- **Entity Name**: Destiny.Artifacts.DestinyArtifactProfileScoped
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Represents a Seasonal Artifact and all data related to it for the requested Account.
It can be combined with Character-scoped data for a full picture of what a character has available/has chosen, or just these settings can be used for overview information.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| artifactHash | integer (uint32) |  | No |
| pointProgression | Destiny.DestinyProgression |  | No |
| pointsAcquired | integer (int32) |  | No |
| powerBonusProgression | Destiny.DestinyProgression |  | No |
| powerBonus | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Artifacts.DestinyArtifactProfileScoped object
const example = {
  artifactHash: 123,
  pointProgression: null,
  pointsAcquired: 123,
  powerBonusProgression: null,
  powerBonus: 123,
};
```

### Python
```python
# Example Destiny.Artifacts.DestinyArtifactProfileScoped object
example = {
    "artifactHash": 123,
    "pointProgression": None,
    "pointsAcquired": 123,
    "powerBonusProgression": None,
    "powerBonus": 123,
}
```

## Related Entities
- **Destiny.Definitions.Artifacts.DestinyArtifactDefinition**: Referenced in this entity
- **Destiny.DestinyProgression**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Artifacts.DestinyArtifactProfileScoped":   {
      "description": "Represents a Seasonal Artifact and all data related to it for the requested Account.\r\nIt can be combined with Character-scoped data for a full picture of what a character has available/has chosen, or just these settings can be used for overview information.",
      "type": "object",
      "properties": {
          "artifactHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Artifacts.DestinyArtifactDefinition"
              }
          },
          "pointProgression": {
              "$ref": "#/definitions/Destiny.DestinyProgression"
          },
          "pointsAcquired": {
              "format": "int32",
              "type": "integer"
          },
          "powerBonusProgression": {
              "$ref": "#/definitions/Destiny.DestinyProgression"
          },
          "powerBonus": {
              "format": "int32",
              "type": "integer"
          }
      }
  }
}
```
