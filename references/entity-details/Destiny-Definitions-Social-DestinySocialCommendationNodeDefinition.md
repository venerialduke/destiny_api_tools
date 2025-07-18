# Destiny.Definitions.Social.DestinySocialCommendationNodeDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Social.DestinySocialCommendationNodeDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Destiny API entity representing destinysocialcommendationnodedefinition data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| color | object | The color associated with this group of commendations. | No |
| tintedIcon | string | A version of the displayProperties icon tinted with the color of this node. | No |
| parentCommendationNodeHash | integer (uint32) |  | No |
| childCommendationNodeHashes | Array[integer] | A list of hashes that map to child commendation nodes. Only the root commendations node is expected to have child nodes. | No |
| childCommendationHashes | Array[integer] | A list of hashes that map to child commendations. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Social.DestinySocialCommendationNodeDefinition object
const example = {
  displayProperties: null,
  color: null,
  tintedIcon: "example value",
  parentCommendationNodeHash: 123,
  childCommendationNodeHashes: [],
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Social.DestinySocialCommendationNodeDefinition object
example = {
    "displayProperties": None,
    "color": None,
    "tintedIcon": "example value",
    "parentCommendationNodeHash": 123,
    "childCommendationNodeHashes": [],
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.Social.DestinySocialCommendationDefinition**: Referenced in this entity
- **Destiny.Definitions.Social.DestinySocialCommendationNodeDefinition**: Referenced in this entity
- **Destiny.Misc.DestinyColor**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Social.DestinySocialCommendationNodeDefinition":   {
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "color": {
              "description": "The color associated with this group of commendations.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Misc.DestinyColor"
                  }
              ]
          },
          "tintedIcon": {
              "description": "A version of the displayProperties icon tinted with the color of this node.",
              "type": "string"
          },
          "parentCommendationNodeHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Social.DestinySocialCommendationNodeDefinition"
              }
          },
          "childCommendationNodeHashes": {
              "description": "A list of hashes that map to child commendation nodes. Only the root commendations node is expected to have child nodes.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Social.DestinySocialCommendationNodeDefinition"
              }
          },
          "childCommendationHashes": {
              "description": "A list of hashes that map to child commendations.",
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Social.DestinySocialCommendationDefinition"
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
      "x-mobile-manifest-name": "SocialCommendationNodes"
  }
}
```
