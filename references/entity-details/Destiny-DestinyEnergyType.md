# Destiny.DestinyEnergyType

## Entity Information
- **Entity Name**: Destiny.DestinyEnergyType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Represents the socket energy types for Armor 2.0, Ghosts 2.0, and Stasis subclasses.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Any |  |
| 1 | Arc |  |
| 2 | Thermal |  |
| 3 | Void |  |
| 4 | Ghost |  |
| 5 | Subclass |  |
| 6 | Stasis |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyEnergyType enumeration values
const DestinyEnergyType = {
  Any: 0,
  Arc: 1,
  Thermal: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyEnergyType.Any;
```

### Python
```python
# Destiny.DestinyEnergyType enumeration values
class DestinyEnergyType:
    ANY = 0
    ARC = 1
    THERMAL = 2
    # ... more values

# Using the enumeration
value = DestinyEnergyType.ANY
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyEnergyType":   {
      "format": "int32",
      "description": "Represents the socket energy types for Armor 2.0, Ghosts 2.0, and Stasis subclasses.",
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
