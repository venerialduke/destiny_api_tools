# Social.Friends.PresenceStatus

## Entity Information
- **Entity Name**: Social.Friends.PresenceStatus
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
API entity for presencestatus operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | OfflineOrUnknown |  |
| 1 | Online |  |

## Usage Examples

### JavaScript
```javascript
// Social.Friends.PresenceStatus enumeration values
const PresenceStatus = {
  OfflineOrUnknown: 0,
  Online: 1,
};

// Using the enumeration
const value = PresenceStatus.OfflineOrUnknown;
```

### Python
```python
# Social.Friends.PresenceStatus enumeration values
class PresenceStatus:
    OFFLINEORUNKNOWN = 0
    ONLINE = 1

# Using the enumeration
value = PresenceStatus.OFFLINEORUNKNOWN
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "Social.Friends.PresenceStatus":   {
      "format": "int32",
      "enum": [
          "0",
          "1"
      ],
      "type": "integer"
  }
}
```
