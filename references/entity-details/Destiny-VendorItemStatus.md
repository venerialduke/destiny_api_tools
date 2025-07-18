# Destiny.VendorItemStatus

## Entity Information
- **Entity Name**: Destiny.VendorItemStatus
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Destiny API entity representing vendoritemstatus data.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Success |  |
| 1 | NoInventorySpace |  |
| 2 | NoFunds |  |
| 4 | NoProgression |  |
| 8 | NoUnlock |  |
| 16 | NoQuantity |  |
| 32 | OutsidePurchaseWindow |  |
| 64 | NotAvailable |  |
| 128 | UniquenessViolation |  |
| 256 | UnknownError |  |
| 512 | AlreadySelling |  |
| 1024 | Unsellable |  |
| 2048 | SellingInhibited |  |
| 4096 | AlreadyOwned |  |
| 8192 | DisplayOnly |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.VendorItemStatus enumeration values
const VendorItemStatus = {
  Success: 0,
  NoInventorySpace: 1,
  NoFunds: 2,
  // ... more values
};

// Using the enumeration
const value = VendorItemStatus.Success;
```

### Python
```python
# Destiny.VendorItemStatus enumeration values
class VendorItemStatus:
    SUCCESS = 0
    NOINVENTORYSPACE = 1
    NOFUNDS = 2
    # ... more values

# Using the enumeration
value = VendorItemStatus.SUCCESS
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.VendorItemStatus":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2",
          "4",
          "8",
          "16",
          "32",
          "64",
          "128",
          "256",
          "512",
          "1024",
          "2048",
          "4096",
          "8192"
      ],
      "type": "integer"
  }
}
```
