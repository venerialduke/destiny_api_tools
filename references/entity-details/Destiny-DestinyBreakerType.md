# Destiny.DestinyBreakerType

## Entity Information
- **Entity Name**: Destiny.DestinyBreakerType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
A plug can optionally have a "Breaker Type": a special ability that can affect units in unique ways. Activating this plug can grant one of these types.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | ShieldPiercing |  |
| 2 | Disruption |  |
| 3 | Stagger |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyBreakerType enumeration values
const DestinyBreakerType = {
  None: 0,
  ShieldPiercing: 1,
  Disruption: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyBreakerType.None;
```

### Python
```python
# Destiny.DestinyBreakerType enumeration values
class DestinyBreakerType:
    NONE = 0
    SHIELDPIERCING = 1
    DISRUPTION = 2
    # ... more values

# Using the enumeration
value = DestinyBreakerType.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyBreakerType":   {
      "format": "int32",
      "description": "A plug can optionally have a \"Breaker Type\": a special ability that can affect units in unique ways. Activating this plug can grant one of these types.",
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
