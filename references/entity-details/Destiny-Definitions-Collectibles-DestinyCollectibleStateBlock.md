# Destiny.Definitions.Collectibles.DestinyCollectibleStateBlock

## Entity Information
- **Entity Name**: Destiny.Definitions.Collectibles.DestinyCollectibleStateBlock
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinycollectiblestateblock data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| obscuredOverrideItemHash | integer (uint32) |  | No |
| requirements | Destiny.Definitions.Presentation.DestinyPresentationNodeRequirementsBlock |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Collectibles.DestinyCollectibleStateBlock object
const example = {
  obscuredOverrideItemHash: 123,
  requirements: null,
};
```

### Python
```python
# Example Destiny.Definitions.Collectibles.DestinyCollectibleStateBlock object
example = {
    "obscuredOverrideItemHash": 123,
    "requirements": None,
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.Presentation.DestinyPresentationNodeRequirementsBlock**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Collectibles.DestinyCollectibleStateBlock":   {
      "type": "object",
      "properties": {
          "obscuredOverrideItemHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "requirements": {
              "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeRequirementsBlock"
          }
      }
  }
}
```
