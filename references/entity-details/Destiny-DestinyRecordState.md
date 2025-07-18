# Destiny.DestinyRecordState

## Entity Information
- **Entity Name**: Destiny.DestinyRecordState
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
A Flags enumeration/bitmask where each bit represents a possible state that a Record/Triumph can be in.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | None | If there are no flags set, the record is in a state where it *could* be redeemed, but it has not been yet. |
| 1 | RecordRedeemed | If this is set, the completed record has been redeemed. |
| 2 | RewardUnavailable | If this is set, there's a reward available from this Record but it's unavailable for redemption. |
| 4 | ObjectiveNotCompleted | If this is set, the objective for this Record has not yet been completed. |
| 8 | Obscured | If this is set, the game recommends that you replace the display text of this Record with DestinyRecordDefinition.stateInfo.obscuredDescription. |
| 16 | Invisible | If this is set, the game recommends that you not show this record. Do what you will with this recommendation. |
| 32 | EntitlementUnowned | If this is set, you can't complete this record because you lack some permission that's required to complete it. |
| 64 | CanEquipTitle | If this is set, the record has a title (check DestinyRecordDefinition for title info) and you can equip it. |

## Usage Examples

### JavaScript
```javascript
// Destiny.DestinyRecordState enumeration values
const DestinyRecordState = {
  None: 0,
  RecordRedeemed: 1,
  RewardUnavailable: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyRecordState.None;
```

### Python
```python
# Destiny.DestinyRecordState enumeration values
class DestinyRecordState:
    NONE = 0
    RECORDREDEEMED = 1
    REWARDUNAVAILABLE = 2
    # ... more values

# Using the enumeration
value = DestinyRecordState.NONE
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.DestinyRecordState":   {
      "format": "int32",
      "description": "A Flags enumeration/bitmask where each bit represents a possible state that a Record/Triumph can be in.",
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
