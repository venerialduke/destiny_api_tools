# GroupsV2.GroupMemberCountFilter

## Entity Information
- **Entity Name**: GroupsV2.GroupMemberCountFilter
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
API entity for groupmembercountfilter operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | All |  |
| 1 | OneToTen |  |
| 2 | ElevenToOneHundred |  |
| 3 | GreaterThanOneHundred |  |

## Usage Examples

### JavaScript
```javascript
// GroupsV2.GroupMemberCountFilter enumeration values
const GroupMemberCountFilter = {
  All: 0,
  OneToTen: 1,
  ElevenToOneHundred: 2,
  // ... more values
};

// Using the enumeration
const value = GroupMemberCountFilter.All;
```

### Python
```python
# GroupsV2.GroupMemberCountFilter enumeration values
class GroupMemberCountFilter:
    ALL = 0
    ONETOTEN = 1
    ELEVENTOONEHUNDRED = 2
    # ... more values

# Using the enumeration
value = GroupMemberCountFilter.ALL
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "GroupsV2.GroupMemberCountFilter":   {
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
