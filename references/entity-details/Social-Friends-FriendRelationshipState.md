# Social.Friends.FriendRelationshipState

## Entity Information
- **Entity Name**: Social.Friends.FriendRelationshipState
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
API entity for friendrelationshipstate operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Unknown |  |
| 1 | Friend |  |
| 2 | IncomingRequest |  |
| 3 | OutgoingRequest |  |

## Usage Examples

### JavaScript
```javascript
// Social.Friends.FriendRelationshipState enumeration values
const FriendRelationshipState = {
  Unknown: 0,
  Friend: 1,
  IncomingRequest: 2,
  // ... more values
};

// Using the enumeration
const value = FriendRelationshipState.Unknown;
```

### Python
```python
# Social.Friends.FriendRelationshipState enumeration values
class FriendRelationshipState:
    UNKNOWN = 0
    FRIEND = 1
    INCOMINGREQUEST = 2
    # ... more values

# Using the enumeration
value = FriendRelationshipState.UNKNOWN
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "Social.Friends.FriendRelationshipState":   {
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
