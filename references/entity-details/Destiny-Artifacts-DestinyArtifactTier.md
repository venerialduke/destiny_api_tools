# Destiny.Artifacts.DestinyArtifactTier

## Entity Information
- **Entity Name**: Destiny.Artifacts.DestinyArtifactTier
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyartifacttier data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| tierHash | integer (uint32) |  | No |
| isUnlocked | boolean |  | No |
| pointsToUnlock | integer (int32) |  | No |
| items | Array[Destiny.Artifacts.DestinyArtifactTierItem] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Artifacts.DestinyArtifactTier object
const example = {
  tierHash: 123,
  isUnlocked: true,
  pointsToUnlock: 123,
  items: [],
};
```

### Python
```python
# Example Destiny.Artifacts.DestinyArtifactTier object
example = {
    "tierHash": 123,
    "isUnlocked": True,
    "pointsToUnlock": 123,
    "items": [],
}
```

## Related Entities
- **Destiny.Artifacts.DestinyArtifactTierItem**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Artifacts.DestinyArtifactTier":   {
      "type": "object",
      "properties": {
          "tierHash": {
              "format": "uint32",
              "type": "integer"
          },
          "isUnlocked": {
              "type": "boolean"
          },
          "pointsToUnlock": {
              "format": "int32",
              "type": "integer"
          },
          "items": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Artifacts.DestinyArtifactTierItem"
              }
          }
      }
  }
}
```
