# Destiny.FireteamFinderOptionValueFlags

## Entity Information
- **Entity Name**: Destiny.FireteamFinderOptionValueFlags
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing fireteamfinderoptionvalueflags data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | CreateListingDefaultValue |  |
| 2 | SearchFilterDefaultValue |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.FireteamFinderOptionValueFlags enumeration values
const FireteamFinderOptionValueFlags = {
  None: 0,
  CreateListingDefaultValue: 1,
  SearchFilterDefaultValue: 2,
};

// Using the enumeration
const value = FireteamFinderOptionValueFlags.None;
```

### Python
```python
# Destiny.FireteamFinderOptionValueFlags enumeration values
class FireteamFinderOptionValueFlags:
    NONE = 0
    CREATELISTINGDEFAULTVALUE = 1
    SEARCHFILTERDEFAULTVALUE = 2

# Using the enumeration
value = FireteamFinderOptionValueFlags.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.FireteamFinderOptionValueFlags":   {
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
