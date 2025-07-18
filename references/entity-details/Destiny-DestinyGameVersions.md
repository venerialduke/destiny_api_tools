# Destiny.DestinyGameVersions

## Entity Information
- **Entity Name**: Destiny.DestinyGameVersions
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
A flags enumeration/bitmask indicating the versions of the game that a given user has purchased.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Destiny2 |  |
| 2 | DLC1 |  |
| 4 | DLC2 |  |
| 8 | Forsaken |  |
| 16 | YearTwoAnnualPass |  |
| 32 | Shadowkeep |  |
| 64 | BeyondLight |  |
| 128 | Anniversary30th |  |
| 256 | TheWitchQueen |  |
| 512 | Lightfall |  |
| 1024 | TheFinalShape |  |
| 28535 | EdgeOfFate |  |
| 28536 | Renegades |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyGameVersions enumeration values
const DestinyGameVersions = {
  None: 0,
  Destiny2: 1,
  DLC1: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyGameVersions.None;
```

### Python
```python
# Destiny.DestinyGameVersions enumeration values
class DestinyGameVersions:
    NONE = 0
    DESTINY2 = 1
    DLC1 = 2
    # ... more values

# Using the enumeration
value = DestinyGameVersions.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyGameVersions":   {
      "format": "int32",
      "description": "A flags enumeration/bitmask indicating the versions of the game that a given user has purchased.",
      "enum": [
          "0",
          "1",
          "2",
          "4",
          "8",
          "16",
          "32",
          "64",
          "128",
          "256",
          "512",
          "1024",
          "28535",
          "28536"
      ],
      "type": "integer"
  }
}
```
