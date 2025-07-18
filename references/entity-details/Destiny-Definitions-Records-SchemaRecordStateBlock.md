# Destiny.Definitions.Records.SchemaRecordStateBlock

## Entity Information
- **Entity Name**: Destiny.Definitions.Records.SchemaRecordStateBlock
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing schemarecordstateblock data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| featuredPriority | integer (int32) |  | No |
| obscuredName | string | A display name override to show when this record is 'obscured' instead of the default obscured display name. | No |
| obscuredDescription | string | A display description override to show when this record is 'obscured' instead of the default obscured display description. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Records.SchemaRecordStateBlock object
const example = {
  featuredPriority: 123,
  obscuredName: "example value",
  obscuredDescription: "example value",
};
```

### Python
```python
# Example Destiny.Definitions.Records.SchemaRecordStateBlock object
example = {
    "featuredPriority": 123,
    "obscuredName": "example value",
    "obscuredDescription": "example value",
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Records.SchemaRecordStateBlock":   {
      "type": "object",
      "properties": {
          "featuredPriority": {
              "format": "int32",
              "type": "integer"
          },
          "obscuredName": {
              "description": "A display name override to show when this record is 'obscured' instead of the default obscured display name.",
              "type": "string"
          },
          "obscuredDescription": {
              "description": "A display description override to show when this record is 'obscured' instead of the default obscured display description.",
              "type": "string"
          }
      }
  }
}
```
