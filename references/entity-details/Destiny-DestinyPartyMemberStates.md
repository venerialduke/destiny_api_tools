# Destiny.DestinyPartyMemberStates

## Entity Information
- **Entity Name**: Destiny.DestinyPartyMemberStates
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
A flags enumeration that represents a Fireteam Member's status.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | FireteamMember | This one's pretty obvious - they're on your Fireteam. |
| 2 | PosseMember | I don't know what it means to be in a 'Posse', but apparently this is it. |
| 4 | GroupMember | Nor do I understand the difference between them being in a 'Group' vs. a 'Fireteam'.
I'll update these docs once I get more info. If I get more info. If you're reading this, I never got more info. You're on your own, kid. |
| 8 | PartyLeader | This person is the party leader. |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyPartyMemberStates enumeration values
const DestinyPartyMemberStates = {
  None: 0,
  FireteamMember: 1,
  PosseMember: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyPartyMemberStates.None;
```

### Python
```python
# Destiny.DestinyPartyMemberStates enumeration values
class DestinyPartyMemberStates:
    NONE = 0
    FIRETEAMMEMBER = 1
    POSSEMEMBER = 2
    # ... more values

# Using the enumeration
value = DestinyPartyMemberStates.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyPartyMemberStates":   {
      "format": "int32",
      "description": "A flags enumeration that represents a Fireteam Member's status.",
      "enum": [
          "0",
          "1",
          "2",
          "4",
          "8"
      ],
      "type": "integer"
  }
}
```
