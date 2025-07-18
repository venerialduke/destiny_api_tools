# Destiny.Definitions.Presentation.DestinyPresentationNodeChildEntryBase

## Entity Information
- **Entity Name**: Destiny.Definitions.Presentation.DestinyPresentationNodeChildEntryBase
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinypresentationnodechildentrybase data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| nodeDisplayPriority | integer (uint32) | Use this value to sort the presentation node children in ascending order. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Presentation.DestinyPresentationNodeChildEntryBase object
const example = {
  nodeDisplayPriority: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Presentation.DestinyPresentationNodeChildEntryBase object
example = {
    "nodeDisplayPriority": 123,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Presentation.DestinyPresentationNodeChildEntryBase":   {
      "type": "object",
      "properties": {
          "nodeDisplayPriority": {
              "format": "uint32",
              "description": "Use this value to sort the presentation node children in ascending order.",
              "type": "integer"
          }
      }
  }
}
```
