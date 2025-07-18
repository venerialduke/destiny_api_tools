# Destiny.DestinyProgressionScope

## Entity Information
- **Entity Name**: Destiny.DestinyProgressionScope
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
There are many Progressions in Destiny (think Character Level, or Reputation). These are the various "Scopes" of Progressions, which affect many things: * Where/if they are stored * How they are calculated * Where they can be used in other game logic

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Account |  |
| 1 | Character |  |
| 2 | Clan |  |
| 3 | Item |  |
| 4 | ImplicitFromEquipment |  |
| 5 | Mapped |  |
| 6 | MappedAggregate |  |
| 7 | MappedStat |  |
| 8 | MappedUnlockValue |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyProgressionScope enumeration values
const DestinyProgressionScope = {
  Account: 0,
  Character: 1,
  Clan: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyProgressionScope.Account;
```

### Python
```python
# Destiny.DestinyProgressionScope enumeration values
class DestinyProgressionScope:
    ACCOUNT = 0
    CHARACTER = 1
    CLAN = 2
    # ... more values

# Using the enumeration
value = DestinyProgressionScope.ACCOUNT
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyProgressionScope":   {
      "format": "int32",
      "description": "There are many Progressions in Destiny (think Character Level, or Reputation). These are the various \"Scopes\" of Progressions, which affect many things: * Where/if they are stored * How they are calculated * Where they can be used in other game logic",
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
