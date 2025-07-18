# Destiny.Definitions.DestinyItemTranslationBlockDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemTranslationBlockDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
This Block defines the rendering data associated with the item, if any.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| weaponPatternIdentifier | string |  | No |
| weaponPatternHash | integer (uint32) |  | No |
| defaultDyes | Array[Destiny.DyeReference] |  | No |
| lockedDyes | Array[Destiny.DyeReference] |  | No |
| customDyes | Array[Destiny.DyeReference] |  | No |
| arrangements | Array[Destiny.Definitions.DestinyGearArtArrangementReference] |  | No |
| hasGeometry | boolean |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemTranslationBlockDefinition object
const example = {
  weaponPatternIdentifier: "example value",
  weaponPatternHash: 123,
  defaultDyes: [],
  lockedDyes: [],
  customDyes: [],
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemTranslationBlockDefinition object
example = {
    "weaponPatternIdentifier": "example value",
    "weaponPatternHash": 123,
    "defaultDyes": [],
    "lockedDyes": [],
    "customDyes": [],
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyGearArtArrangementReference**: Referenced in this entity
- **Destiny.Definitions.DestinySandboxPatternDefinition**: Referenced in this entity
- **Destiny.DyeReference**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyItemTranslationBlockDefinition":   {
      "description": "This Block defines the rendering data associated with the item, if any.",
      "type": "object",
      "properties": {
          "weaponPatternIdentifier": {
              "type": "string"
          },
          "weaponPatternHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinySandboxPatternDefinition"
              }
          },
          "defaultDyes": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.DyeReference"
              }
          },
          "lockedDyes": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.DyeReference"
              }
          },
          "customDyes": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.DyeReference"
              }
          },
          "arrangements": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyGearArtArrangementReference"
              }
          },
          "hasGeometry": {
              "type": "boolean"
          }
      }
  }
}
```
