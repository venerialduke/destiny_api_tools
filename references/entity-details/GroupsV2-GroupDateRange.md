# GroupsV2.GroupDateRange

## Entity Information
- **Entity Name**: GroupsV2.GroupDateRange
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
API entity for groupdaterange operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | All |  |
| 1 | PastDay |  |
| 2 | PastWeek |  |
| 3 | PastMonth |  |
| 4 | PastYear |  |

## Usage Examples

### JavaScript
```javascript
// GroupsV2.GroupDateRange enumeration values
const GroupDateRange = {
  All: 0,
  PastDay: 1,
  PastWeek: 2,
  // ... more values
};

// Using the enumeration
const value = GroupDateRange.All;
```

### Python
```python
# GroupsV2.GroupDateRange enumeration values
class GroupDateRange:
    ALL = 0
    PASTDAY = 1
    PASTWEEK = 2
    # ... more values

# Using the enumeration
value = GroupDateRange.ALL
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "GroupsV2.GroupDateRange":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2",
          "3",
          "4"
      ],
      "type": "integer"
  }
}
```
