# Destiny.DestinyPresentationDisplayStyle

## Entity Information
- **Entity Name**: Destiny.DestinyPresentationDisplayStyle
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
A hint for how the presentation node should be displayed when shown in a list. How you use this is your UI is up to you.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Category | Display the item as a category, through which sub-items are filtered. |
| 1 | Badge |  |
| 2 | Medals |  |
| 3 | Collectible |  |
| 4 | Record |  |
| 5 | SeasonalTriumph |  |
| 6 | GuardianRank |  |
| 7 | CategoryCollectibles |  |
| 8 | CategoryCurrencies |  |
| 9 | CategoryEmblems |  |
| 10 | CategoryEmotes |  |
| 11 | CategoryEngrams |  |
| 12 | CategoryFinishers |  |
| 13 | CategoryGhosts |  |
| 14 | CategoryMisc |  |
| 15 | CategoryMods |  |
| 16 | CategoryOrnaments |  |
| 17 | CategoryShaders |  |
| 18 | CategoryShips |  |
| 19 | CategorySpawnfx |  |
| 20 | CategoryUpgradeMaterials |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyPresentationDisplayStyle enumeration values
const DestinyPresentationDisplayStyle = {
  Category: 0,
  Badge: 1,
  Medals: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyPresentationDisplayStyle.Category;
```

### Python
```python
# Destiny.DestinyPresentationDisplayStyle enumeration values
class DestinyPresentationDisplayStyle:
    CATEGORY = 0
    BADGE = 1
    MEDALS = 2
    # ... more values

# Using the enumeration
value = DestinyPresentationDisplayStyle.CATEGORY
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyPresentationDisplayStyle":   {
      "format": "int32",
      "description": "A hint for how the presentation node should be displayed when shown in a list. How you use this is your UI is up to you.",
      "enum": [
          "0",
          "1",
          "2",
          "3",
          "4",
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
          "15",
          "16",
          "17",
          "18",
          "19",
          "20"
      ],
      "type": "integer"
  }
}
```
