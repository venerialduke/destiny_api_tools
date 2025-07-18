# Destiny.DestinyVendorItemRefundPolicy

## Entity Information
- **Entity Name**: Destiny.DestinyVendorItemRefundPolicy
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
The action that happens when the user attempts to refund an item.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | NotRefundable |  |
| 1 | DeletesItem |  |
| 2 | RevokesLicense |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyVendorItemRefundPolicy enumeration values
const DestinyVendorItemRefundPolicy = {
  NotRefundable: 0,
  DeletesItem: 1,
  RevokesLicense: 2,
};

// Using the enumeration
const value = DestinyVendorItemRefundPolicy.NotRefundable;
```

### Python
```python
# Destiny.DestinyVendorItemRefundPolicy enumeration values
class DestinyVendorItemRefundPolicy:
    NOTREFUNDABLE = 0
    DELETESITEM = 1
    REVOKESLICENSE = 2

# Using the enumeration
value = DestinyVendorItemRefundPolicy.NOTREFUNDABLE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyVendorItemRefundPolicy":   {
      "format": "int32",
      "description": "The action that happens when the user attempts to refund an item.",
      "enum": [
          "0",
          "1",
          "2"
      ],
      "type": "integer"
  }
}
```
