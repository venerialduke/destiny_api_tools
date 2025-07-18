# Destiny.VendorInteractionType

## Entity Information
- **Entity Name**: Destiny.VendorInteractionType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
An enumeration of the known UI interactions for Vendors.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Unknown |  |
| 1 | Undefined | An empty interaction. If this ends up in content, it is probably a game bug. |
| 2 | QuestComplete | An interaction shown when you complete a quest and receive a reward. |
| 3 | QuestContinue | An interaction shown when you talk to a Vendor as an intermediary step of a quest. |
| 4 | ReputationPreview | An interaction shown when you are previewing the vendor's reputation rewards. |
| 5 | RankUpReward | An interaction shown when you rank up with the vendor. |
| 6 | TokenTurnIn | An interaction shown when you have tokens to turn in for the vendor. |
| 7 | QuestAccept | An interaction shown when you're accepting a new quest. |
| 8 | ProgressTab | Honestly, this doesn't seem consistent to me. It is used to give you choices in the Cryptarch as well as some reward prompts by the Eververse vendor. I'll have to look into that further at some point. |
| 9 | End | These seem even less consistent. I don't know what these are. |
| 10 | Start | Also seem inconsistent. I also don't know what these are offhand. |

## Usage Examples

### JavaScript
```javascript
// Destiny.VendorInteractionType enumeration values
const VendorInteractionType = {
  Unknown: 0,
  Undefined: 1,
  QuestComplete: 2,
  // ... more values
};

// Using the enumeration
const value = VendorInteractionType.Unknown;
```

### Python
```python
# Destiny.VendorInteractionType enumeration values
class VendorInteractionType:
    UNKNOWN = 0
    UNDEFINED = 1
    QUESTCOMPLETE = 2
    # ... more values

# Using the enumeration
value = VendorInteractionType.UNKNOWN
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.VendorInteractionType":   {
      "format": "int32",
      "description": "An enumeration of the known UI interactions for Vendors.",
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
          "10"
      ],
      "type": "integer"
  }
}
```
