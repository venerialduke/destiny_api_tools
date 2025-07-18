# Destiny.DestinyItemSubType

## Entity Information
- **Entity Name**: Destiny.DestinyItemSubType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
This Enumeration further classifies items by more specific categorizations than DestinyItemType. The "Sub-Type" is where we classify and categorize items one step further in specificity: "Auto Rifle" instead of just "Weapon" for example, or "Vanguard Bounty" instead of merely "Bounty".
These sub-types are provided for historical compatibility with Destiny 1, but an ideal alternative is to use DestinyItemCategoryDefinitions and the DestinyItemDefinition.itemCategories property instead. Item Categories allow for arbitrary hierarchies of specificity, and for items to belong to multiple categories across multiple hierarchies simultaneously. For this enum, we pick a single type as a "best guess" fit.
NOTE: This is not all of the item types available, and some of these are holdovers from Destiny 1 that may or may not still exist.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Crucible | DEPRECATED. Items can be both "Crucible" and something else interesting. |
| 2 | Vanguard | DEPRECATED. An item can both be "Vanguard" and something else. |
| 5 | Exotic | DEPRECATED. An item can both be Exotic and something else. |
| 6 | AutoRifle |  |
| 7 | Shotgun |  |
| 8 | Machinegun |  |
| 9 | HandCannon |  |
| 10 | RocketLauncher |  |
| 11 | FusionRifle |  |
| 12 | SniperRifle |  |
| 13 | PulseRifle |  |
| 14 | ScoutRifle |  |
| 16 | Crm | DEPRECATED. An item can both be CRM and something else. |
| 17 | Sidearm |  |
| 18 | Sword |  |
| 19 | Mask |  |
| 20 | Shader |  |
| 21 | Ornament |  |
| 22 | FusionRifleLine |  |
| 23 | GrenadeLauncher |  |
| 24 | SubmachineGun |  |
| 25 | TraceRifle |  |
| 26 | HelmetArmor |  |
| 27 | GauntletsArmor |  |
| 28 | ChestArmor |  |
| 29 | LegArmor |  |
| 30 | ClassArmor |  |
| 31 | Bow |  |
| 32 | DummyRepeatableBounty |  |
| 33 | Glaive |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyItemSubType enumeration values
const DestinyItemSubType = {
  None: 0,
  Crucible: 1,
  Vanguard: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyItemSubType.None;
```

### Python
```python
# Destiny.DestinyItemSubType enumeration values
class DestinyItemSubType:
    NONE = 0
    CRUCIBLE = 1
    VANGUARD = 2
    # ... more values

# Using the enumeration
value = DestinyItemSubType.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyItemSubType":   {
      "format": "int32",
      "description": "This Enumeration further classifies items by more specific categorizations than DestinyItemType. The \"Sub-Type\" is where we classify and categorize items one step further in specificity: \"Auto Rifle\" instead of just \"Weapon\" for example, or \"Vanguard Bounty\" instead of merely \"Bounty\".\r\nThese sub-types are provided for historical compatibility with Destiny 1, but an ideal alternative is to use DestinyItemCategoryDefinitions and the DestinyItemDefinition.itemCategories property instead. Item Categories allow for arbitrary hierarchies of specificity, and for items to belong to multiple categories across multiple hierarchies simultaneously. For this enum, we pick a single type as a \"best guess\" fit.\r\nNOTE: This is not all of the item types available, and some of these are holdovers from Destiny 1 that may or may not still exist.",
      "enum": [
          "0",
          "1",
          "2",
          "5",
          "6",
          "7",
          "8",
          "9",
          "10",
          "11",
          "12",
          "13",
          "14",
          "16",
          "17",
          "18",
          "19",
          "20",
          "21",
          "22",
          "23",
          "24",
          "25",
          "26",
          "27",
          "28",
          "29",
          "30",
          "31",
          "32",
          "33"
      ],
      "type": "integer"
  }
}
```
