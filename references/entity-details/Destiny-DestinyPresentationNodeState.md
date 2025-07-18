# Destiny.DestinyPresentationNodeState

## Entity Information
- **Entity Name**: Destiny.DestinyPresentationNodeState
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
I know this doesn't look like a Flags Enumeration/bitmask right now, but I assure you it is. This is the possible states that a Presentation Node can be in, and it is almost certain that its potential states will increase in the future. So don't treat it like a straight up enumeration.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Invisible | If this is set, the game recommends that you not show this node. But you know your life, do what you've got to do. |
| 2 | Obscured | Turns out Presentation Nodes can also be obscured. If they are, this is set. |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyPresentationNodeState enumeration values
const DestinyPresentationNodeState = {
  None: 0,
  Invisible: 1,
  Obscured: 2,
};

// Using the enumeration
const value = DestinyPresentationNodeState.None;
```

### Python
```python
# Destiny.DestinyPresentationNodeState enumeration values
class DestinyPresentationNodeState:
    NONE = 0
    INVISIBLE = 1
    OBSCURED = 2

# Using the enumeration
value = DestinyPresentationNodeState.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyPresentationNodeState":   {
      "format": "int32",
      "description": "I know this doesn't look like a Flags Enumeration/bitmask right now, but I assure you it is. This is the possible states that a Presentation Node can be in, and it is almost certain that its potential states will increase in the future. So don't treat it like a straight up enumeration.",
      "enum": [
          "0",
          "1",
          "2"
      ],
      "type": "integer"
  }
}
```
