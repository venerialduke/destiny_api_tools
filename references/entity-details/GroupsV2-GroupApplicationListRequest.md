# GroupsV2.GroupApplicationListRequest

## Entity Information
- **Entity Name**: GroupsV2.GroupApplicationListRequest
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for groupapplicationlistrequest operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| memberships | Array[User.UserMembership] |  | No |
| message | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example GroupsV2.GroupApplicationListRequest object
const example = {
  memberships: [],
  message: "example value",
};
```

### Python
```python
# Example GroupsV2.GroupApplicationListRequest object
example = {
    "memberships": [],
    "message": "example value",
}
```

## Related Entities
- **User.UserMembership**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "GroupsV2.GroupApplicationListRequest":   {
      "type": "object",
      "properties": {
          "memberships": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/User.UserMembership"
              }
          },
          "message": {
              "type": "string"
          }
      }
  }
}
```
