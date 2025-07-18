# Forum.ForumMediaType

## Entity Information
- **Entity Name**: Forum.ForumMediaType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
API entity for forummediatype operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Image |  |
| 2 | Video |  |
| 3 | Youtube |  |

## Usage Examples

### JavaScript
```javascript
// Forum.ForumMediaType enumeration values
const ForumMediaType = {
  None: 0,
  Image: 1,
  Video: 2,
  // ... more values
};

// Using the enumeration
const value = ForumMediaType.None;
```

### Python
```python
# Forum.ForumMediaType enumeration values
class ForumMediaType:
    NONE = 0
    IMAGE = 1
    VIDEO = 2
    # ... more values

# Using the enumeration
value = ForumMediaType.NONE
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "Forum.ForumMediaType":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2",
          "3"
      ],
      "type": "integer"
  }
}
```
