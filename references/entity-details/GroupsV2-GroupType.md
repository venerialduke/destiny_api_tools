# GroupsV2.GroupType

## Entity Information
- **Entity Name**: GroupsV2.GroupType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
API entity for grouptype operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | General |  |
| 1 | Clan |  |

## Usage Examples

### JavaScript
```javascript
// GroupsV2.GroupType enumeration values
const GroupType = {
  General: 0,
  Clan: 1,
};

// Using the enumeration
const value = GroupType.General;
```

### Python
```python
# GroupsV2.GroupType enumeration values
class GroupType:
    GENERAL = 0
    CLAN = 1

# Using the enumeration
value = GroupType.GENERAL
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "GroupsV2.GroupType":   {
      "format": "int32",
      "enum": [
          "0",
          "1"
      ],
      "type": "integer"
  }
}
```
