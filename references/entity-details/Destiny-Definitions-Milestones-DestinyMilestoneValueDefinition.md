# Destiny.Definitions.Milestones.DestinyMilestoneValueDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Milestones.DestinyMilestoneValueDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
The definition for information related to a key/value pair that is relevant for a particular Milestone or component within the Milestone. 
This lets us more flexibly pass up information that's useful to someone, even if it's not necessarily us.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| key | string |  | No |
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Milestones.DestinyMilestoneValueDefinition object
const example = {
  key: "example value",
  displayProperties: null,
};
```

### Python
```python
# Example Destiny.Definitions.Milestones.DestinyMilestoneValueDefinition object
example = {
    "key": "example value",
    "displayProperties": None,
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Milestones.DestinyMilestoneValueDefinition":   {
      "description": "The definition for information related to a key/value pair that is relevant for a particular Milestone or component within the Milestone. \r\nThis lets us more flexibly pass up information that's useful to someone, even if it's not necessarily us.",
      "type": "object",
      "properties": {
          "key": {
              "type": "string"
          },
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          }
      }
  }
}
```
