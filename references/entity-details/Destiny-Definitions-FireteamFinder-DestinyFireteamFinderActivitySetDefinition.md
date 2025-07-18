# Destiny.Definitions.FireteamFinder.DestinyFireteamFinderActivitySetDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.FireteamFinder.DestinyFireteamFinderActivitySetDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderactivitysetdefinition data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| maximumPartySize | integer (int32) |  | No |
| optionHashes | Array[integer] |  | No |
| labelHashes | Array[integer] |  | No |
| activityGraphHashes | Array[integer] |  | No |
| activityHashes | Array[integer] |  | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.FireteamFinder.DestinyFireteamFinderActivitySetDefinition object
const example = {
  maximumPartySize: 123,
  optionHashes: [],
  labelHashes: [],
  activityGraphHashes: [],
  activityHashes: [],
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.FireteamFinder.DestinyFireteamFinderActivitySetDefinition object
example = {
    "maximumPartySize": 123,
    "optionHashes": [],
    "labelHashes": [],
    "activityGraphHashes": [],
    "activityHashes": [],
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.DestinyActivityDefinition**: Referenced in this entity
- **Destiny.Definitions.FireteamFinder.DestinyFireteamFinderActivityGraphDefinition**: Referenced in this entity
- **Destiny.Definitions.FireteamFinder.DestinyFireteamFinderLabelDefinition**: Referenced in this entity
- **Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionDefinition**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.FireteamFinder.DestinyFireteamFinderActivitySetDefinition":   {
      "type": "object",
      "properties": {
          "maximumPartySize": {
              "format": "int32",
              "type": "integer"
          },
          "optionHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionDefinition"
              }
          },
          "labelHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.FireteamFinder.DestinyFireteamFinderLabelDefinition"
              }
          },
          "activityGraphHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.FireteamFinder.DestinyFireteamFinderActivityGraphDefinition"
              }
          },
          "activityHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityDefinition"
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
      "x-mobile-manifest-name": "FireteamFinderActivitySets"
  }
}
```
