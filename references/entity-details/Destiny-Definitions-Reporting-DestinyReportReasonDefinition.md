# Destiny.Definitions.Reporting.DestinyReportReasonDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Reporting.DestinyReportReasonDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
A specific reason for being banned. Only accessible under the related category (DestinyReportReasonCategoryDefinition) under which it is shown. Note that this means that report reasons' reasonHash are not globally unique: and indeed, entries like "Other" are defined under most categories for example.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| reasonHash | integer (uint32) | The identifier for the reason: they are only guaranteed unique under the Category in which they are found. | No |
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Reporting.DestinyReportReasonDefinition object
const example = {
  reasonHash: 123,
  displayProperties: null,
};
```

### Python
```python
# Example Destiny.Definitions.Reporting.DestinyReportReasonDefinition object
example = {
    "reasonHash": 123,
    "displayProperties": None,
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Reporting.DestinyReportReasonDefinition":   {
      "description": "A specific reason for being banned. Only accessible under the related category (DestinyReportReasonCategoryDefinition) under which it is shown. Note that this means that report reasons' reasonHash are not globally unique: and indeed, entries like \"Other\" are defined under most categories for example.",
      "type": "object",
      "properties": {
          "reasonHash": {
              "format": "uint32",
              "description": "The identifier for the reason: they are only guaranteed unique under the Category in which they are found.",
              "type": "integer"
          },
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          }
      }
  }
}
```
