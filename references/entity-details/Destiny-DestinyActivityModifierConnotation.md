# Destiny.DestinyActivityModifierConnotation

## Entity Information
- **Entity Name**: Destiny.DestinyActivityModifierConnotation
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing destinyactivitymodifierconnotation data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Neutral |  |
| 1 | Positive |  |
| 2 | Negative |  |
| 3 | Affix |  |
| 4 | Informational |  |
| 5 | Reward |  |
| 6 | Event |  |
| 7 | Count |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyActivityModifierConnotation enumeration values
const DestinyActivityModifierConnotation = {
  Neutral: 0,
  Positive: 1,
  Negative: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyActivityModifierConnotation.Neutral;
```

### Python
```python
# Destiny.DestinyActivityModifierConnotation enumeration values
class DestinyActivityModifierConnotation:
    NEUTRAL = 0
    POSITIVE = 1
    NEGATIVE = 2
    # ... more values

# Using the enumeration
value = DestinyActivityModifierConnotation.NEUTRAL
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyActivityModifierConnotation":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2",
          "3",
          "4",
          "5",
          "6",
          "7"
      ],
      "type": "integer"
  }
}
```
