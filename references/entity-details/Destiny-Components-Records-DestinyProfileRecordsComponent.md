# Destiny.Components.Records.DestinyProfileRecordsComponent

## Entity Information
- **Entity Name**: Destiny.Components.Records.DestinyProfileRecordsComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyprofilerecordscomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| score | integer (int32) | Your 'active' Triumphs score, maintained for backwards compatibility. | No |
| activeScore | integer (int32) | Your 'active' Triumphs score. | No |
| legacyScore | integer (int32) | Your 'legacy' Triumphs score. | No |
| lifetimeScore | integer (int32) | Your 'lifetime' Triumphs score. | No |
| trackedRecordHash | integer (uint32) | If this profile is tracking a record, this is the hash identifier of the record it is tracking. | No |
| records | object |  | No |
| recordCategoriesRootNodeHash | integer (uint32) | The hash for the root presentation node definition of Triumph categories. | No |
| recordSealsRootNodeHash | integer (uint32) | The hash for the root presentation node definition of Triumph Seals. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Records.DestinyProfileRecordsComponent object
const example = {
  score: 123,
  activeScore: 123,
  legacyScore: 123,
  lifetimeScore: 123,
  trackedRecordHash: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Components.Records.DestinyProfileRecordsComponent object
example = {
    "score": 123,
    "activeScore": 123,
    "legacyScore": 123,
    "lifetimeScore": 123,
    "trackedRecordHash": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Components.Records.DestinyRecordComponent**: Referenced in this entity
- **Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition**: Referenced in this entity
- **Destiny.Definitions.Records.DestinyRecordDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Records.DestinyProfileRecordsComponent":   {
      "type": "object",
      "properties": {
          "score": {
              "format": "int32",
              "description": "Your 'active' Triumphs score, maintained for backwards compatibility.",
              "type": "integer"
          },
          "activeScore": {
              "format": "int32",
              "description": "Your 'active' Triumphs score.",
              "type": "integer"
          },
          "legacyScore": {
              "format": "int32",
              "description": "Your 'legacy' Triumphs score.",
              "type": "integer"
          },
          "lifetimeScore": {
              "format": "int32",
              "description": "Your 'lifetime' Triumphs score.",
              "type": "integer"
          },
          "trackedRecordHash": {
              "format": "uint32",
              "description": "If this profile is tracking a record, this is the hash identifier of the record it is tracking.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Records.DestinyRecordDefinition"
              }
          },
          "records": {
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.Components.Records.DestinyRecordComponent"
              }
          },
          "recordCategoriesRootNodeHash": {
              "format": "uint32",
              "description": "The hash for the root presentation node definition of Triumph categories.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
              }
          },
          "recordSealsRootNodeHash": {
              "format": "uint32",
              "description": "The hash for the root presentation node definition of Triumph Seals.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
              }
          }
      },
      "x-destiny-component-type-dependency": "Records"
  }
}
```
