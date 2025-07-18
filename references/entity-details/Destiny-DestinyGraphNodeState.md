# Destiny.DestinyGraphNodeState

## Entity Information
- **Entity Name**: Destiny.DestinyGraphNodeState
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Represents a potential state of an Activity Graph node.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Hidden |  |
| 1 | Visible |  |
| 2 | Teaser |  |
| 3 | Incomplete |  |
| 4 | Completed |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyGraphNodeState enumeration values
const DestinyGraphNodeState = {
  Hidden: 0,
  Visible: 1,
  Teaser: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyGraphNodeState.Hidden;
```

### Python
```python
# Destiny.DestinyGraphNodeState enumeration values
class DestinyGraphNodeState:
    HIDDEN = 0
    VISIBLE = 1
    TEASER = 2
    # ... more values

# Using the enumeration
value = DestinyGraphNodeState.HIDDEN
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyGraphNodeState":   {
      "format": "int32",
      "description": "Represents a potential state of an Activity Graph node.",
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
