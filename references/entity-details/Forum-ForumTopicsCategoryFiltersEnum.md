# Forum.ForumTopicsCategoryFiltersEnum

## Entity Information
- **Entity Name**: Forum.ForumTopicsCategoryFiltersEnum
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
API entity for forumtopicscategoryfiltersenum operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Links |  |
| 2 | Questions |  |
| 4 | AnsweredQuestions |  |
| 8 | Media |  |
| 16 | TextOnly |  |
| 32 | Announcement |  |
| 64 | BungieOfficial |  |
| 128 | Polls |  |

## Usage Examples

### JavaScript
```javascript
// Forum.ForumTopicsCategoryFiltersEnum enumeration values
const ForumTopicsCategoryFiltersEnum = {
  None: 0,
  Links: 1,
  Questions: 2,
  // ... more values
};

// Using the enumeration
const value = ForumTopicsCategoryFiltersEnum.None;
```

### Python
```python
# Forum.ForumTopicsCategoryFiltersEnum enumeration values
class ForumTopicsCategoryFiltersEnum:
    NONE = 0
    LINKS = 1
    QUESTIONS = 2
    # ... more values

# Using the enumeration
value = ForumTopicsCategoryFiltersEnum.NONE
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "Forum.ForumTopicsCategoryFiltersEnum":   {
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
