# Destiny.Definitions.Artifacts.DestinyArtifactTierItemDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Artifacts.DestinyArtifactTierItemDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyartifacttieritemdefinition data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| itemHash | integer (uint32) | The identifier of the Plug Item unlocked by activating this item in the Artifact. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Artifacts.DestinyArtifactTierItemDefinition object
const example = {
  itemHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Artifacts.DestinyArtifactTierItemDefinition object
example = {
    "itemHash": 123,
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
  "Destiny.Definitions.Artifacts.DestinyArtifactTierItemDefinition":   {
      "type": "object",
      "properties": {
          "itemHash": {
              "format": "uint32",
              "description": "The identifier of the Plug Item unlocked by activating this item in the Artifact.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          }
      }
  }
}
```
