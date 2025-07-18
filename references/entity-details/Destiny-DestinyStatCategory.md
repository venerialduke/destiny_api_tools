# Destiny.DestinyStatCategory

## Entity Information
- **Entity Name**: Destiny.DestinyStatCategory
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
At last, stats have categories. Use this for whatever purpose you might wish.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Gameplay |  |
| 1 | Weapon |  |
| 2 | Defense |  |
| 3 | Primary |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyStatCategory enumeration values
const DestinyStatCategory = {
  Gameplay: 0,
  Weapon: 1,
  Defense: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyStatCategory.Gameplay;
```

### Python
```python
# Destiny.DestinyStatCategory enumeration values
class DestinyStatCategory:
    GAMEPLAY = 0
    WEAPON = 1
    DEFENSE = 2
    # ... more values

# Using the enumeration
value = DestinyStatCategory.GAMEPLAY
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyStatCategory":   {
      "format": "int32",
      "description": "At last, stats have categories. Use this for whatever purpose you might wish.",
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
