# Destiny.Definitions.DestinyActivityModifierReferenceDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyActivityModifierReferenceDefinition
- **Entity Type**: Object Schema
- **Base Type**: object

## Description
A reference to an Activity Modifier from another entity, such as an Activity (for now, just Activities).
This defines some

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| activityModifierHash | integer (uint32) | The hash identifier for the DestinyActivityModifierDefinition referenced by this activity. | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyActivityModifierReferenceDefinition object
const example = {
  activityModifierHash: 123,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyActivityModifierReferenceDefinition object
example = {
    "activityModifierHash": 123,
}
```

## Related Entities
- **Destiny.Definitions.ActivityModifiers.DestinyActivityModifierDefinition**: Referenced in this entity

## Notes
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.DestinyActivityModifierReferenceDefinition":   {
      "description": "A reference to an Activity Modifier from another entity, such as an Activity (for now, just Activities).\r\nThis defines some",
      "type": "object",
      "properties": {
          "activityModifierHash": {
              "format": "uint32",
              "description": "The hash identifier for the DestinyActivityModifierDefinition referenced by this activity.",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.ActivityModifiers.DestinyActivityModifierDefinition"
              }
          }
      }
  }
}
```
