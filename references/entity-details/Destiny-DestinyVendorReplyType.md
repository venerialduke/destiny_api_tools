# Destiny.DestinyVendorReplyType

## Entity Information
- **Entity Name**: Destiny.DestinyVendorReplyType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
This determines the type of reply that a Vendor will have during an Interaction.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Accept |  |
| 1 | Decline |  |
| 2 | Complete |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyVendorReplyType enumeration values
const DestinyVendorReplyType = {
  Accept: 0,
  Decline: 1,
  Complete: 2,
};

// Using the enumeration
const value = DestinyVendorReplyType.Accept;
```

### Python
```python
# Destiny.DestinyVendorReplyType enumeration values
class DestinyVendorReplyType:
    ACCEPT = 0
    DECLINE = 1
    COMPLETE = 2

# Using the enumeration
value = DestinyVendorReplyType.ACCEPT
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyVendorReplyType":   {
      "format": "int32",
      "description": "This determines the type of reply that a Vendor will have during an Interaction.",
      "enum": [
          "0",
          "1",
          "2"
      ],
      "type": "integer"
  }
}
```
