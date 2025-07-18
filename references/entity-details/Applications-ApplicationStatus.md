# Applications.ApplicationStatus

## Entity Information
- **Entity Name**: Applications.ApplicationStatus
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
API entity for applicationstatus operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None | No value assigned |
| 1 | Private | Application exists and works but will not appear in any public catalog. New applications start in this state, test applications will remain in this state. |
| 2 | Public | Active applications that can appear in an catalog. |
| 3 | Disabled | Application disabled by the owner. All authorizations will be treated as terminated while in this state. Owner can move back to private or public state. |
| 4 | Blocked | Application has been blocked by Bungie. It cannot be transitioned out of this state by the owner. Authorizations are terminated when an application is in this state. |

## Usage Examples

### JavaScript
```javascript
// Applications.ApplicationStatus enumeration values
const ApplicationStatus = {
  None: 0,
  Private: 1,
  Public: 2,
  // ... more values
};

// Using the enumeration
const value = ApplicationStatus.None;
```

### Python
```python
# Applications.ApplicationStatus enumeration values
class ApplicationStatus:
    NONE = 0
    PRIVATE = 1
    PUBLIC = 2
    # ... more values

# Using the enumeration
value = ApplicationStatus.NONE
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "Applications.ApplicationStatus":   {
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
