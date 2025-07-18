# Destiny.DestinyStatAggregationType

## Entity Information
- **Entity Name**: Destiny.DestinyStatAggregationType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
When a Stat (DestinyStatDefinition) is aggregated, this is the rules used for determining the level and formula used for aggregation.
* CharacterAverage = apply a weighted average using the related DestinyStatGroupDefinition on the DestinyInventoryItemDefinition across the character's equipped items. See both of those definitions for details. * Character = don't aggregate: the stat should be located and used directly on the character. * Item = don't aggregate: the stat should be located and used directly on the item.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | CharacterAverage |  |
| 1 | Character |  |
| 2 | Item |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyStatAggregationType enumeration values
const DestinyStatAggregationType = {
  CharacterAverage: 0,
  Character: 1,
  Item: 2,
};

// Using the enumeration
const value = DestinyStatAggregationType.CharacterAverage;
```

### Python
```python
# Destiny.DestinyStatAggregationType enumeration values
class DestinyStatAggregationType:
    CHARACTERAVERAGE = 0
    CHARACTER = 1
    ITEM = 2

# Using the enumeration
value = DestinyStatAggregationType.CHARACTERAVERAGE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyStatAggregationType":   {
      "format": "int32",
      "description": "When a Stat (DestinyStatDefinition) is aggregated, this is the rules used for determining the level and formula used for aggregation.\r\n* CharacterAverage = apply a weighted average using the related DestinyStatGroupDefinition on the DestinyInventoryItemDefinition across the character's equipped items. See both of those definitions for details. * Character = don't aggregate: the stat should be located and used directly on the character. * Item = don't aggregate: the stat should be located and used directly on the item.",
      "enum": [
          "0",
          "1",
          "2"
      ],
      "type": "integer"
  }
}
```
