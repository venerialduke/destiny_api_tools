# StreamInfo

## Entity Information
- **Entity Name**: StreamInfo
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for streaminfo operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| ChannelName | string |  | No |

## Usage Examples

### JavaScript
```javascript
// Example StreamInfo object
const example = {
  ChannelName: "example value",
};
```

### Python
```python
# Example StreamInfo object
example = {
    "ChannelName": "example value",
}
```

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "StreamInfo":   {
      "type": "object",
      "properties": {
          "ChannelName": {
              "type": "string"
          }
      }
  }
}
```
