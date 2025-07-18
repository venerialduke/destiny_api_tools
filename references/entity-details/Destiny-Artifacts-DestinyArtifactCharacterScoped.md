# Destiny.Artifacts.DestinyArtifactCharacterScoped

## Entity Information
- **Entity Name**: Destiny.Artifacts.DestinyArtifactCharacterScoped
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyartifactcharacterscoped data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| artifactHash | integer (uint32) |  | No |
| pointsUsed | integer (int32) |  | No |
| resetCount | integer (int32) |  | No |
| tiers | Array[Destiny.Artifacts.DestinyArtifactTier] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Artifacts.DestinyArtifactCharacterScoped object
const example = {
  artifactHash: 123,
  pointsUsed: 123,
  resetCount: 123,
  tiers: [],
};
```

### Python
```python
# Example Destiny.Artifacts.DestinyArtifactCharacterScoped object
example = {
    "artifactHash": 123,
    "pointsUsed": 123,
    "resetCount": 123,
    "tiers": [],
}
```

## Related Entities
- **Destiny.Artifacts.DestinyArtifactTier**: Referenced in this entity
- **Destiny.Definitions.Artifacts.DestinyArtifactDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Artifacts.DestinyArtifactCharacterScoped":   {
      "type": "object",
      "properties": {
          "artifactHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Artifacts.DestinyArtifactDefinition"
              }
          },
          "pointsUsed": {
              "format": "int32",
              "type": "integer"
          },
          "resetCount": {
              "format": "int32",
              "type": "integer"
          },
          "tiers": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Artifacts.DestinyArtifactTier"
              }
          }
      }
  }
}
```
