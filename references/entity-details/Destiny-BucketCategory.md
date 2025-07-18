# Destiny.BucketCategory

## Entity Information
- **Entity Name**: Destiny.BucketCategory
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing bucketcategory data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Invisible |  |
| 1 | Item |  |
| 2 | Currency |  |
| 3 | Equippable |  |
| 4 | Ignored |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.BucketCategory enumeration values
const BucketCategory = {
  Invisible: 0,
  Item: 1,
  Currency: 2,
  // ... more values
};

// Using the enumeration
const value = BucketCategory.Invisible;
```

### Python
```python
# Destiny.BucketCategory enumeration values
class BucketCategory:
    INVISIBLE = 0
    ITEM = 1
    CURRENCY = 2
    # ... more values

# Using the enumeration
value = BucketCategory.INVISIBLE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.BucketCategory":   {
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
