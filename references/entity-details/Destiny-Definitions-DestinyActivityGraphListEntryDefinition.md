# Destiny.Definitions.DestinyActivityGraphListEntryDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyActivityGraphListEntryDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destinations and Activities may have default Activity Graphs that should be shown when you bring up the Director and are playing in either.
This contract defines the graph referred to and the gating for when it is relevant.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| activityGraphHash | integer (uint32) | The hash identifier of the DestinyActivityGraphDefinition that should be shown when opening the director. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyActivityGraphListEntryDefinition object
const example = {
  activityGraphHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyActivityGraphListEntryDefinition object
example = {
    "activityGraphHash": 123,
}
```

## Related Entities
- **Destiny.Definitions.Director.DestinyActivityGraphDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyActivityGraphListEntryDefinition":   {
      "description": "Destinations and Activities may have default Activity Graphs that should be shown when you bring up the Director and are playing in either.\r\nThis contract defines the graph referred to and the gating for when it is relevant.",
      "type": "object",
      "properties": {
          "activityGraphHash": {
              "format": "uint32",
              "description": "The hash identifier of the DestinyActivityGraphDefinition that should be shown when opening the director.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Director.DestinyActivityGraphDefinition"
              }
          }
      }
  }
}
```
