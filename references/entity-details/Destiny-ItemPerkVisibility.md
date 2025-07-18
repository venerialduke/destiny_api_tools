# Destiny.ItemPerkVisibility

## Entity Information
- **Entity Name**: Destiny.ItemPerkVisibility
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Indicates how a perk should be shown, or if it should be, in the game UI. Maybe useful for those of you trying to filter out internal-use-only perks (or for those of you trying to figure out what they do!)

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Visible |  |
| 1 | Disabled |  |
| 2 | Hidden |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.ItemPerkVisibility enumeration values
const ItemPerkVisibility = {
  Visible: 0,
  Disabled: 1,
  Hidden: 2,
};

// Using the enumeration
const value = ItemPerkVisibility.Visible;
```

### Python
```python
# Destiny.ItemPerkVisibility enumeration values
class ItemPerkVisibility:
    VISIBLE = 0
    DISABLED = 1
    HIDDEN = 2

# Using the enumeration
value = ItemPerkVisibility.VISIBLE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.ItemPerkVisibility":   {
      "format": "int32",
      "description": "Indicates how a perk should be shown, or if it should be, in the game UI. Maybe useful for those of you trying to filter out internal-use-only perks (or for those of you trying to figure out what they do!)",
      "enum": [
          "0",
          "1",
          "2"
      ],
      "type": "integer"
  }
}
```
