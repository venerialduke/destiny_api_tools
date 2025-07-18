# Social.Friends.PlatformFriendType

## Entity Information
- **Entity Name**: Social.Friends.PlatformFriendType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
API entity for platformfriendtype operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Unknown |  |
| 1 | Xbox |  |
| 2 | PSN |  |
| 3 | Steam |  |
| 4 | Egs |  |

## Usage Examples

### JavaScript
```javascript
// Social.Friends.PlatformFriendType enumeration values
const PlatformFriendType = {
  Unknown: 0,
  Xbox: 1,
  PSN: 2,
  // ... more values
};

// Using the enumeration
const value = PlatformFriendType.Unknown;
```

### Python
```python
# Social.Friends.PlatformFriendType enumeration values
class PlatformFriendType:
    UNKNOWN = 0
    XBOX = 1
    PSN = 2
    # ... more values

# Using the enumeration
value = PlatformFriendType.UNKNOWN
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "Social.Friends.PlatformFriendType":   {
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
