# Destiny.DestinyProgressionRewardItemAcquisitionBehavior

## Entity Information
- **Entity Name**: Destiny.DestinyProgressionRewardItemAcquisitionBehavior
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
Represents the different kinds of acquisition behavior for progression reward items.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Instant |  |
| 1 | PlayerClaimRequired |  |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyProgressionRewardItemAcquisitionBehavior enumeration values
const DestinyProgressionRewardItemAcquisitionBehavior = {
  Instant: 0,
  PlayerClaimRequired: 1,
};

// Using the enumeration
const value = DestinyProgressionRewardItemAcquisitionBehavior.Instant;
```

### Python
```python
# Destiny.DestinyProgressionRewardItemAcquisitionBehavior enumeration values
class DestinyProgressionRewardItemAcquisitionBehavior:
    INSTANT = 0
    PLAYERCLAIMREQUIRED = 1

# Using the enumeration
value = DestinyProgressionRewardItemAcquisitionBehavior.INSTANT
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyProgressionRewardItemAcquisitionBehavior":   {
      "format": "int32",
      "description": "Represents the different kinds of acquisition behavior for progression reward items.",
      "enum": [
          "0",
          "1"
      ],
      "type": "integer"
  }
}
```
