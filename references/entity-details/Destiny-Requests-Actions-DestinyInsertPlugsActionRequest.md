# Destiny.Requests.Actions.DestinyInsertPlugsActionRequest

## Entity Information
- **Entity Name**: Destiny.Requests.Actions.DestinyInsertPlugsActionRequest
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyinsertplugsactionrequest data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| actionToken | string | Action token provided by the AwaGetActionToken API call. | No |
| itemInstanceId | integer (int64) | The instance ID of the item having a plug inserted. Only instanced items can have sockets. | No |
| plug | object | The plugs being inserted. | No |
| characterId | integer (int64) |  | No |
| membershipType | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Requests.Actions.DestinyInsertPlugsActionRequest object
const example = {
  actionToken: "example value",
  itemInstanceId: 123,
  plug: null,
  characterId: 123,
  membershipType: 123,
};
```

### Python
```python
# Example Destiny.Requests.Actions.DestinyInsertPlugsActionRequest object
example = {
    "actionToken": "example value",
    "itemInstanceId": 123,
    "plug": None,
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
  "Destiny.Requests.Actions.DestinyInsertPlugsActionRequest":   {
      "type": "object",
      "properties": {
          "actionToken": {
              "description": "Action token provided by the AwaGetActionToken API call.",
              "type": "string"
          },
          "itemInstanceId": {
              "format": "int64",
              "description": "The instance ID of the item having a plug inserted. Only instanced items can have sockets.",
              "type": "integer"
          },
          "plug": {
              "description": "The plugs being inserted.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Requests.Actions.DestinyInsertPlugsRequestEntry"
                  }
              ]
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
