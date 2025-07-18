# Destiny.SpecialItemType

## Entity Information
- **Entity Name**: Destiny.SpecialItemType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
As you run into items that need to be classified for Milestone purposes in ways that we cannot infer via direct data, add a new classification here and use a string constant to represent it in the local item config file.
NOTE: This is not all of the item types available, and some of these are holdovers from Destiny 1 that may or may not still exist.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | SpecialCurrency |  |
| 8 | Armor |  |
| 9 | Weapon |  |
| 23 | Engram |  |
| 24 | Consumable |  |
| 25 | ExchangeMaterial |  |
| 27 | MissionReward |  |
| 29 | Currency |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.SpecialItemType enumeration values
const SpecialItemType = {
  None: 0,
  SpecialCurrency: 1,
  Armor: 8,
  // ... more values
};

// Using the enumeration
const value = SpecialItemType.None;
```

### Python
```python
# Destiny.SpecialItemType enumeration values
class SpecialItemType:
    NONE = 0
    SPECIALCURRENCY = 1
    ARMOR = 8
    # ... more values

# Using the enumeration
value = SpecialItemType.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.SpecialItemType":   {
      "format": "int32",
      "description": "As you run into items that need to be classified for Milestone purposes in ways that we cannot infer via direct data, add a new classification here and use a string constant to represent it in the local item config file.\r\nNOTE: This is not all of the item types available, and some of these are holdovers from Destiny 1 that may or may not still exist.",
      "enum": [
          "0",
          "1",
          "8",
          "9",
          "23",
          "24",
          "25",
          "27",
          "29"
      ],
      "type": "integer"
  }
}
```
