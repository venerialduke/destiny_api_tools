# Destiny.Definitions.FireteamFinder.DestinyActivityGraphReference

## Entity Information
- **Entity Name**: Destiny.Definitions.FireteamFinder.DestinyActivityGraphReference
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyactivitygraphreference data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| activityGraphHash | integer (uint32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.FireteamFinder.DestinyActivityGraphReference object
const example = {
  activityGraphHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.FireteamFinder.DestinyActivityGraphReference object
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
  "Destiny.Definitions.FireteamFinder.DestinyActivityGraphReference":   {
      "type": "object",
      "properties": {
          "activityGraphHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Director.DestinyActivityGraphDefinition"
              }
          }
      }
  }
}
```
