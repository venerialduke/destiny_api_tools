# Destiny.Milestones.DestinyPublicMilestone

## Entity Information
- **Entity Name**: Destiny.Milestones.DestinyPublicMilestone
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Information about milestones, presented in a character state-agnostic manner. Combine this data with DestinyMilestoneDefinition to get a full picture of the milestone, which is basically a checklist of things to do in the game. Think of this as GetPublicAdvisors 3.0, for those who used the Destiny 1 API.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| milestoneHash | integer (uint32) | The hash identifier for the milestone. Use it to look up the DestinyMilestoneDefinition for static data about the Milestone. | No |
| availableQuests | Array[Destiny.Milestones.DestinyPublicMilestoneQuest] | A milestone not need have even a single quest, but if there are active quests they will be returned here. | No |
| activities | Array[Destiny.Milestones.DestinyPublicMilestoneChallengeActivity] |  | No |
| vendorHashes | Array[integer] | Sometimes milestones - or activities active in milestones - will have relevant vendors. These are the vendors that are currently relevant.
Deprecated, already, for the sake of the new "vendors" property that has more data. What was I thinking. | No |
| vendors | Array[Destiny.Milestones.DestinyPublicMilestoneVendor] | This is why we can't have nice things. This is the ordered list of vendors to be shown that relate to this milestone, potentially along with other interesting data. | No |
| startDate | string (date-time) | If known, this is the date when the Milestone started/became active. | No |
| endDate | string (date-time) | If known, this is the date when the Milestone will expire/recycle/end. | No |
| order | integer (int32) | Used for ordering milestones in a display to match how we order them in BNet. May pull from static data, or possibly in the future from dynamic information. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Milestones.DestinyPublicMilestone object
const example = {
  milestoneHash: 123,
  availableQuests: [],
  activities: [],
  vendorHashes: [],
  vendors: [],
  // ... more properties
};
```

### Python
```python
# Example Destiny.Milestones.DestinyPublicMilestone object
example = {
    "milestoneHash": 123,
    "availableQuests": [],
    "activities": [],
    "vendorHashes": [],
    "vendors": [],
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Milestones.DestinyMilestoneDefinition**: Referenced in this entity
- **Destiny.Milestones.DestinyPublicMilestoneChallengeActivity**: Referenced in this entity
- **Destiny.Milestones.DestinyPublicMilestoneQuest**: Referenced in this entity
- **Destiny.Milestones.DestinyPublicMilestoneVendor**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Milestones.DestinyPublicMilestone":   {
      "description": "Information about milestones, presented in a character state-agnostic manner. Combine this data with DestinyMilestoneDefinition to get a full picture of the milestone, which is basically a checklist of things to do in the game. Think of this as GetPublicAdvisors 3.0, for those who used the Destiny 1 API.",
      "type": "object",
      "properties": {
          "milestoneHash": {
              "format": "uint32",
              "description": "The hash identifier for the milestone. Use it to look up the DestinyMilestoneDefinition for static data about the Milestone.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Milestones.DestinyMilestoneDefinition"
              }
          },
          "availableQuests": {
              "description": "A milestone not need have even a single quest, but if there are active quests they will be returned here.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Milestones.DestinyPublicMilestoneQuest"
              }
          },
          "activities": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Milestones.DestinyPublicMilestoneChallengeActivity"
              }
          },
          "vendorHashes": {
              "description": "Sometimes milestones - or activities active in milestones - will have relevant vendors. These are the vendors that are currently relevant.\r\nDeprecated, already, for the sake of the new \"vendors\" property that has more data. What was I thinking.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              }
          },
          "vendors": {
              "description": "This is why we can't have nice things. This is the ordered list of vendors to be shown that relate to this milestone, potentially along with other interesting data.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Milestones.DestinyPublicMilestoneVendor"
              }
          },
          "startDate": {
              "format": "date-time",
              "description": "If known, this is the date when the Milestone started/became active.",
              "type": "string"
          },
          "endDate": {
              "format": "date-time",
              "description": "If known, this is the date when the Milestone will expire/recycle/end.",
              "type": "string"
          },
          "order": {
              "format": "int32",
              "description": "Used for ordering milestones in a display to match how we order them in BNet. May pull from static data, or possibly in the future from dynamic information.",
              "type": "integer"
          }
      }
  }
}
```
