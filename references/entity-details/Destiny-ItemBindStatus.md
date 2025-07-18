# Destiny.ItemBindStatus

## Entity Information
- **Entity Name**: Destiny.ItemBindStatus
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing itembindstatus data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | NotBound |  |
| 1 | BoundToCharacter |  |
| 2 | BoundToAccount |  |
| 3 | BoundToGuild |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.ItemBindStatus enumeration values
const ItemBindStatus = {
  NotBound: 0,
  BoundToCharacter: 1,
  BoundToAccount: 2,
  // ... more values
};

// Using the enumeration
const value = ItemBindStatus.NotBound;
```

### Python
```python
# Destiny.ItemBindStatus enumeration values
class ItemBindStatus:
    NOTBOUND = 0
    BOUNDTOCHARACTER = 1
    BOUNDTOACCOUNT = 2
    # ... more values

# Using the enumeration
value = ItemBindStatus.NOTBOUND
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.ItemBindStatus":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2",
          "3"
      ],
      "type": "integer"
  }
}
```
