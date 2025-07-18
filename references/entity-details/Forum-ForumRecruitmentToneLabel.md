# Forum.ForumRecruitmentToneLabel

## Entity Information
- **Entity Name**: Forum.ForumRecruitmentToneLabel
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: byte

## Description
API entity for forumrecruitmenttonelabel operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | FamilyFriendly |  |
| 2 | Rowdy |  |

## Usage Examples

### JavaScript
```javascript
// Forum.ForumRecruitmentToneLabel enumeration values
const ForumRecruitmentToneLabel = {
  None: 0,
  FamilyFriendly: 1,
  Rowdy: 2,
};

// Using the enumeration
const value = ForumRecruitmentToneLabel.None;
```

### Python
```python
# Forum.ForumRecruitmentToneLabel enumeration values
class ForumRecruitmentToneLabel:
    NONE = 0
    FAMILYFRIENDLY = 1
    ROWDY = 2

# Using the enumeration
value = ForumRecruitmentToneLabel.NONE
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "Forum.ForumRecruitmentToneLabel":   {
      "format": "byte",
      "enum": [
          "0",
          "1",
          "2"
      ],
      "type": "integer"
  }
}
```
