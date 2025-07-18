# Destiny.Definitions.Milestones.DestinyMilestoneActivityDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Milestones.DestinyMilestoneActivityDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Milestones can have associated activities which provide additional information about the context, challenges, modifiers, state etc... related to this Milestone. 
Information we need to be able to return that data is defined here, along with Tier data to establish a relationship between a conceptual Activity and its difficulty levels and variants.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| conceptualActivityHash | integer (uint32) | The "Conceptual" activity hash. Basically, we picked the lowest level activity and are treating it as the canonical definition of the activity for rendering purposes.
If you care about the specific difficulty modes and variations, use the activities under "Variants". | No |
| variants | object | A milestone-referenced activity can have many variants, such as Tiers or alternative modes of play.
Even if there is only a single variant, the details for these are represented within as a variant definition.
It is assumed that, if this DestinyMilestoneActivityDefinition is active, then all variants should be active.
If a Milestone could ever split the variants' active status conditionally, they should all have their own DestinyMilestoneActivityDefinition instead! The potential duplication will be worth it for the obviousness of processing and use. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Milestones.DestinyMilestoneActivityDefinition object
const example = {
  conceptualActivityHash: 123,
  variants: null,
};
```

### Python
```python
# Example Destiny.Definitions.Milestones.DestinyMilestoneActivityDefinition object
example = {
    "conceptualActivityHash": 123,
    "variants": None,
}
```

## Related Entities
- **Destiny.Definitions.DestinyActivityDefinition**: Referenced in this entity
- **Destiny.Definitions.Milestones.DestinyMilestoneActivityVariantDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Milestones.DestinyMilestoneActivityDefinition":   {
      "description": "Milestones can have associated activities which provide additional information about the context, challenges, modifiers, state etc... related to this Milestone. \r\nInformation we need to be able to return that data is defined here, along with Tier data to establish a relationship between a conceptual Activity and its difficulty levels and variants.",
      "type": "object",
      "properties": {
          "conceptualActivityHash": {
              "format": "uint32",
              "description": "The \"Conceptual\" activity hash. Basically, we picked the lowest level activity and are treating it as the canonical definition of the activity for rendering purposes.\r\nIf you care about the specific difficulty modes and variations, use the activities under \"Variants\".",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityDefinition"
              }
          },
          "variants": {
              "description": "A milestone-referenced activity can have many variants, such as Tiers or alternative modes of play.\r\nEven if there is only a single variant, the details for these are represented within as a variant definition.\r\nIt is assumed that, if this DestinyMilestoneActivityDefinition is active, then all variants should be active.\r\nIf a Milestone could ever split the variants' active status conditionally, they should all have their own DestinyMilestoneActivityDefinition instead! The potential duplication will be worth it for the obviousness of processing and use.",
              "type": "object",
              "additionalProperties": {
                  "$ref": "#/definitions/Destiny.Definitions.Milestones.DestinyMilestoneActivityVariantDefinition"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityDefinition"
              }
          }
      }
  }
}
```
