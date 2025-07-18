# Destiny.FireteamFinderOptionDisplayFormat

## Entity Information
- **Entity Name**: Destiny.FireteamFinderOptionDisplayFormat
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing fireteamfinderoptiondisplayformat data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Text |  |
| 1 | Integer |  |
| 2 | Bool |  |
| 3 | FormatString |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.FireteamFinderOptionDisplayFormat enumeration values
const FireteamFinderOptionDisplayFormat = {
  Text: 0,
  Integer: 1,
  Bool: 2,
  // ... more values
};

// Using the enumeration
const value = FireteamFinderOptionDisplayFormat.Text;
```

### Python
```python
# Destiny.FireteamFinderOptionDisplayFormat enumeration values
class FireteamFinderOptionDisplayFormat:
    TEXT = 0
    INTEGER = 1
    BOOL = 2
    # ... more values

# Using the enumeration
value = FireteamFinderOptionDisplayFormat.TEXT
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.FireteamFinderOptionDisplayFormat":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2",
          "3"
      ],
      "type": "integer"
  }
}
```
