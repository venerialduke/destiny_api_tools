# Destiny.Components.Records.DestinyRecordsComponent

## Entity Information
- **Entity Name**: Destiny.Components.Records.DestinyRecordsComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyrecordscomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| records | object |  | No |
| recordCategoriesRootNodeHash | integer (uint32) | The hash for the root presentation node definition of Triumph categories. | No |
| recordSealsRootNodeHash | integer (uint32) | The hash for the root presentation node definition of Triumph Seals. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Records.DestinyRecordsComponent object
const example = {
  records: null,
  recordCategoriesRootNodeHash: 123,
  recordSealsRootNodeHash: 123,
};
```

### Python
```python
# Example Destiny.Components.Records.DestinyRecordsComponent object
example = {
    "records": None,
    "recordCategoriesRootNodeHash": 123,
    "recordSealsRootNodeHash": 123,
}
```

## Related Entities
- **Destiny.Components.Records.DestinyRecordComponent**: Referenced in this entity
- **Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Records.DestinyRecordsComponent":   {
      "type": "object",
      "properties": {
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
