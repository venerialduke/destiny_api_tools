# Destiny.Definitions.Presentation.DestinyPresentationChildBlock

## Entity Information
- **Entity Name**: Destiny.Definitions.Presentation.DestinyPresentationChildBlock
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinypresentationchildblock data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| presentationNodeType | integer (int32) |  | No |
| parentPresentationNodeHashes | Array[integer] |  | No |
| displayStyle | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Presentation.DestinyPresentationChildBlock object
const example = {
  presentationNodeType: 123,
  parentPresentationNodeHashes: [],
  displayStyle: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Presentation.DestinyPresentationChildBlock object
example = {
    "presentationNodeType": 123,
    "parentPresentationNodeHashes": [],
    "displayStyle": 123,
}
```

## Related Entities
- **Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition**: Referenced in this entity
- **Destiny.DestinyPresentationDisplayStyle**: Referenced in this entity
- **Destiny.DestinyPresentationNodeType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Presentation.DestinyPresentationChildBlock":   {
      "type": "object",
      "properties": {
          "presentationNodeType": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyPresentationNodeType"
              }
          },
          "parentPresentationNodeHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
              }
          },
          "displayStyle": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.DestinyPresentationDisplayStyle"
              }
          }
      }
  }
}
```
