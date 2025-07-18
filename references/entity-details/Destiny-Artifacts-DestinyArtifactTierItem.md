# Destiny.Artifacts.DestinyArtifactTierItem

## Entity Information
- **Entity Name**: Destiny.Artifacts.DestinyArtifactTierItem
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyartifacttieritem data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| itemHash | integer (uint32) |  | No |
| isActive | boolean |  | No |
| isVisible | boolean |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Artifacts.DestinyArtifactTierItem object
const example = {
  itemHash: 123,
  isActive: true,
  isVisible: true,
};
```

### Python
```python
# Example Destiny.Artifacts.DestinyArtifactTierItem object
example = {
    "itemHash": 123,
    "isActive": True,
    "isVisible": True,
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Artifacts.DestinyArtifactTierItem":   {
      "type": "object",
      "properties": {
          "itemHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "isActive": {
              "type": "boolean"
          },
          "isVisible": {
              "type": "boolean"
          }
      }
  }
}
```
