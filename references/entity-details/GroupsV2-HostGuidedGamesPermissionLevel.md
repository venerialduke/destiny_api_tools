# GroupsV2.HostGuidedGamesPermissionLevel

## Entity Information
- **Entity Name**: GroupsV2.HostGuidedGamesPermissionLevel
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Used for setting the guided game permission level override (admins and founders can always host guided games).

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Beginner |  |
| 2 | Member |  |

## Usage Examples

### JavaScript
```javascript
// GroupsV2.HostGuidedGamesPermissionLevel enumeration values
const HostGuidedGamesPermissionLevel = {
  None: 0,
  Beginner: 1,
  Member: 2,
};

// Using the enumeration
const value = HostGuidedGamesPermissionLevel.None;
```

### Python
```python
# GroupsV2.HostGuidedGamesPermissionLevel enumeration values
class HostGuidedGamesPermissionLevel:
    NONE = 0
    BEGINNER = 1
    MEMBER = 2

# Using the enumeration
value = HostGuidedGamesPermissionLevel.NONE
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "GroupsV2.HostGuidedGamesPermissionLevel":   {
      "format": "int32",
      "description": "Used for setting the guided game permission level override (admins and founders can always host guided games).",
      "enum": [
          "0",
          "1",
          "2"
      ],
      "type": "integer"
  }
}
```
