# Destiny.Advanced.AwaUserResponse

## Entity Information
- **Entity Name**: Destiny.Advanced.AwaUserResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing awauserresponse data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| selection | integer (int32) | Indication of the selection the user has made (Approving or rejecting the action) | No |
| correlationId | string | Correlation ID of the request | No |
| nonce | Array[string] | Secret nonce received via the PUSH notification. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Advanced.AwaUserResponse object
const example = {
  selection: 123,
  correlationId: "example value",
  nonce: [],
};
```

### Python
```python
# Example Destiny.Advanced.AwaUserResponse object
example = {
    "selection": 123,
    "correlationId": "example value",
    "nonce": [],
}
```

## Related Entities
- **Destiny.Advanced.AwaUserSelection**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Advanced.AwaUserResponse":   {
      "type": "object",
      "properties": {
          "selection": {
              "format": "int32",
              "description": "Indication of the selection the user has made (Approving or rejecting the action)",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.Advanced.AwaUserSelection"
              }
          },
          "correlationId": {
              "description": "Correlation ID of the request",
              "type": "string"
          },
          "nonce": {
              "description": "Secret nonce received via the PUSH notification.",
              "type": "array",
              "items": {
                  "format": "byte",
                  "type": "string"
              }
          }
      }
  }
}
```
