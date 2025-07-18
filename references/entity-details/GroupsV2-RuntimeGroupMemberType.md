# GroupsV2.RuntimeGroupMemberType

## Entity Information
- **Entity Name**: GroupsV2.RuntimeGroupMemberType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
The member levels used by all V2 Groups API. Individual group types use their own mappings in their native storage (general uses BnetDbGroupMemberType and D2 clans use ClanMemberLevel), but they are all translated to this in the runtime api. These runtime values should NEVER be stored anywhere, so the values can be changed as necessary.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Beginner |  |
| 2 | Member |  |
| 3 | Admin |  |
| 4 | ActingFounder |  |
| 5 | Founder |  |

## Usage Examples

### JavaScript
```javascript
// GroupsV2.RuntimeGroupMemberType enumeration values
const RuntimeGroupMemberType = {
  None: 0,
  Beginner: 1,
  Member: 2,
  // ... more values
};

// Using the enumeration
const value = RuntimeGroupMemberType.None;
```

### Python
```python
# GroupsV2.RuntimeGroupMemberType enumeration values
class RuntimeGroupMemberType:
    NONE = 0
    BEGINNER = 1
    MEMBER = 2
    # ... more values

# Using the enumeration
value = RuntimeGroupMemberType.NONE
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "GroupsV2.RuntimeGroupMemberType":   {
      "format": "int32",
      "description": "The member levels used by all V2 Groups API. Individual group types use their own mappings in their native storage (general uses BnetDbGroupMemberType and D2 clans use ClanMemberLevel), but they are all translated to this in the runtime api. These runtime values should NEVER be stored anywhere, so the values can be changed as necessary.",
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
