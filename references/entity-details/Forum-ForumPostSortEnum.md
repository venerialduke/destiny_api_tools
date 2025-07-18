# Forum.ForumPostSortEnum

## Entity Information
- **Entity Name**: Forum.ForumPostSortEnum
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
API entity for forumpostsortenum operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Default |  |
| 1 | OldestFirst |  |

## Usage Examples

### JavaScript
```javascript
// Forum.ForumPostSortEnum enumeration values
const ForumPostSortEnum = {
  Default: 0,
  OldestFirst: 1,
};

// Using the enumeration
const value = ForumPostSortEnum.Default;
```

### Python
```python
# Forum.ForumPostSortEnum enumeration values
class ForumPostSortEnum:
    DEFAULT = 0
    OLDESTFIRST = 1

# Using the enumeration
value = ForumPostSortEnum.DEFAULT
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "Forum.ForumPostSortEnum":   {
      "format": "int32",
      "enum": [
          "0",
          "1"
      ],
      "type": "integer"
  }
}
```
