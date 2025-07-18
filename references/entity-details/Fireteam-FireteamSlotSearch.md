# Fireteam.FireteamSlotSearch

## Entity Information
- **Entity Name**: Fireteam.FireteamSlotSearch
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: byte

## Description
API entity for fireteamslotsearch operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | NoSlotRestriction |  |
| 1 | HasOpenPlayerSlots |  |
| 2 | HasOpenPlayerOrAltSlots |  |

## Usage Examples

### JavaScript
```javascript
// Fireteam.FireteamSlotSearch enumeration values
const FireteamSlotSearch = {
  NoSlotRestriction: 0,
  HasOpenPlayerSlots: 1,
  HasOpenPlayerOrAltSlots: 2,
};

// Using the enumeration
const value = FireteamSlotSearch.NoSlotRestriction;
```

### Python
```python
# Fireteam.FireteamSlotSearch enumeration values
class FireteamSlotSearch:
    NOSLOTRESTRICTION = 0
    HASOPENPLAYERSLOTS = 1
    HASOPENPLAYERORALTSLOTS = 2

# Using the enumeration
value = FireteamSlotSearch.NOSLOTRESTRICTION
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "Fireteam.FireteamSlotSearch":   {
      "format": "byte",
      "enum": [
          "0",
          "1",
          "2"
      ],
      "type": "integer"
  }
}
```
