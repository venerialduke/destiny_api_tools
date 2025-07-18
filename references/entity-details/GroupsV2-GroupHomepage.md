# GroupsV2.GroupHomepage

## Entity Information
- **Entity Name**: GroupsV2.GroupHomepage
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
API entity for grouphomepage operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Wall |  |
| 1 | Forum |  |
| 2 | AllianceForum |  |

## Usage Examples

### JavaScript
```javascript
// GroupsV2.GroupHomepage enumeration values
const GroupHomepage = {
  Wall: 0,
  Forum: 1,
  AllianceForum: 2,
};

// Using the enumeration
const value = GroupHomepage.Wall;
```

### Python
```python
# GroupsV2.GroupHomepage enumeration values
class GroupHomepage:
    WALL = 0
    FORUM = 1
    ALLIANCEFORUM = 2

# Using the enumeration
value = GroupHomepage.WALL
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "GroupsV2.GroupHomepage":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2"
      ],
      "type": "integer"
  }
}
```
