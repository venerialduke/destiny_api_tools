# GroupsV2.GroupsForMemberFilter

## Entity Information
- **Entity Name**: GroupsV2.GroupsForMemberFilter
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
API entity for groupsformemberfilter operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | All |  |
| 1 | Founded |  |
| 2 | NonFounded |  |

## Usage Examples

### JavaScript
```javascript
// GroupsV2.GroupsForMemberFilter enumeration values
const GroupsForMemberFilter = {
  All: 0,
  Founded: 1,
  NonFounded: 2,
};

// Using the enumeration
const value = GroupsForMemberFilter.All;
```

### Python
```python
# GroupsV2.GroupsForMemberFilter enumeration values
class GroupsForMemberFilter:
    ALL = 0
    FOUNDED = 1
    NONFOUNDED = 2

# Using the enumeration
value = GroupsForMemberFilter.ALL
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "GroupsV2.GroupsForMemberFilter":   {
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
