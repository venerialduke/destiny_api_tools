# Destiny.DestinyRace

## Entity Information
- **Entity Name**: Destiny.DestinyRace
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing destinyrace data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Human |  |
| 1 | Awoken |  |
| 2 | Exo |  |
| 3 | Unknown |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyRace enumeration values
const DestinyRace = {
  Human: 0,
  Awoken: 1,
  Exo: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyRace.Human;
```

### Python
```python
# Destiny.DestinyRace enumeration values
class DestinyRace:
    HUMAN = 0
    AWOKEN = 1
    EXO = 2
    # ... more values

# Using the enumeration
value = DestinyRace.HUMAN
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyRace":   {
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
