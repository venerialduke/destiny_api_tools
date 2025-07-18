# Destiny.Definitions.Milestones.DestinyMilestoneActivityVariantDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Milestones.DestinyMilestoneActivityVariantDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Represents a variant on an activity for a Milestone: a specific difficulty tier, or a specific activity variant for example.
These will often have more specific details, such as an associated Guided Game, progression steps, tier-specific rewards, and custom values.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| activityHash | integer (uint32) | The hash to use for looking up the variant Activity's definition (DestinyActivityDefinition), where you can find its distinguishing characteristics such as difficulty level and recommended light level. 
Frequently, that will be the only distinguishing characteristics in practice, which is somewhat of a bummer. | No |
| order | integer (int32) | If you care to do so, render the variants in the order prescribed by this value.
When you combine live Milestone data with the definition, the order becomes more useful because you'll be cross-referencing between the definition and live data. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Milestones.DestinyMilestoneActivityVariantDefinition object
const example = {
  activityHash: 123,
  order: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Milestones.DestinyMilestoneActivityVariantDefinition object
example = {
    "activityHash": 123,
    "order": 123,
}
```

## Related Entities
- **Destiny.Definitions.DestinyActivityDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Milestones.DestinyMilestoneActivityVariantDefinition":   {
      "description": "Represents a variant on an activity for a Milestone: a specific difficulty tier, or a specific activity variant for example.\r\nThese will often have more specific details, such as an associated Guided Game, progression steps, tier-specific rewards, and custom values.",
      "type": "object",
      "properties": {
          "activityHash": {
              "format": "uint32",
              "description": "The hash to use for looking up the variant Activity's definition (DestinyActivityDefinition), where you can find its distinguishing characteristics such as difficulty level and recommended light level. \r\nFrequently, that will be the only distinguishing characteristics in practice, which is somewhat of a bummer.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityDefinition"
              }
          },
          "order": {
              "format": "int32",
              "description": "If you care to do so, render the variants in the order prescribed by this value.\r\nWhen you combine live Milestone data with the definition, the order becomes more useful because you'll be cross-referencing between the definition and live data.",
              "type": "integer"
          }
      }
  }
}
```
