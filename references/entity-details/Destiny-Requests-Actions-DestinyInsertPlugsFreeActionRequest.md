# Destiny.Requests.Actions.DestinyInsertPlugsFreeActionRequest

## Entity Information
- **Entity Name**: Destiny.Requests.Actions.DestinyInsertPlugsFreeActionRequest
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyinsertplugsfreeactionrequest data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| plug | object | The plugs being inserted. | No |
| itemId | integer (int64) | The instance ID of the item for this action request. | No |
| characterId | integer (int64) |  | No |
| membershipType | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Requests.Actions.DestinyInsertPlugsFreeActionRequest object
const example = {
  plug: null,
  itemId: 123,
  characterId: 123,
  membershipType: 123,
};
```

### Python
```python
# Example Destiny.Requests.Actions.DestinyInsertPlugsFreeActionRequest object
example = {
    "plug": None,
    "itemId": 123,
    "characterId": 123,
    "membershipType": 123,
}
```

## Related Entities
- **BungieMembershipType**: Referenced in this entity
- **Destiny.Requests.Actions.DestinyInsertPlugsRequestEntry**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Requests.Actions.DestinyInsertPlugsFreeActionRequest":   {
      "type": "object",
      "properties": {
          "plug": {
              "description": "The plugs being inserted.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Requests.Actions.DestinyInsertPlugsRequestEntry"
                  }
              ]
          },
          "itemId": {
              "format": "int64",
              "description": "The instance ID of the item for this action request.",
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
