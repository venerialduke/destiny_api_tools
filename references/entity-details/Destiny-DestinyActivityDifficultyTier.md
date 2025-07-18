# Destiny.DestinyActivityDifficultyTier

## Entity Information
- **Entity Name**: Destiny.DestinyActivityDifficultyTier
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
An enumeration representing the potential difficulty levels of an activity. Their names are... more qualitative than quantitative.

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

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyActivityDifficultyTier enumeration values
const DestinyActivityDifficultyTier = {
  Trivial: 0,
  Easy: 1,
  Normal: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyActivityDifficultyTier.Trivial;
```

### Python
```python
# Destiny.DestinyActivityDifficultyTier enumeration values
class DestinyActivityDifficultyTier:
    TRIVIAL = 0
    EASY = 1
    NORMAL = 2
    # ... more values

# Using the enumeration
value = DestinyActivityDifficultyTier.TRIVIAL
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyActivityDifficultyTier":   {
      "format": "int32",
      "description": "An enumeration representing the potential difficulty levels of an activity. Their names are... more qualitative than quantitative.",
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
