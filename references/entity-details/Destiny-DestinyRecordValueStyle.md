# Destiny.DestinyRecordValueStyle

## Entity Information
- **Entity Name**: Destiny.DestinyRecordValueStyle
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing destinyrecordvaluestyle data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Integer |  |
| 1 | Percentage |  |
| 2 | Milliseconds |  |
| 3 | Boolean |  |
| 4 | Decimal |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyRecordValueStyle enumeration values
const DestinyRecordValueStyle = {
  Integer: 0,
  Percentage: 1,
  Milliseconds: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyRecordValueStyle.Integer;
```

### Python
```python
# Destiny.DestinyRecordValueStyle enumeration values
class DestinyRecordValueStyle:
    INTEGER = 0
    PERCENTAGE = 1
    MILLISECONDS = 2
    # ... more values

# Using the enumeration
value = DestinyRecordValueStyle.INTEGER
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyRecordValueStyle":   {
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
