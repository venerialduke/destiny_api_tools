# Destiny.Requests.Actions.DestinyLoadoutActionRequest

## Entity Information
- **Entity Name**: Destiny.Requests.Actions.DestinyLoadoutActionRequest
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyloadoutactionrequest data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| loadoutIndex | integer (int32) | The index of the loadout for this action request. | No |
| characterId | integer (int64) |  | No |
| membershipType | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Requests.Actions.DestinyLoadoutActionRequest object
const example = {
  loadoutIndex: 123,
  characterId: 123,
  membershipType: 123,
};
```

### Python
```python
# Example Destiny.Requests.Actions.DestinyLoadoutActionRequest object
example = {
    "loadoutIndex": 123,
    "characterId": 123,
    "membershipType": 123,
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
  "Destiny.Requests.Actions.DestinyLoadoutActionRequest":   {
      "type": "object",
      "properties": {
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
