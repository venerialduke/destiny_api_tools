# Forums.ForumFlagsEnum

## Entity Information
- **Entity Name**: Forums.ForumFlagsEnum
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
API entity for forumflagsenum operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | BungieStaffPost |  |
| 2 | ForumNinjaPost |  |
| 4 | ForumMentorPost |  |
| 8 | TopicBungieStaffPosted |  |
| 16 | TopicBungieVolunteerPosted |  |
| 32 | QuestionAnsweredByBungie |  |
| 64 | QuestionAnsweredByNinja |  |
| 128 | CommunityContent |  |

## Usage Examples

### JavaScript
```javascript
// Forums.ForumFlagsEnum enumeration values
const ForumFlagsEnum = {
  None: 0,
  BungieStaffPost: 1,
  ForumNinjaPost: 2,
  // ... more values
};

// Using the enumeration
const value = ForumFlagsEnum.None;
```

### Python
```python
# Forums.ForumFlagsEnum enumeration values
class ForumFlagsEnum:
    NONE = 0
    BUNGIESTAFFPOST = 1
    FORUMNINJAPOST = 2
    # ... more values

# Using the enumeration
value = ForumFlagsEnum.NONE
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "Forums.ForumFlagsEnum":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2",
          "4",
          "8",
          "16",
          "32",
          "64",
          "128"
      ],
      "type": "integer"
  }
}
```
