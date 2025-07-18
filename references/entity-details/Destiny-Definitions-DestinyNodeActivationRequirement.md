# Destiny.Definitions.DestinyNodeActivationRequirement

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyNodeActivationRequirement
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Talent nodes have requirements that must be met before they can be activated.
This describes the material costs, the Level of the Talent Grid's progression required, and other conditional information that limits whether a talent node can be activated.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| gridLevel | integer (int32) | The Progression level on the Talent Grid required to activate this node.
See DestinyTalentGridDefinition.progressionHash for the related Progression, and read DestinyProgressionDefinition's documentation to learn more about Progressions. | No |
| materialRequirementHashes | Array[integer] | The list of hash identifiers for material requirement sets: materials that are required for the node to be activated. See DestinyMaterialRequirementSetDefinition for more information about material requirements.
In this case, only a single DestinyMaterialRequirementSetDefinition will be chosen from this list, and we won't know which one will be chosen until an instance of the item is created. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyNodeActivationRequirement object
const example = {
  gridLevel: 123,
  materialRequirementHashes: [],
};
```

### Python
```python
# Example Destiny.Definitions.DestinyNodeActivationRequirement object
example = {
    "gridLevel": 123,
    "materialRequirementHashes": [],
}
```

## Related Entities
- **Destiny.Definitions.DestinyMaterialRequirementSetDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyNodeActivationRequirement":   {
      "description": "Talent nodes have requirements that must be met before they can be activated.\r\nThis describes the material costs, the Level of the Talent Grid's progression required, and other conditional information that limits whether a talent node can be activated.",
      "type": "object",
      "properties": {
          "gridLevel": {
              "format": "int32",
              "description": "The Progression level on the Talent Grid required to activate this node.\r\nSee DestinyTalentGridDefinition.progressionHash for the related Progression, and read DestinyProgressionDefinition's documentation to learn more about Progressions.",
              "type": "integer"
          },
          "materialRequirementHashes": {
              "description": "The list of hash identifiers for material requirement sets: materials that are required for the node to be activated. See DestinyMaterialRequirementSetDefinition for more information about material requirements.\r\nIn this case, only a single DestinyMaterialRequirementSetDefinition will be chosen from this list, and we won't know which one will be chosen until an instance of the item is created.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyMaterialRequirementSetDefinition"
              }
          }
      }
  }
}
```
