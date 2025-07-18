# Destiny.Components.Presentation.DestinyPresentationNodesComponent

## Entity Information
- **Entity Name**: Destiny.Components.Presentation.DestinyPresentationNodesComponent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinypresentationnodescomponent data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| nodes | object |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Components.Presentation.DestinyPresentationNodesComponent object
const example = {
  nodes: null,
};
```

### Python
```python
# Example Destiny.Components.Presentation.DestinyPresentationNodesComponent object
example = {
    "nodes": None,
}
```

## Related Entities
- **Destiny.Components.Presentation.DestinyPresentationNodeComponent**: Referenced in this entity
- **Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Components.Presentation.DestinyPresentationNodesComponent":   {
      "type": "object",
      "properties": {
          "nodes": {
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.Components.Presentation.DestinyPresentationNodeComponent"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
              }
          }
      },
      "x-destiny-component-type-dependency": "PresentationNodes"
  }
}
```
