# Destiny.Milestones.DestinyMilestoneContentItemCategory

## Entity Information
- **Entity Name**: Destiny.Milestones.DestinyMilestoneContentItemCategory
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Part of our dynamic, localized Milestone content is arbitrary categories of items. These are built in our content management system, and thus aren't the same as programmatically generated rewards.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| title | string |  | No |
| itemHashes | Array[integer] |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Milestones.DestinyMilestoneContentItemCategory object
const example = {
  title: "example value",
  itemHashes: [],
};
```

### Python
```python
# Example Destiny.Milestones.DestinyMilestoneContentItemCategory object
example = {
    "title": "example value",
    "itemHashes": [],
}
```

## Related Entities
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Milestones.DestinyMilestoneContentItemCategory":   {
      "description": "Part of our dynamic, localized Milestone content is arbitrary categories of items. These are built in our content management system, and thus aren't the same as programmatically generated rewards.",
      "type": "object",
      "properties": {
          "title": {
              "type": "string"
          },
          "itemHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          }
      }
  }
}
```
