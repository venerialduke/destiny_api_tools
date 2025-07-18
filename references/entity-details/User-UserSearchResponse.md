# User.UserSearchResponse

## Entity Information
- **Entity Name**: User.UserSearchResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for usersearchresponse operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| searchResults | Array[User.UserSearchResponseDetail] |  | No |
| page | integer (int32) |  | No |
| hasMore | boolean |  | No |

## Usage Examples

### JavaScript
```javascript
// Example User.UserSearchResponse object
const example = {
  searchResults: [],
  page: 123,
  hasMore: true,
};
```

### Python
```python
# Example User.UserSearchResponse object
example = {
    "searchResults": [],
    "page": 123,
    "hasMore": True,
}
```

## Related Entities
- **User.UserSearchResponseDetail**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "User.UserSearchResponse":   {
      "type": "object",
      "properties": {
          "searchResults": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/User.UserSearchResponseDetail"
              }
          },
          "page": {
              "format": "int32",
              "type": "integer"
          },
          "hasMore": {
              "type": "boolean"
          }
      }
  }
}
```
