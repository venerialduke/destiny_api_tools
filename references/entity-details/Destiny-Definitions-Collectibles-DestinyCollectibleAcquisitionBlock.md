# Destiny.Definitions.Collectibles.DestinyCollectibleAcquisitionBlock

## Entity Information
- **Entity Name**: Destiny.Definitions.Collectibles.DestinyCollectibleAcquisitionBlock
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinycollectibleacquisitionblock data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| acquireMaterialRequirementHash | integer (uint32) |  | No |
| acquireTimestampUnlockValueHash | integer (uint32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Collectibles.DestinyCollectibleAcquisitionBlock object
const example = {
  acquireMaterialRequirementHash: 123,
  acquireTimestampUnlockValueHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Collectibles.DestinyCollectibleAcquisitionBlock object
example = {
    "acquireMaterialRequirementHash": 123,
    "acquireTimestampUnlockValueHash": 123,
}
```

## Related Entities
- **Destiny.Definitions.DestinyMaterialRequirementSetDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyUnlockValueDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Collectibles.DestinyCollectibleAcquisitionBlock":   {
      "type": "object",
      "properties": {
          "acquireMaterialRequirementHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyMaterialRequirementSetDefinition"
              }
          },
          "acquireTimestampUnlockValueHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyUnlockValueDefinition"
              }
          }
      }
  }
}
```
