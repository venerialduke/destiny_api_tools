# Destiny.BucketScope

## Entity Information
- **Entity Name**: Destiny.BucketScope
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing bucketscope data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Character |  |
| 1 | Account |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.BucketScope enumeration values
const BucketScope = {
  Character: 0,
  Account: 1,
};

// Using the enumeration
const value = BucketScope.Character;
```

### Python
```python
# Destiny.BucketScope enumeration values
class BucketScope:
    CHARACTER = 0
    ACCOUNT = 1

# Using the enumeration
value = BucketScope.CHARACTER
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.BucketScope":   {
      "format": "int32",
      "enum": [
          "0",
          "1"
      ],
      "type": "integer"
  }
}
```
