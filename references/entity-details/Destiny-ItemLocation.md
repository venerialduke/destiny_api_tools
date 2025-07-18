# Destiny.ItemLocation

## Entity Information
- **Entity Name**: Destiny.ItemLocation
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing itemlocation data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Unknown |  |
| 1 | Inventory |  |
| 2 | Vault |  |
| 3 | Vendor |  |
| 4 | Postmaster |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.ItemLocation enumeration values
const ItemLocation = {
  Unknown: 0,
  Inventory: 1,
  Vault: 2,
  // ... more values
};

// Using the enumeration
const value = ItemLocation.Unknown;
```

### Python
```python
# Destiny.ItemLocation enumeration values
class ItemLocation:
    UNKNOWN = 0
    INVENTORY = 1
    VAULT = 2
    # ... more values

# Using the enumeration
value = ItemLocation.UNKNOWN
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.ItemLocation":   {
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
