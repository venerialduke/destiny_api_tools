# User.ExactSearchRequest

## Entity Information
- **Entity Name**: User.ExactSearchRequest
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for exactsearchrequest operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayName | string |  | No |
| displayNameCode | integer (int16) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example User.ExactSearchRequest object
const example = {
  displayName: "example value",
  displayNameCode: 123,
};
```

### Python
```python
# Example User.ExactSearchRequest object
example = {
    "displayName": "example value",
    "displayNameCode": 123,
}
```

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "User.ExactSearchRequest":   {
      "type": "object",
      "properties": {
          "displayName": {
              "type": "string"
          },
          "displayNameCode": {
              "format": "int16",
              "type": "integer"
          }
      }
  }
}
```
