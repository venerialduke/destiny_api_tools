# GroupsV2.GroupAllianceStatus

## Entity Information
- **Entity Name**: GroupsV2.GroupAllianceStatus
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
API entity for groupalliancestatus operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Unallied |  |
| 1 | Parent |  |
| 2 | Child |  |

## Usage Examples

### JavaScript
```javascript
// GroupsV2.GroupAllianceStatus enumeration values
const GroupAllianceStatus = {
  Unallied: 0,
  Parent: 1,
  Child: 2,
};

// Using the enumeration
const value = GroupAllianceStatus.Unallied;
```

### Python
```python
# GroupsV2.GroupAllianceStatus enumeration values
class GroupAllianceStatus:
    UNALLIED = 0
    PARENT = 1
    CHILD = 2

# Using the enumeration
value = GroupAllianceStatus.UNALLIED
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "GroupsV2.GroupAllianceStatus":   {
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
