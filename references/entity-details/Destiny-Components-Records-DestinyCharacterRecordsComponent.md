# Destiny.Components.Records.DestinyCharacterRecordsComponent

## Entity Information
- **Entity Name**: Destiny.Components.Records.DestinyCharacterRecordsComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinycharacterrecordscomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| featuredRecordHashes | Array[integer] |  | No |
| records | object |  | No |
| recordCategoriesRootNodeHash | integer (uint32) | The hash for the root presentation node definition of Triumph categories. | No |
| recordSealsRootNodeHash | integer (uint32) | The hash for the root presentation node definition of Triumph Seals. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Records.DestinyCharacterRecordsComponent object
const example = {
  featuredRecordHashes: [],
  records: null,
  recordCategoriesRootNodeHash: 123,
  recordSealsRootNodeHash: 123,
};
```

### Python
```python
# Example Destiny.Components.Records.DestinyCharacterRecordsComponent object
example = {
    "featuredRecordHashes": [],
    "records": None,
    "recordCategoriesRootNodeHash": 123,
    "recordSealsRootNodeHash": 123,
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
  "Destiny.Components.Records.DestinyCharacterRecordsComponent":   {
      "type": "object",
      "properties": {
          "featuredRecordHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
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
