# Destiny.DestinyActivityTreeType

## Entity Information
- **Entity Name**: Destiny.DestinyActivityTreeType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing destinyactivitytreetype data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | FireteamFinder |  |
| 1 | Curator |  |
| 2 | EventHome |  |
| 3 | SeasonHome |  |
| 4 | Count |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyActivityTreeType enumeration values
const DestinyActivityTreeType = {
  FireteamFinder: 0,
  Curator: 1,
  EventHome: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyActivityTreeType.FireteamFinder;
```

### Python
```python
# Destiny.DestinyActivityTreeType enumeration values
class DestinyActivityTreeType:
    FIRETEAMFINDER = 0
    CURATOR = 1
    EVENTHOME = 2
    # ... more values

# Using the enumeration
value = DestinyActivityTreeType.FIRETEAMFINDER
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyActivityTreeType":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2",
          "3",
          "4"
      ],
      "type": "integer"
  }
}
```
