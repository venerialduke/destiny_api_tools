# Fireteam.FireteamPublicSearchOption

## Entity Information
- **Entity Name**: Fireteam.FireteamPublicSearchOption
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: byte

## Description
API entity for fireteampublicsearchoption operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | PublicAndPrivate |  |
| 1 | PublicOnly |  |
| 2 | PrivateOnly |  |

## Usage Examples

### JavaScript
```javascript
// Fireteam.FireteamPublicSearchOption enumeration values
const FireteamPublicSearchOption = {
  PublicAndPrivate: 0,
  PublicOnly: 1,
  PrivateOnly: 2,
};

// Using the enumeration
const value = FireteamPublicSearchOption.PublicAndPrivate;
```

### Python
```python
# Fireteam.FireteamPublicSearchOption enumeration values
class FireteamPublicSearchOption:
    PUBLICANDPRIVATE = 0
    PUBLICONLY = 1
    PRIVATEONLY = 2

# Using the enumeration
value = FireteamPublicSearchOption.PUBLICANDPRIVATE
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "Fireteam.FireteamPublicSearchOption":   {
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
