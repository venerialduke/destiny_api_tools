# GroupsV2.GroupOptionalConversation

## Entity Information
- **Entity Name**: GroupsV2.GroupOptionalConversation
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for groupoptionalconversation operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| groupId | integer (int64) |  | No |
| conversationId | integer (int64) |  | No |
| chatEnabled | boolean |  | No |
| chatName | string |  | No |
| chatSecurity | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example GroupsV2.GroupOptionalConversation object
const example = {
  groupId: 123,
  conversationId: 123,
  chatEnabled: true,
  chatName: "example value",
  chatSecurity: 123,
};
```

### Python
```python
# Example GroupsV2.GroupOptionalConversation object
example = {
    "groupId": 123,
    "conversationId": 123,
    "chatEnabled": True,
    "chatName": "example value",
    "chatSecurity": 123,
}
```

## Related Entities
- **GroupsV2.ChatSecuritySetting**: Referenced in this entity

## Notes
- This is an object schema with defined properties.

## JSON Schema
```json
{
  "GroupsV2.GroupOptionalConversation":   {
      "type": "object",
      "properties": {
          "groupId": {
              "format": "int64",
              "type": "integer"
          },
          "conversationId": {
              "format": "int64",
              "type": "integer"
          },
          "chatEnabled": {
              "type": "boolean"
          },
          "chatName": {
              "type": "string"
          },
          "chatSecurity": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/GroupsV2.ChatSecuritySetting"
              }
          }
      }
  }
}
```
