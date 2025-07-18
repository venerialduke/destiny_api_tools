# Destiny.DestinyPresentationNodeType

## Entity Information
- **Entity Name**: Destiny.DestinyPresentationNodeType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing destinypresentationnodetype data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Default |  |
| 1 | Category |  |
| 2 | Collectibles |  |
| 3 | Records |  |
| 4 | Metric |  |
| 5 | Craftable |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyPresentationNodeType enumeration values
const DestinyPresentationNodeType = {
  Default: 0,
  Category: 1,
  Collectibles: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyPresentationNodeType.Default;
```

### Python
```python
# Destiny.DestinyPresentationNodeType enumeration values
class DestinyPresentationNodeType:
    DEFAULT = 0
    CATEGORY = 1
    COLLECTIBLES = 2
    # ... more values

# Using the enumeration
value = DestinyPresentationNodeType.DEFAULT
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyPresentationNodeType":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2",
          "3",
          "4",
          "5"
      ],
      "type": "integer"
  }
}
```
