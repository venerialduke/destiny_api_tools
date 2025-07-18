# User.OptInFlags

## Entity Information
- **Entity Name**: User.OptInFlags
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int64

## Description
API entity for optinflags operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Newsletter |  |
| 2 | System |  |
| 4 | Marketing |  |
| 8 | UserResearch |  |
| 16 | CustomerService |  |
| 32 | Social |  |
| 64 | PlayTests |  |
| 128 | PlayTestsLocal |  |
| 256 | Careers |  |

## Usage Examples

### JavaScript
```javascript
// User.OptInFlags enumeration values
const OptInFlags = {
  None: 0,
  Newsletter: 1,
  System: 2,
  // ... more values
};

// Using the enumeration
const value = OptInFlags.None;
```

### Python
```python
# User.OptInFlags enumeration values
class OptInFlags:
    NONE = 0
    NEWSLETTER = 1
    SYSTEM = 2
    # ... more values

# Using the enumeration
value = OptInFlags.NONE
```

## Notes
- This is an enumeration with predefined values.
- Values can be combined using bitwise operations for flags.

## JSON Schema
```json
{
  "User.OptInFlags":   {
      "format": "int64",
      "enum": [
          "0",
          "1",
          "2",
          "4",
          "8",
          "16",
          "32",
          "64",
          "128",
          "256"
      ],
      "type": "integer"
  }
}
```
