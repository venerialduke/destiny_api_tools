# Social.Friends.BungieFriendRequestListResponse

## Entity Information
- **Entity Name**: Social.Friends.BungieFriendRequestListResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for bungiefriendrequestlistresponse operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| incomingRequests | Array[Social.Friends.BungieFriend] |  | No |
| outgoingRequests | Array[Social.Friends.BungieFriend] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Social.Friends.BungieFriendRequestListResponse object
const example = {
  incomingRequests: [],
  outgoingRequests: [],
};
```

### Python
```python
# Example Social.Friends.BungieFriendRequestListResponse object
example = {
    "incomingRequests": [],
    "outgoingRequests": [],
}
```

## Related Entities
- **Social.Friends.BungieFriend**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Social.Friends.BungieFriendRequestListResponse":   {
      "type": "object",
      "properties": {
          "incomingRequests": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Social.Friends.BungieFriend"
              }
          },
          "outgoingRequests": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Social.Friends.BungieFriend"
              }
          }
      }
  }
}
```
