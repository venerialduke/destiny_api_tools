# Destiny.FireteamFinderOptionValueProviderType

## Entity Information
- **Entity Name**: Destiny.FireteamFinderOptionValueProviderType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing fireteamfinderoptionvalueprovidertype data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Values |  |
| 2 | PlayerCount |  |
| 3 | FireteamFinderLabels |  |
| 4 | FireteamFinderActivityGraph |  |
| 5 | FireteamFinderUIActivityTree |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.FireteamFinderOptionValueProviderType enumeration values
const FireteamFinderOptionValueProviderType = {
  None: 0,
  Values: 1,
  PlayerCount: 2,
  // ... more values
};

// Using the enumeration
const value = FireteamFinderOptionValueProviderType.None;
```

### Python
```python
# Destiny.FireteamFinderOptionValueProviderType enumeration values
class FireteamFinderOptionValueProviderType:
    NONE = 0
    VALUES = 1
    PLAYERCOUNT = 2
    # ... more values

# Using the enumeration
value = FireteamFinderOptionValueProviderType.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.FireteamFinderOptionValueProviderType":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2",
          "3",
          "4",
          "5"
      ],
      "type": "integer"
  }
}
```
