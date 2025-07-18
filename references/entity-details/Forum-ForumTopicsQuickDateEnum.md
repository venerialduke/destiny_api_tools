# Forum.ForumTopicsQuickDateEnum

## Entity Information
- **Entity Name**: Forum.ForumTopicsQuickDateEnum
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
API entity for forumtopicsquickdateenum operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | All |  |
| 1 | LastYear |  |
| 2 | LastMonth |  |
| 3 | LastWeek |  |
| 4 | LastDay |  |

## Usage Examples

### JavaScript
```javascript
// Forum.ForumTopicsQuickDateEnum enumeration values
const ForumTopicsQuickDateEnum = {
  All: 0,
  LastYear: 1,
  LastMonth: 2,
  // ... more values
};

// Using the enumeration
const value = ForumTopicsQuickDateEnum.All;
```

### Python
```python
# Forum.ForumTopicsQuickDateEnum enumeration values
class ForumTopicsQuickDateEnum:
    ALL = 0
    LASTYEAR = 1
    LASTMONTH = 2
    # ... more values

# Using the enumeration
value = ForumTopicsQuickDateEnum.ALL
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "Forum.ForumTopicsQuickDateEnum":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2",
          "3",
          "4"
      ],
      "type": "integer"
  }
}
```
