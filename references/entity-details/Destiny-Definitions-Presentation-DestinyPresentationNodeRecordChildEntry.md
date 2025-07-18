# Destiny.Definitions.Presentation.DestinyPresentationNodeRecordChildEntry

## Entity Information
- **Entity Name**: Destiny.Definitions.Presentation.DestinyPresentationNodeRecordChildEntry
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinypresentationnoderecordchildentry data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| recordHash | integer (uint32) |  | No |
| nodeDisplayPriority | integer (uint32) | Use this value to sort the presentation node children in ascending order. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Presentation.DestinyPresentationNodeRecordChildEntry object
const example = {
  recordHash: 123,
  nodeDisplayPriority: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Presentation.DestinyPresentationNodeRecordChildEntry object
example = {
    "recordHash": 123,
    "nodeDisplayPriority": 123,
}
```

## Related Entities
- **Destiny.Definitions.Records.DestinyRecordDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Presentation.DestinyPresentationNodeRecordChildEntry":   {
      "type": "object",
      "properties": {
          "recordHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Records.DestinyRecordDefinition"
              }
          },
          "nodeDisplayPriority": {
              "format": "uint32",
              "description": "Use this value to sort the presentation node children in ascending order.",
              "type": "integer"
          }
      }
  }
}
```
