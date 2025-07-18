# Destiny.Definitions.DestinyItemMetricBlockDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyItemMetricBlockDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The metrics available for display and selection on an item.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| availableMetricCategoryNodeHashes | Array[integer] | Hash identifiers for any DestinyPresentationNodeDefinition entry that can be used to list available metrics. Any metric listed directly below these nodes, or in any of these nodes' children will be made available for selection. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyItemMetricBlockDefinition object
const example = {
  availableMetricCategoryNodeHashes: [],
};
```

### Python
```python
# Example Destiny.Definitions.DestinyItemMetricBlockDefinition object
example = {
    "availableMetricCategoryNodeHashes": [],
}
```

## Related Entities
- **Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyItemMetricBlockDefinition":   {
      "description": "The metrics available for display and selection on an item.",
      "type": "object",
      "properties": {
          "availableMetricCategoryNodeHashes": {
              "description": "Hash identifiers for any DestinyPresentationNodeDefinition entry that can be used to list available metrics. Any metric listed directly below these nodes, or in any of these nodes' children will be made available for selection.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
              }
          }
      }
  }
}
```
