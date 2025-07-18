# BungieCredentialType

## Entity Information
- **Entity Name**: BungieCredentialType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: byte

## Description
The types of credentials the Accounts system supports. This is the external facing enum used in place of the internal-only Bungie.SharedDefinitions.CredentialType.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Xuid |  |
| 2 | Psnid |  |
| 3 | Wlid |  |
| 4 | Fake |  |
| 5 | Facebook |  |
| 8 | Google |  |
| 9 | Windows |  |
| 10 | DemonId |  |
| 12 | SteamId |  |
| 14 | BattleNetId |  |
| 16 | StadiaId |  |
| 18 | TwitchId |  |
| 20 | EgsId |  |

## Usage Examples

### JavaScript
```javascript
// BungieCredentialType enumeration values
const BungieCredentialType = {
  None: 0,
  Xuid: 1,
  Psnid: 2,
  // ... more values
};

// Using the enumeration
const value = BungieCredentialType.None;
```

### Python
```python
# BungieCredentialType enumeration values
class BungieCredentialType:
    NONE = 0
    XUID = 1
    PSNID = 2
    # ... more values

# Using the enumeration
value = BungieCredentialType.NONE
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "BungieCredentialType":   {
      "format": "byte",
      "description": "The types of credentials the Accounts system supports. This is the external facing enum used in place of the internal-only Bungie.SharedDefinitions.CredentialType.",
      "enum": [
          "0",
          "1",
          "2",
          "3",
          "4",
          "5",
          "8",
          "9",
          "10",
          "12",
          "14",
          "16",
          "18",
          "20"
      ],
      "type": "integer"
  }
}
```
