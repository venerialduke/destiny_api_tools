# GroupsV2.GroupOptionalConversationEditRequest

## Entity Information
- **Entity Name**: GroupsV2.GroupOptionalConversationEditRequest
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for groupoptionalconversationeditrequest operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| chatEnabled | boolean |  | No |
| chatName | string |  | No |
| chatSecurity | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example GroupsV2.GroupOptionalConversationEditRequest object
const example = {
  chatEnabled: true,
  chatName: "example value",
  chatSecurity: 123,
};
```

### Python
```python
# Example GroupsV2.GroupOptionalConversationEditRequest object
example = {
    "chatEnabled": True,
    "chatName": "example value",
    "chatSecurity": 123,
}
```

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "GroupsV2.GroupOptionalConversationEditRequest":   {
      "type": "object",
      "properties": {
          "chatEnabled": {
              "type": "boolean"
          },
          "chatName": {
              "type": "string"
          },
          "chatSecurity": {
              "format": "int32",
              "enum": [
                  "0",
                  "1"
              ],
              "type": "integer",
              "x-enum-values": [
                  {
                      "numericValue": "0",
                      "identifier": "Group"
                  },
                  {
                      "numericValue": "1",
                      "identifier": "Admins"
                  }
              ]
          }
      }
  }
}
```
