# Social.Friends.BungieFriendListResponse

## Entity Information
- **Entity Name**: Social.Friends.BungieFriendListResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for bungiefriendlistresponse operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| friends | Array[Social.Friends.BungieFriend] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Social.Friends.BungieFriendListResponse object
const example = {
  friends: [],
};
```

### Python
```python
# Example Social.Friends.BungieFriendListResponse object
example = {
    "friends": [],
}
```

## Related Entities
- **Social.Friends.BungieFriend**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Social.Friends.BungieFriendListResponse":   {
      "type": "object",
      "properties": {
          "friends": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Social.Friends.BungieFriend"
              }
          }
      }
  }
}
```
