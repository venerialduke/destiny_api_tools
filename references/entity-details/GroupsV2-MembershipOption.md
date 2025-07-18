# GroupsV2.MembershipOption

## Entity Information
- **Entity Name**: GroupsV2.MembershipOption
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
API entity for membershipoption operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Reviewed |  |
| 1 | Open |  |
| 2 | Closed |  |

## Usage Examples

### JavaScript
```javascript
// GroupsV2.MembershipOption enumeration values
const MembershipOption = {
  Reviewed: 0,
  Open: 1,
  Closed: 2,
};

// Using the enumeration
const value = MembershipOption.Reviewed;
```

### Python
```python
# GroupsV2.MembershipOption enumeration values
class MembershipOption:
    REVIEWED = 0
    OPEN = 1
    CLOSED = 2

# Using the enumeration
value = MembershipOption.REVIEWED
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "GroupsV2.MembershipOption":   {
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
