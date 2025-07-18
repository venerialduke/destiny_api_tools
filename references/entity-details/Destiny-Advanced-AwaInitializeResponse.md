# Destiny.Advanced.AwaInitializeResponse

## Entity Information
- **Entity Name**: Destiny.Advanced.AwaInitializeResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing awainitializeresponse data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| correlationId | string | ID used to get the token. Present this ID to the user as it will identify this specific request on their device. | No |
| sentToSelf | boolean | True if the PUSH message will only be sent to the device that made this request. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Advanced.AwaInitializeResponse object
const example = {
  correlationId: "example value",
  sentToSelf: true,
};
```

### Python
```python
# Example Destiny.Advanced.AwaInitializeResponse object
example = {
    "correlationId": "example value",
    "sentToSelf": True,
}
```

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Advanced.AwaInitializeResponse":   {
      "type": "object",
      "properties": {
          "correlationId": {
              "description": "ID used to get the token. Present this ID to the user as it will identify this specific request on their device.",
              "type": "string"
          },
          "sentToSelf": {
              "description": "True if the PUSH message will only be sent to the device that made this request.",
              "type": "boolean"
          }
      }
  }
}
```
