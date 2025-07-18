# Destiny.VendorDisplayCategorySortOrder

## Entity Information
- **Entity Name**: Destiny.VendorDisplayCategorySortOrder
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Display categories can have custom sort orders. These are the possible options.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Default |  |
| 1 | SortByTier |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.VendorDisplayCategorySortOrder enumeration values
const VendorDisplayCategorySortOrder = {
  Default: 0,
  SortByTier: 1,
};

// Using the enumeration
const value = VendorDisplayCategorySortOrder.Default;
```

### Python
```python
# Destiny.VendorDisplayCategorySortOrder enumeration values
class VendorDisplayCategorySortOrder:
    DEFAULT = 0
    SORTBYTIER = 1

# Using the enumeration
value = VendorDisplayCategorySortOrder.DEFAULT
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.VendorDisplayCategorySortOrder":   {
      "format": "int32",
      "description": "Display categories can have custom sort orders. These are the possible options.",
      "enum": [
          "0",
          "1"
      ],
      "type": "integer"
  }
}
```
