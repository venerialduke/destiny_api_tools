# Destiny.FireteamFinderOptionControlType

## Entity Information
- **Entity Name**: Destiny.FireteamFinderOptionControlType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing fireteamfinderoptioncontroltype data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | ValueCollection |  |
| 2 | RadioButton |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.FireteamFinderOptionControlType enumeration values
const FireteamFinderOptionControlType = {
  None: 0,
  ValueCollection: 1,
  RadioButton: 2,
};

// Using the enumeration
const value = FireteamFinderOptionControlType.None;
```

### Python
```python
# Destiny.FireteamFinderOptionControlType enumeration values
class FireteamFinderOptionControlType:
    NONE = 0
    VALUECOLLECTION = 1
    RADIOBUTTON = 2

# Using the enumeration
value = FireteamFinderOptionControlType.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.FireteamFinderOptionControlType":   {
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
