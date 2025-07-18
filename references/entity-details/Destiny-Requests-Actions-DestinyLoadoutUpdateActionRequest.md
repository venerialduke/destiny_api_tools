# Destiny.Requests.Actions.DestinyLoadoutUpdateActionRequest

## Entity Information
- **Entity Name**: Destiny.Requests.Actions.DestinyLoadoutUpdateActionRequest
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyloadoutupdateactionrequest data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| colorHash | integer (uint32) |  | No |
| iconHash | integer (uint32) |  | No |
| nameHash | integer (uint32) |  | No |
| loadoutIndex | integer (int32) | The index of the loadout for this action request. | No |
| characterId | integer (int64) |  | No |
| membershipType | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Requests.Actions.DestinyLoadoutUpdateActionRequest object
const example = {
  colorHash: 123,
  iconHash: 123,
  nameHash: 123,
  loadoutIndex: 123,
  characterId: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Requests.Actions.DestinyLoadoutUpdateActionRequest object
example = {
    "colorHash": 123,
    "iconHash": 123,
    "nameHash": 123,
    "loadoutIndex": 123,
    "characterId": 123,
    # ... more properties
}
```

## Related Entities
- **BungieMembershipType**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Requests.Actions.DestinyLoadoutUpdateActionRequest":   {
      "type": "object",
      "properties": {
          "colorHash": {
              "format": "uint32",
              "type": "integer"
          },
          "iconHash": {
              "format": "uint32",
              "type": "integer"
          },
          "nameHash": {
              "format": "uint32",
              "type": "integer"
          },
          "loadoutIndex": {
              "format": "int32",
              "description": "The index of the loadout for this action request.",
              "type": "integer"
          },
          "characterId": {
              "format": "int64",
              "type": "integer"
          },
          "membershipType": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/BungieMembershipType"
              }
          }
      }
  }
}
```
