# Destiny.DestinyGatingScope

## Entity Information
- **Entity Name**: Destiny.DestinyGatingScope
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
This enumeration represents the most restrictive type of gating that is being performed by an entity. This is useful as a shortcut to avoid a lot of lookups when determining whether the gating on an Entity applies to everyone equally, or to their specific Profile or Character states.
None = There is no gating on this item.
Global = The gating on this item is based entirely on global game state. It will be gated the same for everyone.
Clan = The gating on this item is at the Clan level. For instance, if you're gated by Clan level this will be the case.
Profile = The gating includes Profile-specific checks, but not on the Profile's characters. An example of this might be when you acquire an Emblem: the Emblem will be available in your Kiosk for all characters in your Profile from that point onward.
Character = The gating includes Character-specific checks, including character level restrictions. An example of this might be an item that you can't purchase from a Vendor until you reach a specific Character Level.
Item = The gating includes item-specific checks. For BNet, this generally implies that we'll show this data only on a character level or deeper.
AssumedWorstCase = The unlocks and checks being used for this calculation are of an unknown type and are used for unknown purposes. For instance, if some great person decided that an unlock value should be globally scoped, but then the game changes it using character-specific data in a way that BNet doesn't know about. Because of the open-ended potential for this to occur, many unlock checks for "globally" scoped unlock data may be assumed as the worst case unless it has been specifically whitelisted as otherwise. That sucks, but them's the breaks.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Global |  |
| 2 | Clan |  |
| 3 | Profile |  |
| 4 | Character |  |
| 5 | Item |  |
| 6 | AssumedWorstCase |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyGatingScope enumeration values
const DestinyGatingScope = {
  None: 0,
  Global: 1,
  Clan: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyGatingScope.None;
```

### Python
```python
# Destiny.DestinyGatingScope enumeration values
class DestinyGatingScope:
    NONE = 0
    GLOBAL = 1
    CLAN = 2
    # ... more values

# Using the enumeration
value = DestinyGatingScope.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyGatingScope":   {
      "format": "int32",
      "description": "This enumeration represents the most restrictive type of gating that is being performed by an entity. This is useful as a shortcut to avoid a lot of lookups when determining whether the gating on an Entity applies to everyone equally, or to their specific Profile or Character states.\r\nNone = There is no gating on this item.\r\nGlobal = The gating on this item is based entirely on global game state. It will be gated the same for everyone.\r\nClan = The gating on this item is at the Clan level. For instance, if you're gated by Clan level this will be the case.\r\nProfile = The gating includes Profile-specific checks, but not on the Profile's characters. An example of this might be when you acquire an Emblem: the Emblem will be available in your Kiosk for all characters in your Profile from that point onward.\r\nCharacter = The gating includes Character-specific checks, including character level restrictions. An example of this might be an item that you can't purchase from a Vendor until you reach a specific Character Level.\r\nItem = The gating includes item-specific checks. For BNet, this generally implies that we'll show this data only on a character level or deeper.\r\nAssumedWorstCase = The unlocks and checks being used for this calculation are of an unknown type and are used for unknown purposes. For instance, if some great person decided that an unlock value should be globally scoped, but then the game changes it using character-specific data in a way that BNet doesn't know about. Because of the open-ended potential for this to occur, many unlock checks for \"globally\" scoped unlock data may be assumed as the worst case unless it has been specifically whitelisted as otherwise. That sucks, but them's the breaks.",
      "enum": [
          "0",
          "1",
          "2",
          "3",
          "4",
          "5",
          "6"
      ],
      "type": "integer"
  }
}
```
