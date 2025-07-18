# Destiny.DestinyGamePrivacySetting

## Entity Information
- **Entity Name**: Destiny.DestinyGamePrivacySetting
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
A player can choose to restrict requests to join their Fireteam to specific states. These are the possible states a user can choose.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Open |  |
| 1 | ClanAndFriendsOnly |  |
| 2 | FriendsOnly |  |
| 3 | InvitationOnly |  |
| 4 | Closed |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyGamePrivacySetting enumeration values
const DestinyGamePrivacySetting = {
  Open: 0,
  ClanAndFriendsOnly: 1,
  FriendsOnly: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyGamePrivacySetting.Open;
```

### Python
```python
# Destiny.DestinyGamePrivacySetting enumeration values
class DestinyGamePrivacySetting:
    OPEN = 0
    CLANANDFRIENDSONLY = 1
    FRIENDSONLY = 2
    # ... more values

# Using the enumeration
value = DestinyGamePrivacySetting.OPEN
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyGamePrivacySetting":   {
      "format": "int32",
      "description": "A player can choose to restrict requests to join their Fireteam to specific states. These are the possible states a user can choose.",
      "enum": [
          "0",
          "1",
          "2",
          "3",
          "4"
      ],
      "type": "integer"
  }
}
```
