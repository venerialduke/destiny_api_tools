# Destiny.Definitions.Social.DestinySocialCommendationDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Social.DestinySocialCommendationDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Destiny API entity representing destinysocialcommendationdefinition data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| cardImagePath | string |  | No |
| color | Destiny.Misc.DestinyColor |  | No |
| displayPriority | integer (int32) |  | No |
| activityGivingLimit | integer (int32) |  | No |
| parentCommendationNodeHash | integer (uint32) |  | No |
| displayActivities | Array[Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition] | The display properties for the the activities that this commendation is available in. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Social.DestinySocialCommendationDefinition object
const example = {
  displayProperties: null,
  cardImagePath: "example value",
  color: null,
  displayPriority: 123,
  activityGivingLimit: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Social.DestinySocialCommendationDefinition object
example = {
    "displayProperties": None,
    "cardImagePath": "example value",
    "color": None,
    "displayPriority": 123,
    "activityGivingLimit": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.Social.DestinySocialCommendationNodeDefinition**: Referenced in this entity
- **Destiny.Misc.DestinyColor**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Social.DestinySocialCommendationDefinition":   {
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "cardImagePath": {
              "type": "string"
          },
          "color": {
              "$ref": "#/definitions/Destiny.Misc.DestinyColor"
          },
          "displayPriority": {
              "format": "int32",
              "type": "integer"
          },
          "activityGivingLimit": {
              "format": "int32",
              "type": "integer"
          },
          "parentCommendationNodeHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Social.DestinySocialCommendationNodeDefinition"
              }
          },
          "displayActivities": {
              "description": "The display properties for the the activities that this commendation is available in.",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
              }
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
      "x-mobile-manifest-name": "SocialCommendations"
  }
}
```
