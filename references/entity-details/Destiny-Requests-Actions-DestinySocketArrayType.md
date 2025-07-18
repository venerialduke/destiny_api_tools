# Destiny.Requests.Actions.DestinySocketArrayType

## Entity Information
- **Entity Name**: Destiny.Requests.Actions.DestinySocketArrayType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
If you look in the DestinyInventoryItemDefinition's "sockets" property, you'll see that there are two types of sockets: intrinsic, and "socketEntry."
Unfortunately, because Intrinsic sockets are a whole separate array, it is no longer sufficient to know the index into that array to know which socket we're talking about. You have to know whether it's in the default "socketEntries" or if it's in the "intrinsic" list.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Default |  |
| 1 | Intrinsic |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.Requests.Actions.DestinySocketArrayType enumeration values
const DestinySocketArrayType = {
  Default: 0,
  Intrinsic: 1,
};

// Using the enumeration
const value = DestinySocketArrayType.Default;
```

### Python
```python
# Destiny.Requests.Actions.DestinySocketArrayType enumeration values
class DestinySocketArrayType:
    DEFAULT = 0
    INTRINSIC = 1

# Using the enumeration
value = DestinySocketArrayType.DEFAULT
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Requests.Actions.DestinySocketArrayType":   {
      "format": "int32",
      "description": "If you look in the DestinyInventoryItemDefinition's \"sockets\" property, you'll see that there are two types of sockets: intrinsic, and \"socketEntry.\"\r\nUnfortunately, because Intrinsic sockets are a whole separate array, it is no longer sufficient to know the index into that array to know which socket we're talking about. You have to know whether it's in the default \"socketEntries\" or if it's in the \"intrinsic\" list.",
      "enum": [
          "0",
          "1"
      ],
      "type": "integer"
  }
}
```
