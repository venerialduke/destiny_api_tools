# Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderoptiondefinition data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| descendingSortPriority | integer (int32) |  | No |
| groupHash | integer (uint32) |  | No |
| codeOptionType | integer (int32) |  | No |
| availability | integer (int32) |  | No |
| visibility | integer (int32) |  | No |
| uiDisplayStyle | string |  | No |
| creatorSettings | Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionCreatorSettings |  | No |
| searcherSettings | Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionSearcherSettings |  | No |
| values | Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionValues |  | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionDefinition object
const example = {
  displayProperties: null,
  descendingSortPriority: 123,
  groupHash: 123,
  codeOptionType: 123,
  availability: 123,
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionDefinition object
example = {
    "displayProperties": None,
    "descendingSortPriority": 123,
    "groupHash": 123,
    "codeOptionType": 123,
    "availability": 123,
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionCreatorSettings**: Referenced in this entity
- **Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionGroupDefinition**: Referenced in this entity
- **Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionSearcherSettings**: Referenced in this entity
- **Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionValues**: Referenced in this entity
- **Destiny.FireteamFinderCodeOptionType**: Referenced in this entity
- **Destiny.FireteamFinderOptionAvailability**: Referenced in this entity
- **Destiny.FireteamFinderOptionVisibility**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionDefinition":   {
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "descendingSortPriority": {
              "format": "int32",
              "type": "integer"
          },
          "groupHash": {
              "format": "uint32",
              "type": "integer",
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionGroupDefinition"
              }
          },
          "codeOptionType": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.FireteamFinderCodeOptionType"
              }
          },
          "availability": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.FireteamFinderOptionAvailability"
              }
          },
          "visibility": {
              "format": "int32",
              "type": "integer",
              "x-enum-reference": {
                  "$ref": "#/components/schemas/Destiny.FireteamFinderOptionVisibility"
              }
          },
          "uiDisplayStyle": {
              "type": "string"
          },
          "creatorSettings": {
              "$ref": "#/definitions/Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionCreatorSettings"
          },
          "searcherSettings": {
              "$ref": "#/definitions/Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionSearcherSettings"
          },
          "values": {
              "$ref": "#/definitions/Destiny.Definitions.FireteamFinder.DestinyFireteamFinderOptionValues"
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
      "x-mobile-manifest-name": "FireteamFinderOptions"
  }
}
```
