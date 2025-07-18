# Destiny.DestinyActivityDifficultyId

## Entity Information
- **Entity Name**: Destiny.DestinyActivityDifficultyId
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing destinyactivitydifficultyid data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Trivial |  |
| 1 | Easy |  |
| 2 | Normal |  |
| 3 | Challenging |  |
| 4 | Hard |  |
| 5 | Brave |  |
| 6 | AlmostImpossible |  |
| 7 | Impossible |  |
| 8 | Count |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyActivityDifficultyId enumeration values
const DestinyActivityDifficultyId = {
  Trivial: 0,
  Easy: 1,
  Normal: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyActivityDifficultyId.Trivial;
```

### Python
```python
# Destiny.DestinyActivityDifficultyId enumeration values
class DestinyActivityDifficultyId:
    TRIVIAL = 0
    EASY = 1
    NORMAL = 2
    # ... more values

# Using the enumeration
value = DestinyActivityDifficultyId.TRIVIAL
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyActivityDifficultyId":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2",
          "3",
          "4",
          "5",
          "6",
          "7",
          "8"
      ],
      "type": "integer"
  }
}
```
