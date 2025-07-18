# GlobalAlertLevel

## Entity Information
- **Entity Name**: GlobalAlertLevel
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
API entity for globalalertlevel operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Unknown |  |
| 1 | Blue |  |
| 2 | Yellow |  |
| 3 | Red |  |

## Usage Examples

### JavaScript
```javascript
// GlobalAlertLevel enumeration values
const GlobalAlertLevel = {
  Unknown: 0,
  Blue: 1,
  Yellow: 2,
  // ... more values
};

// Using the enumeration
const value = GlobalAlertLevel.Unknown;
```

### Python
```python
# GlobalAlertLevel enumeration values
class GlobalAlertLevel:
    UNKNOWN = 0
    BLUE = 1
    YELLOW = 2
    # ... more values

# Using the enumeration
value = GlobalAlertLevel.UNKNOWN
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "GlobalAlertLevel":   {
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
