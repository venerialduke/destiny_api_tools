# Destiny.Definitions.Records.DestinyRecordTitleBlock

## Entity Information
- **Entity Name**: Destiny.Definitions.Records.DestinyRecordTitleBlock
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyrecordtitleblock data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| hasTitle | boolean |  | No |
| titlesByGender | object |  | No |
| titlesByGenderHash | object | For those who prefer to use the definitions. | No |
| gildingTrackingRecordHash | integer (uint32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Records.DestinyRecordTitleBlock object
const example = {
  hasTitle: true,
  titlesByGender: null,
  titlesByGenderHash: null,
  gildingTrackingRecordHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Records.DestinyRecordTitleBlock object
example = {
    "hasTitle": True,
    "titlesByGender": None,
    "titlesByGenderHash": None,
    "gildingTrackingRecordHash": 123,
}
```

## Related Entities
- **Destiny.Definitions.DestinyGenderDefinition**: Referenced in this entity
- **Destiny.Definitions.Records.DestinyRecordDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Records.DestinyRecordTitleBlock":   {
      "type": "object",
      "properties": {
          "hasTitle": {
              "type": "boolean"
          },
          "titlesByGender": {
              "type": "object",
              "additionalProperties": {
                  "type": "string"
              }
          },
          "titlesByGenderHash": {
              "description": "For those who prefer to use the definitions.",
              "type": "object",
              "additionalProperties": {
                  "type": "string"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyGenderDefinition"
              }
          },
          "gildingTrackingRecordHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Records.DestinyRecordDefinition"
              }
          }
      }
  }
}
```
