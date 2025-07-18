# Destiny.Definitions.Reporting.DestinyReportReasonCategoryDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Reporting.DestinyReportReasonCategoryDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
If you're going to report someone for a Terms of Service violation, you need to choose a category and reason for the report. This definition holds both the categories and the reasons within those categories, for simplicity and my own laziness' sake.
Note tha this means that, to refer to a Reason by reasonHash, you need a combination of the reasonHash *and* the associated ReasonCategory's hash: there are some reasons defined under multiple categories.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| reasons | object | The specific reasons for the report under this category. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Reporting.DestinyReportReasonCategoryDefinition object
const example = {
  displayProperties: null,
  reasons: null,
  hash: 123,
  index: 123,
  redacted: true,
};
```

### Python
```python
# Example Destiny.Definitions.Reporting.DestinyReportReasonCategoryDefinition object
example = {
    "displayProperties": None,
    "reasons": None,
    "hash": 123,
    "index": 123,
    "redacted": True,
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.Reporting.DestinyReportReasonDefinition**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Reporting.DestinyReportReasonCategoryDefinition":   {
      "description": "If you're going to report someone for a Terms of Service violation, you need to choose a category and reason for the report. This definition holds both the categories and the reasons within those categories, for simplicity and my own laziness' sake.\r\nNote tha this means that, to refer to a Reason by reasonHash, you need a combination of the reasonHash *and* the associated ReasonCategory's hash: there are some reasons defined under multiple categories.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "reasons": {
              "description": "The specific reasons for the report under this category.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.Definitions.Reporting.DestinyReportReasonDefinition"
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
      "x-mobile-manifest-name": "ReportReasonCategories"
  }
}
```
