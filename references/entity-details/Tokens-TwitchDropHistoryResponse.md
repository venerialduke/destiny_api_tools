# Tokens.TwitchDropHistoryResponse

## Entity Information
- **Entity Name**: Tokens.TwitchDropHistoryResponse
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for twitchdrophistoryresponse operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| Title | string |  | No |
| Description | string |  | No |
| CreatedAt | string (date-time) |  | No |
| ClaimState | integer (byte) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Tokens.TwitchDropHistoryResponse object
const example = {
  Title: "example value",
  Description: "example value",
  CreatedAt: "example value",
  ClaimState: 123,
};
```

### Python
```python
# Example Tokens.TwitchDropHistoryResponse object
example = {
    "Title": "example value",
    "Description": "example value",
    "CreatedAt": "example value",
    "ClaimState": 123,
}
```

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "Tokens.TwitchDropHistoryResponse":   {
      "type": "object",
      "properties": {
          "Title": {
              "type": "string"
          },
          "Description": {
              "type": "string"
          },
          "CreatedAt": {
              "format": "date-time",
              "type": "string"
          },
          "ClaimState": {
              "format": "byte",
              "enum": [
                  "0",
                  "1",
                  "2"
              ],
              "type": "integer",
              "x-enum-values": [
                  {
                      "numericValue": "0",
                      "identifier": "Claimed"
                  },
                  {
                      "numericValue": "1",
                      "identifier": "Applied"
                  },
                  {
                      "numericValue": "2",
                      "identifier": "Fulfilled"
                  }
              ]
          }
      }
  }
}
```
