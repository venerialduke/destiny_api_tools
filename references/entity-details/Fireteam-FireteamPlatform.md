# Fireteam.FireteamPlatform

## Entity Information
- **Entity Name**: Fireteam.FireteamPlatform
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: byte

## Description
API entity for fireteamplatform operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Any |  |
| 1 | Playstation4 |  |
| 2 | XboxOne |  |
| 3 | Blizzard |  |
| 4 | Steam |  |
| 5 | Stadia |  |
| 6 | Egs |  |

## Usage Examples

### JavaScript
```javascript
// Fireteam.FireteamPlatform enumeration values
const FireteamPlatform = {
  Any: 0,
  Playstation4: 1,
  XboxOne: 2,
  // ... more values
};

// Using the enumeration
const value = FireteamPlatform.Any;
```

### Python
```python
# Fireteam.FireteamPlatform enumeration values
class FireteamPlatform:
    ANY = 0
    PLAYSTATION4 = 1
    XBOXONE = 2
    # ... more values

# Using the enumeration
value = FireteamPlatform.ANY
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "Fireteam.FireteamPlatform":   {
      "format": "byte",
      "enum": [
          "0",
          "1",
          "2",
          "3",
          "4",
          "5",
          "6"
      ],
      "type": "integer"
  }
}
```
