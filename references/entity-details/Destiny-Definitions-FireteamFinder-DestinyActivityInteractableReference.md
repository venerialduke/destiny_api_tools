# Destiny.Definitions.FireteamFinder.DestinyActivityInteractableReference

## Entity Information
- **Entity Name**: Destiny.Definitions.FireteamFinder.DestinyActivityInteractableReference
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyactivityinteractablereference data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| activityInteractableHash | integer (uint32) |  | No |
| activityInteractableElementIndex | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.FireteamFinder.DestinyActivityInteractableReference object
const example = {
  activityInteractableHash: 123,
  activityInteractableElementIndex: 123,
};
```

### Python
```python
# Example Destiny.Definitions.FireteamFinder.DestinyActivityInteractableReference object
example = {
    "activityInteractableHash": 123,
    "activityInteractableElementIndex": 123,
}
```

## Related Entities
- **Destiny.Definitions.Activities.DestinyActivityInteractableDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.FireteamFinder.DestinyActivityInteractableReference":   {
      "type": "object",
      "properties": {
          "activityInteractableHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Activities.DestinyActivityInteractableDefinition"
              }
          },
          "activityInteractableElementIndex": {
              "format": "int32",
              "type": "integer"
          }
      }
  }
}
```
