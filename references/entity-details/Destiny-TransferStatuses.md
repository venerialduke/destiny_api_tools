# Destiny.TransferStatuses

## Entity Information
- **Entity Name**: Destiny.TransferStatuses
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Whether you can transfer an item, and why not if you can't.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | CanTransfer | The item can be transferred. |
| 1 | ItemIsEquipped | You can't transfer the item because it is equipped on a character. |
| 2 | NotTransferrable | The item is defined as not transferrable in its DestinyInventoryItemDefinition.nonTransferrable property. |
| 4 | NoRoomInDestination | You could transfer the item, but the place you're trying to put it has run out of room! Check your remaining Vault and/or character space. |

## Usage Examples

### JavaScript
```javascript
// Destiny.TransferStatuses enumeration values
const TransferStatuses = {
  CanTransfer: 0,
  ItemIsEquipped: 1,
  NotTransferrable: 2,
  // ... more values
};

// Using the enumeration
const value = TransferStatuses.CanTransfer;
```

### Python
```python
# Destiny.TransferStatuses enumeration values
class TransferStatuses:
    CANTRANSFER = 0
    ITEMISEQUIPPED = 1
    NOTTRANSFERRABLE = 2
    # ... more values

# Using the enumeration
value = TransferStatuses.CANTRANSFER
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.TransferStatuses":   {
      "format": "int32",
      "description": "Whether you can transfer an item, and why not if you can't.",
      "enum": [
          "0",
          "1",
          "2",
          "4"
      ],
      "type": "integer"
  }
}
```
