# GroupsV2.GroupOptionalConversationAddRequest

## Entity Information
- **Entity Name**: GroupsV2.GroupOptionalConversationAddRequest
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
API entity for groupoptionalconversationaddrequest operations.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| chatName | string |  | No |
| chatSecurity | integer (int32) |  | No |

## Usage Examples

### JavaScript
```javascript
// Example GroupsV2.GroupOptionalConversationAddRequest object
const example = {
  chatName: "example value",
  chatSecurity: 123,
};
```

### Python
```python
# Example GroupsV2.GroupOptionalConversationAddRequest object
example = {
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
  "GroupsV2.GroupOptionalConversationAddRequest":   {
      "type": "object",
      "properties": {
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
