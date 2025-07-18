# Forum.ForumTopicsSortEnum

## Entity Information
- **Entity Name**: Forum.ForumTopicsSortEnum
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: byte

## Description
API entity for forumtopicssortenum operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Default |  |
| 1 | LastReplied |  |
| 2 | MostReplied |  |
| 3 | Popularity |  |
| 4 | Controversiality |  |
| 5 | Liked |  |
| 6 | HighestRated |  |
| 7 | MostUpvoted |  |

## Usage Examples

### JavaScript
```javascript
// Forum.ForumTopicsSortEnum enumeration values
const ForumTopicsSortEnum = {
  Default: 0,
  LastReplied: 1,
  MostReplied: 2,
  // ... more values
};

// Using the enumeration
const value = ForumTopicsSortEnum.Default;
```

### Python
```python
# Forum.ForumTopicsSortEnum enumeration values
class ForumTopicsSortEnum:
    DEFAULT = 0
    LASTREPLIED = 1
    MOSTREPLIED = 2
    # ... more values

# Using the enumeration
value = ForumTopicsSortEnum.DEFAULT
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "Forum.ForumTopicsSortEnum":   {
      "format": "byte",
      "enum": [
          "0",
          "1",
          "2",
          "3",
          "4",
          "5",
          "6",
          "7"
      ],
      "type": "integer"
  }
}
```
