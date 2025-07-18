# GroupsV2.GroupSortBy

## Entity Information
- **Entity Name**: GroupsV2.GroupSortBy
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
API entity for groupsortby operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Name |  |
| 1 | Date |  |
| 2 | Popularity |  |
| 3 | Id |  |

## Usage Examples

### JavaScript
```javascript
// GroupsV2.GroupSortBy enumeration values
const GroupSortBy = {
  Name: 0,
  Date: 1,
  Popularity: 2,
  // ... more values
};

// Using the enumeration
const value = GroupSortBy.Name;
```

### Python
```python
# GroupsV2.GroupSortBy enumeration values
class GroupSortBy:
    NAME = 0
    DATE = 1
    POPULARITY = 2
    # ... more values

# Using the enumeration
value = GroupSortBy.NAME
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "GroupsV2.GroupSortBy":   {
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
