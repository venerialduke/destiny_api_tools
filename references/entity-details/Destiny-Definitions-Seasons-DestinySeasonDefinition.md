# Destiny.Definitions.Seasons.DestinySeasonDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.Seasons.DestinySeasonDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Defines a canonical "Season" of Destiny: a range of a few months where the game highlights certain challenges, provides new loot, has new Clan-related rewards and celebrates various seasonal events.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| backgroundImagePath | string |  | No |
| seasonNumber | integer (int32) |  | No |
| startDate | string (date-time) |  | No |
| endDate | string (date-time) |  | No |
| seasonPassHash | integer (uint32) |  | No |
| seasonPassList | Array[Destiny.Definitions.Seasons.DestinySeasonPassReference] |  | No |
| seasonPassProgressionHash | integer (uint32) |  | No |
| artifactItemHash | integer (uint32) |  | No |
| sealPresentationNodeHash | integer (uint32) |  | No |
| acts | Array[Destiny.Definitions.Seasons.DestinySeasonActDefinition] | A list of Acts for the Episode | No |
| seasonalChallengesPresentationNodeHash | integer (uint32) |  | No |
| preview | object | Optional - Defines the promotional text, images, and links to preview this season. | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.Seasons.DestinySeasonDefinition object
const example = {
  displayProperties: null,
  backgroundImagePath: "example value",
  seasonNumber: 123,
  startDate: "example value",
  endDate: "example value",
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.Seasons.DestinySeasonDefinition object
example = {
    "displayProperties": None,
    "backgroundImagePath": "example value",
    "seasonNumber": 123,
    "startDate": "example value",
    "endDate": "example value",
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyInventoryItemDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyProgressionDefinition**: Referenced in this entity
- **Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition**: Referenced in this entity
- **Destiny.Definitions.Seasons.DestinySeasonActDefinition**: Referenced in this entity
- **Destiny.Definitions.Seasons.DestinySeasonPassDefinition**: Referenced in this entity
- **Destiny.Definitions.Seasons.DestinySeasonPassReference**: Referenced in this entity
- **Destiny.Definitions.Seasons.DestinySeasonPreviewDefinition**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.Seasons.DestinySeasonDefinition":   {
      "description": "Defines a canonical \"Season\" of Destiny: a range of a few months where the game highlights certain challenges, provides new loot, has new Clan-related rewards and celebrates various seasonal events.",
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "backgroundImagePath": {
              "type": "string"
          },
          "seasonNumber": {
              "format": "int32",
              "type": "integer"
          },
          "startDate": {
              "format": "date-time",
              "type": "string"
          },
          "endDate": {
              "format": "date-time",
              "type": "string"
          },
          "seasonPassHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Seasons.DestinySeasonPassDefinition"
              }
          },
          "seasonPassList": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Seasons.DestinySeasonPassReference"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Seasons.DestinySeasonPassDefinition"
              }
          },
          "seasonPassProgressionHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyProgressionDefinition"
              }
          },
          "artifactItemHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyInventoryItemDefinition"
              }
          },
          "sealPresentationNodeHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
              }
          },
          "acts": {
              "description": "A list of Acts for the Episode",
              "type": "array",
              "items": {
                  "$ref": "#/definitions/Destiny.Definitions.Seasons.DestinySeasonActDefinition"
              }
          },
          "seasonalChallengesPresentationNodeHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.Presentation.DestinyPresentationNodeDefinition"
              }
          },
          "preview": {
              "description": "Optional - Defines the promotional text, images, and links to preview this season.",
              "type": "object",
              "allOf": [
                  {
                      "$ref": "#/definitions/Destiny.Definitions.Seasons.DestinySeasonPreviewDefinition"
                  }
              ]
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
      "x-mobile-manifest-name": "Seasons"
  }
}
```
