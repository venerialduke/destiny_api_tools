# Destiny.TierType

## Entity Information
- **Entity Name**: Destiny.TierType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing tiertype data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Unknown |  |
| 1 | Currency |  |
| 2 | Basic |  |
| 3 | Common |  |
| 4 | Rare |  |
| 5 | Superior |  |
| 6 | Exotic |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.TierType enumeration values
const TierType = {
  Unknown: 0,
  Currency: 1,
  Basic: 2,
  // ... more values
};

// Using the enumeration
const value = TierType.Unknown;
```

### Python
```python
# Destiny.TierType enumeration values
class TierType:
    UNKNOWN = 0
    CURRENCY = 1
    BASIC = 2
    # ... more values

# Using the enumeration
value = TierType.UNKNOWN
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.TierType":   {
      "format": "int32",
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
