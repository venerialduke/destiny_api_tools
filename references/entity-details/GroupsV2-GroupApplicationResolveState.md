# GroupsV2.GroupApplicationResolveState

## Entity Information
- **Entity Name**: GroupsV2.GroupApplicationResolveState
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
API entity for groupapplicationresolvestate operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Unresolved |  |
| 1 | Accepted |  |
| 2 | Denied |  |
| 3 | Rescinded |  |

## Usage Examples

### JavaScript
```javascript
// GroupsV2.GroupApplicationResolveState enumeration values
const GroupApplicationResolveState = {
  Unresolved: 0,
  Accepted: 1,
  Denied: 2,
  // ... more values
};

// Using the enumeration
const value = GroupApplicationResolveState.Unresolved;
```

### Python
```python
# GroupsV2.GroupApplicationResolveState enumeration values
class GroupApplicationResolveState:
    UNRESOLVED = 0
    ACCEPTED = 1
    DENIED = 2
    # ... more values

# Using the enumeration
value = GroupApplicationResolveState.UNRESOLVED
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "GroupsV2.GroupApplicationResolveState":   {
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
