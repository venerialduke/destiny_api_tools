# Destiny.DestinyObjectiveUiStyle

## Entity Information
- **Entity Name**: Destiny.DestinyObjectiveUiStyle
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
If the objective has a known UI label, this enumeration will represent it.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Highlighted |  |
| 2 | CraftingWeaponLevel |  |
| 3 | CraftingWeaponLevelProgress |  |
| 4 | CraftingWeaponTimestamp |  |
| 5 | CraftingMementos |  |
| 6 | CraftingMementoTitle |  |
| 7 | DiscoverableMystery0 |  |
| 8 | DiscoverableMystery1 |  |
| 9 | DiscoverableMystery2 |  |
| 10 | DiscoverableMystery3 |  |
| 11 | DiscoverableMystery4 |  |
| 12 | DiscoverableExotic |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyObjectiveUiStyle enumeration values
const DestinyObjectiveUiStyle = {
  None: 0,
  Highlighted: 1,
  CraftingWeaponLevel: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyObjectiveUiStyle.None;
```

### Python
```python
# Destiny.DestinyObjectiveUiStyle enumeration values
class DestinyObjectiveUiStyle:
    NONE = 0
    HIGHLIGHTED = 1
    CRAFTINGWEAPONLEVEL = 2
    # ... more values

# Using the enumeration
value = DestinyObjectiveUiStyle.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyObjectiveUiStyle":   {
      "format": "int32",
      "description": "If the objective has a known UI label, this enumeration will represent it.",
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
          "11",
          "12"
      ],
      "type": "integer"
  }
}
```
