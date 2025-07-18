# Destiny.DestinyCollectibleState

## Entity Information
- **Entity Name**: Destiny.DestinyCollectibleState
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
A Flags Enumeration/bitmask where each bit represents a different state that the Collectible can be in. A collectible can be in any number of these states, and you can choose to use or ignore any or all of them when making your own UI that shows Collectible info. Our displays are going to honor them, but we're also the kind of people who only pretend to inhale before quickly passing it to the left. So, you know, do what you got to do.
(All joking aside, please note the caveat I mention around the Invisible flag: there are cases where it is in the best interest of your users to honor these flags even if you're a "show all the data" person. Collector-oriented compulsion is a very unfortunate and real thing, and I would hate to instill that compulsion in others through showing them items that they cannot earn. Please consider this when you are making your own apps/sites.)

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | NotAcquired | If this flag is set, you have not yet obtained this collectible. |
| 2 | Obscured | If this flag is set, the item is "obscured" to you: you can/should use the alternate item hash found in DestinyCollectibleDefinition.stateInfo.obscuredOverrideItemHash when displaying this collectible instead of the default display info. |
| 4 | Invisible | If this flag is set, the collectible should not be shown to the user.
Please do consider honoring this flag. It is used - for example - to hide items that a person didn't get from the Eververse. I can't prevent these from being returned in definitions, because some people may have acquired them and thus they should show up: but I would hate for people to start feeling some variant of a Collector's Remorse about these items, and thus increasing their purchasing based on that compulsion. That would be a very unfortunate outcome, and one that I wouldn't like to see happen. So please, whether or not I'm your mom, consider honoring this flag and don't show people invisible collectibles. |
| 8 | CannotAffordMaterialRequirements | If this flag is set, the collectible requires payment for creating an instance of the item, and you are lacking in currency. Bring the benjamins next time. Or spinmetal. Whatever. |
| 16 | InventorySpaceUnavailable | If this flag is set, you can't pull this item out of your collection because there's no room left in your inventory. |
| 32 | UniquenessViolation | If this flag is set, you already have one of these items and can't have a second one. |
| 64 | PurchaseDisabled | If this flag is set, the ability to pull this item out of your collection has been disabled. |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyCollectibleState enumeration values
const DestinyCollectibleState = {
  None: 0,
  NotAcquired: 1,
  Obscured: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyCollectibleState.None;
```

### Python
```python
# Destiny.DestinyCollectibleState enumeration values
class DestinyCollectibleState:
    NONE = 0
    NOTACQUIRED = 1
    OBSCURED = 2
    # ... more values

# Using the enumeration
value = DestinyCollectibleState.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyCollectibleState":   {
      "format": "int32",
      "description": "A Flags Enumeration/bitmask where each bit represents a different state that the Collectible can be in. A collectible can be in any number of these states, and you can choose to use or ignore any or all of them when making your own UI that shows Collectible info. Our displays are going to honor them, but we're also the kind of people who only pretend to inhale before quickly passing it to the left. So, you know, do what you got to do.\r\n(All joking aside, please note the caveat I mention around the Invisible flag: there are cases where it is in the best interest of your users to honor these flags even if you're a \"show all the data\" person. Collector-oriented compulsion is a very unfortunate and real thing, and I would hate to instill that compulsion in others through showing them items that they cannot earn. Please consider this when you are making your own apps/sites.)",
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
