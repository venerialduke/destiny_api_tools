# GlobalAlertType

## Entity Information
- **Entity Name**: GlobalAlertType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
API entity for globalalerttype operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | GlobalAlert |  |
| 1 | StreamingAlert |  |

## Usage Examples

### JavaScript
```javascript
// GlobalAlertType enumeration values
const GlobalAlertType = {
  GlobalAlert: 0,
  StreamingAlert: 1,
};

// Using the enumeration
const value = GlobalAlertType.GlobalAlert;
```

### Python
```python
# GlobalAlertType enumeration values
class GlobalAlertType:
    GLOBALALERT = 0
    STREAMINGALERT = 1

# Using the enumeration
value = GlobalAlertType.GLOBALALERT
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "GlobalAlertType":   {
      "format": "int32",
      "enum": [
          "0",
          "1"
      ],
      "type": "integer"
  }
}
```
