# Destiny.DestinyProgressionStepDisplayEffect

## Entity Information
- **Entity Name**: Destiny.DestinyProgressionStepDisplayEffect
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
If progression is earned, this determines whether the progression shows visual effects on the character or its item - or neither.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Character |  |
| 2 | Item |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyProgressionStepDisplayEffect enumeration values
const DestinyProgressionStepDisplayEffect = {
  None: 0,
  Character: 1,
  Item: 2,
};

// Using the enumeration
const value = DestinyProgressionStepDisplayEffect.None;
```

### Python
```python
# Destiny.DestinyProgressionStepDisplayEffect enumeration values
class DestinyProgressionStepDisplayEffect:
    NONE = 0
    CHARACTER = 1
    ITEM = 2

# Using the enumeration
value = DestinyProgressionStepDisplayEffect.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyProgressionStepDisplayEffect":   {
      "format": "int32",
      "description": "If progression is earned, this determines whether the progression shows visual effects on the character or its item - or neither.",
      "enum": [
          "0",
          "1",
          "2"
      ],
      "type": "integer"
  }
}
```
