# GroupsV2.GroupPotentialMemberStatus

## Entity Information
- **Entity Name**: GroupsV2.GroupPotentialMemberStatus
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
API entity for grouppotentialmemberstatus operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Applicant |  |
| 2 | Invitee |  |

## Usage Examples

### JavaScript
```javascript
// GroupsV2.GroupPotentialMemberStatus enumeration values
const GroupPotentialMemberStatus = {
  None: 0,
  Applicant: 1,
  Invitee: 2,
};

// Using the enumeration
const value = GroupPotentialMemberStatus.None;
```

### Python
```python
# GroupsV2.GroupPotentialMemberStatus enumeration values
class GroupPotentialMemberStatus:
    NONE = 0
    APPLICANT = 1
    INVITEE = 2

# Using the enumeration
value = GroupPotentialMemberStatus.NONE
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "GroupsV2.GroupPotentialMemberStatus":   {
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
