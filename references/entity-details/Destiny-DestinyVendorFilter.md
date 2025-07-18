# Destiny.DestinyVendorFilter

## Entity Information
- **Entity Name**: Destiny.DestinyVendorFilter
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Indicates the type of filter to apply to Vendor results.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | ApiPurchasable |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyVendorFilter enumeration values
const DestinyVendorFilter = {
  None: 0,
  ApiPurchasable: 1,
};

// Using the enumeration
const value = DestinyVendorFilter.None;
```

### Python
```python
# Destiny.DestinyVendorFilter enumeration values
class DestinyVendorFilter:
    NONE = 0
    APIPURCHASABLE = 1

# Using the enumeration
value = DestinyVendorFilter.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyVendorFilter":   {
      "format": "int32",
      "description": "Indicates the type of filter to apply to Vendor results.",
      "enum": [
          "0",
          "1"
      ],
      "type": "integer"
  }
}
```
