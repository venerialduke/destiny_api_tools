# Trending.TrendingEntryDestinyRitual

## Entity Information
- **Entity Name**: Trending.TrendingEntryDestinyRitual
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Destiny API entity representing trendingentrydestinyritual data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| image | string |  | No |
| icon | string |  | No |
| title | string |  | No |
| subtitle | string |  | No |
| dateStart | string (date-time) |  | No |
| dateEnd | string (date-time) |  | No |
| milestoneDetails | object | A destiny event does not necessarily have a related Milestone, but if it does the details will be returned here. | No |
| eventContent | object | A destiny event will not necessarily have milestone "custom content", but if it does the details will be here. | No |

## Usage Examples

### JavaScript
```javascript
// Example Trending.TrendingEntryDestinyRitual object
const example = {
  image: "example value",
  icon: "example value",
  title: "example value",
  subtitle: "example value",
  dateStart: "example value",
  // ... more properties
};
```

### Python
```python
# Example Trending.TrendingEntryDestinyRitual object
example = {
    "image": "example value",
    "icon": "example value",
    "title": "example value",
    "subtitle": "example value",
    "dateStart": "example value",
    # ... more properties
}
```

## Related Entities
- **Destiny.Milestones.DestinyMilestoneContent**: Referenced in this entity
- **Destiny.Milestones.DestinyPublicMilestone**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Trending.TrendingEntryDestinyRitual":   {
      "type": "object",
      "properties": {
          "image": {
              "type": "string"
          },
          "icon": {
              "type": "string"
          },
          "title": {
              "type": "string"
          },
          "subtitle": {
              "type": "string"
          },
          "dateStart": {
              "format": "date-time",
              "type": "string"
          },
          "dateEnd": {
              "format": "date-time",
              "type": "string"
          },
          "milestoneDetails": {
              "description": "A destiny event does not necessarily have a related Milestone, but if it does the details will be returned here.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Milestones.DestinyPublicMilestone"
                  }
              ]
          },
          "eventContent": {
              "description": "A destiny event will not necessarily have milestone \"custom content\", but if it does the details will be here.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Milestones.DestinyMilestoneContent"
                  }
              ]
          }
      }
  }
}
```
