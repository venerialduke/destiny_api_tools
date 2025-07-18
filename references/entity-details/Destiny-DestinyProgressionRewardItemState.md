# Destiny.DestinyProgressionRewardItemState

## Entity Information
- **Entity Name**: Destiny.DestinyProgressionRewardItemState
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Represents the different states a progression reward item can be in.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None |  |
| 1 | Invisible | If this is set, the reward should be hidden. |
| 2 | Earned | If this is set, the reward has been earned. |
| 4 | Claimed | If this is set, the reward has been claimed. |
| 8 | ClaimAllowed | If this is set, the reward is allowed to be claimed by this Character. An item can be earned but still can't be claimed in certain circumstances, like if it's only allowed for certain subclasses. It also might not be able to be claimed if you already claimed it! |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyProgressionRewardItemState enumeration values
const DestinyProgressionRewardItemState = {
  None: 0,
  Invisible: 1,
  Earned: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyProgressionRewardItemState.None;
```

### Python
```python
# Destiny.DestinyProgressionRewardItemState enumeration values
class DestinyProgressionRewardItemState:
    NONE = 0
    INVISIBLE = 1
    EARNED = 2
    # ... more values

# Using the enumeration
value = DestinyProgressionRewardItemState.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyProgressionRewardItemState":   {
      "format": "int32",
      "description": "Represents the different states a progression reward item can be in.",
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
