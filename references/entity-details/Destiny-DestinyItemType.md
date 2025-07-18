# Destiny.DestinyItemType

## Entity Information
- **Entity Name**: Destiny.DestinyItemType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
An enumeration that indicates the high-level "type" of the item, attempting to iron out the context specific differences for specific instances of an entity. For instance, though a weapon may be of various weapon "Types", in DestinyItemType they are all classified as "Weapon". This allows for better filtering on a higher level of abstraction for the concept of types.
 This enum is provided for historical compatibility with Destiny 1, but an ideal alternative is to use DestinyItemCategoryDefinitions and the DestinyItemDefinition.itemCategories property instead. Item Categories allow for arbitrary hierarchies of specificity, and for items to belong to multiple categories across multiple hierarchies simultaneously. For this enum, we pick a single type as a "best guess" fit.
 NOTE: This is not all of the item types available, and some of these are holdovers from Destiny 1 that may or may not still exist.
 I keep updating these because they're so damn convenient. I guess I shouldn't fight it.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Currency |  |
| 2 | Armor |  |
| 3 | Weapon |  |
| 7 | Message |  |
| 8 | Engram |  |
| 9 | Consumable |  |
| 10 | ExchangeMaterial |  |
| 11 | MissionReward |  |
| 12 | QuestStep |  |
| 13 | QuestStepComplete |  |
| 14 | Emblem |  |
| 15 | Quest |  |
| 16 | Subclass |  |
| 17 | ClanBanner |  |
| 18 | Aura |  |
| 19 | Mod |  |
| 20 | Dummy |  |
| 21 | Ship |  |
| 22 | Vehicle |  |
| 23 | Emote |  |
| 24 | Ghost |  |
| 25 | Package |  |
| 26 | Bounty |  |
| 27 | Wrapper |  |
| 28 | SeasonalArtifact |  |
| 29 | Finisher |  |
| 30 | Pattern |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyItemType enumeration values
const DestinyItemType = {
  None: 0,
  Currency: 1,
  Armor: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyItemType.None;
```

### Python
```python
# Destiny.DestinyItemType enumeration values
class DestinyItemType:
    NONE = 0
    CURRENCY = 1
    ARMOR = 2
    # ... more values

# Using the enumeration
value = DestinyItemType.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyItemType":   {
      "format": "int32",
      "description": "An enumeration that indicates the high-level \"type\" of the item, attempting to iron out the context specific differences for specific instances of an entity. For instance, though a weapon may be of various weapon \"Types\", in DestinyItemType they are all classified as \"Weapon\". This allows for better filtering on a higher level of abstraction for the concept of types.\r\n This enum is provided for historical compatibility with Destiny 1, but an ideal alternative is to use DestinyItemCategoryDefinitions and the DestinyItemDefinition.itemCategories property instead. Item Categories allow for arbitrary hierarchies of specificity, and for items to belong to multiple categories across multiple hierarchies simultaneously. For this enum, we pick a single type as a \"best guess\" fit.\r\n NOTE: This is not all of the item types available, and some of these are holdovers from Destiny 1 that may or may not still exist.\r\n I keep updating these because they're so damn convenient. I guess I shouldn't fight it.",
      "enum": [
          "0",
          "1",
          "2",
          "3",
          "7",
          "8",
          "9",
          "10",
          "11",
          "12",
          "13",
          "14",
          "15",
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
          "30"
      ],
      "type": "integer"
  }
}
```
