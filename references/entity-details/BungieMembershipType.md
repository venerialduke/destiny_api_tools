# BungieMembershipType

## Entity Information
- **Entity Name**: BungieMembershipType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
The types of membership the Accounts system supports. This is the external facing enum used in place of the internal-only Bungie.SharedDefinitions.MembershipType.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | TigerXbox |  |
| 2 | TigerPsn |  |
| 3 | TigerSteam |  |
| 4 | TigerBlizzard |  |
| 5 | TigerStadia |  |
| 6 | TigerEgs |  |
| 10 | TigerDemon |  |
| 20 | GoliathGame |  |
| 254 | BungieNext |  |
| -1 | All | "All" is only valid for searching capabilities: you need to pass the actual matching BungieMembershipType for any query where you pass a known membershipId. |

## Usage Examples

### JavaScript
```javascript
// BungieMembershipType enumeration values
const BungieMembershipType = {
  None: 0,
  TigerXbox: 1,
  TigerPsn: 2,
  // ... more values
};

// Using the enumeration
const value = BungieMembershipType.None;
```

### Python
```python
# BungieMembershipType enumeration values
class BungieMembershipType:
    NONE = 0
    TIGERXBOX = 1
    TIGERPSN = 2
    # ... more values

# Using the enumeration
value = BungieMembershipType.NONE
```

## Notes
- This is an enumeration with predefined values.

## JSON Schema
```json
{
  "BungieMembershipType":   {
      "format": "int32",
      "description": "The types of membership the Accounts system supports. This is the external facing enum used in place of the internal-only Bungie.SharedDefinitions.MembershipType.",
      "enum": [
          "0",
          "1",
          "2",
          "3",
          "4",
          "5",
          "6",
          "10",
          "20",
          "254",
          "-1"
      ],
      "type": "integer"
  }
}
```
