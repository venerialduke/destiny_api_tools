# Destiny.ActivityGraphNodeHighlightType

## Entity Information
- **Entity Name**: Destiny.ActivityGraphNodeHighlightType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
The various known UI styles in which an item can be highlighted. It'll be up to you to determine what you want to show based on this highlighting, BNet doesn't have any assets that correspond to these states. And yeah, RiseOfIron and Comet have their own special highlight states. Don't ask me, I can't imagine they're still used.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Normal |  |
| 2 | Hyper |  |
| 3 | Comet |  |
| 4 | RiseOfIron |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.ActivityGraphNodeHighlightType enumeration values
const ActivityGraphNodeHighlightType = {
  None: 0,
  Normal: 1,
  Hyper: 2,
  // ... more values
};

// Using the enumeration
const value = ActivityGraphNodeHighlightType.None;
```

### Python
```python
# Destiny.ActivityGraphNodeHighlightType enumeration values
class ActivityGraphNodeHighlightType:
    NONE = 0
    NORMAL = 1
    HYPER = 2
    # ... more values

# Using the enumeration
value = ActivityGraphNodeHighlightType.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.ActivityGraphNodeHighlightType":   {
      "format": "int32",
      "description": "The various known UI styles in which an item can be highlighted. It'll be up to you to determine what you want to show based on this highlighting, BNet doesn't have any assets that correspond to these states. And yeah, RiseOfIron and Comet have their own special highlight states. Don't ask me, I can't imagine they're still used.",
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
