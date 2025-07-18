# GroupsV2.ChatSecuritySetting

## Entity Information
- **Entity Name**: GroupsV2.ChatSecuritySetting
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
API entity for chatsecuritysetting operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Group |  |
| 1 | Admins |  |

## Usage Examples

### JavaScript
```javascript
// GroupsV2.ChatSecuritySetting enumeration values
const ChatSecuritySetting = {
  Group: 0,
  Admins: 1,
};

// Using the enumeration
const value = ChatSecuritySetting.Group;
```

### Python
```python
# GroupsV2.ChatSecuritySetting enumeration values
class ChatSecuritySetting:
    GROUP = 0
    ADMINS = 1

# Using the enumeration
value = ChatSecuritySetting.GROUP
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "GroupsV2.ChatSecuritySetting":   {
      "format": "int32",
      "enum": [
          "0",
          "1"
      ],
      "type": "integer"
  }
}
```
