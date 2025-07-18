# Destiny.SocketTypeActionType

## Entity Information
- **Entity Name**: Destiny.SocketTypeActionType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Indicates the type of actions that can be performed

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | InsertPlug |  |
| 1 | InfuseItem |  |
| 2 | ReinitializeSocket |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.SocketTypeActionType enumeration values
const SocketTypeActionType = {
  InsertPlug: 0,
  InfuseItem: 1,
  ReinitializeSocket: 2,
};

// Using the enumeration
const value = SocketTypeActionType.InsertPlug;
```

### Python
```python
# Destiny.SocketTypeActionType enumeration values
class SocketTypeActionType:
    INSERTPLUG = 0
    INFUSEITEM = 1
    REINITIALIZESOCKET = 2

# Using the enumeration
value = SocketTypeActionType.INSERTPLUG
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.SocketTypeActionType":   {
      "format": "int32",
      "description": "Indicates the type of actions that can be performed",
      "enum": [
          "0",
          "1",
          "2"
      ],
      "type": "integer"
  }
}
```
