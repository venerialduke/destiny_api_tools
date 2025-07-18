# Destiny.Definitions.DestinyActivityTypeDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.DestinyActivityTypeDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
The definition for an Activity Type.
In Destiny 2, an Activity Type represents a conceptual categorization of Activities.
These are most commonly used in the game for the subtitle under Activities, but BNet uses them extensively to identify and group activities by their common properties.
Unfortunately, there has been a movement away from providing the richer data in Destiny 2 that we used to get in Destiny 1 for Activity Types. For instance, Nightfalls are grouped under the same Activity Type as regular Strikes. 
For this reason, BNet will eventually migrate toward Activity Modes as a better indicator of activity category. But for the time being, it is still referred to in many places across our codebase.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.DestinyActivityTypeDefinition object
const example = {
  displayProperties: null,
  hash: 123,
  index: 123,
  redacted: true,
};
```

### Python
```python
# Example Destiny.Definitions.DestinyActivityTypeDefinition object
example = {
    "displayProperties": None,
    "hash": 123,
    "index": 123,
    "redacted": True,
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
  "Destiny.Definitions.DestinyActivityTypeDefinition":   {
      "description": "The definition for an Activity Type.\r\nIn Destiny 2, an Activity Type represents a conceptual categorization of Activities.\r\nThese are most commonly used in the game for the subtitle under Activities, but BNet uses them extensively to identify and group activities by their common properties.\r\nUnfortunately, there has been a movement away from providing the richer data in Destiny 2 that we used to get in Destiny 1 for Activity Types. For instance, Nightfalls are grouped under the same Activity Type as regular Strikes. \r\nFor this reason, BNet will eventually migrate toward Activity Modes as a better indicator of activity category. But for the time being, it is still referred to in many places across our codebase.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
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
      "x-mobile-manifest-name": "ActivityTypes"
  }
}
```
