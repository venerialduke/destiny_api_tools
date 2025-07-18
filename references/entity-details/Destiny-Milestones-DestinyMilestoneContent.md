# Destiny.Milestones.DestinyMilestoneContent

## Entity Information
- **Entity Name**: Destiny.Milestones.DestinyMilestoneContent
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Represents localized, extended content related to Milestones. This is intentionally returned by a separate endpoint and not with Character-level Milestone data because we do not put localized data into standard Destiny responses, both for brevity of response and for caching purposes. If you really need this data, hit the Milestone Content endpoint.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| about | string | The "About this Milestone" text from the Firehose. | No |
| status | string | The Current Status of the Milestone, as driven by the Firehose. | No |
| tips | Array[string] | A list of tips, provided by the Firehose. | No |
| itemCategories | Array[Destiny.Milestones.DestinyMilestoneContentItemCategory] | If DPS has defined items related to this Milestone, they can categorize those items in the Firehose. That data will then be returned as item categories here. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Milestones.DestinyMilestoneContent object
const example = {
  about: "example value",
  status: "example value",
  tips: [],
  itemCategories: [],
};
```

### Python
```python
# Example Destiny.Milestones.DestinyMilestoneContent object
example = {
    "about": "example value",
    "status": "example value",
    "tips": [],
    "itemCategories": [],
}
```

## Related Entities
- **Destiny.Milestones.DestinyMilestoneContentItemCategory**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Milestones.DestinyMilestoneContent":   {
      "description": "Represents localized, extended content related to Milestones. This is intentionally returned by a separate endpoint and not with Character-level Milestone data because we do not put localized data into standard Destiny responses, both for brevity of response and for caching purposes. If you really need this data, hit the Milestone Content endpoint.",
      "type": "object",
      "properties": {
          "about": {
              "description": "The \"About this Milestone\" text from the Firehose.",
              "type": "string"
          },
          "status": {
              "description": "The Current Status of the Milestone, as driven by the Firehose.",
              "type": "string"
          },
          "tips": {
              "description": "A list of tips, provided by the Firehose.",
              "type": "array",
              "items": {
                  "type": "string"
              }
          },
          "itemCategories": {
              "description": "If DPS has defined items related to this Milestone, they can categorize those items in the Firehose. That data will then be returned as item categories here.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Milestones.DestinyMilestoneContentItemCategory"
              }
          }
      }
  }
}
```
