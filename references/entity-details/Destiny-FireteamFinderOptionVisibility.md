# Destiny.FireteamFinderOptionVisibility

## Entity Information
- **Entity Name**: Destiny.FireteamFinderOptionVisibility
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing fireteamfinderoptionvisibility data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Always |  |
| 1 | ShowWhenChangedFromDefault |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.FireteamFinderOptionVisibility enumeration values
const FireteamFinderOptionVisibility = {
  Always: 0,
  ShowWhenChangedFromDefault: 1,
};

// Using the enumeration
const value = FireteamFinderOptionVisibility.Always;
```

### Python
```python
# Destiny.FireteamFinderOptionVisibility enumeration values
class FireteamFinderOptionVisibility:
    ALWAYS = 0
    SHOWWHENCHANGEDFROMDEFAULT = 1

# Using the enumeration
value = FireteamFinderOptionVisibility.ALWAYS
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.FireteamFinderOptionVisibility":   {
      "format": "int32",
      "enum": [
          "0",
          "1"
      ],
      "type": "integer"
  }
}
```
