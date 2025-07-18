# Destiny.Definitions.DestinyBubbleDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyBubbleDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Basic identifying data about the bubble. Combine with DestinyDestinationBubbleSettingDefinition - see DestinyDestinationDefinition.bubbleSettings for more information.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| hash | integer (uint32) | The identifier for the bubble: only guaranteed to be unique within the Destination. | No |
| displayProperties | object | The display properties of this bubble, so you don't have to look them up in a separate list anymore. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyBubbleDefinition object
const example = {
  hash: 123,
  displayProperties: null,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyBubbleDefinition object
example = {
    "hash": 123,
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
  "Destiny.Definitions.DestinyBubbleDefinition":   {
      "description": "Basic identifying data about the bubble. Combine with DestinyDestinationBubbleSettingDefinition - see DestinyDestinationDefinition.bubbleSettings for more information.",
      "type": "object",
      "properties": {
          "hash": {
              "format": "uint32",
              "description": "The identifier for the bubble: only guaranteed to be unique within the Destination.",
              "type": "integer"
          },
          "displayProperties": {
              "description": "The display properties of this bubble, so you don't have to look them up in a separate list anymore.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
                  }
              ]
          }
      }
  }
}
```
