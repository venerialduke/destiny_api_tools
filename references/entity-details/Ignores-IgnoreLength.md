# Ignores.IgnoreLength

## Entity Information
- **Entity Name**: Ignores.IgnoreLength
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
API entity for ignorelength operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Week |  |
| 2 | TwoWeeks |  |
| 3 | ThreeWeeks |  |
| 4 | Month |  |
| 5 | ThreeMonths |  |
| 6 | SixMonths |  |
| 7 | Year |  |
| 8 | Forever |  |
| 9 | ThreeMinutes |  |
| 10 | Hour |  |
| 11 | ThirtyDays |  |

## Usage Examples

### JavaScript
```javascript
// Ignores.IgnoreLength enumeration values
const IgnoreLength = {
  None: 0,
  Week: 1,
  TwoWeeks: 2,
  // ... more values
};

// Using the enumeration
const value = IgnoreLength.None;
```

### Python
```python
# Ignores.IgnoreLength enumeration values
class IgnoreLength:
    NONE = 0
    WEEK = 1
    TWOWEEKS = 2
    # ... more values

# Using the enumeration
value = IgnoreLength.NONE
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "Ignores.IgnoreLength":   {
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
          "8",
          "9",
          "10",
          "11"
      ],
      "type": "integer"
  }
}
```
