# Destiny.EquippingItemBlockAttributes

## Entity Information
- **Entity Name**: Destiny.EquippingItemBlockAttributes
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing equippingitemblockattributes data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | EquipOnAcquire |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.EquippingItemBlockAttributes enumeration values
const EquippingItemBlockAttributes = {
  None: 0,
  EquipOnAcquire: 1,
};

// Using the enumeration
const value = EquippingItemBlockAttributes.None;
```

### Python
```python
# Destiny.EquippingItemBlockAttributes enumeration values
class EquippingItemBlockAttributes:
    NONE = 0
    EQUIPONACQUIRE = 1

# Using the enumeration
value = EquippingItemBlockAttributes.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.EquippingItemBlockAttributes":   {
      "format": "int32",
      "enum": [
          "0",
          "1"
      ],
      "type": "integer"
  }
}
```
