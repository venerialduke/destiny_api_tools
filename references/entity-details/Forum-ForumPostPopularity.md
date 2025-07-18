# Forum.ForumPostPopularity

## Entity Information
- **Entity Name**: Forum.ForumPostPopularity
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
API entity for forumpostpopularity operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Empty |  |
| 1 | Default |  |
| 2 | Discussed |  |
| 3 | CoolStory |  |
| 4 | HeatingUp |  |
| 5 | Hot |  |

## Usage Examples

### JavaScript
```javascript
// Forum.ForumPostPopularity enumeration values
const ForumPostPopularity = {
  Empty: 0,
  Default: 1,
  Discussed: 2,
  // ... more values
};

// Using the enumeration
const value = ForumPostPopularity.Empty;
```

### Python
```python
# Forum.ForumPostPopularity enumeration values
class ForumPostPopularity:
    EMPTY = 0
    DEFAULT = 1
    DISCUSSED = 2
    # ... more values

# Using the enumeration
value = ForumPostPopularity.EMPTY
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "Forum.ForumPostPopularity":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2",
          "3",
          "4",
          "5"
      ],
      "type": "integer"
  }
}
```
