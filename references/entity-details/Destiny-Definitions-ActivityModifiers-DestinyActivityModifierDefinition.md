# Destiny.Definitions.ActivityModifiers.DestinyActivityModifierDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.ActivityModifiers.DestinyActivityModifierDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Modifiers - in Destiny 1, these were referred to as "Skulls" - are changes that can be applied to an Activity.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| displayInNavMode | boolean |  | No |
| displayInActivitySelection | boolean |  | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.ActivityModifiers.DestinyActivityModifierDefinition object
const example = {
  displayProperties: null,
  displayInNavMode: true,
  displayInActivitySelection: true,
  hash: 123,
  index: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.ActivityModifiers.DestinyActivityModifierDefinition object
example = {
    "displayProperties": None,
    "displayInNavMode": True,
    "displayInActivitySelection": True,
    "hash": 123,
    "index": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.ActivityModifiers.DestinyActivityModifierDefinition":   {
      "description": "Modifiers - in Destiny 1, these were referred to as \"Skulls\" - are changes that can be applied to an Activity.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "displayInNavMode": {
              "type": "boolean"
          },
          "displayInActivitySelection": {
              "type": "boolean"
          },
          "hash": {
              "format": "uint32",
              "description": "The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.\r\nWhen entities refer to each other in Destiny content, it is this hash that they are referring to.",
              "type": "integer"
          },
          "index": {
              "format": "int32",
              "description": "The index of the entity as it was found in the investment tables.",
              "type": "integer"
          },
          "redacted": {
              "description": "If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!",
              "type": "boolean"
          }
      },
      "x-mobile-manifest-name": "ActivityModifiers"
  }
}
```
