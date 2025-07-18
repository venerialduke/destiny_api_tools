# Destiny.DestinyVendorInteractionRewardSelection

## Entity Information
- **Entity Name**: Destiny.DestinyVendorInteractionRewardSelection
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
When a Vendor Interaction provides rewards, they'll either let you choose one or let you have all of them. This determines which it will be.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | One |  |
| 2 | All |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyVendorInteractionRewardSelection enumeration values
const DestinyVendorInteractionRewardSelection = {
  None: 0,
  One: 1,
  All: 2,
};

// Using the enumeration
const value = DestinyVendorInteractionRewardSelection.None;
```

### Python
```python
# Destiny.DestinyVendorInteractionRewardSelection enumeration values
class DestinyVendorInteractionRewardSelection:
    NONE = 0
    ONE = 1
    ALL = 2

# Using the enumeration
value = DestinyVendorInteractionRewardSelection.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyVendorInteractionRewardSelection":   {
      "format": "int32",
      "description": "When a Vendor Interaction provides rewards, they'll either let you choose one or let you have all of them. This determines which it will be.",
      "enum": [
          "0",
          "1",
          "2"
      ],
      "type": "integer"
  }
}
```
