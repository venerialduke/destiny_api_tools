# Destiny.Definitions.Director.DestinyActivityGraphArtElementDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Director.DestinyActivityGraphArtElementDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
These Art Elements are meant to represent one-off visual effects overlaid on the map. Currently, we do not have a pipeline to import the assets for these overlays, so this info exists as a placeholder for when such a pipeline exists (if it ever will)

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| position | object | The position on the map of the art element. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Director.DestinyActivityGraphArtElementDefinition object
const example = {
  position: null,
};
```

### Python
```python
# Example Destiny.Definitions.Director.DestinyActivityGraphArtElementDefinition object
example = {
    "position": None,
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyPositionDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Director.DestinyActivityGraphArtElementDefinition":   {
      "description": "These Art Elements are meant to represent one-off visual effects overlaid on the map. Currently, we do not have a pipeline to import the assets for these overlays, so this info exists as a placeholder for when such a pipeline exists (if it ever will)",
      "type": "object",
      "properties": {
          "position": {
              "description": "The position on the map of the art element.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Common.DestinyPositionDefinition"
                  }
              ]
          }
      }
  }
}
```
