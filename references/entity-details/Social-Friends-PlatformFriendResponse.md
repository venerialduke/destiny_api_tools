# Social.Friends.PlatformFriendResponse

## Entity Information
- **Entity Name**: Social.Friends.PlatformFriendResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for platformfriendresponse operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| itemsPerPage | integer (int32) |  | No |
| currentPage | integer (int32) |  | No |
| hasMore | boolean |  | No |
| platformFriends | Array[Social.Friends.PlatformFriend] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Social.Friends.PlatformFriendResponse object
const example = {
  itemsPerPage: 123,
  currentPage: 123,
  hasMore: true,
  platformFriends: [],
};
```

### Python
```python
# Example Social.Friends.PlatformFriendResponse object
example = {
    "itemsPerPage": 123,
    "currentPage": 123,
    "hasMore": True,
    "platformFriends": [],
}
```

## Related Entities
- **Social.Friends.PlatformFriend**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Social.Friends.PlatformFriendResponse":   {
      "type": "object",
      "properties": {
          "itemsPerPage": {
              "format": "int32",
              "type": "integer"
          },
          "currentPage": {
              "format": "int32",
              "type": "integer"
          },
          "hasMore": {
              "type": "boolean"
          },
          "platformFriends": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Social.Friends.PlatformFriend"
              }
          }
      }
  }
}
```
