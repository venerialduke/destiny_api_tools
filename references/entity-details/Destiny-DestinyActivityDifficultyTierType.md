# Destiny.DestinyActivityDifficultyTierType

## Entity Information
- **Entity Name**: Destiny.DestinyActivityDifficultyTierType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing destinyactivitydifficultytiertype data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Default |  |
| 1 | Training |  |
| 2 | Count |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyActivityDifficultyTierType enumeration values
const DestinyActivityDifficultyTierType = {
  Default: 0,
  Training: 1,
  Count: 2,
};

// Using the enumeration
const value = DestinyActivityDifficultyTierType.Default;
```

### Python
```python
# Destiny.DestinyActivityDifficultyTierType enumeration values
class DestinyActivityDifficultyTierType:
    DEFAULT = 0
    TRAINING = 1
    COUNT = 2

# Using the enumeration
value = DestinyActivityDifficultyTierType.DEFAULT
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyActivityDifficultyTierType":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2"
      ],
      "type": "integer"
  }
}
```
