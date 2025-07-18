# Destiny.FireteamFinderCodeOptionType

## Entity Information
- **Entity Name**: Destiny.FireteamFinderCodeOptionType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing fireteamfindercodeoptiontype data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | ApplicationOnly |  |
| 2 | OnlineOnly |  |
| 3 | PlayerCount |  |
| 4 | Title |  |
| 5 | Tags |  |
| 6 | FinderActivityGraph |  |
| 7 | MicrophoneRequired |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.FireteamFinderCodeOptionType enumeration values
const FireteamFinderCodeOptionType = {
  None: 0,
  ApplicationOnly: 1,
  OnlineOnly: 2,
  // ... more values
};

// Using the enumeration
const value = FireteamFinderCodeOptionType.None;
```

### Python
```python
# Destiny.FireteamFinderCodeOptionType enumeration values
class FireteamFinderCodeOptionType:
    NONE = 0
    APPLICATIONONLY = 1
    ONLINEONLY = 2
    # ... more values

# Using the enumeration
value = FireteamFinderCodeOptionType.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.FireteamFinderCodeOptionType":   {
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
