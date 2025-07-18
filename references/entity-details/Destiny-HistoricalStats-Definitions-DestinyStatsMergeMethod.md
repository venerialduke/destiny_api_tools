# Destiny.HistoricalStats.Definitions.DestinyStatsMergeMethod

## Entity Information
- **Entity Name**: Destiny.HistoricalStats.Definitions.DestinyStatsMergeMethod
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing destinystatsmergemethod data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Add | When collapsing multiple instances of the stat together, add the values. |
| 1 | Min | When collapsing multiple instances of the stat together, take the lower value. |
| 2 | Max | When collapsing multiple instances of the stat together, take the higher value. |

## Usage Examples

### JavaScript
```javascript
// Destiny.HistoricalStats.Definitions.DestinyStatsMergeMethod enumeration values
const DestinyStatsMergeMethod = {
  Add: 0,
  Min: 1,
  Max: 2,
};

// Using the enumeration
const value = DestinyStatsMergeMethod.Add;
```

### Python
```python
# Destiny.HistoricalStats.Definitions.DestinyStatsMergeMethod enumeration values
class DestinyStatsMergeMethod:
    ADD = 0
    MIN = 1
    MAX = 2

# Using the enumeration
value = DestinyStatsMergeMethod.ADD
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.HistoricalStats.Definitions.DestinyStatsMergeMethod":   {
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
