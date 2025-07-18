# Destiny.Definitions.Activities.DestinyActivityInteractableEntryDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Activities.DestinyActivityInteractableEntryDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
Defines a specific interactable and the action that can occur when triggered.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| activityHash | integer (uint32) | The activity that will trigger when you interact with this interactable. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Activities.DestinyActivityInteractableEntryDefinition object
const example = {
  activityHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.Activities.DestinyActivityInteractableEntryDefinition object
example = {
    "activityHash": 123,
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
  "Destiny.Definitions.Activities.DestinyActivityInteractableEntryDefinition":   {
      "description": "Defines a specific interactable and the action that can occur when triggered.",
      "type": "object",
      "properties": {
          "activityHash": {
              "format": "uint32",
              "description": "The activity that will trigger when you interact with this interactable.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityDefinition"
              }
          }
      }
  }
}
```
