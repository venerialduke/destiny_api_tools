# Destiny.DestinyObjectiveGrantStyle

## Entity Information
- **Entity Name**: Destiny.DestinyObjectiveGrantStyle
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Some Objectives provide perks, generally as part of providing some kind of interesting modifier for a Challenge or Quest. This indicates when the Perk is granted.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | WhenIncomplete |  |
| 1 | WhenComplete |  |
| 2 | Always |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyObjectiveGrantStyle enumeration values
const DestinyObjectiveGrantStyle = {
  WhenIncomplete: 0,
  WhenComplete: 1,
  Always: 2,
};

// Using the enumeration
const value = DestinyObjectiveGrantStyle.WhenIncomplete;
```

### Python
```python
# Destiny.DestinyObjectiveGrantStyle enumeration values
class DestinyObjectiveGrantStyle:
    WHENINCOMPLETE = 0
    WHENCOMPLETE = 1
    ALWAYS = 2

# Using the enumeration
value = DestinyObjectiveGrantStyle.WHENINCOMPLETE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyObjectiveGrantStyle":   {
      "format": "int32",
      "description": "Some Objectives provide perks, generally as part of providing some kind of interesting modifier for a Challenge or Quest. This indicates when the Perk is granted.",
      "enum": [
          "0",
          "1",
          "2"
      ],
      "type": "integer"
  }
}
```
