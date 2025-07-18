# Destiny.Definitions.DestinyObjectiveDisplayProperties

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyObjectiveDisplayProperties
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyobjectivedisplayproperties data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| activityHash | integer (uint32) | The activity associated with this objective in the context of this item, if any. | No |
| displayOnItemPreviewScreen | boolean | If true, the game shows this objective on item preview screens. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyObjectiveDisplayProperties object
const example = {
  activityHash: 123,
  displayOnItemPreviewScreen: true,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyObjectiveDisplayProperties object
example = {
    "activityHash": 123,
    "displayOnItemPreviewScreen": True,
}
```

## Related Entities
- **Destiny.Definitions.DestinyActivityDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyObjectiveDisplayProperties":   {
      "type": "object",
      "properties": {
          "activityHash": {
              "format": "uint32",
              "description": "The activity associated with this objective in the context of this item, if any.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityDefinition"
              }
          },
          "displayOnItemPreviewScreen": {
              "description": "If true, the game shows this objective on item preview screens.",
              "type": "boolean"
          }
      }
  }
}
```
