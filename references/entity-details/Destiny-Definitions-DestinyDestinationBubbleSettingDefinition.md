# Destiny.Definitions.DestinyDestinationBubbleSettingDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyDestinationBubbleSettingDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Human readable data about the bubble. Combine with DestinyBubbleDefinition - see DestinyDestinationDefinition.bubbleSettings for more information.
DEPRECATED - Just use bubbles.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyDestinationBubbleSettingDefinition object
const example = {
  displayProperties: null,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyDestinationBubbleSettingDefinition object
example = {
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
  "Destiny.Definitions.DestinyDestinationBubbleSettingDefinition":   {
      "description": "Human readable data about the bubble. Combine with DestinyBubbleDefinition - see DestinyDestinationDefinition.bubbleSettings for more information.\r\nDEPRECATED - Just use bubbles.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          }
      }
  }
}
```
