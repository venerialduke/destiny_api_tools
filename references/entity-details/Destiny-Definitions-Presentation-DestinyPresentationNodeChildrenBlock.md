# Destiny.Definitions.Presentation.DestinyPresentationNodeChildrenBlock

## Entity Information
- **Entity Name**: Destiny.Definitions.Presentation.DestinyPresentationNodeChildrenBlock
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
As/if presentation nodes begin to host more entities as children, these lists will be added to. One list property exists per type of entity that can be treated as a child of this presentation node, and each holds the identifier of the entity and any associated information needed to display the UI for that entity (if anything)

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| presentationNodes | Array[Destiny.Definitions.Presentation.DestinyPresentationNodeChildEntry] |  | No |
| collectibles | Array[Destiny.Definitions.Presentation.DestinyPresentationNodeCollectibleChildEntry] |  | No |
| records | Array[Destiny.Definitions.Presentation.DestinyPresentationNodeRecordChildEntry] |  | No |
| metrics | Array[Destiny.Definitions.Presentation.DestinyPresentationNodeMetricChildEntry] |  | No |
| craftables | Array[Destiny.Definitions.Presentation.DestinyPresentationNodeCraftableChildEntry] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Presentation.DestinyPresentationNodeChildrenBlock object
const example = {
  presentationNodes: [],
  collectibles: [],
  records: [],
  metrics: [],
  craftables: [],
};
```

### Python
```python
# Example Destiny.Definitions.Presentation.DestinyPresentationNodeChildrenBlock object
example = {
    "presentationNodes": [],
    "collectibles": [],
    "records": [],
    "metrics": [],
    "craftables": [],
}
```

## Related Entities
- **Destiny.Definitions.Presentation.DestinyPresentationNodeChildEntry**: Referenced in this entity
- **Destiny.Definitions.Presentation.DestinyPresentationNodeCollectibleChildEntry**: Referenced in this entity
- **Destiny.Definitions.Presentation.DestinyPresentationNodeCraftableChildEntry**: Referenced in this entity
- **Destiny.Definitions.Presentation.DestinyPresentationNodeMetricChildEntry**: Referenced in this entity
- **Destiny.Definitions.Presentation.DestinyPresentationNodeRecordChildEntry**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Presentation.DestinyPresentationNodeChildrenBlock":   {
      "description": "As/if presentation nodes begin to host more entities as children, these lists will be added to. One list property exists per type of entity that can be treated as a child of this presentation node, and each holds the identifier of the entity and any associated information needed to display the UI for that entity (if anything)",
      "type": "object",
      "properties": {
          "presentationNodes": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeChildEntry"
              }
          },
          "collectibles": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeCollectibleChildEntry"
              }
          },
          "records": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeRecordChildEntry"
              }
          },
          "metrics": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeMetricChildEntry"
              }
          },
          "craftables": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeCraftableChildEntry"
              }
          }
      }
  }
}
```
