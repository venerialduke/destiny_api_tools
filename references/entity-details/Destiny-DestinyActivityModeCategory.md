# Destiny.DestinyActivityModeCategory

## Entity Information
- **Entity Name**: Destiny.DestinyActivityModeCategory
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Activity Modes are grouped into a few possible broad categories.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None | Activities that are neither PVP nor PVE, such as social activities. |
| 1 | PvE | PvE activities, where you shoot aliens in the face. |
| 2 | PvP | PvP activities, where you shoot your "friends". |
| 3 | PvECompetitive | PVE competitive activities, where you shoot whoever you want whenever you want. Or run around collecting small glowing triangles. |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyActivityModeCategory enumeration values
const DestinyActivityModeCategory = {
  None: 0,
  PvE: 1,
  PvP: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyActivityModeCategory.None;
```

### Python
```python
# Destiny.DestinyActivityModeCategory enumeration values
class DestinyActivityModeCategory:
    NONE = 0
    PVE = 1
    PVP = 2
    # ... more values

# Using the enumeration
value = DestinyActivityModeCategory.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyActivityModeCategory":   {
      "format": "int32",
      "description": "Activity Modes are grouped into a few possible broad categories.",
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
