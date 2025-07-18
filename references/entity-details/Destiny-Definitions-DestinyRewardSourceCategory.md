# Destiny.Definitions.DestinyRewardSourceCategory

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyRewardSourceCategory
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
BNet's custom categorization of reward sources. We took a look at the existing ways that items could be spawned, and tried to make high-level categorizations of them. This needs to be re-evaluated for Destiny 2.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None | The source doesn't fit well into any of the other types. |
| 1 | Activity | The source is directly related to the rewards gained by playing an activity or set of activities. This currently includes Quests and other action in-game. |
| 2 | Vendor | This source is directly related to items that Vendors sell. |
| 3 | Aggregate | This source is a custom aggregation of items that can be earned in many ways, but that share some other property in common that is useful to share. For instance, in Destiny 1 we would make "Reward Sources" for every game expansion: that way, you could search reward sources to see what items became available with any given Expansion. |

## Usage Examples

### JavaScript
```javascript
// Destiny.Definitions.DestinyRewardSourceCategory enumeration values
const DestinyRewardSourceCategory = {
  None: 0,
  Activity: 1,
  Vendor: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyRewardSourceCategory.None;
```

### Python
```python
# Destiny.Definitions.DestinyRewardSourceCategory enumeration values
class DestinyRewardSourceCategory:
    NONE = 0
    ACTIVITY = 1
    VENDOR = 2
    # ... more values

# Using the enumeration
value = DestinyRewardSourceCategory.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyRewardSourceCategory":   {
      "format": "int32",
      "description": "BNet's custom categorization of reward sources. We took a look at the existing ways that items could be spawned, and tried to make high-level categorizations of them. This needs to be re-evaluated for Destiny 2.",
      "enum": [
          "0",
          "1",
          "2",
          "3"
      ],
      "type": "integer"
  }
}
```
