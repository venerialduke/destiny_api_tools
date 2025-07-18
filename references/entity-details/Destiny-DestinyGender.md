# Destiny.DestinyGender

## Entity Information
- **Entity Name**: Destiny.DestinyGender
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing destinygender data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Male |  |
| 1 | Female |  |
| 2 | Unknown |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyGender enumeration values
const DestinyGender = {
  Male: 0,
  Female: 1,
  Unknown: 2,
};

// Using the enumeration
const value = DestinyGender.Male;
```

### Python
```python
# Destiny.DestinyGender enumeration values
class DestinyGender:
    MALE = 0
    FEMALE = 1
    UNKNOWN = 2

# Using the enumeration
value = DestinyGender.MALE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyGender":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2"
      ],
      "type": "integer"
  }
}
```
