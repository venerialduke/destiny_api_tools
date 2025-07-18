# Ignores.IgnoreStatus

## Entity Information
- **Entity Name**: Ignores.IgnoreStatus
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
API entity for ignorestatus operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | NotIgnored |  |
| 1 | IgnoredUser |  |
| 2 | IgnoredGroup |  |
| 4 | IgnoredByGroup |  |
| 8 | IgnoredPost |  |
| 16 | IgnoredTag |  |
| 32 | IgnoredGlobal |  |

## Usage Examples

### JavaScript
```javascript
// Ignores.IgnoreStatus enumeration values
const IgnoreStatus = {
  NotIgnored: 0,
  IgnoredUser: 1,
  IgnoredGroup: 2,
  // ... more values
};

// Using the enumeration
const value = IgnoreStatus.NotIgnored;
```

### Python
```python
# Ignores.IgnoreStatus enumeration values
class IgnoreStatus:
    NOTIGNORED = 0
    IGNOREDUSER = 1
    IGNOREDGROUP = 2
    # ... more values

# Using the enumeration
value = IgnoreStatus.NOTIGNORED
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "Ignores.IgnoreStatus":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2",
          "4",
          "8",
          "16",
          "32"
      ],
      "type": "integer"
  }
}
```
