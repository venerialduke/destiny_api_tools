# Destiny.DestinyActivityModifierDisplayCategory

## Entity Information
- **Entity Name**: Destiny.DestinyActivityModifierDisplayCategory
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing destinyactivitymodifierdisplaycategory data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | ModeRules |  |
| 2 | SelfBuildcraft |  |
| 3 | EnemyAdjustment |  |
| 4 | EnemyBuildcraft |  |
| 5 | Seasonal |  |
| 6 | Fun |  |
| 7 | Count |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyActivityModifierDisplayCategory enumeration values
const DestinyActivityModifierDisplayCategory = {
  None: 0,
  ModeRules: 1,
  SelfBuildcraft: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyActivityModifierDisplayCategory.None;
```

### Python
```python
# Destiny.DestinyActivityModifierDisplayCategory enumeration values
class DestinyActivityModifierDisplayCategory:
    NONE = 0
    MODERULES = 1
    SELFBUILDCRAFT = 2
    # ... more values

# Using the enumeration
value = DestinyActivityModifierDisplayCategory.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyActivityModifierDisplayCategory":   {
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
