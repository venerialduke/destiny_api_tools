# GlobalAlert

## Entity Information
- **Entity Name**: GlobalAlert
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for globalalert operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| AlertKey | string |  | No |
| AlertHtml | string |  | No |
| AlertTimestamp | string (date-time) |  | No |
| AlertLink | string |  | No |
| AlertLevel | integer (int32) |  | No |
| AlertType | integer (int32) |  | No |
| StreamInfo | StreamInfo |  | No |

## Usage Examples

### JavaScript
```javascript
// Example GlobalAlert object
const example = {
  AlertKey: "example value",
  AlertHtml: "example value",
  AlertTimestamp: "example value",
  AlertLink: "example value",
  AlertLevel: 123,
  // ... more properties
};
```

### Python
```python
# Example GlobalAlert object
example = {
    "AlertKey": "example value",
    "AlertHtml": "example value",
    "AlertTimestamp": "example value",
    "AlertLink": "example value",
    "AlertLevel": 123,
    # ... more properties
}
```

## Related Entities
- **GlobalAlertLevel**: Referenced in this entity
- **GlobalAlertType**: Referenced in this entity
- **StreamInfo**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "GlobalAlert":   {
      "type": "object",
      "properties": {
          "AlertKey": {
              "type": "string"
          },
          "AlertHtml": {
              "type": "string"
          },
          "AlertTimestamp": {
              "format": "date-time",
              "type": "string"
          },
          "AlertLink": {
              "type": "string"
          },
          "AlertLevel": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/GlobalAlertLevel"
              }
          },
          "AlertType": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/GlobalAlertType"
              }
          },
          "StreamInfo": {
              "$ref": "#/definitions/StreamInfo"
          }
      }
  }
}
```
