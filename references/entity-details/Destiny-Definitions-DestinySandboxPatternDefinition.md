# Destiny.Definitions.DestinySandboxPatternDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinySandboxPatternDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Destiny API entity representing destinysandboxpatterndefinition data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| patternHash | integer (uint32) |  | No |
| patternGlobalTagIdHash | integer (uint32) |  | No |
| weaponContentGroupHash | integer (uint32) |  | No |
| weaponTranslationGroupHash | integer (uint32) |  | No |
| weaponTypeHash | integer (uint32) |  | No |
| weaponType | integer (int32) |  | No |
| filters | Array[Destiny.Definitions.DestinyArrangementRegionFilterDefinition] |  | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinySandboxPatternDefinition object
const example = {
  patternHash: 123,
  patternGlobalTagIdHash: 123,
  weaponContentGroupHash: 123,
  weaponTranslationGroupHash: 123,
  weaponTypeHash: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.DestinySandboxPatternDefinition object
example = {
    "patternHash": 123,
    "patternGlobalTagIdHash": 123,
    "weaponContentGroupHash": 123,
    "weaponTranslationGroupHash": 123,
    "weaponTypeHash": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyArrangementRegionFilterDefinition**: Referenced in this entity
- **Destiny.DestinyItemSubType**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinySandboxPatternDefinition":   {
      "type": "object",
      "properties": {
          "patternHash": {
              "format": "uint32",
              "type": "integer"
          },
          "patternGlobalTagIdHash": {
              "format": "uint32",
              "type": "integer"
          },
          "weaponContentGroupHash": {
              "format": "uint32",
              "type": "integer"
          },
          "weaponTranslationGroupHash": {
              "format": "uint32",
              "type": "integer"
          },
          "weaponTypeHash": {
              "format": "uint32",
              "type": "integer"
          },
          "weaponType": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyItemSubType"
              }
          },
          "filters": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyArrangementRegionFilterDefinition"
              }
          },
          "hash": {
              "format": "uint32",
              "description": "The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.\r\nWhen entities refer to each other in Destiny content, it is this hash that they are referring to.",
              "type": "integer"
          },
          "index": {
              "format": "int32",
              "description": "The index of the entity as it was found in the investment tables.",
              "type": "integer"
          },
          "redacted": {
              "description": "If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!",
              "type": "boolean"
          }
      },
      "x-mobile-manifest-name": "SandboxPatterns"
  }
}
```
