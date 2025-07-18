# Destiny.Definitions.FireteamFinder.DestinyFireteamFinderConstantsDefinition

## Entity Information
- **Entity Name**: Destiny.Definitions.FireteamFinder.DestinyFireteamFinderConstantsDefinition
- **Entity Type**: Mobile Manifest Entity
- **Base Type**: object

## Description
Destiny API entity representing destinyfireteamfinderconstantsdefinition data.

## Properties

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| displayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| fireteamFinderActivityGraphRootCategoryHashes | Array[integer] |  | No |
| allFireteamFinderActivityHashes | Array[integer] |  | No |
| guardianOathDisplayProperties | Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition |  | No |
| guardianOathTenets | Array[Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition] |  | No |
| hash | integer (uint32) | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
When entities refer to each other in Destiny content, it is this hash that they are referring to. | No |
| index | integer (int32) | The index of the entity as it was found in the investment tables. | No |
| redacted | boolean | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | No |

## Usage Examples

### JavaScript
```javascript
// Example Destiny.Definitions.FireteamFinder.DestinyFireteamFinderConstantsDefinition object
const example = {
  displayProperties: null,
  fireteamFinderActivityGraphRootCategoryHashes: [],
  allFireteamFinderActivityHashes: [],
  guardianOathDisplayProperties: null,
  guardianOathTenets: [],
  // ... more properties
};
```

### Python
```python
# Example Destiny.Definitions.FireteamFinder.DestinyFireteamFinderConstantsDefinition object
example = {
    "displayProperties": None,
    "fireteamFinderActivityGraphRootCategoryHashes": [],
    "allFireteamFinderActivityHashes": [],
    "guardianOathDisplayProperties": None,
    "guardianOathTenets": [],
    # ... more properties
}
```

## Related Entities
- **Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition**: Referenced in this entity
- **Destiny.Definitions.DestinyActivityDefinition**: Referenced in this entity
- **Destiny.Definitions.FireteamFinder.DestinyFireteamFinderActivityGraphDefinition**: Referenced in this entity

## Notes
- This entity is part of the Mobile Manifest and contains static definition data.
- This is an object schema with defined properties.
- This entity is part of the Destiny API and requires appropriate authentication scopes.

## JSON Schema
```json
{
  "Destiny.Definitions.FireteamFinder.DestinyFireteamFinderConstantsDefinition":   {
      "type": "object",
      "properties": {
          "displayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "fireteamFinderActivityGraphRootCategoryHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.FireteamFinder.DestinyFireteamFinderActivityGraphDefinition"
              }
          },
          "allFireteamFinderActivityHashes": {
              "type": "array",
              "items": {
                  "format": "uint32",
                  "type": "integer"
              },
              "x-mapped-definition": {
                  "$ref": "#/definitions/Destiny.Definitions.DestinyActivityDefinition"
              }
          },
          "guardianOathDisplayProperties": {
              "$ref": "#/definitions/Destiny.Definitions.Common.DestinyDisplayPropertiesDefinition"
          },
          "guardianOathTenets": {
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
      "x-mobile-manifest-name": "FireteamFinderConstants"
  }
}
```
