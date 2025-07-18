# Destiny.Definitions.Director.DestinyLinkedGraphDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Director.DestinyLinkedGraphDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
This describes links between the current graph and others, as well as when that link is relevant.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| description | string |  | No |
| name | string |  | No |
| unlockExpression | Destiny.Definitions.DestinyUnlockExpressionDefinition |  | No |
| linkedGraphId | integer (uint32) |  | No |
| linkedGraphs | Array[Destiny.Definitions.Director.DestinyLinkedGraphEntryDefinition] |  | No |
| overview | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Director.DestinyLinkedGraphDefinition object
const example = {
  description: "example value",
  name: "example value",
  unlockExpression: null,
  linkedGraphId: 123,
  linkedGraphs: [],
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Director.DestinyLinkedGraphDefinition object
example = {
    "description": "example value",
    "name": "example value",
    "unlockExpression": None,
    "linkedGraphId": 123,
    "linkedGraphs": [],
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyUnlockExpressionDefinition**: Referenced in this entity
- **Destiny.Definitions.Director.DestinyLinkedGraphEntryDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Director.DestinyLinkedGraphDefinition":   {
      "description": "This describes links between the current graph and others, as well as when that link is relevant.",
      "type": "object",
      "properties": {
          "description": {
              "type": "string"
          },
          "name": {
              "type": "string"
          },
          "unlockExpression": {
              "$ref": "#/definitions/Destiny.Definitions.DestinyUnlockExpressionDefinition"
          },
          "linkedGraphId": {
              "format": "uint32",
              "type": "integer"
          },
          "linkedGraphs": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Director.DestinyLinkedGraphEntryDefinition"
              }
          },
          "overview": {
              "type": "string"
          }
      }
  }
}
```
