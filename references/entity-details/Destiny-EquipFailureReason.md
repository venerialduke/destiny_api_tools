# Destiny.EquipFailureReason

## Entity Information
- **Entity Name**: Destiny.EquipFailureReason
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
The reasons why an item cannot be equipped, if any. Many flags can be set, or "None" if

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None | The item is/was able to be equipped. |
| 1 | ItemUnequippable | This is not the kind of item that can be equipped. Did you try equipping Glimmer or something? |
| 2 | ItemUniqueEquipRestricted | This item is part of a "unique set", and you can't have more than one item of that same set type equipped at once. For instance, if you already have an Exotic Weapon equipped, you can't equip a second one in another weapon slot. |
| 4 | ItemFailedUnlockCheck | This item has state-based gating that prevents it from being equipped in certain circumstances. For instance, an item might be for Warlocks only and you're a Titan, or it might require you to have beaten some special quest that you haven't beaten yet. Use the additional failure data passed on the item itself to get more information about what the specific failure case was (See DestinyInventoryItemDefinition and DestinyItemInstanceComponent) |
| 8 | ItemFailedLevelCheck | This item requires you to have reached a specific character level in order to equip it, and you haven't reached that level yet. |
| 16 | ItemWrapped | This item is 'wrapped' and must be unwrapped before being equipped. NOTE: This value used to be called ItemNotOnCharacter but that is no longer accurate. |
| 32 | ItemNotLoaded | This item is not yet loaded and cannot be equipped yet. |
| 64 | ItemEquipBlocklisted | This item is block-listed and cannot be equipped. |
| 128 | ItemLoadoutRequirementNotMet | This item does not meet the loadout requirements for the current activity |

## Usage Examples

### JavaScript
```javascript
// Destiny.EquipFailureReason enumeration values
const EquipFailureReason = {
  None: 0,
  ItemUnequippable: 1,
  ItemUniqueEquipRestricted: 2,
  // ... more values
};

// Using the enumeration
const value = EquipFailureReason.None;
```

### Python
```python
# Destiny.EquipFailureReason enumeration values
class EquipFailureReason:
    NONE = 0
    ITEMUNEQUIPPABLE = 1
    ITEMUNIQUEEQUIPRESTRICTED = 2
    # ... more values

# Using the enumeration
value = EquipFailureReason.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.EquipFailureReason":   {
      "format": "int32",
      "description": "The reasons why an item cannot be equipped, if any. Many flags can be set, or \"None\" if",
      "enum": [
          "0",
          "1",
          "2",
          "4",
          "8",
          "16",
          "32",
          "64",
          "128"
      ],
      "type": "integer"
  }
}
```
