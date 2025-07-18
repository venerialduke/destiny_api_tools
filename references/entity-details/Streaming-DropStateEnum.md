# Streaming.DropStateEnum

## Entity Information
- **Entity Name**: Streaming.DropStateEnum
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: byte

## Description
API entity for dropstateenum operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Claimed |  |
| 1 | Applied |  |
| 2 | Fulfilled |  |

## Usage Examples

### JavaScript
```javascript
// Streaming.DropStateEnum enumeration values
const DropStateEnum = {
  Claimed: 0,
  Applied: 1,
  Fulfilled: 2,
};

// Using the enumeration
const value = DropStateEnum.Claimed;
```

### Python
```python
# Streaming.DropStateEnum enumeration values
class DropStateEnum:
    CLAIMED = 0
    APPLIED = 1
    FULFILLED = 2

# Using the enumeration
value = DropStateEnum.CLAIMED
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "Streaming.DropStateEnum":   {
      "format": "byte",
      "enum": [
          "0",
          "1",
          "2"
      ],
      "type": "integer"
  }
}
```
