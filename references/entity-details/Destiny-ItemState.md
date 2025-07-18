# Destiny.ItemState

## Entity Information
- **Entity Name**: Destiny.ItemState
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
A flags enumeration/bitmask where each bit represents a different possible state that the item can be in that may effect how the item is displayed to the user and what actions can be performed against it.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Locked | If this bit is set, the item has been "locked" by the user and cannot be deleted. You may want to represent this visually with a "lock" icon. |
| 2 | Tracked | If this bit is set, the item is a quest that's being tracked by the user. You may want a visual indicator to show that this is a tracked quest. |
| 4 | Masterwork | If this bit is set, the item has a Masterwork plug inserted. This usually coincides with having a special "glowing" effect applied to the item's icon. |
| 8 | Crafted | If this bit is set, the item has been 'crafted' by the player. You may want to represent this visually with a "crafted" icon overlay. |
| 16 | HighlightedObjective | If this bit is set, the item has a 'highlighted' objective. You may want to represent this with an orange-red icon border color. |

## Usage Examples

### JavaScript
```javascript
// Destiny.ItemState enumeration values
const ItemState = {
  None: 0,
  Locked: 1,
  Tracked: 2,
  // ... more values
};

// Using the enumeration
const value = ItemState.None;
```

### Python
```python
# Destiny.ItemState enumeration values
class ItemState:
    NONE = 0
    LOCKED = 1
    TRACKED = 2
    # ... more values

# Using the enumeration
value = ItemState.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.ItemState":   {
      "format": "int32",
      "description": "A flags enumeration/bitmask where each bit represents a different possible state that the item can be in that may effect how the item is displayed to the user and what actions can be performed against it.",
      "enum": [
          "0",
          "1",
          "2",
          "4",
          "8",
          "16"
      ],
      "type": "integer"
  }
}
```
