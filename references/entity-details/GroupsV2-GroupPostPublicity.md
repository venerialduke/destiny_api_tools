# GroupsV2.GroupPostPublicity

## Entity Information
- **Entity Name**: GroupsV2.GroupPostPublicity
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
API entity for grouppostpublicity operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Public |  |
| 1 | Alliance |  |
| 2 | Private |  |

## Usage Examples

### JavaScript
```javascript
// GroupsV2.GroupPostPublicity enumeration values
const GroupPostPublicity = {
  Public: 0,
  Alliance: 1,
  Private: 2,
};

// Using the enumeration
const value = GroupPostPublicity.Public;
```

### Python
```python
# GroupsV2.GroupPostPublicity enumeration values
class GroupPostPublicity:
    PUBLIC = 0
    ALLIANCE = 1
    PRIVATE = 2

# Using the enumeration
value = GroupPostPublicity.PUBLIC
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "GroupsV2.GroupPostPublicity":   {
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
