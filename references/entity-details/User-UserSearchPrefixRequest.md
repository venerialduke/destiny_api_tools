# User.UserSearchPrefixRequest

## Entity Information
- **Entity Name**: User.UserSearchPrefixRequest
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for usersearchprefixrequest operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayNamePrefix | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example User.UserSearchPrefixRequest object
const example = {
  displayNamePrefix: "example value",
};
```

### Python
```python
# Example User.UserSearchPrefixRequest object
example = {
    "displayNamePrefix": "example value",
}
```

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "User.UserSearchPrefixRequest":   {
      "type": "object",
      "properties": {
          "displayNamePrefix": {
              "type": "string"
          }
      }
  }
}
```
