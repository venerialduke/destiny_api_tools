# Destiny.Definitions.Milestones.DestinyMilestoneType

## Entity Information
- **Entity Name**: Destiny.Definitions.Milestones.DestinyMilestoneType
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
The type of milestone. Milestones can be Tutorials, one-time/triggered/non-repeating but not necessarily tutorials, or Repeating Milestones.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | Unknown |  |
| 1 | Tutorial | One-time milestones that are specifically oriented toward teaching players about new mechanics and gameplay modes. |
| 2 | OneTime | Milestones that, once completed a single time, can never be repeated. |
| 3 | Weekly | Milestones that repeat/reset on a weekly basis. They need not all reset on the same day or time, but do need to reset weekly to qualify for this type. |
| 4 | Daily | Milestones that repeat or reset on a daily basis. |
| 5 | Special | Special indicates that the event is not on a daily/weekly cadence, but does occur more than once. For instance, Iron Banner in Destiny 1 or the Dawning were examples of what could be termed "Special" events. |

## Usage Examples

### JavaScript
```javascript
// Destiny.Definitions.Milestones.DestinyMilestoneType enumeration values
const DestinyMilestoneType = {
  Unknown: 0,
  Tutorial: 1,
  OneTime: 2,
  // ... more values
};

// Using the enumeration
const value = DestinyMilestoneType.Unknown;
```

### Python
```python
# Destiny.Definitions.Milestones.DestinyMilestoneType enumeration values
class DestinyMilestoneType:
    UNKNOWN = 0
    TUTORIAL = 1
    ONETIME = 2
    # ... more values

# Using the enumeration
value = DestinyMilestoneType.UNKNOWN
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Milestones.DestinyMilestoneType":   {
      "format": "int32",
      "description": "The type of milestone. Milestones can be Tutorials, one-time/triggered/non-repeating but not necessarily tutorials, or Repeating Milestones.",
      "enum": [
          "0",
          "1",
          "2",
          "3",
          "4",
          "5"
      ],
      "type": "integer"
  }
}
```
