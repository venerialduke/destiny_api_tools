# Destiny.DestinyClass

## Entity Information
- **Entity Name**: Destiny.DestinyClass
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing destinyclass data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Titan |  |
| 1 | Hunter |  |
| 2 | Warlock |  |
| 3 | Unknown |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyClass enumeration values
const DestinyClass = {
  Titan: 0,
  Hunter: 1,
  Warlock: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyClass.Titan;
```

### Python
```python
# Destiny.DestinyClass enumeration values
class DestinyClass:
    TITAN = 0
    HUNTER = 1
    WARLOCK = 2
    # ... more values

# Using the enumeration
value = DestinyClass.TITAN
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyClass":   {
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
