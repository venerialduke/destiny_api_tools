# Destiny.Definitions.Milestones.DestinyMilestoneDisplayPreference

## Entity Information
- **Entity Name**: Destiny.Definitions.Milestones.DestinyMilestoneDisplayPreference
- **Entity Type**: Enumeration
- **Base Type**: integer
- **Format**: int32

## Description
A hint for the UI as to what display information ought to be shown. Defaults to showing the static MilestoneDefinition's display properties.
 If for some reason the indicated property is not populated, fall back to the MilestoneDefinition.displayProperties.

## Enumeration Values

| Value | Identifier | Description |
|-------|------------|-------------|
| 0 | MilestoneDefinition | Indicates you should show DestinyMilestoneDefinition.displayProperties for this Milestone. |
| 1 | CurrentQuestSteps | Indicates you should show the displayProperties for any currently active Quest Steps in DestinyMilestone.availableQuests. |
| 2 | CurrentActivityChallenges | Indicates you should show the displayProperties for any currently active Activities and their Challenges in DestinyMilestone.activities. |

## Usage Examples

### JavaScript
```javascript
// Destiny.Definitions.Milestones.DestinyMilestoneDisplayPreference enumeration values
const DestinyMilestoneDisplayPreference = {
  MilestoneDefinition: 0,
  CurrentQuestSteps: 1,
  CurrentActivityChallenges: 2,
};

// Using the enumeration
const value = DestinyMilestoneDisplayPreference.MilestoneDefinition;
```

### Python
```python
# Destiny.Definitions.Milestones.DestinyMilestoneDisplayPreference enumeration values
class DestinyMilestoneDisplayPreference:
    MILESTONEDEFINITION = 0
    CURRENTQUESTSTEPS = 1
    CURRENTACTIVITYCHALLENGES = 2

# Using the enumeration
value = DestinyMilestoneDisplayPreference.MILESTONEDEFINITION
```

## Notes
- This is an enumeration with predefined values.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Milestones.DestinyMilestoneDisplayPreference":   {
      "format": "int32",
      "description": "A hint for the UI as to what display information ought to be shown. Defaults to showing the static MilestoneDefinition's display properties.\r\n If for some reason the indicated property is not populated, fall back to the MilestoneDefinition.displayProperties.",
      "enum": [
          "0",
          "1",
          "2"
      ],
      "type": "integer"
  }
}
```
