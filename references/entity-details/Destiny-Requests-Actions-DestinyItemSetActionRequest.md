# Destiny.Requests.Actions.DestinyItemSetActionRequest

## Entity Information
- **Entity Name**: Destiny.Requests.Actions.DestinyItemSetActionRequest
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing destinyitemsetactionrequest data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| itemIds | Array[integer] |  | No |
| characterId | integer (int64) |  | No |
| membershipType | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Requests.Actions.DestinyItemSetActionRequest object
const example = {
  itemIds: [],
  characterId: 123,
  membershipType: 123,
};
```

### Python
```python
# Example Destiny.Requests.Actions.DestinyItemSetActionRequest object
example = {
    "itemIds": [],
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
  "Destiny.Requests.Actions.DestinyItemSetActionRequest":   {
      "type": "object",
      "properties": {
          "itemIds": {
              "type": "array",
              "items": {
                  "format": "int64",
                  "type": "integer"
              }
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
