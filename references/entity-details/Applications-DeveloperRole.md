# Applications.DeveloperRole

## Entity Information
- **Entity Name**: Applications.DeveloperRole
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
API entity for developerrole operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Owner |  |
| 2 | TeamMember |  |

## Usage Examples

### JavaScript
```javascript
// Applications.DeveloperRole enumeration values
const DeveloperRole = {
  None: 0,
  Owner: 1,
  TeamMember: 2,
};

// Using the enumeration
const value = DeveloperRole.None;
```

### Python
```python
# Applications.DeveloperRole enumeration values
class DeveloperRole:
    NONE = 0
    OWNER = 1
    TEAMMEMBER = 2

# Using the enumeration
value = DeveloperRole.NONE
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "Applications.DeveloperRole":   {
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
