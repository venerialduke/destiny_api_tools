# Destiny.Definitions.Metrics.DestinyMetricDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Metrics.DestinyMetricDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Destiny API entity representing destinymetricdefinition data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| trackingObjectiveHash | integer (uint32) |  | No |
| lowerValueIsBetter | boolean |  | No |
| presentationNodeType | integer (int32) |  | No |
| traitIds | Array[string] |  | No |
| traitHashes | Array[integer] |  | No |
| parentNodeHashes | Array[integer] | A quick reference to presentation nodes that have this node as a child. Presentation nodes can be parented under multiple parents. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Metrics.DestinyMetricDefinition object
const example = {
  displayProperties: null,
  trackingObjectiveHash: 123,
  lowerValueIsBetter: true,
  presentationNodeType: 123,
  traitIds: [],
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Metrics.DestinyMetricDefinition object
example = {
    "displayProperties": None,
    "trackingObjectiveHash": 123,
    "lowerValueIsBetter": True,
    "presentationNodeType": 123,
    "traitIds": [],
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyObjectiveDefinition**: Referenced in this entity
- **Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition**: Referenced in this entity
- **Destiny.Definitions.Traits.DestinyTraitDefinition**: Referenced in this entity
- **Destiny.DestinyPresentationNodeType**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Metrics.DestinyMetricDefinition":   {
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "trackingObjectiveHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyObjectiveDefinition"
              }
          },
          "lowerValueIsBetter": {
              "type": "boolean"
          },
          "presentationNodeType": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyPresentationNodeType"
              }
          },
          "traitIds": {
              "type": "array",
              "items": {
                  "type": "string"
              }
          },
          "traitHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Traits.DestinyTraitDefinition"
              }
          },
          "parentNodeHashes": {
              "description": "A quick reference to presentation nodes that have this node as a child. Presentation nodes can be parented under multiple parents.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
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
      "x-mobile-manifest-name": "Metrics"
  }
}
```
