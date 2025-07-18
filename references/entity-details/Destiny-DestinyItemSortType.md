# Destiny.DestinyItemSortType

## Entity Information
- **Entity Name**: Destiny.DestinyItemSortType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Determines how items are sorted in an inventory bucket.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | ItemId |  |
| 1 | Timestamp |  |
| 2 | StackSize |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyItemSortType enumeration values
const DestinyItemSortType = {
  ItemId: 0,
  Timestamp: 1,
  StackSize: 2,
};

// Using the enumeration
const value = DestinyItemSortType.ItemId;
```

### Python
```python
# Destiny.DestinyItemSortType enumeration values
class DestinyItemSortType:
    ITEMID = 0
    TIMESTAMP = 1
    STACKSIZE = 2

# Using the enumeration
value = DestinyItemSortType.ITEMID
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyItemSortType":   {
      "format": "int32",
      "description": "Determines how items are sorted in an inventory bucket.",
      "enum": [
          "0",
          "1",
          "2"
      ],
      "type": "integer"
  }
}
```
