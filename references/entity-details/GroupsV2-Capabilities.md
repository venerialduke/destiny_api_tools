# GroupsV2.Capabilities

## Entity Information
- **Entity Name**: GroupsV2.Capabilities
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
API entity for capabilities operations.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Leaderboards |  |
| 2 | Callsign |  |
| 4 | OptionalConversations |  |
| 8 | ClanBanner |  |
| 16 | D2InvestmentData |  |
| 32 | Tags |  |
| 64 | Alliances |  |

## Usage Examples

### JavaScript
```javascript
// GroupsV2.Capabilities enumeration values
const Capabilities = {
  None: 0,
  Leaderboards: 1,
  Callsign: 2,
  // ... more values
};

// Using the enumeration
const value = Capabilities.None;
```

### Python
```python
# GroupsV2.Capabilities enumeration values
class Capabilities:
    NONE = 0
    LEADERBOARDS = 1
    CALLSIGN = 2
    # ... more values

# Using the enumeration
value = Capabilities.NONE
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "GroupsV2.Capabilities":   {
      "format": "int32",
      "enum": [
          "0",
          "1",
          "2",
          "4",
          "8",
          "16",
          "32",
          "64"
      ],
      "type": "integer"
  }
}
```
