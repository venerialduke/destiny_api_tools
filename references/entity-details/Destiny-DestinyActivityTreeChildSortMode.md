# Destiny.DestinyActivityTreeChildSortMode

## Entity Information
- **Entity Name**: Destiny.DestinyActivityTreeChildSortMode
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing destinyactivitytreechildsortmode data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Investment |  |
| 1 | FocusFirst |  |
| 2 | BonusAndFocusFirst |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyActivityTreeChildSortMode enumeration values
const DestinyActivityTreeChildSortMode = {
  Investment: 0,
  FocusFirst: 1,
  BonusAndFocusFirst: 2,
};

// Using the enumeration
const value = DestinyActivityTreeChildSortMode.Investment;
```

### Python
```python
# Destiny.DestinyActivityTreeChildSortMode enumeration values
class DestinyActivityTreeChildSortMode:
    INVESTMENT = 0
    FOCUSFIRST = 1
    BONUSANDFOCUSFIRST = 2

# Using the enumeration
value = DestinyActivityTreeChildSortMode.INVESTMENT
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyActivityTreeChildSortMode":   {
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
