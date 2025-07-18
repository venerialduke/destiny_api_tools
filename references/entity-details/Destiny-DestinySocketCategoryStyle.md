# Destiny.DestinySocketCategoryStyle

## Entity Information
- **Entity Name**: Destiny.DestinySocketCategoryStyle
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Represents the possible and known UI styles used by the game for rendering Socket Categories.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Unknown |  |
| 1 | Reusable |  |
| 2 | Consumable |  |
| 3 | Unlockable |  |
| 4 | Intrinsic |  |
| 5 | EnergyMeter |  |
| 6 | LargePerk |  |
| 7 | Abilities |  |
| 8 | Supers |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinySocketCategoryStyle enumeration values
const DestinySocketCategoryStyle = {
  Unknown: 0,
  Reusable: 1,
  Consumable: 2,
  // ... more values
};

// Using the enumeration
const value = DestinySocketCategoryStyle.Unknown;
```

### Python
```python
# Destiny.DestinySocketCategoryStyle enumeration values
class DestinySocketCategoryStyle:
    UNKNOWN = 0
    REUSABLE = 1
    CONSUMABLE = 2
    # ... more values

# Using the enumeration
value = DestinySocketCategoryStyle.UNKNOWN
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinySocketCategoryStyle":   {
      "format": "int32",
      "description": "Represents the possible and known UI styles used by the game for rendering Socket Categories.",
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
