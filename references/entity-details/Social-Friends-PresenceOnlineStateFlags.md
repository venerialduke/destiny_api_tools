# Social.Friends.PresenceOnlineStateFlags

## Entity Information
- **Entity Name**: Social.Friends.PresenceOnlineStateFlags
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
API entity for presenceonlinestateflags operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Destiny1 |  |
| 2 | Destiny2 |  |

## Usage Examples

### JavaScript
```javascript
// Social.Friends.PresenceOnlineStateFlags enumeration values
const PresenceOnlineStateFlags = {
  None: 0,
  Destiny1: 1,
  Destiny2: 2,
};

// Using the enumeration
const value = PresenceOnlineStateFlags.None;
```

### Python
```python
# Social.Friends.PresenceOnlineStateFlags enumeration values
class PresenceOnlineStateFlags:
    NONE = 0
    DESTINY1 = 1
    DESTINY2 = 2

# Using the enumeration
value = PresenceOnlineStateFlags.NONE
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "Social.Friends.PresenceOnlineStateFlags":   {
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
